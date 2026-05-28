# Class (NativeMediaPlayerSurfaceInfo)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

使用[enableNativeMediaPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enablenativemediaplayer12)来进行同层渲染的surface信息配置，以开启应用接管网页媒体播放功能。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 12开始支持。 示例效果请以真机运行为准。

  

##### 属性

**系统能力：** SystemCapability.Web.Webview.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id12+ | string | 否 | 否 | surface的id，用于同层渲染的NativeImage的surfaceId。 详见NativeEmbedDataInfo。 |
| rect12+ | RectEvent | 否 | 否 | surface的位置信息。 |
