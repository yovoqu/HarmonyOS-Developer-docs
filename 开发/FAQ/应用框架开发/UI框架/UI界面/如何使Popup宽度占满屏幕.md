# 如何使Popup宽度占满屏幕

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-814

#### 问题现象

使用bindPopup创建气泡弹窗，如何使气泡弹窗的宽度占满屏幕？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Aw-h4j1FRdOFbpS20ssYvg/zh-cn_image_0000002658917117.png?HW-CC-KV=V1&HW-CC-Date=20260701T041155Z&HW-CC-Expire=86400&HW-CC-Sign=A0AF559090FF3DE1B012875D8C78EF872E7475BC5FA97A31260B3F1726DBFA31)

 
 

#### 背景知识

[bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)方法中填入的Popup参数有两种类型，[PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)和[CustomPopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8类型说明)：
 
- PopupOptions依靠文本信息构建内容，样式相对固定。
- CustomPopupOptions通过自定义构建函数@Builder构建内容。

 
 

#### 解决方案

选用CustomPopupOptions类型的参数，并依靠自定义构建函数@Builder构建内容。
 
将CustomPopupOptions中的width设为100%：
 
```text
@Entry
@Component
struct PopupWidth {
  @State handlePopup: boolean = false;

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Text('Custom Popup').fontSize(12);
    }.width(100).height(50).padding(5);
  }

  build() {
    Column({ space: 100 }) {
      Button('CustomPopupOptions中width设置为100%')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          width: '100%',
          builder: this.popupBuilder,
          arrowPointPosition: ArrowPointPosition.START, <em>// </em><em>设置箭头的位置</em>
          backgroundBlurStyle: BlurStyle.NONE, <em>// </em><em>关闭气泡的模糊背景</em>
          autoCancel: true,
        });
    }
    .margin({ top: 50 })
    .width('100%');
  }
}
```
 
 

#### 常见FAQ

Q：使用Popup时，创建监听，会导致崩溃，是什么原因？
 
```text
aboutToAppear(): void {
  this.listener.on('draw', () => {
    this.pageMainContentHeight = componentUtils.getRectangleById('pageMainContent').size.height<em> </em><em>// 单位是px</em>
  })
}
```
 
A：使用Popup时要手动取消监听。
 
```text
aboutToDisappear() {
 <em> // Unregister callback before destruction</em>
  this.listener.off('draw', () => {});
}
```
