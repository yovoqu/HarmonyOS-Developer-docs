# Image组件长按和拖拽的系统手势和自定义手势冲突

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-365

开发者可根据业务逻辑，使用parallelGesture或者priorityGesture绑定，解决自定义手势与系统手势之间的冲突。
 
系统默认手势效果保留，自定义的LongPressGesture和panGesture手势也能响应，使用parallelGesture绑定。
 
**参考代码****：**
 
```text
@Entry
@Component
struct Index {
  build() {
    Column() {
      Image($r('app.media.app_icon'))
        .width('80%')
        .parallelGesture(GestureGroup(GestureMode.Exclusive,
          TapGesture({ count: 2, fingers: 1 })
        <em>  // Double click</em>
            .onAction(() => {
              console.log('TapGesture--double click');
            }),
          TapGesture({ count: 1, fingers: 1 })
       <em>   // TapGesture single</em>
            .onAction(() => {
              console.log('TapGesture--single click');
            }),
          LongPressGesture({ repeat: true })
        <em>  // LongPressGesture Long</em>
            .onAction(() => {
              console.log('LongPressGesture--Long press');
            }),
          PanGesture()
        <em>  // PanGesture drag</em>
            .onActionStart((gestureEvent: GestureEvent | undefined) => {
              console.info('PanGesture--drag');
            })
        ))
    }
    .height('100%')
    .width('100%')
  }
}
```
 
**参考链接**
 
[绑定手势方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding)
