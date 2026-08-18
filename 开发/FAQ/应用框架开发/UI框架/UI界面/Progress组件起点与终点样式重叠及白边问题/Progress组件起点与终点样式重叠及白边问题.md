# Progress组件起点与终点样式重叠及白边问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-522

#### 问题现象

采用Progress组件设置环形进度条，运行时存在以下问题：
 1. 进度值为100时起点与终点样式重叠形成一个点，如何使该点消失。
2. 进度条已经走过的边上有一点白边，如何去掉该白边？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
export struct Index {
  @State remainingTime: number = 0; // 剩余时间（默认10秒）

  aboutToAppear(): void {
    let timer: number
    timer = setInterval(() => {
      this.remainingTime += 1
      if (this.remainingTime == 100) {
        clearInterval(timer)
      }
    }, 50)
  }

  build() {
    Column() {
      Stack() { // 创建垂直布局容器
        Column() {
          Progress({
            value: this.remainingTime, // 设置进度
            total: 100, // 最大进度为100
            type: ProgressType.Ring, // 使用环形进度条
          })
            .style({ strokeWidth: 20 })
            .rotate({ angle: 90 })
            .color('#800a59f7')
            .backgroundColor('#fff')
            .width(300)
            .aspectRatio(1)
            .animation({ duration: 10 })
        }
        .justifyContent(FlexAlign.Center)
        .borderRadius(200)
        .backgroundColor(`rgba('10, 89, 247, 0.5')`)
      }
      .width(350)
      .aspectRatio(1)
      .borderRadius(200)
      .backgroundColor('#800a59f7')
      .alignContent(Alignment.Center)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/pn35qMjmShaL6gd9Tq9bpw/zh-cn_image_0000002658790419.png?HW-CC-KV=V1&HW-CC-Date=20260811T005646Z&HW-CC-Expire=86400&HW-CC-Sign=569D192EE1BCEB5F6B2E8CCC5C70F3F2D2CB6CCCAE14FB29FACBD96BA9A230FE)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/iw3bZYZqTsy6d0u-npmOoA/zh-cn_image_0000002628551060.png?HW-CC-KV=V1&HW-CC-Date=20260811T005646Z&HW-CC-Expire=86400&HW-CC-Sign=505129877D184FC17E0CC6CA1453AA4454358F2873F3BC48C39E9CFBF1B634DA)

 
 

#### 背景知识

[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)进度条组件，用于显示内容加载或操作处理等进度。Progress组件的[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundcolor)属性是直接添加在Progress组件上，生效进度条的底色。如需设置整个Progress组件的背景色，需要在外层容器上设置backgroundColor，并将Progress组件嵌入到容器中。
 
 

#### 解决方案
1. 针对问题一的解决方案：外层Stack容器的backgroundColor和Progress组件进度条颜色设置了透明度，颜色叠加导致进度值为100时起点与终点样式重叠形成一个点。建议将外层Stack容器的backgroundColor和Progress组件底色设置成相同且不透明的颜色。
2. 针对问题二的解决方案：设置进度条前景色为白色，Progress组件底色设置与外层容器相同，进度值改为从100到0，由此解决白边的问题。此时进度条旋转方向与原代码相反，设置direction(Direction.Rtl)翻转Progress组件，实现与原效果一致。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct ProgressIndex {
  @State remainingTime: number = 100;

  aboutToAppear(): void {
    let timer: number;
    timer = setInterval(() => {
      this.remainingTime--;
      if (this.remainingTime === 0) {
        clearInterval(timer);
      }
    }, 50);
  }

  build() {
    Column() {
      Stack() { // 创建垂直布局容器
        Column() {
          Progress({
            value: this.remainingTime, // 设置进度
            total: 100, // 最大进度为100
            type: ProgressType.Ring, // 使用环形进度条
          })
            .style({ strokeWidth: 20 })
            .rotate({ angle: 90 })
            // 设置进度条前景色为白色
            .color('#fff')
            // 1、问题一，将外层容器backgroundColor和Progress组件底色设置成相同且不透明的颜色
            // 2、Progress组件底色设置与外层容器相同
            .backgroundColor('#0a59f7')
            // 设置翻转
            .direction(Direction.Rtl)
            .width(300)
            .aspectRatio(1)
            .animation({ duration: 10 });
        }
        .justifyContent(FlexAlign.Center)
        .borderRadius(200);
      }
      .width(350)
      .aspectRatio(1)
      .borderRadius(200)
      // 问题一与问题二都需将外层容器backgroundColor修改为不透明相同颜色
      .backgroundColor('#0a59f7')
      .alignContent(Alignment.Center);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
