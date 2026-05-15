# DevEco如何配置不响应raise捕获到的assert信号

更新时间：2026-03-12 12:31:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：


![](assets/DevEco如何配置不响应raise捕获到的assert信号/file-20260515130326332-0.png)


![](assets/DevEco如何配置不响应raise捕获到的assert信号/file-20260515130326332-1.png)
