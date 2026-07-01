# 如何解决OffscreenCanvas绘制鼠标路径时路径不平滑的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-996

## 如何解决OffscreenCanvas绘制鼠标路径时路径不平滑的问题
 


##### 问题现象

PC应用使用OffscreenCanvas离屏画布绘制鼠标路径，绘制路径不平滑，特别是快速移动鼠标时，出现明显折线。
 
问题效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/STVktlPySGmZ52O189ip9w/zh-cn_image_0000002658801089.png?HW-CC-KV=V1&HW-CC-Date=20260701T025717Z&HW-CC-Expire=86400&HW-CC-Sign=5F118AC5584406A276194C2B9A5A9FC0E38827D217C67E8AC6593F14F8A04FB7)

 
问题代码如下：
 
```text
import { display } from '@kit.ArkUI';

// 绘画状态接口
export class DrawingState {
  isDrawing: boolean = false;
  currentColor: string = 'rgb(0,255,0)';
  currentSize: number = 5;
  startX: number = 0;
  startY: number = 0;
}

/**
 *  canvas绘画工具类
 */
@ObservedV2
export class CanvasUtils {
  static instance: CanvasUtils | null = null;

  static getInstance() {
    if (!CanvasUtils.instance) {
      CanvasUtils.instance = new CanvasUtils();
    }
    return CanvasUtils.instance;
  }

  canvasRenderingContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
  offscreenCanvas = new OffscreenCanvasRenderingContext2D(this.getWidth(), this.getHeight());
  @Trace drawingState: DrawingState = {
    isDrawing: false,
    currentColor: '#000000',
    currentSize: 3,
    startX: 0,
    startY: 0
  };

  // 初始化画布
  initCanvas() {
    // 填充背景色
    this.offscreenCanvas.fillStyle = '#000';
    // 填充一个矩形
    this.offscreenCanvas.fillRect(0, 0, this.getWidth(), this.getHeight());
    this.offscreenCanvas.lineCap = 'round';
    this.offscreenCanvas.lineJoin = 'round';
    this.canvasRenderingContext.transferFromImageBitmap(this.offscreenCanvas.transferToImageBitmap());
  }


  getWidth() {
    const displayInstance = display.getDefaultDisplaySync();
    return displayInstance.width;
  }

  getHeight() {
    const displayInstance = display.getDefaultDisplaySync();
    return displayInstance.height;
  }


  // 设置绘画样式
  setupDrawingStyle() {
    this.offscreenCanvas.strokeStyle = this.drawingState.currentColor;
    this.offscreenCanvas.lineWidth = this.drawingState.currentSize;
    this.offscreenCanvas.globalCompositeOperation = 'source-over';
    this.offscreenCanvas.shadowBlur = 0;
    this.canvasRenderingContext.transferFromImageBitmap(this.offscreenCanvas.transferToImageBitmap());
  }

  // 开始绘画
  startDrawing(event: MouseEvent) {
    this.drawingState.isDrawing = true;
    this.drawingState.startX = event.displayX;
    this.drawingState.startY = event.displayY;
    this.setupDrawingStyle();
    this.offscreenCanvas.beginPath();
    this.offscreenCanvas.moveTo(event.displayX, event.displayY);
    this.canvasRenderingContext.transferFromImageBitmap(this.offscreenCanvas.transferToImageBitmap());
  }

  // 绘画中
  drawing(event: MouseEvent) {
    if (!this.drawingState.isDrawing) {
      return;
    }
    // 从当前点到指定点路径连接
    this.offscreenCanvas.lineTo(event.displayX, event.displayY);
    // 根据当前路径进行边框绘制操作
    this.offscreenCanvas.stroke();
    this.offscreenCanvas.globalCompositeOperation = 'source-over';
    this.canvasRenderingContext.transferFromImageBitmap(this.offscreenCanvas.transferToImageBitmap());
  }


  // 结束绘画
  stopDrawing() {
    if (this.drawingState.isDrawing) {
      this.drawingState.isDrawing = false;
      this.offscreenCanvas.globalCompositeOperation = 'source-over';
      this.canvasRenderingContext.transferFromImageBitmap(this.offscreenCanvas.transferToImageBitmap());
    }
  }
}

@Entry
@Component
struct Index {
  canvasUtils: CanvasUtils = CanvasUtils.getInstance();

  build() {
    Stack({ alignContent: Alignment.TopStart }) {

      // 画布
      Canvas(this.canvasUtils.canvasRenderingContext)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
        .border({ width: 3, color: '#dee2e6' })
        .borderRadius(10)
        .margin({ bottom: 20 })
        .onMouse((event: MouseEvent) => {
          if (event.action === MouseAction.Press) {
            this.canvasUtils.setupDrawingStyle();
            this.canvasUtils.startDrawing(event);
          } else if (event.action === MouseAction.Move) {
            this.canvasUtils.drawing(event);

          } else if (event.action === MouseAction.Release) {
            this.canvasUtils.stopDrawing();
          }
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000');
  }
}
```
 
 

##### 背景知识

