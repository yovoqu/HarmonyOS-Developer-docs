# RichEditor获取ImageSpan中图片信息

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-943

#### 问题现象

在RichEditor组件中通过\$r('app.media.background')方式添加ImageSpan，并使用getSpans获取span信息时，由于base目录中的资源文件会被编译成二进制文件并分配资源ID，导致获取的图片名称与实际图片名称不一致。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vKmRvw4ySVmhQHnG8bEk9w/zh-cn_image_0000002658800487.png?HW-CC-KV=V1&HW-CC-Date=20260811T005749Z&HW-CC-Expire=86400&HW-CC-Sign=7A1BCBD02690180CA3A9B4C9B1F5DAE3F51F549D23BA601BF80DD5FDD0D69EE0)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)是支持图文混排和文本交互式编辑的组件，可以通过[getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)方法获取所有span信息。
 
 

#### 解决方案

将图片资源放到rawfile文件夹下，再通过getSpans获取valueResourceStr字段，能够正常获取到图片的名称。
 
```text
@Entry
@Component
struct RichEditorPage {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('点击按钮在此处添加image。', {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          });
        })
        .width('100%')
        .height(100);
      Row() {
        Button('添加图片', {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.controller.addImageSpan($rawfile('background.png'), {
              imageStyle: {
                size: ['57px', '57px']
              }
            });
          });
        Button('获取图片span', {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .onClick(() => {
            this.controller.getSpans({ start: 0 }).forEach(item => {
              console.info(`imageName is : ${(item as RichEditorImageSpanResult).valueResourceStr}`);
            });
          });
      }
      .justifyContent(FlexAlign.SpaceAround)
      .width('100%');
    }
    .border({ width: 1 });
  }
}
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/C_cNKk7OSTiC_HyiHa5AQw/zh-cn_image_0000002628561128.png?HW-CC-KV=V1&HW-CC-Date=20260811T005749Z&HW-CC-Expire=86400&HW-CC-Sign=0DB0EECF0AA7BD36E61AEFEB31604213F3DB1C5F95BFF469A02B839EDB69D8A3)
