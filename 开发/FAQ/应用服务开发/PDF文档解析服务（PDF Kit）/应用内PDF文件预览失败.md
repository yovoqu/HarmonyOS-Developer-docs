# 应用内PDF文件预览失败

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-1

## 应用内PDF文件预览失败
 


##### 问题现象

用户在应用内预览PDF文件时，可能会出现预览失败，显示空白的现象。
 
 

##### 背景知识

- [PdfView预览组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-implements)：HarmonyOS应用通过集成该组件完成PDF文件的预览功能。[预览PDF文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-component)：通过加载本地路径的PDF文档，实现打开PDF文档的预览功能（为了避免文件目录的权限问题，建议通过沙箱目录加载和保存PDF文档）。
  
| 接口名 | 描述 |
| --- | --- |
| loadDocument() | 加载PDF文档。 |
| saveDocument() | 保存PDF文档。 |
- [Web组件预览PDF文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-pdf-preview)：Web组件提供了在网页中预览PDF的能力。应用通过Web组件的[src](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#weboptions)参数和[loadUrl()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)接口加载PDF文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/zjSQ2HU5TmqnTqB8Ydofbg/notice_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025836Z&HW-CC-Expire=86400&HW-CC-Sign=9EFE9C6124838662840A6246CD4276B8B8C645CE16F8AAD6AD4C1B4FF9E41A7B)
 
由于PDF预览页面会根据用户操作使用window.localStorage记录侧边导航栏的展开状态，因此需要开启文档对象模型存储[domStorageAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#domstorageaccess)权限。

 
 

##### 问题定位

- [PdfView预览组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-implements)提供预览PDF文档能力：搜索[loadDocument()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section073321844615)，检查传入的文件是否属于本地文件，不支持在线预览。
- 使用Web组件的PDF文档预览能力：
搜索[domStorageAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#domstorageaccess)，检查是否开启文档对象模型存储接口。
- 搜索Web组件的[src](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#weboptions)参数和[loadUrl()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)接口，检查传入的URL是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/jQ6KaqthSF-ZfQYEHSo63g/notice_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025836Z&HW-CC-Expire=86400&HW-CC-Sign=B66C88469E7011F6687D4909825738530D9F58E6BAFB796E079F0C1219EAD71A)
 
对于加载应用沙箱内PDF文档，检查是否开启应用中文件系统的访问[fileAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#fileaccess)权限。
 

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/QZ_MeyCOQA-r59Plrdj2ow/notice_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025836Z&HW-CC-Expire=86400&HW-CC-Sign=AA28FE8B425E75F623D9821F50C4D5DE6F4E9444CE89AB34A9B44C32A0D390FE)
 
Web组件的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过loadUrl()重新加载。

 
 
 

##### 分析结论

 

##### [h2]场景一

[PdfView预览组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-implements)提供预览PDF文档能力，由于不支持在线预览，导致预览失败。
 
 

##### [h2]场景二

使用Web组件的PDF文档预览能力：
 
- 由于未开启Web组件的文档对象模型存储（[domStorageAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#domstorageaccess)）接口，导致预览失败。
- 传入Web组件中[src](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#weboptions)参数和[loadUrl()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)接口的URL不正确，导致预览失败。

 
 

##### 修改建议

 

##### [h2]场景一

应用需要预览在线PDF文档时，可以先将PDF文件下载到本地，然后再通过PdfView组件进行预览，具体可参见[预览PDF文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-component)。
 
 

##### [h2]场景二

- 将[domStorageAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#domstorageaccess)的值设置为true，开启文档对象模型存储。
- 正确使用Web组件的[src](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#weboptions)参数和[loadUrl()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl)接口加载PDF文件。大致分为预览加载网络PDF文档、预览加载应用沙箱内PDF文档（需要开启应用中文件系统的访问[fileAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#fileaccess)权限）和预览加载本地PDF文档。详情请参考[使用Web组件的PDF文档预览能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-pdf-preview)。

 
 

##### FAQ

Q：Windows(X86)系统模拟器中使用Web组件加载PDF文档，为什么无法显示？
 
A：模拟器加载PDF文档只支持在MacOS(ARM)版本上运行，Windows(X86)系统的模拟器不支持加载预览。
