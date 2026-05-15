# 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下hidumper命令手动触发延迟任务执行回调。

```bash
hdc shell hidumper -s 1904 -a '-t com.hmos.workschedulerdemo MyWorkSchedulerExtensionAbility'
```

com.hmos.workschedulerdemo、MyWorkSchedulerExtensionAbility需要替换为需要查询应用的bundleName和abilityName。


![](assets/如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调/file-20260515125637854-0.png)
