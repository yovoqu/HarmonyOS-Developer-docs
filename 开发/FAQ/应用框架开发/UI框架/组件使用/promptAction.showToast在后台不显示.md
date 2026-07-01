# promptAction.showToast在后台不显示

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1480

#### 问题现象

APP进入后台时，希望能弹出Toast提示用户进入后台，但是Toast不显示。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/nhgU333oQryD5zhxSOzeNg/zh-cn_image_0000002658845071.png?HW-CC-KV=V1&HW-CC-Date=20260701T041255Z&HW-CC-Expire=86400&HW-CC-Sign=D7A8C5B2E6D28D79A8F617D9769E0FBE4C374DF7406538B4F9CCDAF44D221067)

 
 

#### 背景知识

- [Toast](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-toast)：即时反馈（Toast）是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。它通常在屏幕的底部或顶部短暂弹出，随后在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，避免干扰用户当前的操作流程。
- [Notification Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-overview)：Notification Kit（用户通知服务）为开发者提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

 
 

#### 解决方案

为了安全考虑，例如Toast恶意遮挡其他页面，Toast只能显示在当前的UI实例中，应用退出后，不会单独显示在桌面上。若是想在应用退出到后台时继续提醒用户，可以使用横幅通知功能。
 
- 在EntryAbility.ets文件中增加以下代码，在程序退至后台时会触发[onBackground](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle#onbackground)回调，在此回调中弹出横幅提醒用户。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">notificationManager </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.NotificationKit'</span><span style="color: rgb(181,106,1);">;</span>
```
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">通知方法</span></em>
<span style="color: rgb(0,0,255);">publishNotification</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">notificationRequest</span><span style="color: rgb(181,106,1);">:</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">描述通知的请求</span></em>
    <span style="color: rgb(181,106,1);">notificationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NotificationRequest </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">ID</span></em>
    <span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知内容</span></em>
    <span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">notificationContentType</span><span style="color: rgb(181,106,1);">:</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">普通文本类型通知</span></em>
      <span style="color: rgb(255,255,255);">notificationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ContentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NOTIFICATION_CONTENT_BASIC_TEXT</span><span style="color: rgb(181,106,1);">,</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">基本类型通知内容</span></em>
      <span style="color: rgb(255,255,255);">normal</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">应用名称</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">应用在后台运行</span><span style="color: rgb(132,63,161);">'</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">notificationSlotType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">notificationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SlotType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SOCIAL_COMMUNICATION</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发布通知</span></em>
  <span style="color: rgb(255,255,255);">notificationManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">publish</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">notificationRequest</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'publish success'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`publish failed,message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span>void <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">publishNotification</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
<em>  <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
  <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onBackground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

- 应用页面按照正常业务逻辑写即可，以hello world工程为例。Index.ets：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'HelloWorld'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.float.page_text_font_size'</span><span style="color: rgb(255,0,170);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bold</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'Welcome'</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
> [!NOTE]
> 运行上述示例需要在通知设置里开启此应用通知开关。也可通过代码拉起弹窗请求用户授权，实现详细请参考 业务流程 和 请求通知授权

 
 

#### 常见FAQ

Q：横幅通知可以提醒用户APP进入后台，是否有其他方案来实现？
 
A：可以使用[SoundPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#soundpool)播放自定义的提示音来提醒用户。这可以让用户听到明显的音频提示，知道应用已经转到后台。具体开发步骤及注意事项可以参考：[使用SoundPool播放短音频](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundpool-for-playback)。
 
 

#### 总结

- Toast不支持在应用退至后台后，仍发送提示框消息。
- 退至后台时，消息可以通过Notification Kit在客户端本地推送给用户。
- 若应用退到后台或进程终止后，仍希望有一些提醒用户的定时类通知，可以使用[Background Tasks Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/background-task-overview)进行消息创建。
- 远程推送消息至本地请使用[Push Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-introduction)。
