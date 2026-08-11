# @State修饰单例模式实例时无法刷新UI

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-557

#### 问题现象

@State修饰一个单例模式类的实例时，变更该实例中的属性，UI没有刷新。
 
效果演示如下：在Page2中改变颜色后，返回Index页面，颜色没有同步刷新。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/jOYxSf0iS_WMHFSNf6Rnjw/zh-cn_image_0000002628392114.png?HW-CC-KV=V1&HW-CC-Date=20260811T005640Z&HW-CC-Expire=86400&HW-CC-Sign=61DC835323E5D43043293E3BAFFE93AA994B73610E2702A7CC29C8C10E7F7FA8)

 
问题代码如下：
 
```ArkTS
<em>// Index.ets</em>
import { VoiceReadHelper } from './VoiceReadHelper';

@Entry
@Component
struct Index {
  @State private voiceReadHelper: VoiceReadHelper = VoiceReadHelper.getInstance();

  build() {
    Column() {
      Text()
        .width(100)
        .height(100)
        .backgroundColor(this.voiceReadHelper.isSpeaking ? '#61CFBE' : '#8981F7')
        .borderRadius(8)
        .margin({ bottom: 100 })
        .onClick(() => {
          this.voiceReadHelper.isSpeaking = !this.voiceReadHelper.isSpeaking;
        });

      Text('去Page2').onClick(() => {
        this.getUIContext().getRouter().pushUrl({ url: 'pages/Page2' });
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
 
```ArkTS
<em>// Page2.ets</em>
import { VoiceReadHelper } from './VoiceReadHelper';

@Entry
@Component
struct Page2 {
  @State private voiceReadHelper: VoiceReadHelper = VoiceReadHelper.getInstance();

  build() {
    Column() {
      Text()
        .width(100)
        .height(100)
        .backgroundColor(this.voiceReadHelper.isSpeaking ? '#61CFBE' : '#8981F7')
        .borderRadius(8)
        .margin({ bottom: 100 })
        .onClick(() => {
          this.voiceReadHelper.isSpeaking = !this.voiceReadHelper.isSpeaking;
        });

      Text('这是Page2');
    }
    .height('100%')
    .width('100%');
  }
}
```
 
```text
export class VoiceReadHelper {
  private static instance: VoiceReadHelper | null = null;
  isSpeaking = false;

  private constructor() {
  }

  static getInstance(): VoiceReadHelper {
    if (VoiceReadHelper.instance == null) {
      VoiceReadHelper.instance = new VoiceReadHelper();
    }
    return VoiceReadHelper.instance;
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/j554BvMuSCmy8fa8g5CMew/zh-cn_image_0000002658791395.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005640Z&HW-CC-Expire=86400&HW-CC-Sign=38A56CEB96D45EFE796E43117B033A461EACC8AF758760FD8AAFDC2043C36167)

 
 

#### 背景知识

- [@State装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)修饰一个状态变量，若变量是类时可以观察到第一层属性变化，同时该变量改变时UI可以同步刷新。但@State通过getInstance函数获取实例时，虽然修改其属性时可以在本页面内进行UI刷新，但是无法跨页面进行同步，即其他页面无法在UI层面上感知到属性变化，此时可以借助[@Observed装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)进行同步与共享。
- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)可以实现应用级的状态共享，[@StorageLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage#storagelink)修饰的变量发生变化时，该变化会被写回AppStorage中。

 
 

#### 解决方案

- **方案一**：由于@State装饰的是VoiceReadHelper的实例对象，需要给类VoiceReadHelper添加@Observed装饰器，才能使@State装饰器观察到其中属性的变化。
```text
@Observed
export class VoiceReadHelper {
  private static instance: VoiceReadHelper | null = null;
  isSpeaking = false;

  private constructor() {
  }

  static getInstance(): VoiceReadHelper {
    if (VoiceReadHelper.instance == null) {
      VoiceReadHelper.instance = new VoiceReadHelper();
    }
    return VoiceReadHelper.instance;
  }
}
```

- **方案二**：可以将该实例存入AppStorage中，通过@StorageLink同步组件状态。1. 创建VoiceReadHelper的实例时，将该实例存入AppStorage中。
```text
export class VoiceReadHelper {
  private static instance: VoiceReadHelper | null = null;
  isSpeaking = false;

  private constructor() {
  }

  static getInstance(): VoiceReadHelper {
    if (VoiceReadHelper.instance == null) {
      VoiceReadHelper.instance = new VoiceReadHelper();
      AppStorage.setOrCreate('voiceReadHelper', VoiceReadHelper.instance);
    }
    return VoiceReadHelper.instance;
  }
}
```


2. 在页面中使用@StorageLink修饰VoiceReadHelper实例，建立数据的双向同步。
```ArkTS
<em>// Index.ets</em>
import { VoiceReadHelper } from './VoiceReadHelper';

@Entry
@Component
struct Index {
  @StorageLink('voiceReadHelper') voiceReadHelper: VoiceReadHelper = VoiceReadHelper.getInstance();

  build() {
    Column() {
      Text()
        .width(100)
        .height(100)
        .backgroundColor(this.voiceReadHelper.isSpeaking ? '#61CFBE' : '#8981F7')
        .borderRadius(8)
        .margin({ bottom: 100 })
        .onClick(() => {
          this.voiceReadHelper.isSpeaking = !this.voiceReadHelper.isSpeaking;
        });

      Text('去Page2').onClick(() => {
        this.getUIContext().getRouter().pushUrl({ url: 'pages/Page2' });
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
 
```ArkTS
<em>// Page2.ets</em>
import { VoiceReadHelper } from './VoiceReadHelper';

@Entry
@Component
struct Page2 {
  @StorageLink('voiceReadHelper') voiceReadHelper: VoiceReadHelper = VoiceReadHelper.getInstance();

  build() {
    Column() {
      Text()
        .width(100)
        .height(100)
        .backgroundColor(this.voiceReadHelper.isSpeaking ? '#61CFBE' : '#8981F7')
        .borderRadius(8)
        .margin({ bottom: 100 })
        .onClick(() => {
          this.voiceReadHelper.isSpeaking = !this.voiceReadHelper.isSpeaking;
        });

      Text('这是Page2');
    }
    .height('100%')
    .width('100%');
  }
}
```


 
 

#### 总结
 
| 方案 | 适用场景 |
| --- | --- |
| @State+@Observed | 本地组件状态+单例对象引用，在需要使用的页面过多时难以维护，更适用于局部状态管理。 |
| AppStorage | AppStorage就像一个“全局状态仓库”，所有组件通过@StorageLink('key')从仓库中读取状态，修改时也写回仓库，更适用于全局状态管理。同时，AppStorage中的属性可以通过PersistentStorage持久化写入硬盘，实现状态在重启后保留。 |
