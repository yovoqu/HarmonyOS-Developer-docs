# 修改被@State修饰的gesture属性参数不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-640

#### 问题现象

对手势属性进行修改时，绑定手势gesture没有生效，如何解决该问题？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct PinchGesturePage {
  @State scaleValue: number = 1;
  private lastScale: number = 1;
  @State isGesture: boolean = false;

  build() {
    Stack() {
      Row()
        .width(200)
        .height(200)
        .margin({ top: 50 })
        .backgroundColor('#61CFBE')
        .scale(this.isGesture ? { x: this.scaleValue, y: this.scaleValue, z: 1 } : null)
        .gesture(this.isGesture ?
        PinchGesture({ fingers: 2 })
          .onActionStart(() => {
            <em>// 在手势开始时，记录当前的缩放比例</em>
            this.lastScale = this.scaleValue;
          })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
             <em> // 计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例</em>
              let newScale = this.lastScale * event.scale;
             <em> // 进行边界检查</em>
              if (newScale < 1) {
                newScale = 1;
              } else if (newScale > 5) {
                newScale = 5;
              }
              <em>// </em><em>更新缩放值</em>
              this.scaleValue = newScale;
            }
          })
          .onActionEnd(() => {
          <em>  // 手势结束时，不需要特殊处理</em>
          }) : null
        );
      Row()
        .width(200)
        .height(200)
        .onClick(() => {
          this.isGesture = true;
          console.info(`TWT->onClick ${this.isGesture}`);
        })
        .hitTestBehavior(HitTestMode.Transparent)
        .backgroundColor('#5291FF');
    }
    .height('100%')
    .width('100%');
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/SRfFAAEARqO1_x-q9mr1KA/zh-cn_image_0000002628554400.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072322Z&HW-CC-Expire=86400&HW-CC-Sign=F054C5E75A45FFE56AAA22AA9845B6C6A0693DB87CC60DE6540BB8C86DE15712)

 
 

#### 背景知识

[自定义手势判定](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge)为组件提供自定义手势判定能力。开发者可根据需要，在手势识别期间，决定是否响应手势。
 
 

#### 问题定位

问题代码中通过this.isGesture的值判断是否执行手势事件。但参考[绑定手势方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings)的说明部分，gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。
 
 

#### 分析结论

gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。但是可以通过[onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)来进行判断并决定是否识别手势。
 
 

#### 解决方案

使用手势拦截onGestureJudgeBegin来判断是否识别手势。
 
```text
@Entry
@Component
struct PinchGesturePage {
  @State scaleValue: number = 1;
  private lastScale: number = 1;
  @State isGesture: boolean = false;

  build() {
    Stack() {
      Row()
        .width(400)
        .height(400)
        .margin({ top: 50 })
        .backgroundColor('#61CFBE')
        .scale(this.isGesture ? { x: this.scaleValue, y: this.scaleValue, z: 1 } : null)
        .onGestureJudgeBegin(() => {
          if (this.isGesture) {
            return GestureJudgeResult.CONTINUE;
          } else {
            return GestureJudgeResult.REJECT;
          }
        })
        .gesture(PinchGesture({ fingers: 2 })
          .onActionStart(() => {
          <em>  // 在手势开始时，记录当前的缩放比例</em>
            console.info(`The lastScale is ${this.lastScale}`);
            this.lastScale = this.scaleValue;
          })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
            <em>  // 计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例</em>
              let newScale = this.lastScale * event.scale;
            <em>  // 进行边界检查</em>
              if (newScale < 1) {
                newScale = 1;
              } else if (newScale > 5) {
                newScale = 5;
              }
             <em> // 更新缩放值</em>
              this.scaleValue = newScale;
              console.info(`The newScale is ${this.scaleValue}`);
            }
          })
          .onActionEnd(() => {
         <em>   // 手势结束时，不需要特殊处理</em>
            console.info('The action is end');
          })
        );
      Row()
        .width(400)
        .height(400)
        .onClick(() => {
          this.isGesture = true;
          console.info(`TWT->onClick ${this.isGesture}`);
        })
        .hitTestBehavior(HitTestMode.Transparent)
        .backgroundColor('#5291FF');
    }
    .height('100%')
    .width('100%');
  }
}
```
