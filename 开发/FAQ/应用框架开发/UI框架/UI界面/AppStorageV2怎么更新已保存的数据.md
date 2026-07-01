# AppStorageV2怎么更新已保存的数据

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1336

## AppStorageV2怎么更新已保存的数据
 


##### 问题现象

AppStorageV2只有connect、remove、keys方法，没有update更新方法，如何更新已保存的数据？每次更新是否需要remove后再保存新的数据？
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/L_jr2R-LTAKGBJEQw6flKA/zh-cn_image_0000002628600020.png?HW-CC-KV=V1&HW-CC-Date=20260701T025700Z&HW-CC-Expire=86400&HW-CC-Sign=B2B1B36EFF4C8DA75D9DD41C2BFD243BEA9FF463A9939218FA037B017CC2A806)

 
 

##### 背景知识

[AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement#appstoragev2)是在应用UI启动时会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorageV2将在应用运行过程保留其数据。数据通过唯一的键字符串值访问。
 
 

##### 解决方案

AppStorageV2当前并未提供更新接口，开发者可以先connect获取已保存的对象，然后直接给对象的属性赋值就可以实现数据更新，示例代码如下：
 
```text
import { AppStorageV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Page {
  promptAction = this.getUIContext().getPromptAction();

  aboutToAppear(): void {
    AppStorageV2.connect(Sample, () => new Sample())!;
  }

  build() {
    Column({ space: 10 }) {
      Button('AppStorageV2 update')
        .onClick(() => {
          let sample = AppStorageV2.connect(Sample, () => new Sample())!;
          sample.p1 = 100;
        });
      Button('AppStorageV2 get value')
        .onClick(() => {
          let sample = AppStorageV2.connect(Sample, () => new Sample())!;
          this.promptAction.showToast({ message: 'p1 =' + sample.p1 });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}

@ObservedV2
export class Sample {
  p1: number = 0;
}
```
 
 

##### 常见FAQ

Q：AppStorageV2如何保存简单的string、number、boolean等变量？
 
A：AppStorageV2局限性详见[使用限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2#使用限制)。字符串等简单数据保存可参考以下方式：
 
- 参考“解决方案”，将数字（number）等基本类型封装为类。
- 可以使用String、Number等构造类型：@Local prop: String = AppStorageV2.connect(String, () => new String('test'))!;

 
Q：若AppStorageV2与AppStorage使用相同的Key获取与储存数据是否会导致冲突？
 
A：AppStorageV2与AppStorage使用相同的Key并不会导致冲突。
 
Q：@Monitor如何监听AppStorageV2保存的数据的修改？
 
A：AppStorageV2的connect方法绑定状态变量后，状态变量的修改会同步到AppStorageV2内，可以通过监听该状态变量的修改实现AppStorageV2的修改监听。
