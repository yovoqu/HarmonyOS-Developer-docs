# AI服务Cannot read property xxx of undefined报错

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-4

#### 问题现象

当接入AI服务遇到Cannot read property xxx of undefined报错。如，接入文字转语音遇到Cannot read property createEngine of undefined报错，接入图文识别能力遇到Cannot read property recognizeText of undefined报错，如何解决。
 
 

#### 解决方案

此类报错基本都是通过模拟器测试AI能力时出现。当前所有AI能力无法在模拟器中使用，模拟器能力支持情况详见[文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-specification)。
 
 

#### 总结

请勿使用模拟器测试AI能力。
