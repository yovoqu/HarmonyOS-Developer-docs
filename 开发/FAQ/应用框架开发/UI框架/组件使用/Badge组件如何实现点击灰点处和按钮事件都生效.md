# Badge组件如何实现点击灰点处和按钮事件都生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1577

#### 问题现象

点击按钮蓝色部分才会响应点击事件，被灰点遮挡的部分点击无响应，如何实现点击灰点处和按钮事件都生效？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/e1Uvipy3RLuOLBkS635P0g/zh-cn_image_0000002658969083.png?HW-CC-KV=V1&HW-CC-Date=20260701T041239Z&HW-CC-Expire=86400&HW-CC-Sign=7FF88C564559BFB61829A102C337F5DFD46E61CDA010EF043AF2F32F5CE1502F)

 
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


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bBuW0JoUSvuy4X3-OuBs3Q/zh-cn_image_0000002658849135.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041239Z&HW-CC-Expire=86400&HW-CC-Sign=0A84D816994B4D868FB047F8EAE64ACE666938ED027433B2B6DC421DFEDCCD6B)

 
 

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
        <em>// </em><em>将按钮点击事件迁移至Badge组件</em>
        this.badgeCount += 1;
      })
    }
    .width('100%')
    .height('100%')
  }
}
```
