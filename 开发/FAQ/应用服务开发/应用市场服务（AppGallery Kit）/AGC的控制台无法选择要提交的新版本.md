# AGC的控制台无法选择要提交的新版本

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-63

## AGC的控制台无法选择要提交的新版本
 


##### 问题现象

AGC的控制台进行新版本提交，无法选择需要提交的新版本。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ErjydVfyRSacbx5oqg1z1Q/zh-cn_image_0000002628554516.png?HW-CC-KV=V1&HW-CC-Date=20260701T025902Z&HW-CC-Expire=86400&HW-CC-Sign=2B655E03C1126DFD40BB623A56E3DD489E61D8FD453312E2360B9C9B8B48EE39)

 
 

##### 解决方案

- 在“上传包”窗口，先选择“使用场景”，然后点击“+”上传软件包。若软件包需要在全网正式发布，请选择“测试和正式上架”，根据需求选择是否在中国大陆发布。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/wB_kd_3hRKqzefw8_5uLEw/zh-cn_image_0000002658913839.png?HW-CC-KV=V1&HW-CC-Date=20260701T025902Z&HW-CC-Expire=86400&HW-CC-Sign=65C5EFE9CEC902760ECE3AF30966BCCC7CA2F290358166E583897BDB1F0CAD7D)

- 配置发布国家或地区，选择“特定国家或地区”：应用仅在所选国家或地区发布。其中，发布国家的中国大陆选项选择需与“上传包”窗口中的选择保持一致。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/CpelGQsvT2mEy9o5ELcgAg/zh-cn_image_0000002658793897.png?HW-CC-KV=V1&HW-CC-Date=20260701T025902Z&HW-CC-Expire=86400&HW-CC-Sign=BF0D37ECAC49F5AA532D52876CDCDCFC2F78D964BA8835829C13713E880276B4)


 
 

##### 总结

如果上传包时选择中国大陆，则发布国家必须包含中国大陆；如果上传包时没有选择中国大陆，则发布国家必须不包含中国大陆；如果不一致，则重新上传即可。
