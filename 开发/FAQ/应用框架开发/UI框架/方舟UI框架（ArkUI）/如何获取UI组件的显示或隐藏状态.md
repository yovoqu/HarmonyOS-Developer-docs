# 如何获取UI组件的显示或隐藏状态

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-30

- 方法1：使用if条件渲染，通过变量控制组件的显隐。使用@Watch监听变量，可以判断组件的显示状态。
- 方法2：组件显示或隐藏时，生命周期方法 aboutToAppear() 和 aboutToDisappear() 会触发，可以感知组件的显示状态。


具体可参考示例代码：

```ts
@Component
struct ComponentA {
aboutToAppear(): void {
// Perception components are visible and hidden
console.log('Component A display');
}

aboutToDisappear(): void {
// Perception components are visible and hidden
console.log('Component A hidden');
}

build() {
Column() {
Text('Component A').fontSize(16).fontColor(Color.Black);
}
.width(100)
.height(50)
}
}

@Entry
@Component
struct ComponentB {
@State @Watch('onCompAShowStatusChange') isShowA: boolean = false;
onCompAShowStatusChange() {
// Perception components are visible and hidden
console.log('Monitor component A：' + `${this.isShowA ? 'display' : 'hide'}`);
}

build() {
Column() {
Button('Switch between visible and hidden').type(ButtonType.Normal).width(100).height(50).onClick(() => {
this.isShowA = !this.isShowA;
})
if (this.isShowA) {
ComponentA();
}
}
}
}
```

参考链接

@Watch装饰器：状态变量更改通知、if/else：条件渲染
