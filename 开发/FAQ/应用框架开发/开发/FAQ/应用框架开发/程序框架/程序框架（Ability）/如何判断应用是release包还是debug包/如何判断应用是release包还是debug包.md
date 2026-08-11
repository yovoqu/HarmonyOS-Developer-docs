# 如何判断应用是release包还是debug包

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-171

#### 问题现象

如何判断应用是否为release包？
 
 

#### 解决方案

- 方法1：通过命令行：
bm dump -n [bundleName] |grep appProvisionType：判断应用程序签名证书文件的类型来判断release还是debug。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/NcixGPTvQJiAKE6HhE6Mkw/zh-cn_image_0000002628791476.png?HW-CC-KV=V1&HW-CC-Date=20260811T005856Z&HW-CC-Expire=86400&HW-CC-Sign=16A3BD5FABFB4C25713B34E99F91D08A3EC2B0F0867095039F6092B575F17B38)

- bm dump -n [bundleName] |grep debug：标识应用是否处于调试模式，取值为true表示应用处于调试模式，取值为false表示应用处于非调试模式，以及应用程序签名证书文件的类型。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/AFBMwcHUR3iz722kETzk8Q/zh-cn_image_0000002658990791.png?HW-CC-KV=V1&HW-CC-Date=20260811T005856Z&HW-CC-Expire=86400&HW-CC-Sign=AC47F26F16E7FF0B2A65629FE769B72B54AD5F69B12F836F1D8E2CE8E19EAE68)


 - 方法2：通过bundleManager.getBundleInfoForSelf获取自身的应用程序信息：
[ApplicationInfo.appProvisionType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)表示应用程序签名证书文件的类型，分为debug和release两种类型。示例代码如下：
```text
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  build() {
    RelativeContainer() {
      Text('查询应用程序信息')
        .id('HelloWorld')
        .fontSize('25vp')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
          bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
            let appProvisionType = data.appInfo.appProvisionType;
            console.info(`应用签名证书类型: ${appProvisionType}`);
          }).catch((err: BusinessError) => {
            console.info(`code: ${err.code}; message: ${err.message}`);
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```


 - 方法三：在编译构建时，Hvigor会生成BuildProfile类，可以通过该类在运行时获取编译构建参数，BuildProfile.BUILD_MODE_NAME即为编译模式。参考链接：[获取自定义编译参数-能力说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-guide)。
