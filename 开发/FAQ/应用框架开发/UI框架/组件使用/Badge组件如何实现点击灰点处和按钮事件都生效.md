# Badge组件如何实现点击灰点处和按钮事件都生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1577

## Badge组件如何实现点击灰点处和按钮事件都生效
 


##### 问题现象

点击按钮蓝色部分才会响应点击事件，被灰点遮挡的部分点击无响应，如何实现点击灰点处和按钮事件都生效？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/e1Uvipy3RLuOLBkS635P0g/zh-cn_image_0000002658969083.png?HW-CC-KV=V1&HW-CC-Date=20260701T025621Z&HW-CC-Expire=86400&HW-CC-Sign=C545231EFAFAF69AD8B3020618470DA56A06AFA9635023EAA8F46DC4D00721F7)

 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct BadgeClickTest {
  @State badgeCount: number = 80;

  build() {
    Stack() {
      Badge({
        count: this.badgeCount,
        maxCount: 99,
        position: { x: 90, y: 5 },
        style: {
          fontSize: '20vp',
          badgeColor: '#ddd',
          badgeSize: 30,
          borderWidth: 0
        }
      }) {
        Button('点击+1')
          .width(170)
          .padding({ left: 25 })
          .fontSize(18)
          .align(Alignment.Start)
          .onClick(() => {
            this.badgeCount += 1
          })
          .backgroundColor('#0D5AF5')
      }
    }.width('100%').height('100%')
  }
}
```
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bBuW0JoUSvuy4X3-OuBs3Q/zh-cn_image_0000002658849135.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025621Z&HW-CC-Expire=86400&HW-CC-Sign=FF61032422244CCD56EE500732F58842AA700D7D080C8CB17573A6FACF5912A0)

 
 

##### 背景知识

- [Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)：信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

##### 解决方案

将按钮点击事件迁移至Badge组件，可以实现点击灰点处和按钮事件都生效。
 
```text
@Entry
@Component
struct BadgeClickTest {
  @State badgeCount: number = 80;

  build() {
    Stack() {
      Badge({
        count: this.badgeCount,
        maxCount: 99,
        position: { x: 90, y: 5 },
        style: {
          fontSize: '20vp',
          badgeColor: '#ddd',
          badgeSize: 30,
          borderWidth: 0
        }
      }) {
        Button('点击+1')
          .width(170)
          .padding({ left: 25 })
          .fontSize(18)
          .align(Alignment.Start)
      }
      .onClick(() => {
        // 将按钮点击事件迁移至Badge组件
        this.badgeCount += 1;
      })
    }
    .width('100%')
    .height('100%')
  }
}
```
