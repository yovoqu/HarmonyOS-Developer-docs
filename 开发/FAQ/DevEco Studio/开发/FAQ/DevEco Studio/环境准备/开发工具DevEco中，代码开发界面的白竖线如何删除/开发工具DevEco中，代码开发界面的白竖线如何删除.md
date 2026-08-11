# 开发工具DevEco中，代码开发界面的白竖线如何删除

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-24

#### 问题现象

DevEco Studio中，代码开发界面显示的白竖线如何取消？
 
在这个白竖线附近时，代码就会自动折行显示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/xT6SqCnBRhG0kAQc4vUVoQ/zh-cn_image_0000002658804341.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=86BA27DB52DC8CA341F158895295ACC191254686070056E51EDF2AD47FF9536D)

 
 

#### 背景知识

代码开发界面的白竖线是一个视觉分割线，它允许用户设置一个特定的列数作为代码的宽度限制。当代码行超过这个限制时，编程工具会自动将代码换行到下一行，从而保持代码的整洁和可读性。
 
 

#### 解决方案

可以使用如下两种解决方案：
 
- 完全取消分割线：在开发工具File->Settings->Editor->General->Appearance取消勾选show hard wrap and visual guides。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/keBm0PyxS72I45Sp4HIAJQ/zh-cn_image_0000002628564982.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=813F707A088F0757DA8D977DAA23EA89AFEAF2341B22EE81B753342FABEF3947)

- 增大代码的宽度限制：在开发工具File->Settings->Editor->Code Style中增大Hard wrap值，如将其值改为1000。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QsBGDNZSTTGcOUsdDOy2qQ/zh-cn_image_0000002628405078.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=4896A8D4BD55C9C9B35C0702D6FCCEFAA4F22F175B41D048FEDB4B58BE92DF6D)


 
 

#### 常见FAQ

Q：过长的三元表达式会直接换行但不带缩进，是否有办法可以调节？
 
A：在IDE的setting中，Editor-Code Style-ArkTS下，找到Ternary operation，勾选下面的两个选项。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/w6brR5PrQ_2vbMax9F2z6A/zh-cn_image_0000002658924295.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=61ADA3F2F72E184F92CFA5E735F1E87207E52CAA6D61F7631C992BB18895B88E)

 
Q：粘贴代码时，如何关闭编辑器自动格式化？
 
A：在IDE的setting中，Editor-General-Smart Keys下，找到Reformat on paste选项，下拉选择None。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/msPscaHnR-W0zc4VzLqDMQ/zh-cn_image_0000002658804349.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=1B0F1BAF1845DFEFF1FA0ADD3983F0289324EB88538BB4E2262A82FE8821DAD1)

 
Q：在File -> Settings -> Appearance -> Editor -> Font设置字体大小大于14（比如设置为16），在File -> Settings -> Editor -> Color Scheme修改任意类型代码颜色，预览器颜色错乱。
 
A：设置代码颜色后需要按回车确认。
 
Q：如何使用快捷键批量注释代码？
 
A：选中需要注释的代码，按住ctrl + /键方可批量注释。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/1uM11eMpSdStds8Vcz7BQg/zh-cn_image_0000002628564986.png?HW-CC-KV=V1&HW-CC-Date=20260811T005524Z&HW-CC-Expire=86400&HW-CC-Sign=033056343B79E8B8DCCEBBA7EC8E1A4DE4830067E6BD4B328812DA63B00DCAEC)
