# ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9

问题现象

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。


![](assets/ohosTest测试文件引用了启动页的导出方法，测试时报错“Load%20Page%20Failed／%20pages／Index”/file-20260515130346091-0.png)
解决措施

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。


![](assets/ohosTest测试文件引用了启动页的导出方法，测试时报错“Load%20Page%20Failed／%20pages／Index”/file-20260515130346091-1.png)
