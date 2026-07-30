# 怎么解决Progress组件配合animateTo实现循环动画无反应问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-508

#### 问题现象

使用Progress组件配合animateTo来实现进度条循环动画，动画效果失效无反应。
 
```text
<em>/** </em><em>进度条最小值 */</em>
const PROGRESS_MIN1 = 0;
<em>/** </em><em>进度条最大值 */</em>
const PROGRESS_MAX1 = 100;

@Entry
@Component
struct ProgressAnimWithProblem {
<em>  /** 进度条当前值 */</em>
  @State progressValue: number = PROGRESS_MIN1;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    };
    this.uiContext?.animateTo({
      duration: 2000,
      iterations: -1, <em>// 设置-1表示动画无限循环</em>
    }, () => {
      this.progressValue = PROGRESS_MAX1;
    });
  };

  build() {
    Column({ space: 15 }) {
      Progress({
        value: this.progressValue, <em>// 进度条当前进度值</em>
        total: PROGRESS_MAX1, <em>// </em><em>进度条总长</em>
        type: ProgressType.Ring, <em>// </em><em>进度条类型，分为Linear线性样式、ScaleRing环形有刻度样式、Ring环形无刻度样式、Eclipse圆形样式、Capsule</em><em>胶囊样式</em>
      })
        .style({
          strokeWidth: 10, <em>// 进度条宽度，默认4vp</em>
          enableSmoothEffect: true <em>// </em><em>进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值true</em>
        })
        .width(100) <em>// 进度条组件宽度</em>
        .color('#0A59F7')<em> </em><em>// 进度条前景色</em>
        .backgroundColor(Color.White);<em> </em><em>// 进度条背景色</em>
    }
    .width('100%')
    .height('100%')
    .padding({ top: 5 })
    .justifyContent(FlexAlign.Center);
  };
};
```
 
 

#### 背景知识

- [进度条（Progress）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator)：用于显示内容加载或操作处理等进度。可以有多种表现形式，官方提供胶囊型、环形有刻度、环形无刻度、圆形，且支持自定义图形样式。
- 显式动画（animateTo）：提供全局[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、Canvas的内容等。
- [定时器（Timer）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer)：[setInterval()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#setinterval)方法重复调用一个函数，在每次调用之间具有固定的时间延迟。此方法创建一个定时器并返回该定时器ID，删除该定时器需要手动调用[clearInterval()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#clearinterval)。

 
 

#### 问题定位

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），问题代码使用animateTo改变Progress组件的进度值，结果是进度条从0到100动画仅执行一次。可见不支持使用animateTo控制Progress组件进度条循环效果。
 
 

#### 分析结论

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），不支持使用animateTo控制Progress组件进度值变化来实现进度条循环效果。
 
 

#### 修改建议

可以使用定时器来控制Progress组件进度值变化。用setInterval()方法创建定时任务，每间隔一段时间（如20毫秒）均匀地改变Progress组件进度值（如每次加1），即可实现预期效果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/6PBO4eIsSv-yFu51GT99tw/zh-cn_image_0000002628388622.png?HW-CC-KV=V1&HW-CC-Date=20260730T072317Z&HW-CC-Expire=86400&HW-CC-Sign=0776012EF1B918A89A5A500E38BF22A6980FFF3FBA181DEE93DDCB44FF4E37DA)

 
```text
<em>/** </em><em>进度条最小值 */</em>
const PROGRESS_MIN = 0;
<em>/** </em><em>进度条最大值 */</em>
const PROGRESS_MAX = 100;

@Entry
@Component
struct ProgressAnim {
 <em> /** 进度条当前值 */</em>
  @State progressValue: number = PROGRESS_MIN;


  aboutToAppear(): void {
  <em>  // 进入界面时即启动进度条动画</em>
    this.startAnim();
  };

  build() {
    Column({ space: 15 }) {
      Progress({
        value: this.progressValue,<em> </em><em>// 进度条当前进度值</em>
        total: PROGRESS_MAX,<em> </em><em>// 进度条总长</em>
        type: ProgressType.Ring, <em>// 进度条类型，分为Linear线性样式、ScaleRing环形有刻度样式、Ring环形无刻度样式、Eclipse圆形样式、Capsule</em><em>胶囊样式</em>
      })
        .style({
          strokeWidth: 10, <em>// </em><em>进度条宽度，默认4vp</em>
          enableSmoothEffect: true <em>// </em><em>进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值true</em>
        })
        .width(100)<em> </em><em>// 进度条组件宽度</em>
        .color('#0A59F7') <em>// 进度条前景色</em>
        .backgroundColor(Color.White);<em> </em><em>// 进度条背景色</em>
    }
    .width('100%')
    .height('100%')
    .padding({ top: 5 })
    .justifyContent(FlexAlign.Center);
  };

 <em> // 开启进度条动画</em>
  private startAnim() {
   <em> // intervalId为null时表示未启动interval</em>
    setInterval(() => {
      <em>// 使用setInterval()方法重复执行以下代码片段，在每次调用之间具有固定的时间间隔20毫秒</em>
<em>      // 每次进度值+1</em>
      this.progressValue++;
     <em> // 当进度值达到最大值时，将进度值重置为最小值，循环往复</em>
      if (this.progressValue == PROGRESS_MAX) {
        this.progressValue = PROGRESS_MIN;
      };
    }, 20);
  };
};
```
