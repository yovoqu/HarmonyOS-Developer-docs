# 如何查询应用进程的pid信息

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81

可以通过以下两种方式获取：
 
- 方式一：通过以下命令查询应用进程信息。执行hdc shell命令，进入设备的命令行。执行“ps -ef”命令，查看所有正在运行的进程信息。
- 方式二：通过调用[process](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-process)相关接口查询。
```ArkTS
import { process } from '@kit.ArkTS';

let pid = process.pid;
```
