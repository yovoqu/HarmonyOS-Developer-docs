# 上传应用图标到AGC报错文件类型不对

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-30

#### 问题现象

发布应用时，上传应用图标到AGC失败，报错“文件类型错误，请上传PNG、WEBP格式的文件”。但是检查文件类型是PNG，这是什么原因？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/rHsFyIpKR66C7lZvicy71A/zh-cn_image_0000002628394596.png?HW-CC-KV=V1&HW-CC-Date=20260701T041115Z&HW-CC-Expire=86400&HW-CC-Sign=94E873709319B087BBECB773E78258DF5875C76DFC6F7DE73BEB7F3F3C668EB1)

 
 

#### 解决方案

检查是否对图片进行了修改。常见的错误是手动将其他格式的图标修改后缀成.PNG。系统是校验原始图片的二进制编码格式，仅仅手动修改图片的后缀名不能修改文件二进制编码类型。需要通过专业软件修改图片类型，如使用画图软件打开图片，点击文件另存为需要的图片类型：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/A5ueWT_kQw2dk6Cl7gq30g/zh-cn_image_0000002628554486.png?HW-CC-KV=V1&HW-CC-Date=20260701T041115Z&HW-CC-Expire=86400&HW-CC-Sign=8E75B7556F41AF21804F5980E17F442EB72B5C450E5E10382DCC633B49ABC593)

 
 

#### 总结

可以通过专业工具（如DevEco Studio）查看图片的原始二进制编码格式，如下图片手动修改了后缀名为PNG，但实际是JPEG格式。上传至AGC就会报文件类型错误。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/JYgRABoJT3iVQKAojbK2QA/zh-cn_image_0000002658913815.png?HW-CC-KV=V1&HW-CC-Date=20260701T041115Z&HW-CC-Expire=86400&HW-CC-Sign=FB97DA64A827457F492AA5F30CD87199285566520B93A8B21BDEDB9ECB675D09)
