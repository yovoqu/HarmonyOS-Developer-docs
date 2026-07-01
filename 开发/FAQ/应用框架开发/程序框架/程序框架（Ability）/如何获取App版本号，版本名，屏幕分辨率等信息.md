# 如何获取App版本号，版本名，屏幕分辨率等信息

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-71

1. 通过@kit.AbilityKit中的bundleManager模块查询bundleInfo，其中包含App版本号和版本名。
```text
import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';

<em>// ...</em>
bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo) => {
  let versionName = bundleInfo.versionName; <em>// App version name</em>
  let versionNo = bundleInfo.versionCode; <em>// App version code</em>
}).catch((error: BusinessError) => {
  console.error('get bundleInfo failed, error is ' + error);
})
```

2. 在context.config中获取screenDensity，其中包含屏幕分辨率信息。
```text
import { common } from '@kit.AbilityKit';

<em>// ...</em>
<em>// In the utility class: Save the context to AppStorage in the EntryAbility - onCreate lifecycle, then use AppStorage to retrieve it in the utility class</em>
let context = AppStorage.get('context') as common.UIAbilityContext;

let screenDensity = context.config.screenDensity;
```
