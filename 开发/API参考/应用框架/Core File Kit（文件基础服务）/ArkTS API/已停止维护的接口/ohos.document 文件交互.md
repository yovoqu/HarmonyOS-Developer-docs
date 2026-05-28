# @ohos.document (文件交互)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-document
**支持设备：** Phone | PC/2in1 | Tablet | TV

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口从API version 9开始废弃。不建议使用以下接口，调用以下接口将抛出异常。

  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
import document from '@ohos.document';
```
 
  

##### document.choose(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

choose(types?: string[]): Promise&lt;string&gt;
 
通过文件管理器选择文件，异步返回文件URI，使用promise形式返回结果。
 
**系统能力**：SystemCapability.FileManagement.UserFileService
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 否 | 限定文件选择的类型 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | 异步返回文件URI（注：当前返回错误码） |
 
 
**示例：**
 
```text
let types: Array<string> = [];
document.choose(types);
```
 
  

##### document.choose(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

choose(callback:AsyncCallback&lt;string&gt;): void
 
通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。
 
**系统能力**：SystemCapability.FileManagement.UserFileService
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 异步获取对应文件URI（注：当前返回错误码） |
 
 
**示例：**
 
```text
let uri: string = "";
document.choose((err: TypeError, uri: string) => {
  //do something with uri
});
```
 
  

##### document.choose(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

choose(types:string[], callback:AsyncCallback&lt;string&gt;): void
 
通过文件管理器选择文件，异步返回文件URI，使用callback形式返回结果。
 
**系统能力**：SystemCapability.FileManagement.UserFileService
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | string[] | 是 | 限定选择文件的类型 |
| callback | AsyncCallback&lt;string&gt; | 是 | 异步获取对应文件URI（注：当前返回错误码） |
 
 
**示例：**
 
```text
let types: Array<string> = [];
let uri: string = "";
document.choose(types, (err: TypeError, uri: string) => {
  //do something with uri
});
```
 
  

##### document.show(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

show(uri:string, type:string):Promise&lt;void&gt;
 
异步打开URI对应的文件，使用promise形式返回结果。
 
**系统能力**：SystemCapability.FileManagement.UserFileService
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise回调返回void表示成功打开文件（注：当前返回错误码） |
 
 
**示例：**
 
```text
let type: string = "";
let uri: string = "";
document.show(uri, type);
```
 
  

##### document.show(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

show(uri:string, type:string, callback:AsyncCallback&lt;void&gt;): void
 
异步打开URI对应的文件，使用callback形式返回结果。
 
**系统能力**：SystemCapability.FileManagement.UserFileService
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待打开的文件URI |
| type | string | 是 | 待打开文件的类型 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步打开uri对应文件（注：当前返回错误码） |
 
 
**示例：**
 
```text
let type: string = "";
let uri: string = "";
document.show(uri, type, (err: TypeError) => {
  //do something
});
```
