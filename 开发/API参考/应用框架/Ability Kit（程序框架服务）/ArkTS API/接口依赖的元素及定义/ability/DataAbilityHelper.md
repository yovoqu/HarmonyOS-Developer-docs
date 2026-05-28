# DataAbilityHelper

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可以通过[acquireDataAbilityHelper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#featureabilityacquiredataabilityhelper7)接口获取DataAbilityHelper对象。
 
> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import ability from '@ohos.ability.ability';
```
 
  

#### 使用说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

使用前根据具体情况引入如下模块
 
```text
import ohos_data_ability from '@ohos.data.dataAbility';
import relationalStore from '@ohos.data.relationalStore';
```
 
  

#### DataAbilityHelper.openFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

openFile(uri: string, mode: string, callback: AsyncCallback&lt;number&gt;): void
 
打开指定uri对应的文件，返回文件描述符。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的uri。 |
| mode | string | 是 | 表示文件打开模式，可以设置为‘r’表示只读访问，‘w’表示只写访问，‘rw’表示读写访问等。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回文件描述符。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let mode = 'rw';
DAHelper.openFile('dataability:///com.example.DataAbility', mode, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`openFile fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`openFile success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.openFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

openFile(uri: string, mode: string): Promise&lt;number&gt;
 
打开指定uri对应的文件，返回文件描述符。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待打开文件的uri。 |
| mode | string | 是 | 表示文件打开模式，可以设置为‘r’表示只读访问，‘w’表示只写访问，‘rw’表示读写访问等。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回文件说明符。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let mode = 'rw';
DAHelper.openFile('dataability:///com.example.DataAbility', mode).then((data) => {
    console.info(`openFile data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.on('dataChange')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'dataChange', uri: string, callback: AsyncCallback&lt;void&gt;): void
 
注册观察者以监听uri指定数据的数据变化通知。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示监听操作类型，'dataChange'表示数据变化操作。 |
| uri | string | 是 | 表示待监听数据变化的uri。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当注册观察者以监听uri指定数据的数据变化通知成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
function onChangeNotify() {
    console.info('onChangeNotify call back');
};
DAHelper.on(
    'dataChange',
    'dataability:///com.example.DataAbility',
    onChangeNotify
);
```
 
  

#### DataAbilityHelper.off('dataChange')

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'dataChange', uri: string, callback?: AsyncCallback&lt;void&gt;): void
 
注销观察者以停止监听uri指定数据的数据变化通知。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 表示监听操作类型，'dataChange'表示数据变化操作。 |
| uri | string | 是 | 表示待取消监听数据变化的uri。 |
| callback | AsyncCallback&lt;void&gt; | 否 | 回调函数。当注销观察者以停止监听uri指定数据的数据变化通知成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```text
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
function onChangeNotify() {
    console.info('onChangeNotify call back');
};
DAHelper.off(
    'dataChange',
    'dataability:///com.example.DataAbility',
    onChangeNotify
);
DAHelper.off(
    'dataChange',
    'dataability:///com.example.DataAbility',
);
```
 
  

#### DataAbilityHelper.getType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getType(uri: string, callback: AsyncCallback&lt;string&gt;): void
 
获取给定uri指向数据的媒体资源类型。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取数据的uri。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回与uri指向数据匹配的媒体资源类型。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.getType('dataability:///com.example.DataAbility', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`getType fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getType success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.getType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getType(uri: string): Promise&lt;string&gt;
 
