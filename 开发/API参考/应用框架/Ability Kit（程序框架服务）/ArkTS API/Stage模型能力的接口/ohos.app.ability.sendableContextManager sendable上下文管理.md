# @ohos.app.ability.sendableContextManager (sendable上下文管理)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-sendablecontextmanager
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

sendableContextManager模块提供Context与[SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext)相互转换的能力。


## 使用场景
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本模块主要用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

例如，从主线程向子线程（如TaskPool或Worker工作线程）传递Sendable数据（符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)的数据）时，需要通过Context与SendableContext之间的相互转换来实现。过程如下：


- 主线程向子线程传递Sendable数据时，需要将Context转换为SendableContext。
- 子线程使用Sendable数据时，需要将SendableContext转换为Context。

这里的Context与[createModuleContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application#applicationcreatemodulecontext)方法创建的Context不同，具体差异如下：


- 与SendableContext相互转换的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应同一个Context对象。当一个实例中Context属性和方法被修改时，相关实例中的Context属性和方法将会同步修改。其中，Context实例中的eventHub属性比较特殊，不同实例中的eventHub是独立的对象，不支持跨ArkTS实例使用。如果需要使用[EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)跨实例传递数据，可以通过[setEventHubMultithreadingEnabled](#sendablecontextmanagerseteventhubmultithreadingenabled20)启用跨线程数据传递功能。
- 通过[createModuleContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application#applicationcreatemodulecontext)创建的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应不同的Context对象。


## 约束限制
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

“Context转换为SendableContext”和“SendableContext转换为Context”两个环节中的Context类型必须保持一致。例如，主线程使用[convertFromContext](#sendablecontextmanagerconvertfromcontext)将[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)转换为SendableContext，子线程收到该SendableContext之后，需要通过[convertToUIAbilityContext](#sendablecontextmanagerconverttouiabilitycontext)将SendableContext转换为[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

目前支持转换的Context包括[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)、[ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)、[AbilityStageContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext)、[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { sendableContextManager } from '@kit.AbilityKit';
```


## SendableContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

type SendableContext = _SendableContext

Sendable上下文，符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，继承自[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang#langisendable)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。


| 类型 | 说明 |
| --- | --- |
| [_SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext) | 表示Sendable上下文，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&amp;Worker工作线程）的数据传递。 |


## sendableContextManager.convertFromContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

convertFromContext(context: common.Context): SendableContext

将Context转换为SendableContext对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | Context对象。支持Context基类，[ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)、[AbilityStageContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext)和[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)子类。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| SendableContext | [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext)对象。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |


**示例：**


```ts
import {
  AbilityConstant,
  UIAbility,
  Want,
  sendableContextManager,
} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext) {
    this.sendableContext = sendableContext;
  }

  sendableContext: sendableContextManager.SendableContext;
  // other sendable object
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker(
    'entry/ets/workers/Worker.ets',
  );

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext);
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
}
```


## sendableContextManager.convertToContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

convertToContext(sendableContext: SendableContext): common.Context

将SendableContext对象转换为Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参��名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext) | 是 | SendableContext对象。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| common.Context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)对象。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |


**示例：**

主线程传递Context：


```ts
import {
  AbilityConstant,
  UIAbility,
  Want,
  common,
  sendableContextManager,
} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker(
    'entry/ets/workers/Worker.ets',
  );

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(context);
      let object: SendableObject = new SendableObject(
        sendableContext,
        'BaseContext',
      );
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
}
```

Worker线程接收Context：


```ts
import {
  ErrorEvent,
  MessageEvents,
  ThreadWorkerGlobalScope,
  worker,
} from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext =
    object.sendableContext;
  if (object.contextName == 'BaseContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to context.');
    try {
      let context: common.Context =
        sendableContextManager.convertToContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(
        0x0000,
        'testTag',
        'worker context.databaseDir: %{public}s',
        context.databaseDir,
      );
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertToContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
};
```


## sendableContextManager.convertToApplicationContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

convertToApplicationContext(sendableContext: SendableContext): common.ApplicationContext

将SendableContext对象转换为ApplicationContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext) | 是 | SendableContext对象。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| common.ApplicationContext | [ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)对象。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |


**示例：**

主线程传递Context：


```ts
import {
  AbilityConstant,
  UIAbility,
  Want,
  common,
  sendableContextManager,
} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker(
    'entry/ets/workers/Worker.ets',
  );

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let applicationContext = context.getApplicationContext();
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(applicationContext);
      let object: SendableObject = new SendableObject(
        sendableContext,
        'ApplicationContext',
      );
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
}
```

Worker线程接收Context：


```ts
import {
  ErrorEvent,
  MessageEvents,
  ThreadWorkerGlobalScope,
  worker,
} from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext =
    object.sendableContext;
  if (object.contextName == 'ApplicationContext') {
    hilog.info(
      0x0000,
      'testTag',
      '%{public}s',
      'convert to application context.',
    );
    try {
      let context: common.ApplicationContext =
        sendableContextManager.convertToApplicationContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(
        0x0000,
        'testTag',
        'worker context.databaseDir: %{public}s',
        context.databaseDir,
      );
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertToApplicationContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
};
```


## sendableContextManager.convertToAbilityStageContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

convertToAbilityStageContext(sendableContext: SendableContext): common.AbilityStageContext

将SendableContext对象转换为AbilityStageContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext) | 是 | SendableContext对象。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| common.AbilityStageContext | [AbilityStageContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext)对象。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |


**示例：**

主线���传递Context：


```ts
import { UIAbility, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker(
    'entry/ets/workers/Worker.ets',
  );

  onCreate(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(
        sendableContext,
        'AbilityStageContext',
      );
      hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
}
```

Worker线程接收Context：


```ts
import {
  ErrorEvent,
  MessageEvents,
  ThreadWorkerGlobalScope,
  worker,
} from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext =
    object.sendableContext;
  if (object.contextName == 'AbilityStageContext') {
    hilog.info(
      0x0000,
      'testTag',
      '%{public}s',
      'convert to abilitystage context.',
    );
    try {
      let context: common.AbilityStageContext =
        sendableContextManager.convertToAbilityStageContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(
        0x0000,
        'testTag',
        'worker context.databaseDir: %{public}s',
        context.databaseDir,
      );
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertToAbilityStageContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
};
```


## sendableContextManager.convertToUIAbilityContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

convertToUIAbilityContext(sendableContext: SendableContext): common.UIAbilityContext

将SendableContext对象转换为UIAbilityContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext) | 是 | SendableContext对象。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| common.UIAbilityContext | [UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)对象。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |


**示例：**

主线程传递Context：


```ts
import {
  AbilityConstant,
  UIAbility,
  Want,
  common,
  sendableContextManager,
} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker(
    'entry/ets/workers/Worker.ets',
  );

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(
        sendableContext,
        'EntryAbilityContext',
      );
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
}
```

Worker线程接收Context：


```ts
import {
  ErrorEvent,
  MessageEvents,
  ThreadWorkerGlobalScope,
  worker,
} from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext =
    object.sendableContext;
  if (object.contextName == 'EntryAbilityContext') {
    hilog.info(
      0x0000,
      'testTag',
      '%{public}s',
      'convert to UIAbility context.',
    );
    try {
      let context: common.UIAbilityContext =
        sendableContextManager.convertToUIAbilityContext(sendableContext);
      // 获取context后获取沙箱路径
      hilog.info(
        0x0000,
        'testTag',
        'worker context.databaseDir: %{public}s',
        context.databaseDir,
      );
    } catch (error) {
      hilog.error(
        0x0000,
        'testTag',
        `convertToUIAbilityContext failed, error code: ${error.code}, error msg: ${error.message}`,
      );
    }
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
};
```


## sendableContextManager.setEventHubMultithreadingEnabled20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setEventHubMultithreadingEnabled(context: common.Context, enabled: boolean): void

设置[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)中的[EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)是否启用跨线程通信能力。


**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | Context对象。其中，Eventhub支持传递的序列化数据类型参见[序列化支持的类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#序列化支持类型)，数据大小不超过16MB。 |
| enabled | boolean | 是 | 表示是否启用Context的EventHub跨线程通信能力。          - true：表示启用跨线程通信能力，数据将通过引用的方式传递。          - false：表示禁用跨线程通信能力，数据将通过序列化的方式传递，即发送端线程与接收端线程的数据相互独立。 |


**示例：**

主线程启用[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)中[EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)的跨线程通信能力，并将Context转换为[SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext)后发送到[Worker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker)线程。


```ts
import { common, sendableContextManager } from '@kit.AbilityKit';
import { worker } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

@Entry
@Component
struct Index {
  @State context: common.Context | undefined = this.getUIContext().getHostContext();
  worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  aboutToAppear(): void {
    let context: common.Context = this.context as common.Context;
    context.eventHub.on('event1', this.eventFunc);
    context.eventHub.emit('event1', 'xingming', 22);
  }

  eventFunc(name: string, age: number) {
    hilog.info(DOMAIN, 'testTag', 'name %{public}s age %{public}d', name, age);
  }

  build() {
    Column() {
      Row() {
        Button('thread 1')
        .size({ width: 100, height: 100 })
        .onClick(() => {
          if (this.context == undefined) {
            return;
          }
          sendableContextManager.setEventHubMultithreadingEnabled(this.context, true);
          let sendableContext: sendableContextManager.SendableContext =
          sendableContextManager.convertFromContext(this.context);
          let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
          this.worker1.postMessageWithSharedSendable(object);
        })
      }
    }
  }
}
```

[Worker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker)线程接收到[SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext)后，将其转换为[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。然后，在Worker线程内，启用Context中[EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)的跨线程通信能力，并通过该功能向主线程发送消息。


```ts
import {
  ErrorEvent,
  MessageEvents,
  ThreadWorkerGlobalScope,
  worker,
} from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(
    sendableContext: sendableContextManager.SendableContext,
    contextName: string,
  ) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext =
    object.sendableContext;
  if (object.contextName == 'BaseContext') {
    let context: common.Context =
      sendableContextManager.convertToContext(sendableContext);
    sendableContextManager.setEventHubMultithreadingEnabled(context, true);
    context.eventHub.emit('event1', 'xingming', 40);
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onerror');
};
```
