# 使用串口开发API时提示系统能力不支持

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-58

## 使用串口开发API时提示系统能力不支持
 


##### 问题现象

使用API19的串口开发，提示系统能力不支持，需要配置syscap.json文件，详细报错如下：
 
```text
The default system capabilities of devices phone do not include SystemCapability.USB.USBManager.Serial. Configure the capabilities in syscap.json.
```
 
 

##### 解决方案

在DevEco Studio工程的模块“/src/main”目录下，手动创建syscap.json文件,在addedSysCaps字段新增缺失的配置，参考：[多设备应用开发](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-function#多设备应用开发)。
