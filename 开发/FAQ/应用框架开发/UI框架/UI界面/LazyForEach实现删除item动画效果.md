# LazyForEach实现删除item动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-910

## LazyForEach实现删除item动画效果
 


##### 问题现象

通过LazyForEach管理的数据源，使用List展示，当数据源删除一个数据后，如何实现item从右往左的删除动画。
 
 

##### 效果预览

LazyForEach删除item：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/j-msylLeRWWG4xysWgm6Eg/zh-cn_image_0000002628399760.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025654Z&HW-CC-Expire=86400&HW-CC-Sign=2DF99F41B9B33BC00BF4B21B66B16074AFE3DB512B103C908E6FC66FE326C8F4)

 
 

##### 背景知识

- [组件内转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)可以用于实现容器组件中的子组件插入和删除时的动画效果。
- [LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)从提供的数据源中按需迭代数据，数据源类型为IDataSource，需要开发者实现相关接口。

 
 

##### 解决方案

CustomDataSource实现了LazyForEach提供的IDataSource接口，将其作为LazyForEach的数据源，然后管理监听器和更新数据。
 
```text
export class CustomDataSource implements IDataSource {
  data: string[] = ['Item 0', 'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'];
  private listeners: DataChangeListener[] = [];

  // 获取数据总数
  totalCount(): number {
    return this.data.length;
  }

  // 获取指定索引数据
  getData(index: number): string {
    return this.data[index];
  }

  // 删除数据方法
  deleteData(index: number) {
    if (index >= 0 && index  this.data.length) {
      this.data.splice(index, 1);
      this.notifyDataDelete(index);
    }
  }

  // 注册数据变化监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener)  0) {
      this.listeners.push(listener);
    }
  }

  // 注销数据变化监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  // 通知数据删除
  private notifyDataDelete(index: number) {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }
}
```
 
在AnimatedPage的ListItem实现从右向左的删除动画，点击Button按钮会执行deleteItem方法。deleteItem方法中，调用[transition()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)在删除时显示过渡动效，与visibility属性配合对目标删除组件进行隐藏，但参与布局进行占位，延迟250毫秒后，执行播放数据删除的动画。
 
```text
@Entry
@Component
struct AnimatedPage {
  private dataSource = new CustomDataSource();
  @State toBeDeletedItem: string = ''; // 待删除的Index

  build() {
    Column() {
      Button('delete item')
        .onClick(() => this.deleteItem(0))
        .margin('16vp');
      List({ space: 10 }) {
        LazyForEach(this.dataSource, (item: string) => {
          ListItem() {
            Text(item).fontSize(20).height(30);
          }
          .width('100%')
          .height('62vp')
          .backgroundColor('#F1F3F5')
          .borderRadius(5)
          .visibility(this.toBeDeletedItem === item ? Visibility.Hidden : Visibility.Visible)
          .transition(TransitionEffect.opacity(0.5) // 删除动画实现
            .combine(TransitionEffect.translate({ x: '-100%' })));
        }, (item: string) => item);
      }
      .padding(16);
    };
  }

  deleteItem(index: number) {
    // 配合visibility对组件隐藏，但参与布局进行占位。
    this.getUIContext().animateTo({ duration: 250 }, () => {
      this.toBeDeletedItem = this.dataSource.getData(index);
    });
    // 删除数据
    this.getUIContext().animateTo({ duration: 250, delay: 250 }, () => {
      this.dataSource.deleteData(index);
    });
  }
}
```
