# Target AOT编译，AP文件生成失败

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29

问题现象

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。


![](assets/Target%20AOT编译，AP文件生成失败/file-20260515130102537-0.png)


解决措施

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。
```bash
hdc shell
setenforce 0
```


以上设置重启将会失效，若设备重启请重新进行以上设置
