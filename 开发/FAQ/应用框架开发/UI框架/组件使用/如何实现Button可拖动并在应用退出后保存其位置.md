# 如何实现Button可拖动并在应用退出后保存其位置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1544

#### 问题现象

页面有多个按钮，其中一个按钮用于控制按钮能否拖动，如何实现按钮可通过滑动手势改变位置，并在退出应用时保存按钮的位置。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/GMcxye4fQW6J3aoOozRiFg/zh-cn_image_0000002658848487.png?HW-CC-KV=V1&HW-CC-Date=20260701T041304Z&HW-CC-Expire=86400&HW-CC-Sign=1E77A0B30F81E075F3F2457A05B8894391F38AEE9DB5BCDE6C582F72BA1E5C11)

 
 

#### 背景知识

- 通用属性[translate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#translate)用于设置组件的平移，可使组件在以组件左上角为坐标原点的[组件坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-glossary#组件坐标系)中进行移动，如x大于0表示组件右移。
- [gesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings#gesture)可以为组件绑定手势，并根据手势动作触发回调。
- [PersistentStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage)可以持久化存储选定的[AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)属性，确保应用重新启动时能获取到持久化存储的属性值。

 
 

#### 解决方案

可以通过为组件绑定滑动手势[PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)，识别滑动动作，通过translate实现改变位置，并通过PersistentStorage持久化保存按钮组件的translate位移的值，使组件位置在应用重新启动时与关闭时一致。
 
- EntryAbility.ets文件，onWindowStageCreate中初始化PersistentStorage。
```json
onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    // 初始化PersistentStorage
    PersistentStorage.persistProp('customerFlag', false);
    PersistentStorage.persistProp('offsetX', 0);
    PersistentStorage.persistProp('offsetY', 0);
    PersistentStorage.persistProp('offset2X', 0);
    PersistentStorage.persistProp('offset2Y', 0);
  });
}
```

- Index.ets文件，获取持久化的按钮位置信息，实现滑动手势改变位置功能，并将新的按钮位置信息持久化。
```text
@Entry
@Component
struct Index {
  @State flag: boolean = false;
  positionX: number = 0;
  positionY: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State offset2X: number = 0;
  @State offset2Y: number = 0;

  aboutToAppear(): void {
    // AppStorage获取对应值
    this.flag = AppStorage.get<boolean>('customerFlag') ?? false;
    this.offsetX = AppStorage.get<number>('offsetX') ?? 0;
    this.offsetY = AppStorage.get<number>('offsetY') ?? 0;
    this.offset2X = AppStorage.get<number>('offset2X') ?? 0;
    this.offset2Y = AppStorage.get<number>('offset2Y') ?? 0;
  }

  build() {
    Column({ space: 10 }) {
      Row() {
        Button(this.flag ? '完成' : '自定义位置')
          .onClick(() => {
            this.flag = !this.flag;
            // AppStorage设置对应属性值
            AppStorage.setOrCreate('customerFlag', this.flag);
          });
      }
      .width('100%')
      .height(80)
      .justifyContent(FlexAlign.End)
      .margin({ right: 10 });

      Button('组件1')
        .zIndex(3)
        // 组件平移位置
        .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
        .gesture(
          // 绑定拖动手势
          PanGesture()
            .onActionStart(() => {
              this.positionX = this.offsetX;
              this.positionY = this.offsetY;
            }) // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
            .onActionUpdate((event: GestureEvent | undefined) => {
              if (!this.flag) {
                return;
              }
              if (event) {
                this.offsetX = this.positionX + event.offsetX;
                this.offsetY = this.positionY + event.offsetY;
              }
            })
            .onActionEnd(() => {
              // AppStorage设置对应属性值
              AppStorage.setOrCreate('offsetX', this.offsetX);
              AppStorage.setOrCreate('offsetY', this.offsetY);
            })
        );

      Button('组件2')
        .zIndex(2)
        // 组件平移位置
        .translate({ x: this.offset2X, y: this.offset2Y, z: 0 })
        .gesture(
          // 绑定拖动手势
          PanGesture()
            .onActionStart(() => {
              this.positionX = this.offset2X;
              this.positionY = this.offset2Y;
            }) // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
            .onActionUpdate((event: GestureEvent | undefined) => {
              if (!this.flag) {
                return;
              }
              if (event) {
                this.offset2X = this.positionX + event.offsetX;
                this.offset2Y = this.positionY + event.offsetY;
              }
            })
            .onActionEnd(() => {
              // AppStorage设置对应属性值
              AppStorage.setOrCreate('offset2X', this.offset2X);
              AppStorage.setOrCreate('offset2Y', this.offset2Y);
            })
        );
    }
    .height('100%')
    .width('100%');
  }
}
```
