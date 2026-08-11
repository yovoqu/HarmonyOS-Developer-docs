# 使用AppLinking拉起应用，为什么webview会展示一段json代码

更新时间：2026-07-31 00:56:37

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-158

#### 问题现象

使用Web加载本地H5文件，在H5文件中加载AppLinking链接拉起应用时会展示一段json代码。
 
问题代码示例参考如下：
 
```json
var scheme = "https://xxxx.com/.well-known/applinking.json?xxxx=xxxx";
function deepLinkApp() {
    urlOpen.location(scheme)
}
```
 
问题现象如图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/0zhUYCr0ROmFAkQiOc_NaQ/zh-cn_image_0000002628789250.png?HW-CC-KV=V1&HW-CC-Date=20260811T005855Z&HW-CC-Expire=86400&HW-CC-Sign=11307F7523A54D56B5AF25FD8942F993F216BDF29A4F72E6F190DB19CAFA2777)

 
 

#### 解决方案

根据展示的json代码中可以看出，是applinking.json配置文件代码。检查H5中加载的AppLinking链接是否包含“/.well-known/applinking.json”。确认包含，将该链接中的“/.well-known/applinking.json”删除即可。applinking.json域名配置文件需要放在域名服务器的固定目录下，使用AppLinking拉起应用只需要加载[在AGC控制台关联的网址域名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp)即可。
