# 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-14

问题描述

自动生成签名失败。


![](assets/自动签名时提示“The%20signature%20does%20not%20take%20effect%20or%20has%20expired.%20It%20may%20be%20the%20current%20system%20time%20is%20inaccurate,%20please%20calibrate%20the%20system%20time%20and%20sign%20again”错误/file-20260515130002261-0.png)


解决方案

报错原因：本地PC和服务器时间不一致。请将本地PC时间与北京时间进行对比，精确到秒。

DevEco Studio签名提示系统时间不正确，请在设置中选择“时间和语言”>“日期和时间”，开启自动设置时间功能，确保时间精确到1-2秒。
