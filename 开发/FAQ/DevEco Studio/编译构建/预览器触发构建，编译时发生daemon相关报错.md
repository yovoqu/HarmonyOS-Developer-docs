# 预览器触发构建，编译时发生daemon相关报错

更新时间：2026-06-15 08:43:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-197

## 预览器触发构建，编译时发生daemon相关报错
 

**问题现象**
 
IDE环境下，通过预览器间接调用hvigor执行构建，出现以下这几种报错:
 
```text
hvigor ERROR: hvigor client: Connection between client and daemon is disconnected with a connect error
```
 
```text
hvigor Create hvigor server failed. No Idle daemon can be found.
```
 
```text
hvigor Create hvigor server failed. The daemon is closed or not the hvigor process.
```
 
```text
长时间卡住在 hvigor client: Starting hvigor daemon.
```
 
**问题原因：**
 
- hvigor尝试申请的端口范围(45000-45099)，所有端口都被占用或无权限
- daemon进程被安全软件拦截，例如公司安全软件、VPN、流量代理、杀毒软件
- hvigor没有用户目录下缓存路径的访问权限，或缓存文件损坏

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/O7_JQ3QOS-ScE3lIL6TR0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025914Z&HW-CC-Expire=86400&HW-CC-Sign=ECDB351615451F8C0E949E5AC91E82945DE40F26E58C228B141798EEAA22F987)
 

预览器的运行强制要求hvigor运行在daemon模式下，因此所有关闭daemon的配置在执行预览构建时均不会生效。
 

 
**解决方案**
 
- 检查确保端口(45000-45099)可用，检查本机路径访问权限可用，测试：
```text
netstat -ano | findstr 450
```
 
```text
ping 127.0.0.1
```

- 检查并关闭可能会拦截的安全软件
- 删除以下缓存目录：
Windows: C:\Users\&lt;用户名&gt;\.hvigor
- Linux/macOS: ~/.hvigor

 - 如果以上方式仍然报错，卸载现有 DevEco Studio并执行默认安装后，重新创建项目后尝试预览
