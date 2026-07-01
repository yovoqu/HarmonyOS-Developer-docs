# AGC的控制台无法选择要提交的新版本

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-63

#### 问题现象

AGC的控制台进行新版本提交，无法选择需要提交的新版本。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ErjydVfyRSacbx5oqg1z1Q/zh-cn_image_0000002628554516.png?HW-CC-KV=V1&HW-CC-Date=20260701T041113Z&HW-CC-Expire=86400&HW-CC-Sign=FCB25B83225F55D313D9052ED8F7555F3965667EB36DA0B16521F66E21EA5785)

 
 

#### 解决方案
1. 在“上传包”窗口，先选择“使用场景”，然后点击“+”上传软件包。若软件包需要在全网正式发布，请选择“测试和正式上架”，根据需求选择是否在中国大陆发布。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/wB_kd_3hRKqzefw8_5uLEw/zh-cn_image_0000002658913839.png?HW-CC-KV=V1&HW-CC-Date=20260701T041113Z&HW-CC-Expire=86400&HW-CC-Sign=3A707085658BC6DECC3DE02AC237A8371DA46C5F6D37758BB4A65C28EE20291A)

2. 配置发布国家或地区，选择“特定国家或地区”：应用仅在所选国家或地区发布。其中，发布国家的中国大陆选项选择需与“上传包”窗口中的选择保持一致。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/CpelGQsvT2mEy9o5ELcgAg/zh-cn_image_0000002658793897.png?HW-CC-KV=V1&HW-CC-Date=20260701T041113Z&HW-CC-Expire=86400&HW-CC-Sign=2953356C658523C389E54E3C7304C1B8776A5387334BBD0831BE1BB14A1A3FDA)

 
 

#### 总结

如果上传包时选择中国大陆，则发布国家必须包含中国大陆；如果上传包时没有选择中国大陆，则发布国家必须不包含中国大陆；如果不一致，则重新上传即可。
