# @ohos.application.testRunner (TestRunner)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-testrunner
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

TestRunner模块提供了框架测试的能力。包括准备单元测试环境、运行测试用例。
 
如果您想实现自己的单元测试框架，您必须继承这个类并覆盖它的所有方法。
 
> [!NOTE]
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在 单元测试框架 中使用。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { TestRunner } from '@kit.TestKit';
```
 
  

#### TestRunner.onPrepare

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onPrepare(): void
 
为运行测试用例准备单元测试环境。
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**示例：**
 
```text
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
  }
}
```
 
  

#### TestRunner.onRun

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onRun(): void
 
运行测试用例。
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**示例：**
 
```text
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  onRun() {
    console.info('Trigger onRun');
  }
}
```
