# 使用request.uploadFile进行多文件上传，后台未收到文件

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-29

#### 问题现象

多文件上传场景下使用[request.uploadFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestuploadfile9-1)，后台服务未收到文件，如何排查？
 
 

#### 解决方案

- 检查是否调用request.uploadFile时，文件不存在于应用缓存文件路径下。
- 检查是否UploadConfig配置参数中文件的uri不是"internal://cache/"的形式。
- 检查是否后台服务将接收文件参数设置为"MultipartFile[] file"，如果后端服务接口定义接收文件参数设置为"MultipartFile[] file"，则不应使用request.uploadFile，可以使用[request.agent.create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentcreate10)或者三方库[@ohos/axios](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Faxios)进行多文件上传。
