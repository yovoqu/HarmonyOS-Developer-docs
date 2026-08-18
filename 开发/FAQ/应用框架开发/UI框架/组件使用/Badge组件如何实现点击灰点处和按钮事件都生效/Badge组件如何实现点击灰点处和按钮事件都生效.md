# Badge组件如何实现点击灰点处和按钮事件都生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1577

#### 问题现象

点击按钮蓝色部分才会响应点击事件，被灰点遮挡的部分点击无响应，如何实现点击灰点处和按钮事件都生效？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/e1Uvipy3RLuOLBkS635P0g/zh-cn_image_0000002658969083.png?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=052A62EB17C80159A3376B0E11180D5EFF5AF1E1043A3FB81725369DB2692FDD)

 
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
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bBuW0JoUSvuy4X3-OuBs3Q/zh-cn_image_0000002658849135.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=30C1C9500833C713E7837F46E58F4A6E8968507E7FF7CD6835BCF9F44134FE01)

 
 

#### 背景知识

- [Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)：信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

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
