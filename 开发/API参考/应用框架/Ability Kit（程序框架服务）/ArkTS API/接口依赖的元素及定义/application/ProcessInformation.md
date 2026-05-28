# ProcessInformation

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

运行进程信息，可以通过appManager的[getRunningProcessInformation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager#appmanagergetrunningprocessinformation)来获取运行进程信息。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### 导入模块

```text
import { appManager } from '@kit.AbilityKit';
```
 
  

##### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 否 | 否 | 应用程序的UID。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| processName | string | 否 | 否 | 进程名称。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| bundleNames | Array&lt;string&gt; | 否 | 否 | 进程中所有运行的Bundle名称。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| state10+ | appManager.ProcessState | 否 | 否 | 当前进程运行状态。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| bundleType12+ | bundleManager.BundleType | 否 | 否 | 当前进程运行的包类型。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| appCloneIndex12+ | number | 否 | 是 | 分身应用索引。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
 
 
**示例：**
 
```json
import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((error, data) => {
  if (error) {
    console.error(`getRunningProcessInformation fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`getRunningProcessInformation success, data: ${JSON.stringify(data)}`);
  }
});
```
