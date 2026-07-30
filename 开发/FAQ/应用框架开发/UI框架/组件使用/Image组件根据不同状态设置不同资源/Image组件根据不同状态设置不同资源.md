# Image组件根据不同状态设置不同资源

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-756

#### 问题现象

如何根据三种不同状态设置不同的资源，如正常态，显示图片1，按压态显示图片2，不可用态显示图片3？
 
 

#### 背景知识

- 对于需要在应用中显示图片的场景，例如：按钮中的icon、网络图片、本地图片等。可以使用Image组件实现，Image支持多种图片格式，包括png、jpg、bmp、svg、gif和heif类型的图片格式，具体用法请参考[Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)。
- [stateStyles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles)可以依据组件的内部状态的不同，快速设置不同样式，目前提供了以下六种状态：
focused：获焦态。
- normal：正常态。
- pressed：按压态。
- disabled：不可用态。
- clicked：点击态。
- selected：选中态。

 - 触摸事件[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)可以识别手指在屏幕上的各种状态，如按压、抬起、移动等，更多状态请参考[TouchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#touchtype)。
- 长按手势[LongPressGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture#longpressgesture-1)在识别成功后会触发onAction事件回调，更多参考回调[事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture#事件)。

 
 

#### 解决方案

- **方案一**：通过stateStyles的normal、pressed、disabled实现，对三种状态设置不同的背景图。
```text
@Entry
@Component
struct Solution1 {
  @State imageEnable: boolean = true;

<em>  // 正常态</em>
  @Styles
  normalStyle() {
    .backgroundImage($r('app.media.normalStyle')); <em>// 运行时替换为实际图片资源</em>
  }

 <em> // 按压态</em>
  @Styles
  pressedStyle() {
    .backgroundImage($r('app.media.pressedStyle'));<em> </em><em>// 运行时替换为实际图片资源</em>
  }

  <em>// 不可用态</em>
  @Styles
  unableStyle() {
    .backgroundImage($r('app.media.unableStyle')); <em>// </em><em>运行时替换为实际图片资源</em>
  }

  build() {
    Column() {
      Button('控制是否可用')
        .onClick(() => {
          this.imageEnable = !this.imageEnable;
        })
        .margin({ bottom: 30 }); <em>// </em><em>按钮和图片之间的间距</em>

    <em>  // 使用stateStyles控制不同状态的图片显示</em>
      Column()
        .width(200)
        .height(200)
        .enabled(this.imageEnable)
        .backgroundImageSize({ width: 200, height: 200 })
        .backgroundImagePosition(Alignment.Center)
        .stateStyles({
          normal: this.normalStyle,
          disabled: this.unableStyle,
          pressed: this.pressedStyle
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

- **方案二**：通过onTouch的TouchType.Up与TouchType.Down实现正常态和按压态图片的切换。
```text
@Entry
@Component
struct Solution2 {
  @State imageSrc: Resource | string = $r('app.media.normalStyle'); <em>// </em><em>运行时替换为实际图片资源</em>

  build() {
    Column() {
   <em>   // 通过onTouch控制不同状态的图片显示</em>
      Image(this.imageSrc)
        .onTouch((e) => {
          if (e.type === TouchType.Up) {
          <em>  // 手指抬起后切换为常态图片</em>
            this.imageSrc = $r('app.media.normalStyle'); <em>// </em><em>运行时替换为实际图片资源</em>
          } else if (e.type === TouchType.Down) {
          <em>  // 手指按下后切换为按压态图片</em>
            this.imageSrc = $r('app.media.pressedStyle'); <em>// 运行时替换为实际图片资源</em>
          }
        })
        .width(200)
        .height(200);
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .backgroundColor(Color.White);
  }
}
```

- **方案三**：通过LongPress手势识别成功回调修改展示的图片。在onAction中更改为按压态图片资源，在onActionEnd中改回正常态图片资源。
```text
@Entry
@Component
struct Solution3 {
  @State imageSrc: Resource | string = $r('app.media.normalStyle');<em> </em><em>// 运行时替换为实际图片资源</em>

  build() {
    Row() {
      Image(this.imageSrc)
        .width(200).height(200)
        .gesture(
          LongPressGesture({ repeat: true, duration: 100 })
            .onAction(() => {
              this.imageSrc = $r('app.media.pressedStyle'); <em>// </em><em>运行时替换为实际图片资源</em>
            })
            .onActionEnd(() => {
              this.imageSrc = $r('app.media.normalStyle');<em> </em><em>// 运行时替换为实际图片资源</em>
            })
        );
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(VerticalAlign.Center);
  }
}
```
