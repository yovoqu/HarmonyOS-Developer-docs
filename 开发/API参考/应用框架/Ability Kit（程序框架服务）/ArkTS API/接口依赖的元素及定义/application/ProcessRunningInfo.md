# ProcessRunningInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processrunninginfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

运行进程信息，可以通过appManager中[getProcessRunningInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-appmanager#appmanagergetprocessrunninginfosdeprecated)方法来获取运行进程信息。
 
> [!NOTE]
> 本模块接口从API version 9 开始废弃，建议使用 ProcessInformation 9+ 替代。 本模块首批接口从API version 8 开始支持。

  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import appManager from '@ohos.application.appManager';
```
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 |
| uid | number | 否 | 否 | 应用程序的UID。 |
| processName | string | 否 | 否 | 进程名称。 |
| bundleNames | Array&lt;string&gt; | 否 | 否 | 进程中所有运行的Bundle名称。 |
 
 
**示例：**
 
```json
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getProcessRunningInfos().then((data) => {
    console.info(`success: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed: ${JSON.stringify(error)}`);
});
```
