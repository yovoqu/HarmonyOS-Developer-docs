# 如何在多设备情况下使用hdc

更新时间：2026-06-15 08:32:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-48

**问题场景**
 
启动模拟器并连接真机，然后调用hdc命令获取udid。此时仅打印一条模拟器的udid。
 
**解决措施**
 
在多设备环境下直接执行hdc shell会失败，需要使用hdc -t [connect-key] shell指定设备进行操作。其中，connect-key为每个设备的唯一标识符，可通过执行hdc list targets命令获取。
 
参考链接
 
[查询设备列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#查询设备列表)
 
[连接指定的目标设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#连接指定的目标设备)
