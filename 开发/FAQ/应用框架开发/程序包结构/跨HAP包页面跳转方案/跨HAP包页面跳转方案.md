# 跨HAP包页面跳转方案

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-76

#### 问题现象

在多HAP场景中，开发者需要实现跨HAP模块的页面跳转。Navigation路由操作不支持从一个HAP跳转到另一个HAP的页面，会抛出跳转失败的错误。
 
 

#### 背景知识

[多HAP场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package#开发)是指在HarmonyOS中使用多个应用包（一个entry包和多个feature包）来实现复杂应用的开发方式。这种开发模式允许将复杂应用拆分成多个模块，每个模块可以独立开发、测试和更新，提高了开发效率和维护性。
 
区别于[HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)和[HSP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/in-app-hsp)，每个HAP模块具有各自的UIAbility组件。多HAP应用运行时，同一进程中的UIAbility组件被启动时，才加载对应HAP的资源和代码。[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router)和[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)可以实现HAP至HAR/HSP页面的跳转，无法跳转其它HAP页面。可以通过UIAbility中的[startAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability)方法拉起其它HAP包中的页面。
 
 

#### 解决方案
1. 在项目中创建targetHap：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/3zXsLf2NQ3W1Qc0APqA8hQ/zh-cn_image_0000002628628222.png?HW-CC-KV=V1&HW-CC-Date=20260730T072300Z&HW-CC-Expire=86400&HW-CC-Sign=DD1B4F49411D03755AFAE68D3DC891752304B8F4A81A6003D62992857EBF18DE)

2. 在entry模块中使用startAbility拉起targetHap模块的实例，需要配置bundleName和Ability名称，并在被拉起的HAP中配置期望打开的页面即可。发起侧示例代码如下：
```json
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

const BUNDLE_NAME: string = 'com.example.jumphap'; <em>// 在应用app.json5文件中"bundleName"节点获得</em>
const ABILITY_NAME: string = 'TargetHapAbility'; <em>// 在HAP包的对应Ability文件中获得</em>

@Entry
@Component
struct Index {
  private context?: common.UIAbilityContext; <em>// 创建context实例</em>

  aboutToAppear(): void {
    this.context = this.getUIContext().getHostContext() as common.UIAbilityContext; <em>// 获取当前页面关联的UIAbilityContext</em>
  }

  jumpHap() {
    if (this.context) {
      <em>// 启动Ability，拉起HAP模块的UIAbility实例</em>
      this.context.startAbility({
        bundleName: BUNDLE_NAME,
        abilityName: ABILITY_NAME
      }).then(() => {
        console.info('start ability success');
      }).catch((error: BusinessError) => {
        console.error(`start ability failed, error: ${error}`);
      });
    }
  }

  build() {
    RelativeContainer() {
      Button('startAbility跳转HAP')
        .fontSize(25)
        .width(350)
        .height(50)
        .margin({ top: 400 })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.jumpHap(); <em>// 点击跳转</em>
        });
    };
  }
}
```

3. 进入“Run”>“Edit Configurations”>“Run/Debug Configuration”，勾选主模块的Deploy Multi Hap/Hsp选框下的Deploy Multi Hap/Hsp Packages和All Modules选项，即可运行验证。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/RnYEKFvpRBev40imTl02Dg/zh-cn_image_0000002658867501.png?HW-CC-KV=V1&HW-CC-Date=20260730T072300Z&HW-CC-Expire=86400&HW-CC-Sign=38D23DED20345E7DB578CB8B95A312977FB8F5BFD4862A8A5A36534AB2E54447)

4. 若是有多模块页面跳转的需求，建议还是使用静态库HAR或动态库HSP，尽量避免涉及多HAP之间的页面跳转。
 
 

#### 常见FAQ

Q：feature类型的HAP包支持导出组件或者接口给其他模块使用吗？
 
A：feature类型的HAP包不支持导出接口或组件给其他模块使用。该类型的HAP包用于实现动态特性扩展的核心模块设计，可参考案例：[示例代码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package#示例代码)。如果需要共享资源，需要使用HSP(动态共享包)或者HAR(静态共享包)。可参考多HAP场景的[使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package#使用场景)。
