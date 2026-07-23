# 如何实现资源替换overlay机制

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-164

#### 问题现象

HarmonyOS如何实现资源替换的静态overlay以及动态overlay？
 
 

#### 背景知识

- [overlay机制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#overlay机制)：overlay是一种资源替换机制，针对不同品牌、产品的显示风格，开发者可以在不重新打包HAP的情况下，通过配置和使用overlay资源包，实现应用界面风格变换。overlay资源包只包含资源文件、资源索引文件和配置文件。
- 静态overlay机制：在应用安装时已确定的资源包（如主题、图标、多语言文本等）。这些资源包作为HAP（Harmony Ability Package）的一部分被固化到应用中，初始状态（启用/禁用）在安装时设定。
- 动态overlay机制：通过运行时API动态切换静态overlay资源包状态（启用/禁用）的机制。它不修改资源内容，而是控制静态资源包的生效状态。
- [HSP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/in-app-hsp)（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布上架，而是跟随宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。
- [addResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#addresource10)：应用运行时加载指定的资源路径，实现资源覆盖。
- [overlay.setOverlayEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay#overlaysetoverlayenabled)：设置当前应用中overlay特征module的禁用使能状态。

 
 

#### 解决方案
 
|    | 动态overlay | 静态overlay |
| --- | --- | --- |
| overlay资源包类型 | HAP/HSP | HSP |
| 核心API | ResourceManager.addResource/removeResource | overlay.setOverlayEnabled |
| 应用场景 | 静态资源定制（多语言、主题）。 | 动态UI交互（导航菜单、浮动面板）。 |
 
1. 利用静态overlay机制实现资源替换：
- 主应用EntryAbility中使能静态overlay：
```ArkTS
<em>// EntryAbility.ets文件</em>
onCreate(): void {
  this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
 <em> // 系统默认使能，这里可以不设置</em>
  overlay.setOverlayEnabled('staticOverlay', true, (err) => {
    if (err) {
      hilog.error(DOMAIN, 'testTag', 'err code: ' + err.code + ' ' + 'message:' + err.message);
      return;
    }
    console.info('setOverlayEnabled success');
  });
}
```


2. 主应用Index页面中使用Resource目录下的“bg.png”文件:
```ArkTS
<em>// Index.ets</em>
@Entry
@Component
struct Index {

  build() {
    RelativeContainer() {
      Image($r('app.media.bg'))
        .width(100)
        .height(100)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-W2u7NBjTiuRuUpetMfciA/zh-cn_image_0000002658870847.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=008E934E9D4C7EC78CBAED790C2326DAC02F02D7850968B222BFD98D300CFAD6)


3. 创建静态overlay资源包staticOverlay.hsp，Resource目录中也有“bg.png”文件，路径和entry相同：
[使用DevEco Studio创建HSP模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp#section7717162312546)，和正常创建HSP步骤一致，不再赘述。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/e2T2ysWyTu2yoWMH4YK0pw/zh-cn_image_0000002628791472.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=7357C9599B16D7322A11324BA2B88FB93D2540BCB482C9D913ECA3587F0D20D7)


4. staticOverlay.hsp中module.json5配置：targetModuleName和targetPriority标签需要单独设置。

  targetModuleName：字符串类型，指定要overlay的应用中的目标moduleName，这里需要替换Entry的资源，所以设置为Entry的moduleName。

  targetPriority：整数类型，指定overlay优先级。

  
```json
<em>// staticOverlay module.json5</em>
{
  "module": {
    "name": "staticOverlay",
    "type": "shared",
    "description": "$string:shared_desc",
    "deviceTypes": [
      "phone"
    ],
    "deliveryWithInstall": true,
    "pages": "$profile:main_pages",
    "targetModuleName": "entry",
    "targetPriority": 1
  }
}
```


5. 编译静态overlay资源包staticOverlay.hsp：由于静态overlay需要替换实现主Entry包中的资源，所以需要注意的是，要在DevEco Studio上Run->Edit Configurations中选中entry包进行勾选“Deploy Multi Hap/Hsp Packages”选项，打包编译时会将静态资源包编译到应用HAP中：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/5uZEZOz2QmuW7bGADrYWxg/zh-cn_image_0000002658990787.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=0ED77625596FA2DDC4D76538B2AB510073497D8408D0F7863F395DC734D33D7C)


  执行编译后，在静态资源包这里会看到编译生成了编译产物：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iFf1imkYTMCiu47YmINL2w/zh-cn_image_0000002628631570.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=BA97D8779BB13FCE74CC85BDB60BE98346D14DEF22825604691793BB4B9ADC8F)


6. 最终，应用安装后的效果为：
> [!NOTE]
> staticOverlay包中“bg.png”资源替换了entry包中的“bg.png”，资源文件的路径、名称要和被替换包中资源文件一致。


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/c30IytwuT22qtBM8mkEldw/zh-cn_image_0000002658870849.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=1AABCD0191289D9A5489E3DC79C77D6B5EFA4C496B157FA0AC92FFE6E8433EFD)

- 利用动态overlay机制实现资源替换：1. 主应用Index页面中使用Resource目录下的“bg.png”文件:
```ArkTS
<em>// Index1.ets</em>
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index1 {
  context: common.Context = this.getUIContext().getHostContext() as common.Context;
  @State image: PixelMap = this.context.resourceManager.getDrawableDescriptor($r('app.media.bg').id).getPixelMap();

  build() {
    RelativeContainer() {
      Image(this.image)
        .width(100)
        .height(100)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        }).onClick(()=> {
          let path = this.context.bundleCodeDir + '/dynamicOverlay.hsp';
          try {
            this.context.resourceManager.addResource(path);
            this.image = this.context.resourceManager.getDrawableDescriptor($r('app.media.bg').id).getPixelMap();
          } catch (error) {
            let code: number = (error as BusinessError<number>).code;
            let message: string = (error as BusinessError<string>).message;
            console.error(`addResource failed, error code: ${code}, message: ${message}.`);
          }
      })
    }
    .height('100%')
    .width('100%')
  }
}
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/_pHPye5jRxqwov6_oslYJQ/zh-cn_image_0000002628791474.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=0FF7C3C4AA05A1558EBCCB2257D4014A3599A1AF20A696667B3988311291FA04)


2. 创建动态overlay资源包dynamicOverlay.hsp，Resource目录中也有“bg.png”文件，路径和entry相同：
使用DevEco Studio创建HSP，和正常创建HSP步骤一致，不再赘述。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/DnkwvWiuT36ZOm5q7YvfeA/zh-cn_image_0000002658990789.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=C2FDD43F8746CEE2E1C532F500920E939834ABC02E9DC126B864ADE8AA0471B9)


3. dynamicOverlay.hsp中module.json5配置：（动态overlay不需要配置targetModuleName和targetPriority标签）。
```json
<em>// dynamicOverlay module.json5</em>
{
  "module": {
    "name": "dynamicOverlay",
    "type": "shared",
    "description": "$string:shared_desc",
    "deviceTypes": [
      "phone"
    ],
    "deliveryWithInstall": true,
    "pages": "$profile:main_pages"
  }
}
```


4. 编译动态overlay资源包dynamicOverlay.hsp，和上述静态overlay资源包编译步骤一致，不再赘述。

5. 应用安装后，点击图标运行效果预览：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/yKBNxOVFTzqMrkuwVnrndg/zh-cn_image_0000002628631572.png?HW-CC-KV=V1&HW-CC-Date=20260723T012457Z&HW-CC-Expire=86400&HW-CC-Sign=54FD58A27198D93DEB446B6291E349008E82400428F1EF185ADB2ACA82B780C4)
