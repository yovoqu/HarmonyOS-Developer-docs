# 上传应用图标到AGC报错文件类型不对

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-30

#### 问题现象

发布应用时，上传应用图标到AGC失败，报错“文件类型错误，请上传PNG、WEBP格式的文件”。但是检查文件类型是PNG，这是什么原因？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/p09LV8OHR7-nsaicifyEIQ/zh-cn_image_0000002628394596.png?HW-CC-KV=V1&HW-CC-Date=20260730T072659Z&HW-CC-Expire=86400&HW-CC-Sign=8EC1107193E78BE9F9D619249197CBF5EEAD1BDAF389031639A40235FB219671)

 
 

#### 解决方案

检查是否对图片进行了修改。常见的错误是手动将其他格式的图标修改后缀成.PNG。系统是校验原始图片的二进制编码格式，仅仅手动修改图片的后缀名不能修改文件二进制编码类型。需要通过专业软件修改图片类型，如使用画图软件打开图片，点击文件另存为需要的图片类型：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/VrlSB_BbSeSABJHHgjkwSg/zh-cn_image_0000002628554486.png?HW-CC-KV=V1&HW-CC-Date=20260730T072659Z&HW-CC-Expire=86400&HW-CC-Sign=79A9DD0F9A91223AD4AF86C628A0596017B363003CC799121CA1D59AAC6E413C)

 
 

#### 总结

可以通过专业工具（如DevEco Studio）查看图片的原始二进制编码格式，如下图片手动修改了后缀名为PNG，但实际是JPEG格式。上传至AGC就会报文件类型错误。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Ld9AjmyVRdWUwIw5kkfRNw/zh-cn_image_0000002658913815.png?HW-CC-KV=V1&HW-CC-Date=20260730T072659Z&HW-CC-Expire=86400&HW-CC-Sign=C77D787F783AA50EB335145F8C90CD855AB590641CD8356F2C751884D0C78FB4)
