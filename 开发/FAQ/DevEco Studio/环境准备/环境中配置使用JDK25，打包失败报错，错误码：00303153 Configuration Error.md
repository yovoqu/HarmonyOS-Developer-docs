# 打开工程，反复执行“Updating indexes”

更新时间：2026-05-30 09:08:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-17

**问题现象**
 
在DevEco Studio 新建 / 打开工程，反复执行“Updating indexes”、“Indexing”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/16kUcDrBRl--J9flJph0WA/zh-cn_image_0000002615227079.png?HW-CC-KV=V1&HW-CC-Date=20260604T012614Z&HW-CC-Expire=86400&HW-CC-Sign=975FB1ACD786D717BEDDE2CBA57FEB4981AC3D2A893D96B1BFB7390755B7994C)

 
**解决措施**
 
导致该问题的原因是缓存路径下的文件被加密，请联系企业内的IT，确认是否有加密软件在运作，将该目录内容加入白名单中。
 
- MAC的缓存路径为：~/Library/Caches/Huawei/DevEcoStudio&lt;版本号&gt; 和 ~/Library/Application Support/Huawei/DevEcoStudio&lt;版本号&gt;示例：~/Library/Caches/Huawei/DevEcoStudio6.1 和 ~/Library/Application Support/Huawei/DevEcoStudio6.1
- Windows的缓存路径为：%APPDATA%\Huawei\DevEcoStudio&lt;版本号&gt; 和 %LOCALAPPDATA%\Huawei/DevEcoStudio&lt;版本号&gt;示例：C:\Users\用户名\AppData\Roaming\Huawei\DevEcoStudio6.1 和 C:\Users\用户名\AppData\Local\Huawei\DevEcoStudio6.1
