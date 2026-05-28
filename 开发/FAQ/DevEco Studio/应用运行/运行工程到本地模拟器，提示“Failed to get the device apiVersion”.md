# 运行工程到本地模拟器，提示“Failed to get the device apiVersion”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5

**问题现象**
 
本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。
 

![](assets/运行工程到本地模拟器，提示“Failed%20to%20get%20the%20device%20apiVersion”/file-20260515130245919-0.png)

 
**解决措施**
 
可以通过以下方法重新运行工程：
 
- 在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
- 打开命令行工具，进入HarmonyOS SDK安装目录下的 `default/base/toolchains` 路径，执行以下命令重启 hdc server：
```bash
./hdc kill -r
```
 
![](assets/运行工程到本地模拟器，提示“Failed%20to%20get%20the%20device%20apiVersion”/file-20260515130245919-1.png)
