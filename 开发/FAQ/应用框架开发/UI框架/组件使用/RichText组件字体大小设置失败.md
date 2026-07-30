# RichText组件字体大小设置失败

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1439

#### 问题现象

从前端获取富文本内容时，无法直接通过属性修改字体大小。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/NwFGtrepS_m5jrgU3l2Ptg/zh-cn_image_0000002628604256.png?HW-CC-KV=V1&HW-CC-Date=20260701T041247Z&HW-CC-Expire=86400&HW-CC-Sign=993F0BD186A7D1948497CF885B1E98E2E95E06C8613E764C6F2D43BD36EA96FD)

 
 

#### 背景知识

- [RichText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)用于解析并显示HTML格式文本，适用于不需要对显示效果进行较多自定义的应用场景，并且仅支持有限的通用属性和事件。只支持通用属性中width，height，size，layoutWeight四个属性。padding，margin，constraintSize属性使用时与通用属性描述不符，暂不支持。不支持通过设置属性与事件，来修改背景颜色、字体颜色、字体大小、动态改变内容等。
- [WebviewController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller)：可以控制Web组件各种行为（包括页面导航、生命周期状态、JavaScript交互等行为）。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。

 
 

#### 解决方案

RichText组件通过复用Web组件来提供基础能力，如HTML页面的解析和渲染等。在需要对HTML字符串显示效果进行大量自定义的应用场景中，可以考虑使用Web组件作为替代方案。
 
设置富文本字体大小具体方案如下：
 1. 在富文本前添加head标签；
2. 将meta中content属性值设置为width=device-width, initial-scale=1，使页面的布局视口自动设置为各个移动设备的理想视口，实现HTML适配移动端设备；
3. 在onControllerAttached回调中使用loadData加载指定数据。
 
示例代码如下：
 
```text
import web_webview from '@ohos.web.webview';

@Entry
@Component
struct RichTextExample {
  value: string =
    '<html><body style="font-size:48px;padding:16px"><big>RichText用于解析并显示HTML格式文本。</big><br>适用于不需要对显示效果进行较多自定义的应用场景，并且仅支持有限的通用属性和事件。</body></html>';
  richStrHead: string = '<head><meta name="viewport" content="width=device-width, initial-scale=0.5"></head>';
  webviewController: web_webview.WebviewController = new web_webview.WebviewController();

  build() {
    Column() {
      Text('RichText显示模块')
        .padding({bottom:16})
      RichText(this.value)
        .width('100%')
        .height(100)
        .backgroundColor('#f1f3f5')
        .borderRadius(10)
     <em> // .padding(16)</em>

      Divider()
        .height(2)
        .color('#182431')
        .opacity(0.6)
        .margin({
          left: 8,
          right: 8,
          top: 16,
          bottom: 16
        })
      Text('Web显示模块')
        .padding({bottom:16})
      Web({ src: '', controller: this.webviewController })
        .onControllerAttached(() => { <em>// 当Controller成功绑定到Web组件时触发该回调</em>
          this.webviewController.loadData(this.richStrHead + this.value, 'text/html', 'UTF-8', '', '');
        })
        .fileAccess(false)
        .geolocationAccess(false)
        .width('100%')
        .height(200)
        .backgroundColor('#f1f3f5')
        .minFontSize(30)
        .borderRadius(10)
    }
    .width('100%')
    .height('100%')
    .margin({ top: 30 })
    .padding(16)
  }
}
```
 
 

#### 常见FAQ

Q：RichText组件如何设置字体大小？
 
A：RichText底层是WebView，如果要使用更大的字号，可以使用CSS语法，如：RichText('<p style="font-size: 100px; font-family: verdana; color: rgb(24,78,228)">ABC</p>')
 
 

#### 总结

Web组件支持的字体大小相关属性如下：
  
| 属性 | 说明 |
| --- | --- |
| defaultFontSize | 设置网页的默认等宽字体大小，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。默认值：13。 |
| minFontSize | 设置网页字体大小最小值，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。默认值：8。 |
| minLogicalFontSize | 设置网页逻辑字体大小最小值，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。默认值：8。 |
| defaultFixedFontSize | 设置网页的默认等宽字体大小，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。默认值：13。 |
