# Web组件加载H5，页面中视频全屏按钮置灰

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-145

## Web组件加载H5，页面中视频全屏按钮置灰
 


##### 问题现象

通过Web组件加载H5页面，页面中视频的全屏按钮置灰，无法点击。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9cmkUE5MRgSvZGJTmLBc3w/zh-cn_image_0000002628899138.png?HW-CC-KV=V1&HW-CC-Date=20260701T025741Z&HW-CC-Expire=86400&HW-CC-Sign=70987EA5E2910FED077D86E50A289C3B11F919C932121B79D003C81D8A4656FC)

 
 

##### 背景知识

[使用Web组件加载页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-page-loading-with-web-components)：页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。
 
 

##### 问题定位

- 查看浏览器访问H5页面时视频的全屏按钮是否是置灰状态。
- Web组件加载时全屏按钮是否是置灰状态。

 
 

##### 分析结论

直接打开HTML文件在浏览器中全屏按钮也是置灰的，由此怀疑是H5页面写法有问题，打开H5页面发现其加载了iframe，浏览器对iframe中的视频播放做了限制，根据其安全策略阻止视频全屏播放。
 
 

##### 修改建议

需要添加iframe全屏权限属性allowfullscreen="true"，为了解决浏览器兼容问题，最好也加上mozallowfullscreen="true"、webkitallowfullscreen="true"这两个属性。
 
WebComponent.ets（下方Web组件引入的本地文件需要在rawfile文件夹中有相应的文件）：
 
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('test.html'), controller: this.controller })
        .domStorageAccess(true)
        .geolocationAccess(false)
        .fileAccess(false)
        .width('100%')
        .height('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```
 
test.html（需要将下方iframe加载的src内容替换为实际的业务中的有视频播放的链接）：
 
```text


    
    
    Responsive iFrame


    


```
