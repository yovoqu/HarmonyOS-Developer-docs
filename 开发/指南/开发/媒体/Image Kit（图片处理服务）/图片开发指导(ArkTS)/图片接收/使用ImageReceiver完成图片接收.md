# 使用ImageReceiver完成图片接收

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver

图片接收类ImageReceiver用于获取组件SurfaceId，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。


> [!NOTE]
> Receiver作为消费者，需要有对应的生产者提供数据才能实现完整功能。常见的生产者是相机的拍照流或预览流。ImageReceiver只作为图片的接收方、消费者，在ImageReceiver设置的size、format等属性实际上并不会生效，图片createImageReceiver时传入的参数不产生实际影响。图片属性需要在发送方、生产者进行设置，如相机创建预览流时配置profile。

ImageReceiver可以接收相机预览流中的图片，实现[双路预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview)。

相关API的详细介绍请参见[ImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver)。


## 开发步骤

创建ImageReceiver对象，获取SurfaceId创建预览流，注册图像监听，按需处理预览流每帧图像。 导入相关模块包。
```text
import { image } from '@kit.ImageKit'
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit'
import { hilog } from '@kit.PerformanceAnalysisKit';
```

创建ImageReceiver对象，通过ImageReceiver对象可获取预览流SurfaceId。
```text
async function initImageReceiver(): Promise {
  // 创建ImageReceiver对象。createImageReceiver的参数不会对接收到的数据产生实际影响。
  let size: image.Size = { width: imageWidth, height: imageHeight };
  let imageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  // 获取预览流SurfaceId。
  let imageReceiverSurfaceId = await imageReceiver.getReceivingSurfaceId();
  console.info(`initImageReceiver imageReceiverSurfaceId:${imageReceiverSurfaceId}`);
}
```

注册监听处理预览流每帧图像数据：通过ImageReceiver中imageArrival事件监听获取底层返回的图像数据。详细的API说明请参考[ImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver)。
```text
function onImageArrival(receiver: image.ImageReceiver) {
  // 注册imageArrival监听。
  receiver.on('imageArrival', () => {
    // 获取图像。
    receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
      if (err || nextImage === undefined) {
        console.error('readNextImage failed');
        return;
      }
      // 解析图像内容。
      nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
        imgComponent: image.Component) => {
        if (err || imgComponent === undefined) {
          console.error('getComponent failed');
        }
        if (imgComponent.byteBuffer) {
          // 详情见下方解析图片buffer数据参考，本示例以方式一为例。
          let width = nextImage.size.width; // 获取图片的宽。
          let height = nextImage.size.height; // 获取图片的高。
          let stride = imgComponent.rowStride; // 获取图片的stride。
          console.debug(`getComponent with width:${width} height:${height} stride:${stride}`);
          // stride与width一致。
          if (stride == width) {
            let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
              size: { height: height, width: width },
              srcPixelFormat: 8,
            })
          } else {
            // stride与width不一致。
            const dstBufferSize = width * height * 1.5;
            const dstArr = new Uint8Array(dstBufferSize);
            for (let j = 0; j           通过[image.Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#component9)解析图片的buffer数据。           ![](assets/使用ImageReceiver完成图片接收/file-20260514131537866-0.png)              需要确认图像的宽（width）是否与行距（rowStride）一致，如果不一致可参考以下方式一和方式二进行预处理。                方式一：去除imgComponent.byteBuffer中stride数据，拷贝得到新的buffer，调用不支持stride的接口处理buffer。
```text
// stride与width不一致。
const dstBufferSize = width * height * 1.5
const dstArr = new Uint8Array(dstBufferSize)
for (let j = 0; j 方式二：根据stride * height创建pixelMap，然后调用pixelMap的cropSync方法裁剪掉多余的像素。
```text
// 创建pixelMap，width传入行距（stride）的值。
let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
  size:{height: height, width: stride}, srcPixelFormat: 8});
// 裁剪多余的像素。
try {
  pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
} catch (err) {
  hilog.error(0x00000, TAG, `adjust bufferSize failed: ${err}!`);
}
```
