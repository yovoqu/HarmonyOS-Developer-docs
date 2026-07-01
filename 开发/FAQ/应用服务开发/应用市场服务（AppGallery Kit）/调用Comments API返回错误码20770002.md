# 调用Comments API返回错误码20770002

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-45

## 调用Comments API返回错误码20770002
 


##### 问题现象

在调用Comments API的[查询应用评论列表](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/agcapi-comapi-getreviews-harmonyos-0000002470893976)结果返回了以下错误信息，创建API客户端使用的是团队主账号。
 
```text
{
    "code": 20770002,
    "msg": "uid no white list permission"
}
```
 
 

##### 解决方案

该错误信息显示用户没有白名单权限，Comments API下的所有API接口依赖于Marketing API，需要先参考[Marketing API](https://developer.huawei.com/consumer/cn/doc/promotion/bp-functions-marketing_api-0000001435633681)，开通权限后即可使用。
