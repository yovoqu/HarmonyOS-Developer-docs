# 启动C++调试时出现错误

更新时间：2026-06-15 08:43:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-25

**问题现象**
 
启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\*\*\*\*\*\*\*\*\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。
 

![](assets/启动C++调试时出现错误，提示“Failed%20to%20connect%20to%20unix-abstract-connect”/file-20260515130319265-0.png)

 
**解决措施**
 1. 如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2. 签名使用了release证书，请更换为debug证书。
3. 到设备路径 /data/local/tmp/ 下，删除debugserver文件夹，并重启设备。
4. MacOS下 /etc/hosts文件被修改，在/etc/hosts文件后添加如下内容：
```text
127.0.0.1 localhost
255.255.255.255 broadcasthost
::1 localhost
```
 重启电脑使修改生效。
 

 
**问题现象**
 
启动C++调试时出现错误，提示“com.huawei.bitfun.utils.DapRuntimeException: server already exited”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/oAOLR3ShTgWKZPnnXsDNdA/zh-cn_image_0000002625018745.png?HW-CC-KV=V1&HW-CC-Date=20260624T020452Z&HW-CC-Expire=86400&HW-CC-Sign=9554FC56DF17C3F38DBA96CD176EB23D447AD4A22A1772C51C9DA117A924BF20)

 
**解决措施**
 
使用的sdk与DevEco Studio内置的sdk版本差异过大，请更新sdk或使用DevEco Studio内置的sdk进行调试。
