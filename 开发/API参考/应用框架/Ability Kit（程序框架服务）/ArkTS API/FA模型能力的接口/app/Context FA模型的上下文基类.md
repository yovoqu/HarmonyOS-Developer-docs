# Context (FA模型的上下文基类)

更新时间：2026-03-23 08:10:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Context模块提供了Ability或Application的上下文的基础能力，包括允许访问特定于应用程序的资源、请求和验证权限等。
 
> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在FA模型下使用。

  

##### 导入模块

```text
import featureAbility from '@ohos.ability.featureAbility';
```
 
  

##### 使用说明

Context对象是在featureAbility中创建实例，并通过featureAbility的[getContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#featureabilitygetcontext)接口返回，因此在使用Context时，必须导入@ohos.ability.featureAbility库。示例如下：
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir().then((data) => {
    console.info(`getOrCreateLocalDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getOrCreateLocalDir7+

getOrCreateLocalDir(callback: AsyncCallback&lt;string&gt;): void
 
获取应用程序的本地根目录。使用callback异步回调。
 
如果是第一次调用，将创建目录。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回应用程序的本地根目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir((error, data)=>{
    if (error && error.code !== 0) {
        console.error(`getOrCreateLocalDir fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getOrCreateLocalDir success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getOrCreateLocalDir7+

getOrCreateLocalDir(): Promise&lt;string&gt;
 
获取应用程序的本地根目录。使用Promise异步回调。
 
如果是第一次调用，将创建目录。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回应用程序的本地根目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateLocalDir().then((data) => {
    console.info(`getOrCreateLocalDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.verifyPermission7+

verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback&lt;number&gt;): void
 
验证系统中运行的特定pid和uid是否允许指定的权限。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| options | PermissionOptions | 是 | 权限选项。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回权限验证结果，0有权限，-1无权限。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';
import bundle from '@ohos.bundle.bundleManager';
import { BusinessError } from '@ohos.base';

let context: featureAbility.Context = featureAbility.getContext();
bundle.getBundleInfo('com.context.test', 1, (err: BusinessError, datainfo: bundle.BundleInfo) =>{
    context.verifyPermission('com.example.permission', {uid:datainfo.appInfo.uid}, (error, data) =>{
        if (error && error.code !== 0) {
            console.error(`verifyPermission fail, error: ${JSON.stringify(error)}`);
        } else {
            console.info(`verifyPermission success, data: ${JSON.stringify(data)}`);
        }
    });
});
```
 
示例代码中出现的getBundleInfo相关描述可参考对应[文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager)。
 
  

##### Context.verifyPermission7+

verifyPermission(permission: string, callback: AsyncCallback&lt;number&gt;): void
 
验证系统中运行的当前pid和uid是否具有指定的权限。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回权限验证结果，0有权限，-1无权限。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.verifyPermission('com.example.permission', (error, data) =>{
    if (error && error.code !== 0) {
        console.error(`verifyPermission fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`verifyPermission success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.verifyPermission7+

verifyPermission(permission: string, options?: PermissionOptions): Promise&lt;number&gt;
 
验证系统中运行的特定pid和uid是否具有指定的权限。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| options | PermissionOptions | 否 | 权限选项。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，如果pid和uid具有权限，则使用0进行异步回调；否则使用-1回调。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.verifyPermission('com.context.permission', {pid:1}).then((data) => {
    console.info(`verifyPermission data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.requestPermissionsFromUser7+

requestPermissionsFromUser(permissions: Array&lt;string&gt;, requestCode: number, resultCallback: AsyncCallback&lt;PermissionRequestResult&gt;): void
 
从系统请求某些权限。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissions | Array&lt;string&gt; | 是 | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | 是 | 指示要传递给PermissionRequestResult的请求代码。 |
| resultCallback | AsyncCallback&lt;PermissionRequestResult&gt; | 是 | 回调函数，返回授权结果信息。 |
 
 
**示例：**
 
ArkTS示例：
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.requestPermissionsFromUser(
    ['com.example.permission1',
     'com.example.permission2',
     'com.example.permission3',
     'com.example.permission4',
     'com.example.permission5'],
    1,
    (error, data) => {
        if (error && error.code !== 0) {
            console.error(`requestPermissionsFromUser fail, error: ${JSON.stringify(error)}`);
        } else {
            console.info(`requestPermissionsFromUser success, data: ${JSON.stringify(data)}`);
        }
    }
);
```
 
JS示例：
 
```xml
<!-- xxx.hml -->
<div class="container">
    <div>
        <input class="perm-btn" type="button" value="申请权限" onclick="requestPermissions" />
    </div>
</div>
```
 
```text
/*xxx.css*/
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 100%;
}

.perm-btn {
    width: 200px;
    height: 60px;
    background-color: #007dff;
    color: white;
    font-size: 20px;
    border: none;
    border-radius: 8px;
}

.perm-btn:active {
    background-color: #0058b3;
}
```
 
```json
// xxx.js
import featureAbility from '@ohos.ability.featureAbility';

export default {
    data: {
    },
    onInit() {
    },
    requestPermissions() {
        let context = featureAbility.getContext();
        context.requestPermissionsFromUser(
            ['com.example.permission1',
            'com.example.permission2',
            'com.example.permission3',
            'com.example.permission4',
            'com.example.permission5'],
            1,
            (error, data) => {
                if (error && error.code !== 0) {
                    console.error(`requestPermissionsFromUser fail, error: ${JSON.stringify(error)}`);
                } else {
                    console.info(`requestPermissionsFromUser success, data: ${JSON.stringify(data)}`);
                }
            }
        );
    }
}
```
 
  

##### Context.requestPermissionsFromUser7+

requestPermissionsFromUser(permissions: Array&lt;string&gt;, requestCode: number): Promise&lt;PermissionRequestResult&gt;
 
从系统请求某些权限。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissions | Array&lt;string&gt; | 是 | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | 是 | 指示要传递给PermissionRequestResult的请求代码。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;PermissionRequestResult&gt; | Promise对象，返回授权结果信息。 |
 
 
**示例：**
 
ArkTS示例：
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.requestPermissionsFromUser(
    ['com.example.permission1',
     'com.example.permission2',
     'com.example.permission3',
     'com.example.permission4',
     'com.example.permission5'],
    1).then((data)=>{
        console.info(`requestPermissionsFromUser data: ${JSON.stringify(data)}`);
    }
);
```
 
JS示例：
 
```xml
<!-- xxx.hml -->
<div class="container">
    <div>
        <input class="perm-btn" type="button" value="申请权限" onclick="requestPermissions" />
    </div>
</div>
```
 
```text
/*xxx.css*/
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 100%;
}

.perm-btn {
    width: 200px;
    height: 60px;
    background-color: #007dff;
    color: white;
    font-size: 20px;
    border: none;
    border-radius: 8px;
}

.perm-btn:active {
    background-color: #0058b3;
}
```
 
```json
// xxx.js
import featureAbility from '@ohos.ability.featureAbility';

export default {
    data: {
    },
    onInit() {
    },
    requestPermissions() {
        let context = featureAbility.getContext();
        context.requestPermissionsFromUser(
            ['com.example.permission1',
            'com.example.permission2',
            'com.example.permission3',
            'com.example.permission4',
            'com.example.permission5'],
            1).then((data)=>{
                console.info(`requestPermissionsFromUser data: ${JSON.stringify(data)}`);
            }
        );
    }
}
```
 
  

##### Context.getApplicationInfo7+

getApplicationInfo(callback: AsyncCallback&lt;ApplicationInfo&gt;): void
 
获取有关当前应用程序的信息。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;ApplicationInfo&gt; | 是 | 回调函数，返回当前应用程序的信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getApplicationInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getApplicationInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getApplicationInfo success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getApplicationInfo7+

getApplicationInfo(): Promise&lt;ApplicationInfo&gt;
 
获取有关当前应用程序的信息。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;ApplicationInfo&gt; | Promise对象，返回当前应用程序的信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getApplicationInfo().then((data) => {
    console.info(`getApplicationInfo data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getBundleName7+

getBundleName(callback: AsyncCallback&lt;string&gt;): void
 
获取当前ability的Bundle名称。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回当前ability的Bundle名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getBundleName((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getBundleName fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getBundleName success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getBundleName7+

getBundleName(): Promise&lt;string&gt;
 
获取当前ability的Bundle名称。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前ability的Bundle名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getBundleName().then((data) => {
    console.info(`getBundleName data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getDisplayOrientation7+

getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void
 
获取当前ability的显示方向。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<bundle.DisplayOrientation> | 是 | 回调函数，返回屏幕显示方向。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getDisplayOrientation((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getDisplayOrientation fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getDisplayOrientation success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getDisplayOrientation7+

getDisplayOrientation(): Promise<bundle.DisplayOrientation>
 
获取此能力的当前显示方向。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise<bundle.DisplayOrientation> | Promise对象，返回屏幕显示方向。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getDisplayOrientation().then((data) => {
    console.info(`getDisplayOrientation data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getExternalCacheDir(deprecated)

getExternalCacheDir(callback: AsyncCallback&lt;string&gt;): void
 
获取应用程序的外部缓存目录。使用callback异步回调。
 
> [!NOTE]
> 从API version 7开始不再支持。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回应用程序的缓存目录的绝对路径。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getExternalCacheDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getExternalCacheDir fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getExternalCacheDir success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getExternalCacheDir(deprecated)

getExternalCacheDir(): Promise&lt;string&gt;
 
获取应用程序的外部缓存目录。使用Promise异步回调。
 
> [!NOTE]
> 从API version 7开始不再支持。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回应用程序的缓存目录的绝对路径。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getExternalCacheDir().then((data) => {
    console.info(`getExternalCacheDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.setDisplayOrientation7+

setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback&lt;void&gt;): void
 
设置当前Ability的显示方向。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | bundle.DisplayOrientation | 是 | 指示当前能力的新方向。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置当前Ability的显示方向成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';
import bundleManager from '@ohos.bundle';

let context: featureAbility.Context = featureAbility.getContext();
let orientation = bundleManager.DisplayOrientation.LANDSCAPE;
context.setDisplayOrientation(orientation, (error) => {
    console.error(`setDisplayOrientation fail, error: ${JSON.stringify(error)}`);
});
```
 
  

##### Context.setDisplayOrientation7+

setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise&lt;void&gt;
 
设置当前Ability的显示方向。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | bundle.DisplayOrientation | 是 | 表示屏幕显示方向。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';
import bundleManager from '@ohos.bundle';

let context: featureAbility.Context = featureAbility.getContext();
let orientation = bundleManager.DisplayOrientation.UNSPECIFIED;
context.setDisplayOrientation(orientation).then((data) => {
    console.info(`setDisplayOrientation data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.setShowOnLockScreen(deprecated)

setShowOnLockScreen(show: boolean, callback: AsyncCallback&lt;void&gt;): void
 
设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用callback异步回调。
 
> [!NOTE]
> 该接口功能仅对系统应用生效。 从API version 7开始支持，从API version 9开始废弃。建议使用window.setShowOnLockScreen替代，新接口为系统接口。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置每当显示锁屏时是否在锁屏顶部显示此功能并使该功能保持激活状态的操作成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let show = true;
context.setShowOnLockScreen(show, (error) => {
    console.error(`setShowOnLockScreen fail, error: ${JSON.stringify(error)}`);
});
```
 
  

##### Context.setShowOnLockScreen(deprecated)

setShowOnLockScreen(show: boolean): Promise&lt;void&gt;
 
设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用Promise异步回调。
 
> [!NOTE]
> 该接口功能仅对系统应用生效。 从API version 7开始支持，从API version 9开始废弃。建议使用window.setShowOnLockScreen替代，新接口为系统接口。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let show = true;
context.setShowOnLockScreen(show).then((data) => {
    console.info(`setShowOnLockScreen data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.setWakeUpScreen(deprecated)

setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback&lt;void&gt;): void
 
设置恢复此功能时是否唤醒屏幕。使用callback异步回调。
 
> [!NOTE]
> 该接口功能仅对系统应用生效。 从API version 7开始支持，从API version 12开始废弃。替代接口window.setWakeUpScreen替代，新接口为系统接口。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wakeUp | boolean | 是 | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当设置恢复此功能时是否唤醒屏幕成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let wakeUp = true;
context.setWakeUpScreen(wakeUp, (error) => {
    console.error(`setWakeUpScreen fail, error: ${JSON.stringify(error)}`);
});
```
 
  

##### Context.setWakeUpScreen(deprecated)

setWakeUpScreen(wakeUp: boolean): Promise&lt;void&gt;
 
设置恢复此功能时是否唤醒屏幕。使用Promise异步回调。
 
> [!NOTE]
> 该接口功能仅对系统应用生效。 从API version 7开始支持，从API version 12开始废弃。替代接口window.setWakeUpScreen替代，新接口为系统接口。

 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wakeUp | boolean | 是 | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
let wakeUp = true;
context.setWakeUpScreen(wakeUp).then((data) => {
    console.info(`setWakeUpScreen data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getProcessInfo7+

getProcessInfo(callback: AsyncCallback&lt;ProcessInfo&gt;): void
 
获取有关当前进程的信息，包括进程ID和名称。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;ProcessInfo&gt; | 是 | 回调函数，返回当前进程的信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getProcessInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getProcessInfo success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getProcessInfo7+

getProcessInfo(): Promise&lt;ProcessInfo&gt;
 
获取有关当前进程的信息，包括进程id和名称。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;ProcessInfo&gt; | Promise对象，返回当前进程的信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessInfo().then((data) => {
    console.info(`getProcessInfo data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getElementName7+

getElementName(callback: AsyncCallback&lt;ElementName&gt;): void
 
获取当前ability的ohos.bundleManager.ElementName对象。使用callback异步回调。
 
此方法仅适用于页面功能。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;ElementName&gt; | 是 | 回调函数，返回当前ability的ohos.bundleManager.ElementName对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getElementName((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getElementName fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getElementName success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getElementName7+

getElementName(): Promise&lt;ElementName&gt;
 
获取当前能力的ohos.bundleManager.ElementName对象。使用Promise异步回调。
 
此方法仅适用于页面功能。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;ElementName&gt; | Promise对象，返回当前ability的ohos.bundleManager.ElementName对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getElementName().then((data) => {
    console.info(`getElementName data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getProcessName7+

getProcessName(callback: AsyncCallback&lt;string&gt;): void
 
获取当前进程的名称。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回当前进程的名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessName((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getProcessName fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getProcessName success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getProcessName7+

getProcessName(): Promise&lt;string&gt;
 
获取当前进程的名称。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前进程的名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getProcessName().then((data) => {
    console.info(`getProcessName data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getCallingBundle7+

getCallingBundle(callback: AsyncCallback&lt;string&gt;): void
 
获取ability调用方的Bundle名称。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回ability调用方的Bundle名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCallingBundle((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getCallingBundle fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getCallingBundle success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getCallingBundle7+

getCallingBundle(): Promise&lt;string&gt;
 
获取ability调用方的Bundle名称。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回ability调用方的Bundle名称。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCallingBundle().then((data) => {
    console.info(`getCallingBundle data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getCacheDir

getCacheDir(callback: AsyncCallback&lt;string&gt;): void
 
获取该应用程序的内部存储目录。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回该应用程序的内部存储目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCacheDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getCacheDir fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getCacheDir success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getCacheDir

getCacheDir(): Promise&lt;string&gt;
 
获取该应用程序的内部存储目录。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回该应用程序的内部存储目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getCacheDir().then((data) => {
    console.info(`getCacheDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getFilesDir

getFilesDir(callback: AsyncCallback&lt;string&gt;): void
 
获取内部存储器上此应用程序的文件目录。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回内部存储器上此应用程序的文件目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getFilesDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getFilesDir fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getFilesDir success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getFilesDir

getFilesDir(): Promise&lt;string&gt;
 
获取内部存储器上此应用程序的文件目录。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回内部存储器上此应用程序的文件目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getFilesDir().then((data) => {
    console.info(`getFilesDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getOrCreateDistributedDir7+

getOrCreateDistributedDir(callback: AsyncCallback&lt;string&gt;): void
 
获取Ability或应用的分布式文件路径。使用callback异步回调。
 
如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回Ability或应用的分布式文件路径。 若路径不存在，系统将创建一个路径并返回创建的路径。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateDistributedDir((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getOrCreateDistributedDir fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getOrCreateDistributedDir success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getOrCreateDistributedDir7+

getOrCreateDistributedDir(): Promise&lt;string&gt;
 
获取Ability或应用的分布式文件路径。使用Promise异步回调。
 
如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回Ability或应用的分布式文件路径。若为首次调用，则将创建目录。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getOrCreateDistributedDir().then((data) => {
    console.info(`getOrCreateDistributedDir data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getAppType7+

getAppType(callback: AsyncCallback&lt;string&gt;): void
 
获取此应用的类型。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回此应用程序的类型。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppType((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getAppType fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getAppType success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getAppType7+

getAppType(): Promise&lt;string&gt;
 
获取此应用的类型。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回此应用的类型。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppType().then((data) => {
    console.info(`getAppType data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getHapModuleInfo7+

getHapModuleInfo(callback: AsyncCallback&lt;HapModuleInfo&gt;): void
 
获取应用的ModuleInfo对象。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;HapModuleInfo&gt; | 是 | 回调函数，返回应用的ModuleInfo对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getHapModuleInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getHapModuleInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getHapModuleInfo success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getHapModuleInfo7+

getHapModuleInfo(): Promise&lt;HapModuleInfo&gt;
 
获取应用的ModuleInfo对象。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;HapModuleInfo&gt; | Promise对象，返回应用的ModuleInfo对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getHapModuleInfo().then((data) => {
    console.info(`getHapModuleInfo data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getAppVersionInfo7+

getAppVersionInfo(callback: AsyncCallback&lt;AppVersionInfo&gt;): void
 
获取应用的版本信息。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AppVersionInfo&gt; | 是 | 回调函数，返回应用版本信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppVersionInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getAppVersionInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getAppVersionInfo success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getAppVersionInfo7+

getAppVersionInfo(): Promise&lt;AppVersionInfo&gt;
 
获取应用的版本信息。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;AppVersionInfo&gt; | Promise对象，返回应用版本信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAppVersionInfo().then((data) => {
    console.info(`getAppVersionInfo data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getAbilityInfo7+

getAbilityInfo(callback: AsyncCallback&lt;AbilityInfo&gt;): void
 
查询当前归属Ability详细信息。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AbilityInfo&gt; | 是 | 回调函数，返回当前归属Ability详细信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAbilityInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getAbilityInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getAbilityInfo success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.getAbilityInfo7+

getAbilityInfo(): Promise&lt;AbilityInfo&gt;
 
查询当前归属Ability详细信息。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;AbilityInfo&gt; | Promise对象，返回当前归属Ability详细信息。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.getAbilityInfo().then((data) => {
    console.info(`getAbilityInfo data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.getApplicationContext7+

getApplicationContext(): Context
 
获取应用上下文信息。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Context | 返回应用上下文信息。 |
 
 
**示例：**
 
```text
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext().getApplicationContext();
```
 
  

##### Context.isUpdatingConfigurations7+

isUpdatingConfigurations(callback: AsyncCallback&lt;boolean&gt;): void
 
检查此能力的配置是否正在更改。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数，返回true表示该Ability的配置正在更改，否则返回false。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.isUpdatingConfigurations((error, data) => {
    if (error && error.code !== 0) {
        console.error(`isUpdatingConfigurations fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`isUpdatingConfigurations success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

##### Context.isUpdatingConfigurations7+

isUpdatingConfigurations(): Promise&lt;boolean&gt;
 
检查此能力的配置是否正在更改。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回true表示该Ability的配置正在更改，否则返回false。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.isUpdatingConfigurations().then((data) => {
    console.info(`isUpdatingConfigurations data: ${JSON.stringify(data)}`);
});
```
 
  

##### Context.printDrawnCompleted7+

printDrawnCompleted(callback: AsyncCallback&lt;void&gt;): void
 
通知系统绘制此页面功能所需的时间。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当通知系统绘制此页面功能所需的时间成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.printDrawnCompleted((err) => {
    console.error(`printDrawnCompleted err: ${JSON.stringify(err)}`);
});
```
 
  

##### Context.printDrawnCompleted7+

printDrawnCompleted(): Promise&lt;void&gt;
 
通知系统绘制此页面功能所需的时间。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```json
import featureAbility from '@ohos.ability.featureAbility';

let context: featureAbility.Context = featureAbility.getContext();
context.printDrawnCompleted().then((data) => {
    console.info(`printDrawnCompleted data: ${JSON.stringify(data)}`);
});
```
 
  

##### PermissionOptions7+

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 是 | 进程id。 |
| uid | number | 否 | 是 | 用户id。 |
 
 
  

##### PermissionRequestResult7+

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestCode | number | 否 | 否 | 用户传入的请求代码。 |
| permissions | Array&lt;string&gt; | 否 | 否 | 用户传入的权限。 |
| authResults | Array&lt;number&gt; | 否 | 否 | 请求权限的结果。 |
