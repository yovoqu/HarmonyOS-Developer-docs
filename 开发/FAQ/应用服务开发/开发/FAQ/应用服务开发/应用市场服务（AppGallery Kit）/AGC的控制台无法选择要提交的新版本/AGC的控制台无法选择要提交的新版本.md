# AGC的控制台无法选择要提交的新版本

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-63

#### 问题现象

AGC的控制台进行新版本提交，无法选择需要提交的新版本。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/s48Z155kSkiNJXrBk_obRg/zh-cn_image_0000002628554516.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=22696E12A4EEA1577B649E0E7999CC71E513E5C844B53550AEA8638882C5F1CD)

 
 

#### 解决方案
1. 在“上传包”窗口，先选择“使用场景”，然后点击“+”上传软件包。若软件包需要在全网正式发布，请选择“测试和正式上架”，根据需求选择是否在中国大陆发布。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/zaDavZTUTQ2s1ly1Pr3JAg/zh-cn_image_0000002658913839.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=A512D57473273B025BCAA399ED09F0A549BDD732AE19F250BC25AFB19DB740AC)

2. 配置发布国家或地区，选择“特定国家或地区”：应用仅在所选国家或地区发布。其中，发布国家的中国大陆选项选择需与“上传包”窗口中的选择保持一致。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/f3NFUUP8RkKzM2q6-HGQGw/zh-cn_image_0000002658793897.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=7A89061D3178B8CA701FBABC53845982C672B0759F14D95A5B7F65FE09BAD527)

 
 

#### 总结

如果上传包时选择中国大陆，则发布国家必须包含中国大陆；如果上传包时没有选择中国大陆，则发布国家必须不包含中国大陆；如果不一致，则重新上传即可。
