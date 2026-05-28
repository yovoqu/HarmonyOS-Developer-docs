# deferredLink (延迟链接能力)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/applinking-deferredlink-api
**支持设备：** Phone | PC/2in1 | Tablet

本模块提供App Linking Kit的延迟链接能力。通过该能力，系统会对用户点击的应用链接保存十分钟，以便当用户下载安装并打开应用时，仍能获取之前点击的该应用相关链接。
 
**起始版本：** 5.0.3(15)
  

##### 导入模块

```text
import { deferredLink } from '@kit.AppLinkingKit';
```
 
  

##### popDeferredLink

popDeferredLink(): Promise&lt;string&gt;
 
应用首次启动时从系统缓存中获取用户之前点击的该应用相关链接信息，链接仅能被获取一次。获取链接后，系统会从缓存中删除该链接。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.BundleManager.AppLinking.DeferredLink
 
**起始版本：** 5.0.3(15)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回延迟链接。 |
 
 
**示例**：
 
```text
import { deferredLink } from '@kit.AppLinkingKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 应用首次启动时，获取用户之前点击的该应用相关链接
deferredLink.popDeferredLink().then((link: string) => {
  hilog.info(0x0000, 'testTag', `Succeeded in getting deferred link, result: ${link}`);
  // 若延迟链接不为空，开发者可根据自身业务逻辑配置链接，跳转至详情页面
  if (link) {
    // 根据业务逻辑配置链接，自行跳转至详情页面
  }
}).catch(() => {
  // 发生未知错误
  hilog.error(0x0000, 'testTag', `Failed to get deferred link.`);
})
```
