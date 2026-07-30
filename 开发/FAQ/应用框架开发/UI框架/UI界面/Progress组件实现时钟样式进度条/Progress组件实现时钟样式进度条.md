# Progress组件实现时钟样式进度条

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-773

#### 问题现象

如何实现一个360度圆形刻度盘，并在圆周上添加一根跟随旋转的白色虚线（类似钟表的指针）？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/1wDwVzS8RWi3N8rZtLuKJA/zh-cn_image_0000002658915021.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072455Z&HW-CC-Expire=86400&HW-CC-Sign=2AEA3E1C243CB88A7F6CB71791AC21F7E97D7E94217B8C717FB046AB91E334A2)

 
 

#### 背景知识

[进度条 (Progress)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator)：Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)。
 
 

#### 解决方案

圆环进度条参考官方文档中的[进度条 ](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator)，虚线通过Divider()组件设置属性，旋转角度跟随进度条进度。
 
```text
@Entry
@Component
struct Index {
  @State rotateAngle: number = 0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  build() {
    Column() {
      Column() {
        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
          .backgroundColor(Color.Black)
          .style({ scaleCount: 20, scaleWidth: 5 })

        Divider()
          .height(40)
          .width(0)
          .borderWidth(2)
          .margin({ top: -90 }) <em>// </em><em>通过centerX、centerY设置旋转中心</em>
          .rotate({
            centerX: '100%',
            centerY: '100%',
            angle: this.rotateAngle
          })
          .onAppear(() => {
            this.uiContext?.animateTo({
              duration: 3000,
              curve: Curve.Linear,
              iterations: -1, <em>// 设置-1表示动画无限循环</em>
            }, () => {
              this.rotateAngle = 360 * 20 / 150;
            });
          })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
}
```
