# Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-28

## Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决
 


##### 问题现象

使用driver.swipe(direction=UiParam.UP)方法执行上滑操作时，报错NameError: name 'UiParam' is not defined。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Nls-yt1yRsmbGVm7bK5jZA/zh-cn_image_0000002628569514.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=80F88FE38735F26D45BFAE3B2F8832D1B8DA533F3646610DBF1CBC26DBD62DA3)

 
 

##### 解决方案

- 根据报错提示找到相关代码行，将鼠标光标移动到有波浪线报错的位置，会弹出如下提示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LSyhfsZhRpejvDjPLZ6EVQ/zh-cn_image_0000002658928837.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=4F3251B8104BCC1BAD5300E3C14B0EB195D371AD1DC0A0A4C6A9EC96F103F2B0)

- 点击导入'hypium.model.UiParam'，此时查看代码页面顶端，自动导入了相关模块，如下图：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/P0C7nCC4Rrq1m2Lhzt_cCA/zh-cn_image_0000002628409624.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=598D64CA3A4E7992F0E7AFDE7393589D40415616077021624832C796620E4FBD)


 
 

##### 总结

当出现NameError: name 'XXX' is not defined，都可以尝试使用此方式导入相关模块来进行方法调用。
