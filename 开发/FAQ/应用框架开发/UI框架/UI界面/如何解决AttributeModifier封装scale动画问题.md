# 如何解决AttributeModifier封装scale动画问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1523

#### 问题现象

- **问题一**：使用AttributeModifier封装组件的弹出和消失动画，在实际使用过程中无动画效果。
```text
class FrameWorkAnimation implements AttributeModifier<CommonAttribute> {
  @Track scaleDialog: number = 1

  <em>// </em><em>弹窗退出时的动画</em>
  exitShowDialog(context: UIContext, onFinish: () => void) {
    this.scaleDialog = 1.0
    <em>// 弹窗展示时的帧动画</em>
    context.keyframeAnimateTo({
      iterations: 1, onFinish: () => {
        onFinish()
      }
    }, [{
      duration: 500,
      event: () => {
        this.scaleDialog = 0.5;
      }
    }]);
  }

 <em> // 开始展示弹窗</em>
  startShowDialog(context: UIContext) {
    this.scaleDialog = 0
    setTimeout(() => {
      <em>// </em><em>弹窗展示时的帧动画</em>
      context.keyframeAnimateTo({ iterations: 1 }, [
        {
          duration: 500,
          event: () => {
            this.scaleDialog = 1.0;
          }
        }
      ]);
    }, 200)
  }

  applyNormalAttribute(instance: CommonAttribute): void {
    instance.scale({
      x: this.scaleDialog,
      y: this.scaleDialog,
      centerX: '50%',
      centerY: '50%',
    })
  }
}
```

- **问题二**：为什么CommonModifier重写的onAppear和onDisAppear没有被调用，如何使其跟随绑定组件的生命周期调用？
```text
export class FrameWorkAnimation extends CommonModifier {
  scaleDialog: number = 0
  private uiContext?: UIContext

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext
  }

  onAppear(event: () => void): CommonAttribute {
    console.info('FrameWorkAnimation onAppear', event)
    return super.onAppear(event)
  }

  onDisAppear(event: () => void): CommonAttribute {
    console.info('FrameWorkAnimation onDisAppear', event)
    return super.onDisAppear(event)
  }
}
```


 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/saGXa9f8SqSqLjOd3Hp2cg/zh-cn_image_0000002628606986.png?HW-CC-KV=V1&HW-CC-Date=20260701T041209Z&HW-CC-Expire=86400&HW-CC-Sign=D0327473B9CE37EAAA02DFBA0C81A1F989AD51B8C51637DD21137661D7F2D1A9)

 
 

#### 背景知识

[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifiert)支持自定义class实现动态设置组件的属性，但不支持封装[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)属性。组件的布局类属性（如scale、rotate等）变化时的动画效果，无法用AttributeModifier封装。
 
 

#### 问题定位

- 问题一分析：调用FrameWorkAnimation的startShowDialog、exitShowDialog方法后会改变scaleDialog值，再通过scale属性控制组件的缩放实现动画效果，但是scale属于animation一类属性，AttributeModifier不支持封装。
- 问题二分析：FrameWorkAnimation重写了onAppear、onDisAppear方法，希望组件在创建和消失时调用。组件的生命周期是在运行时由开发框架在特定的时间进行调用。而AttributeModifier是一种属性修饰器，用于动态修改组件属性，在组件中使用AttributeModifier时，其onAppear等事件并不会跟随组件生命周期，而是作用于AttributeModifier本身。

 
 

#### 分析结论
1. AttributeModifier不支持封装组件的scale属性，所以无法实现动画效果。
2. AttributeModifier的onAppear、onDisAppear只作用于自身，不会跟随被绑定的组件生命周期。
 
 

#### 修改建议

不用AttributeModifier封装，直接使用class封装startShowDialog、exitShowDialog方法，在组件尾部直接调用scale方法，在startShowDialog中修改scaleDialog后，变化同步至scale，实现动画效果。通过export关键字可将封装的class导出，即可在别的文件中调用。
 
```text
<em>// </em><em>动画封装类</em>
export class AnimateTest {
  @Track scaleDialog: number;

  constructor(num: number) {
    this.scaleDialog = num;
  }

 <em> // 缩小按钮的帧动画</em>
  startAnimate(context: UIContext) {
    context.keyframeAnimateTo({ iterations: 1 }, [
      {
        duration: 500,
        event: () => {
          this.scaleDialog = 0.5;
        }
      }
    ]);
  }
}

@Entry
@Component
struct AttributeModifierAnimateDemo {
  @State message: string = 'Button';
  @State animate: AnimateTest = new AnimateTest(3);

  build() {
    Column() {
      Button(this.message)
        .backgroundColor('#0A59F7')
        .width(70)
        .height(100)
        .scale({
         <em> // 监听动画类中scaleDialog变化来缩放</em>
          x: this.animate.scaleDialog,
          y: this.animate.scaleDialog,
          centerX: '50%',
          centerY: '50%'
        })
        .onClick(() => {
          this.message = 'Button2';
          let context = this.getUIContext();
        <em>  // 开始动画</em>
          this.animate.startAnimate(context);
        });
    }.height('100%').width('100%').justifyContent(FlexAlign.Center);
  }
}
```
