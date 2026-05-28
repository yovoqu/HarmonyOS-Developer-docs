# WorkSchedulerExtensionContext

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。
 
WorkSchedulerExtensionContext可直接作为WorkSchedulerExtension的上下文环境，提供允许访问特定于WorkSchedulerExtensionAbility的资源的能力。
 
> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。

  

#### 使用说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

通过WorkSchedulerExtensionAbility子类实例来获取。
 
```text
import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';

class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
    onWorkStart(workInfo: workScheduler.WorkInfo) {
        let WorkSchedulerExtensionContext = this.context; // 获取WorkSchedulerExtensionContext
    }
}
```
 
  

#### WorkSchedulerExtensionContext

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境。
 
**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler
 
**模型约束：** 本模块接口仅可在Stage模型下使用。
