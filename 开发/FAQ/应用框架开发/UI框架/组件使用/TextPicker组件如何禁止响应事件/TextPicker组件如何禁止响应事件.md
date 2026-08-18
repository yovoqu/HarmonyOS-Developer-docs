# TextPicker组件如何禁止响应事件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-734

#### 问题现象

TextPicker组件如何禁止所有响应事件，或者禁止指定响应事件？
 
 

#### 背景知识

- [enabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable#enabled)：用于控制事件交互，值为true表示组件可交互，值为false表示组件不可交互。
- [onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)：用于自定义手势判定。

 
 

#### 解决方案
1. 禁止组件的全部响应事件，可以配置enabled属性值为false使TextPicker组件不可交互，不响应事件。
```text
@Entry
@Component
struct TextPickerExample1 {
  private select: number = 1;
  private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        // 核心代码：交互能力（false）
        .enabled(false)
        .margin({ bottom: 30 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/J9yH8ZgURXK_hwdbLJmQpQ/zh-cn_image_0000002658794593.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=6C2369A677D58D9DA16507E5098F4C9E78086197944A7EE40327CD897477F618)

2. 禁止组件指定的响应事件，可以通过onGestureJudgeBegin自定义手势判定函数，自主决定是否响应。如下相关代码实现了当前TextPicker的选中项点击事件被禁止，而不影响对其他手势事件的响应。
```text
@Entry
@Component
struct TextPickerExample2 {
  private select: number = 0;
  private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits[this.select]
      })
        .margin({ bottom: 30 })
          // 核心代码：判断是否为点击事件，使用长按做对比
        .gesture(
          LongPressGesture()
            .tag('longPress1') // 设置长按手势标志
            .onAction(() => {
              console.info('长按longPress');
            })
        )
        .gesture(
          TapGesture()
            .tag('tap1') // 设置点击手势标志
            .onAction(() => {
              console.info('点击tap1');
            })
        )
        .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
          if (gestureInfo.type === GestureControl.GestureType.TAP_GESTURE) {
            // 返回REJECT会使点击手势失败
            console.info(`REJECT 点击已禁用  event: ${event}`);
            return GestureJudgeResult.REJECT;
          } else {
            // 返回CONTINUE将保持系统判定。
            console.info(`CONTINUE 保持系统判定`);
            return GestureJudgeResult.CONTINUE;
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/kaYeAGqgSA6oT0E67IfBhw/zh-cn_image_0000002628555226.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=B2FA0FBFC66E3C049213C6136E0FBC9D2A716501905B8D999E5A442E43186BBB)


  以长按手势为例，区分是否禁用对应的手势。代码中设置点击手势标志：“点击tap1”无打印，长按手势标志打印：“长按longPress”。

  日志如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/FIITL8SZTjGzuUADcSZJeg/zh-cn_image_0000002658914549.png?HW-CC-KV=V1&HW-CC-Date=20260811T005754Z&HW-CC-Expire=86400&HW-CC-Sign=BD88F2D93E598F3AE16FC6740CD45F4BF64F63FC9F56D496BDCF8D8FEB1038EB)

 
 

#### 总结

若需全局禁用组件交互行为，建议优先使用enabled属性，该属性可直接禁用所有事件响应。对于需要选择性禁用特定交互事件的场景，可通过onGestureJudgeBegin方法进行自定义是否响应特定事件。
