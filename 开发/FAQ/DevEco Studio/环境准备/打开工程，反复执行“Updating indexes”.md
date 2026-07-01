# 打开工程，反复执行“Updating indexes”

更新时间：2026-06-15 08:43:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-18

## 打开工程，反复执行“Updating indexes”
 

**问题现象**
 
在DevEco Studio 新建 / 打开工程，反复执行“Updating indexes”、“Indexing”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/WJy5OxbKTlSIfrXRulnuSQ/zh-cn_image_0000002654797779.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=8C6B2A2FAC6965C0D9CC3204ED225471F9EB41D1A567612B342E7D59E4E553E5)

 
**解决措施**
 
导致该问题的原因是缓存路径下的文件被加密，请联系企业内的IT，确认是否有加密软件在运作，将该目录内容加入白名单中。
 
- MAC的缓存路径为：~/Library/Caches/Huawei/DevEcoStudio&lt;版本号&gt; 和 ~/Library/Application Support/Huawei/DevEcoStudio&lt;版本号&gt;示例：~/Library/Caches/Huawei/DevEcoStudio6.1 和 ~/Library/Application Support/Huawei/DevEcoStudio6.1
- Windows的缓存路径为：%APPDATA%\Huawei\DevEcoStudio&lt;版本号&gt; 和 %LOCALAPPDATA%\Huawei/DevEcoStudio&lt;版本号&gt;示例：C:\Users\用户名\AppData\Roaming\Huawei\DevEcoStudio6.1 和 C:\Users\用户名\AppData\Local\Huawei\DevEcoStudio6.1
