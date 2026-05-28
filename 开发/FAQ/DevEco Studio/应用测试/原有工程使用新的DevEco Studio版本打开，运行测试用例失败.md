# 原有工程使用新的DevEco Studio版本打开，运行测试用例失败

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6

**   

**问题现象**
 
如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test_pages.json' must have one and only one '@Entry' decorator”。
 
图1 ****
![](assets/原有工程使用新的DevEco%20Studio版本打开，运行测试用例失败/file-20260515130341704-0.png)

 
**解决措施**
 
将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。
 
图2 **

![](assets/原有工程使用新的DevEco%20Studio版本打开，运行测试用例失败/file-20260515130341704-1.png)