- [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)提供画布组件，用于绘制图形。
- [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)是用于在Canvas上进行绘制的画笔，在主线程上通过CPU进行绘制。
- [OffscreenCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas)是离屏绘制的画笔，在单独的线程中通过GPU进行绘制。
- [onMouse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key#onmouse)是鼠标被移动或点击时触发的回调，返回的数据中包含路径中的坐标点。

 
 

##### 问题定位

问题代码中主要通过onMouse获取鼠标路径中的各个点的坐标，通过[lineTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#lineto)方法将这些点连接起来，进而实现了绘制鼠标移动路径的方法。其中，onMouse的回调频率与屏幕刷新率相关，刷新率越高，触发频率越高。通过GPU进行绘制的OffscreenCanvas在绘制速度上不如使用CPU进行绘制CanvasRenderingContext2D。
 
 

##### 分析结论

由于屏幕刷新率不足和OffscreenCanvas绘制速度较慢，导致了问题代码在快速移动鼠标时出现明显折线。其中，离屏渲染和在屏渲染是出现明显折线的主要原因。当刷新率提升时，也能在一定程度上优化体验。
 
以下是不同刷新率+离屏/在屏渲染的比较：
 
120Hz刷新率+离屏渲染：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7pLrwyV-RBWRE5UE72Rktw/zh-cn_image_0000002628401816.png?HW-CC-KV=V1&HW-CC-Date=20260701T025717Z&HW-CC-Expire=86400&HW-CC-Sign=4D024671842A318570A3A75E16AA8A87514B54CC5227548B86E65408D285B70C)

 
60Hz刷新率+在屏渲染：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_YDdrAgPQUa-BE40aRVxJQ/zh-cn_image_0000002628561724.png?HW-CC-KV=V1&HW-CC-Date=20260701T025717Z&HW-CC-Expire=86400&HW-CC-Sign=DD3783544FF310F74670F74D274F9AEC7F6777A971C6A7A4FED824B903EAD8E5)

 
120Hz刷新率+在屏渲染：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/twPonIcxSPWI5lJuUI6MhQ/zh-cn_image_0000002658921037.png?HW-CC-KV=V1&HW-CC-Date=20260701T025717Z&HW-CC-Expire=86400&HW-CC-Sign=4B51AAFE460B1F0B75C5DFC5760A15EDF43BC0DFA7E2A80E0699A5805802C1E9)

 
 

##### 修改建议

将离屏渲染OffscreenCanvas改为在屏渲染CanvasRenderingContext2D，即可显著提升绘制性能。同时，建议在PC设备的设置中将屏幕刷新率改为120Hz，优化体验。
 
示例代码如下：
 
```text
import { display } from '@kit.ArkUI';

// 绘画状态接口
export class DrawingState {
  isDrawing: boolean = false;
  currentColor: string = 'rgb(0,255,0)';
  currentSize: number = 5;
  startX: number = 0;
  startY: number = 0;
}

/**
 *  canvas绘画工具类
 */
@ObservedV2
export class CanvasUtils {
  static instance: CanvasUtils | null = null;
  static getInstance() {
    if (!CanvasUtils.instance) {
      CanvasUtils.instance = new CanvasUtils();
    }
    return CanvasUtils.instance;
  }

  canvasRenderingContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
  @Trace drawingState: DrawingState = {
    isDrawing: false,
    currentColor: '#000000',
    currentSize: 3,
    startX: 0,
    startY: 0
  };

  // 初始化画布
  initCanvas() {
    // 填充背景色
    this.canvasRenderingContext.fillStyle = '#000';
    // 填充一个矩形
    this.canvasRenderingContext.fillRect(0, 0, this.getWidth(), this.getHeight());
    this.canvasRenderingContext.lineCap = 'round';
    this.canvasRenderingContext.lineJoin = 'round';
  }

  getWidth() {
    const displayInstance = display.getDefaultDisplaySync();
    return displayInstance.width;
  }

  getHeight() {
    const displayInstance = display.getDefaultDisplaySync();
    return displayInstance.height;
  }

  // 设置绘画样式
  setupDrawingStyle() {
    this.canvasRenderingContext.strokeStyle = this.drawingState.currentColor;
    this.canvasRenderingContext.lineWidth = this.drawingState.currentSize;
    this.canvasRenderingContext.globalCompositeOperation = 'source-over';
    this.canvasRenderingContext.shadowBlur = 0;
  }

  // 开始绘画
  startDrawing(event: MouseEvent) {
    this.drawingState.isDrawing = true;
    this.drawingState.startX = event.displayX;
    this.drawingState.startY = event.displayY;
    this.setupDrawingStyle();
    this.canvasRenderingContext.beginPath();
    this.canvasRenderingContext.moveTo(event.displayX, event.displayY);
  }

  // 绘画中
  drawing(event: MouseEvent) {
    if (!this.drawingState.isDrawing) {
      return;
    }
    // 从当前点到指定点路径连接
    this.canvasRenderingContext.lineTo(event.displayX, event.displayY);
    // 根据当前路径进行边框绘制操作
    this.canvasRenderingContext.stroke();
    this.canvasRenderingContext.globalCompositeOperation = 'source-over';
  }

  // 结束绘画
  stopDrawing() {
    if (this.drawingState.isDrawing) {
      this.drawingState.isDrawing = false;
      this.canvasRenderingContext.globalCompositeOperation = 'source-over';
    }
  }
}

@Entry
@Component
struct CanvasRenderingContext2DDemo {
  canvasUtils: CanvasUtils = CanvasUtils.getInstance();

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      // 画布
      Canvas(this.canvasUtils.canvasRenderingContext)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
        .border({ width: 3, color: '#dee2e6' })
        .borderRadius(10)
        .margin({ bottom: 20 })
        .onMouse((event: MouseEvent) => {
          if (event.action === MouseAction.Press) {
            this.canvasUtils.setupDrawingStyle();
            this.canvasUtils.startDrawing(event);
          } else if (event.action === MouseAction.Move) {
            this.canvasUtils.drawing(event);

          } else if (event.action === MouseAction.Release) {
            this.canvasUtils.stopDrawing();
          }
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000');
  }
}
```
