# 开发工具DevEco中，代码开发界面的白竖线如何删除

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-24

#### 问题现象

DevEco Studio中，代码开发界面显示的白竖线如何取消？
 
在这个白竖线附近时，代码就会自动折行显示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/xT6SqCnBRhG0kAQc4vUVoQ/zh-cn_image_0000002658804341.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=D097ED00FF51E9BC3C618C9D87E83DC5C30E4316B5CCE35F806EC569BE7062A9)

 
 

#### 背景知识

代码开发界面的白竖线是一个视觉分割线，它允许用户设置一个特定的列数作为代码的宽度限制。当代码行超过这个限制时，编程工具会自动将代码换行到下一行，从而保持代码的整洁和可读性。
 
 

#### 解决方案

可以使用如下两种解决方案：
 
- 完全取消分割线：在开发工具File->Settings->Editor->General->Appearance取消勾选show hard wrap and visual guides。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/keBm0PyxS72I45Sp4HIAJQ/zh-cn_image_0000002628564982.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=BF2A778E8E3D63DB609485165B827A1C2A91B0E6EFAC9CEA2A161A7ADC4AB7A2)

- 增大代码的宽度限制：在开发工具File->Settings->Editor->Code Style中增大Hard wrap值，如将其值改为1000。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QsBGDNZSTTGcOUsdDOy2qQ/zh-cn_image_0000002628405078.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=C255100E6AC3B0065117368B87C47F5A53E2B80F2E5939F57A3EA73C6FEE7CEF)


 
 

#### 常见FAQ

Q：过长的三元表达式会直接换行但不带缩进，是否有办法可以调节？
 
A：在IDE的setting中，Editor-Code Style-ArkTS下，找到Ternary operation，勾选下面的两个选项。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/w6brR5PrQ_2vbMax9F2z6A/zh-cn_image_0000002658924295.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=A2CE781087C6555F524CF09695245A2083811C1CBBF661A541A88E586D4631CF)

 
Q：粘贴代码时，如何关闭编辑器自动格式化？
 
A：在IDE的setting中，Editor-General-Smart Keys下，找到Reformat on paste选项，下拉选择None。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/msPscaHnR-W0zc4VzLqDMQ/zh-cn_image_0000002658804349.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=1B471A73E0EBDBDDA890F0C968015B9185DF41310077BB3FBF873078A3B1DBA1)

 
Q：在File -> Settings -> Appearance -> Editor -> Font设置字体大小大于14（比如设置为16），在File -> Settings -> Editor -> Color Scheme修改任意类型代码颜色，预览器颜色错乱。
 
A：设置代码颜色后需要按回车确认。
 
Q：如何使用快捷键批量注释代码？
 
A：选中需要注释的代码，按住ctrl + /键方可批量注释。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/1uM11eMpSdStds8Vcz7BQg/zh-cn_image_0000002628564986.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=4519BB8662EABD0F3BF6E6AC64BC0AB1841682295107B828A0142DD46ADCCE3B)
