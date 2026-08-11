# request上传文件后headerReceive内容无法解析

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-64

#### 问题现象

[request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request)上传文件后通过[on('headerReceive')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#onheaderreceive7)获取headerReceive内容：
 
```json
{ <span style="color: rgb(132,63,161);">"headers"</span><span style="color: rgb(181,106,1);">: </span>{}<span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">"body"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"{"</span><span style="color: rgb(132,63,161);">code ":0,"msg ":"</span><span style="color: rgb(132,63,161);">操作成功</span><span style="color: rgb(132,63,161);">","data ":{"name ":"file.png ","url ":"","path ":""}}"</span>}
```
 
使用JSON序列化解析，报错Error message:Unexpected Object in JSON：
 
```json
let <span style="color: rgb(255,255,255);">headerObject</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RequestUploadHeaderInterface </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">headersStr</span><span style="color: rgb(255,0,170);">)</span>
```
 
 

#### 解决方案

通过JSON校验工具可以看出，需要序列化的内容不是正规的JSON字符串，若在已知响应内容的情况下，通过属性名的字符串形式获取body对象的属性，再用JSON序列化，如：JSON.parse(headersStr["body"])。
