# 使用Testing API的更新测试版本接口，报错204144691

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-58

## 使用Testing API的更新测试版本接口，报错204144691
 


##### 问题现象

调用[更新测试版本](https://developer.huawei.com/consumer/cn/doc/app/agc-help-test-api-modify-test-version-0000002271160657)接口时，报错204144691。
 
报错信息：
 
```text
{
  "ret":
  {
    "code": 204144691,
    "msg": "[amis] update version information failed, additional msg is [[AppGalleryConnectAppMetaInfoService]Harmony test apiLevel check failed, support apiLevel at least 10]"
  }
}
```
 
 

##### 解决方案

调用提交审核接口报错：
 
{"ret":{"code":204144691,"msg":"[amis] update version information failed, additional msg is [[AppGalleryConnectAppMetaInfoService]Harmony test apiLevel check failed, support apiLevel at least 10]"}}
 
这个问题的两种原因与解决方案如下：
 
- 提交审核的应用app包apiLevel确实低于10，这种情况请使用apiLevel更高的包。
- 包还没有解析完成，就调用提交审核接口，这种情况需要轮询查询包状态接口建议设置轮询时间5分钟，待包解析完成后再调用提交审核接口。
