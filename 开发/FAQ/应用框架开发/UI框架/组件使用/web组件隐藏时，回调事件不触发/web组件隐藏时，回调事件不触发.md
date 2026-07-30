# web组件隐藏时，回调事件不触发

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1543

#### 问题现象

当web组件需要隐藏时，回调事件不触发，比如onPageBegin未触发。
 
问题代码示例参考如下：
 
```text
Web({})
  .onPageBegin(() => {
    console.info(`into onPageBegin`)
  })
  .visibility(Visibility.None)
```
 
 

#### 背景知识

[visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility)是控制组件显隐控制的一个基础属性。其值类型说明参考文档：[Visibility枚举说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#visibility)。
 
 

#### 问题定位

通过ArkUI Inspector工具，可以看到出问题的组件并没有被渲染出来。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/_gzHfCtTRE2BiJzcRj985w/zh-cn_image_0000002658968439.png?HW-CC-KV=V1&HW-CC-Date=20260730T072409Z&HW-CC-Expire=86400&HW-CC-Sign=2E0138B803ACA884F85655A2D8CCE8FF67C0ADE2388D6E238B23D8CDDE60062B)

 
 

#### 分析结论

visibility属性设置Visibility.None后，是不会渲染组件的，所以组件相关的生命周期也不会触发。
 
 

#### 修改建议

把visibility属性的值改成Visibility.Hidden即可。
 
```text
import webview from '@ohos.web.webview';

@Entry
@Component
struct Index {
<em>  // 开发者需根据自身需求填写网址</em>
  @State webSrc: string = 'xxx';
  @State webController: WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: this.webSrc, controller: this.webController })
        .size({ width: '100%', height: '100%' })
        .onPageBegin(() => {
          console.info(`into onPageBegin (web Hidden)`);
        })
    <em>    // 按照示例代码，开发者需要隐藏，因此设置为Visibility.Hidden</em>
        .visibility(Visibility.Hidden)
        .geolocationAccess(false)
        .fileAccess(false);
    }
    .height('100%')
    .width('100%')
  }
}
```
 
日志中onPageBegin()触发，打印了into onPageBegin (web Hidden)。