获取给定uri指向数据的媒体资源类型。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取数据的uri。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回与uri指向数据匹配的媒体资源类型。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.getType('dataability:///com.example.DataAbility').then((data) => {
    console.info(`getType data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.getFileTypes

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFileTypes(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array&lt;string&gt;>): void
 
获取支持的文件媒体资源类型。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取文件的uri。 |
| mimeTypeFilter | string | 是 | 表示待获取文件的媒体资源类型。 |
| callback | AsyncCallback<Array&lt;string&gt;> | 是 | 回调函数，返回匹配的媒体资源类型数组。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.getFileTypes( 'dataability:///com.example.DataAbility', 'image/*', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`getFileTypes fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getFileTypes success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.getFileTypes

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFileTypes(uri: string, mimeTypeFilter: string): Promise<Array&lt;string&gt;>
 
获取支持的文件媒体资源类型。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待获取文件的uri。 |
| mimeTypeFilter | string | 是 | 表示待获取文件的媒体资源类型。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;string&gt;> | Promise对象，返回匹配的媒体资源类型数组。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.getFileTypes('dataability:///com.example.DataAbility', 'image/*').then((data) => {
    console.info(`getFileTypes data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.normalizeUri

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

normalizeUri(uri: string, callback: AsyncCallback&lt;string&gt;): void
 
将引用数据功能的给定uri转换为规范化uri。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，如果数据功能支持uri规范化，则返回规范化uri对象；否则返回null。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.normalizeUri('dataability:///com.example.DataAbility', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`normalizeUri fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`normalizeUri success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.normalizeUri

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

normalizeUri(uri: string): Promise&lt;string&gt;
 
将引用数据功能的给定uri转换为规范化uri。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，如果数据功能支持uri规范化，则返回规范化uri对象；否则返回null。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.normalizeUri('dataability:///com.example.DataAbility').then((data) => {
    console.info(`normalizeUri data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.denormalizeUri

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

denormalizeUri(uri: string, callback: AsyncCallback&lt;string&gt;): void
 
将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要反规范化的uri对象。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回反规范化uri对象。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.denormalizeUri('dataability:///com.example.DataAbility', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`denormalizeUri fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`denormalizeUri success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.denormalizeUri

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

denormalizeUri(uri: string): Promise&lt;string&gt;
 
将由normalizeUri（uri）生成的给定规范化uri转换为非规范化uri。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要规范化的uri对象。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回反规范化uri对象。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.denormalizeUri('dataability:///com.example.DataAbility').then((data) => {
    console.info(`denormalizeUri data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.notifyChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

notifyChange(uri: string, callback: AsyncCallback&lt;void&gt;): void
 
通知注册的观察者，uri指定数据的数据变化。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示数据变化的uri。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当通知注册的观察者成功，err为undefined，否则为错误对象。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.notifyChange('dataability:///com.example.DataAbility', (error) => {
    if (error && error.code !== 0) {
        console.error(`notifyChange fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info('notifyChange success');
    }
});
```
 
  

#### DataAbilityHelper.notifyChange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

notifyChange(uri: string): Promise&lt;void&gt;
 
通知注册的观察者，uri指定数据的数据变化。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示数据变化的uri。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.notifyChange('dataability:///com.example.DataAbility').then(() => {
    console.info('================>notifyChangeCallback================>');
});
```
 
  

#### DataAbilityHelper.insert

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

insert(uri: string, valuesBucket: [rdb.ValuesBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb#valuesbucket), callback: AsyncCallback&lt;number&gt;): void
 
将单个数据记录插入数据库。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBucket | rdb.ValuesBucket | 是 | 表示要插入的数据记录。如果此参数为空，将插入一个空行。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回插入数据记录的索引。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
const valueBucket: rdb.ValuesBucket = {
    'name': 'rose',
    'age': 22,
    'salary': 200.5,
    'blobType': 'u8',
};
DAHelper.insert('dataability:///com.example.DataAbility', valueBucket, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`insert fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`insert success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.insert

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

insert(uri: string, valuesBucket: [rdb.ValuesBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb#valuesbucket)): Promise&lt;number&gt;
 
将单个数据记录插入数据库。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBucket | rdb.ValuesBucket | 是 | 表示要插入的数据记录。如果此参数为空，将插入一个空行。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回插入数据记录的索引。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
const valueBucket: rdb.ValuesBucket = {
    'name': 'rose1',
    'age': 221,
    'salary': 20.5,
    'blobType': 'u8',
};
DAHelper.insert('dataability:///com.example.DataAbility', valueBucket).then((data) => {
    console.info(`insert data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.batchInsert

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback&lt;number&gt;): void
 
将多个数据记录插入数据库。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBuckets | Array<rdb.ValuesBucket> | 是 | 表示要插入的数据记录数组。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回插入的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let cars = new Array({'name': 'roe11', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
                     {'name': 'roe12', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
                     {'name': 'roe13', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket);
DAHelper.batchInsert('dataability:///com.example.DataAbility', cars, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`batchInsert fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`batchInsert success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.batchInsert

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

batchInsert(uri: string, valuesBuckets: Array<rdb.ValuesBucket>): Promise&lt;number&gt;
 
将多个数据记录插入数据库。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要插入数据的uri。 |
| valuesBuckets | Array<rdb.ValuesBucket> | 是 | 表示要插入的数据记录数组。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回插入的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let cars = new Array({'name': 'roe11', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
                     {'name': 'roe12', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket,
                     {'name': 'roe13', 'age': 21, 'salary': 20.5, 'blobType': 'u8',} as rdb.ValuesBucket);
DAHelper.batchInsert('dataability:///com.example.DataAbility', cars).then((data) => {
    console.info(`batchInsert data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.delete

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback&lt;number&gt;): void
 
从数据库中删除一个或多个数据记录。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回已删除的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.delete('dataability:///com.example.DataAbility', da, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`delete fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`delete success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.delete

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

delete(uri: string, predicates?: dataAbility.DataAbilityPredicates): Promise&lt;number&gt;
 
从数据库中删除一个或多个数据记录。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回已删除的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.delete('dataability:///com.example.DataAbility', da).then((data) => {
    console.info(`delete data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.delete

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

delete(uri: string, callback: AsyncCallback&lt;number&gt;): void
 
predicates筛选条件为空，自定义数据库删除数据记录的处理逻辑。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要删除数据的uri。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回已删除的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.delete('dataability:///com.example.DataAbility', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`delete fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`delete success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.update

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

update(uri: string, valuesBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback&lt;number&gt;): void
 
更新数据库中的数据记录。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | rdb.ValuesBucket | 是 | 表示要更新的数据。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回更新的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
const va: rdb.ValuesBucket = {
    'name': 'roe1',
    'age': 21,
    'salary': 20.5,
    'blobType': 'u8',
};
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.update('dataability:///com.example.DataAbility', va, da, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`update fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`update success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.update

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

update(uri: string, valuesBucket: rdb.ValuesBucket, predicates?: dataAbility.DataAbilityPredicates): Promise&lt;number&gt;
 
更新数据库中的数据记录。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | rdb.ValuesBucket | 是 | 表示要更新的数据。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，应定义处理逻辑。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回更新的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
const va: rdb.ValuesBucket = {
    'name': 'roe1',
    'age': 21,
    'salary': 20.5,
    'blobType': 'u8',
};
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.update('dataability:///com.example.DataAbility', va, da).then((data) => {
    console.info(`update data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.update

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

update(uri: string, valuesBucket: rdb.ValuesBucket, callback: AsyncCallback&lt;number&gt;): void
 
predicates筛选条件为空，自定义更新数据库的处理逻辑。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要更新数据的uri。 |
| valuesBucket | rdb.ValuesBucket | 是 | 表示要更新的数据。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回更新的数据记录数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
const va: rdb.ValuesBucket = {
    'name': 'roe1',
    'age': 21,
    'salary': 20.5,
    'blobType': 'u8',
};
DAHelper.update('dataability:///com.example.DataAbility', va, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`update fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`update success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.query

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

query(uri: string, columns: Array&lt;string&gt;, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback&lt;ResultSet&gt;): void
 
查询数据库中的数据。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array&lt;string&gt; | 是 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |
| callback | AsyncCallback&lt;ResultSet&gt; | 是 | 回调函数，返回查询结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let cars=new Array('value1', 'value2', 'value3', 'value4');
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.query('dataability:///com.example.DataAbility', cars, da, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`query fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`query success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.query

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

query(uri: string, callback: AsyncCallback&lt;ResultSet&gt;): void
 
查询数据库中的数据。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| callback | AsyncCallback&lt;ResultSet&gt; | 是 | 回调函数，返回查询结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
DAHelper.query('dataability:///com.example.DataAbility', (error, data) => {
    if (error && error.code !== 0) {
        console.error(`query fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`query success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.query

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

query(uri: string, columns: Array&lt;string&gt;, callback: AsyncCallback&lt;ResultSet&gt;): void
 
查询数据库中的数据。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array&lt;string&gt; | 是 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| callback | AsyncCallback&lt;ResultSet&gt; | 是 | 回调函数，返回查询结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let cars = new Array('value1', 'value2', 'value3', 'value4');
DAHelper.query('dataability:///com.example.DataAbility', cars, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`query fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`query success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.query

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

query(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback&lt;ResultSet&gt;): void
 
查询数据库中的数据。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| predicates | dataAbility.DataAbilityPredicates | 是 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |
| callback | AsyncCallback&lt;ResultSet&gt; | 是 | 回调函数，返回查询结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.query('dataability:///com.example.DataAbility', da, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`query fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`query success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.query

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

query(uri: string, columns?: Array&lt;string&gt;, predicates?: dataAbility.DataAbilityPredicates): Promise&lt;ResultSet&gt;
 
查询数据库中的数据。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要查询数据的uri。 |
| columns | Array&lt;string&gt; | 否 | 表示要查询的列。如果此参数为空，则查询所有列。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 表示筛选条件。当此参数为null时，自定义查询数据库中数据的处理逻辑。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;ResultSet&gt; | Promise对象，返回查询结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import ohos_data_ability from '@ohos.data.dataAbility';

let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.DataAbility'
);
let cars = new Array('value1', 'value2', 'value3', 'value4');
let da = new ohos_data_ability.DataAbilityPredicates();
DAHelper.query('dataability:///com.example.DataAbility', cars, da).then((data) => {
    console.info(`query data: ${JSON.stringify(data)}`);
});
```
 
  

#### DataAbilityHelper.call

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

call(uri: string, method: string, arg: string, extras: PacMap, callback: AsyncCallback&lt;PacMap&gt;): void
 
调用DataAbility的扩展接口。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx' |
| method | string | 是 | 表示被调用的方法名。 |
| arg | string | 是 | 表示需传入的参数。 |
| extras | PacMap | 是 | 表示扩展的键值对参数。 |
| callback | AsyncCallback&lt;PacMap&gt; | 是 | 回调函数，返回扩展的键值对参数。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.jsapidemo.UserDataAbility'
);
dataAbilityHelper.call('dataability:///com.example.jsapidemo.UserDataAbility',
    'method', 'arg', {'key1':'value1'}, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`call fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`call success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.call

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

call(uri: string, method: string, arg: string, extras: PacMap): Promise&lt;PacMap&gt;
 
调用DataAbility的扩展接口。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx' |
| method | string | 是 | 表示被调用的方法名。 |
| arg | string | 是 | 表示需传入的参数。 |
| extras | PacMap | 是 | 表示扩展的键值对参数。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;PacMap&gt; | Promise对象，返回扩展的键值对参数。 |
 
 
**示例：**
 
```text
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.jsapidemo.UserDataAbility'
);
dataAbilityHelper.call('dataability:///com.example.jsapidemo.UserDataAbility',
    'method', 'arg', {'key1':'value1'}).then((data) => {
    console.info(`call success, data: ${data}`);
}).catch((error: BusinessError) => {
    console.error(`call failed, error: ${error}`);
});
```
 
  

#### DataAbilityHelper.executeBatch

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

executeBatch(uri: string, operations: Array&lt;DataAbilityOperation&gt;, callback: AsyncCallback<Array&lt;DataAbilityResult&gt;>): void
 
批量操作数据库中的数据。使用callback异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| operations | Array&lt;DataAbilityOperation&gt; | 是 | 表示数据操作数组，其中可以包含对数据库的多个不同操作。 |
| callback | AsyncCallback<Array&lt;DataAbilityResult&gt;> | 是 | 回调函数，在DataAbilityResult数组中返回每个操作的结果。 |
 
 
**示例：**
 
```json
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';

// 根据DataAbilityOperation列表选择要对数据库做的操作
let op: Array<ability.DataAbilityOperation> = new Array();
let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.jsapidemo.UserDataAbility'
);
dataAbilityHelper.executeBatch('dataability:///com.example.jsapidemo.UserDataAbility', op, (error, data) => {
    if (error && error.code !== 0) {
        console.error(`executeBatch fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`executeBatch success, data: ${JSON.stringify(data)}`);
    }
});
```
 
  

#### DataAbilityHelper.executeBatch

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

executeBatch(uri: string, operations: Array&lt;DataAbilityOperation&gt;): Promise<Array&lt;DataAbilityResult&gt;>
 
批量操作数据库中的数据。使用Promise异步回调。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| operations | Array&lt;DataAbilityOperation&gt; | 是 | 表示数据操作数组，其中可以包含对数据库的多个不同操作。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;DataAbilityResult&gt;> | Promise对象，在DataAbilityResult数组中返回每个操作的结果。 |
 
 
**示例：**
 
```text
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

// 根据DataAbilityOperation列表选择要对数据库做的操作
let op: Array<ability.DataAbilityOperation> = new Array();
let dataAbilityHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(
    'dataability:///com.example.jsapidemo.UserDataAbility'
);
dataAbilityHelper.executeBatch('dataability:///com.example.jsapidemo.UserDataAbility', op).then((data) => {
    console.info(`executeBatch success, data: ${data}`);
}).catch((error: BusinessError) => {
    console.error(`executeBatch failed, error: ${error}`);
});
```
 
  

#### PacMap

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于存储数据的PacMap类型。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [key: string] | number \| string \| boolean \| Array<string \| number \| boolean> \| null | 否 | 是 | 数据存储在键值对中。 |
