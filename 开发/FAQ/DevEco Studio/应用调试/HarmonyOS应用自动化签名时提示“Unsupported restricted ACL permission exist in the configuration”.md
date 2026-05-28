# HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5

**问题现象**
 
在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。
 

![](assets/HarmonyOS应用自动化签名时提示“Unsupported%20restricted%20ACL%20permission%20exist%20in%20the%20configuration”/file-20260515130306605-0.png)

 
**解决措施**
 
出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。
 
**参考链接**
 
[自动签名支持的ACL权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section5301916183411)
 
[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)
