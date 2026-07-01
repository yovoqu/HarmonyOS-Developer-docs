# 为什么配置胶囊实况窗icon后，胶囊实况窗中显示应用icon

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-liveview-4

## 为什么配置胶囊实况窗icon后，胶囊实况窗中显示应用icon
 


##### 问题现象

在liveViewData.capsule胶囊实况窗的icon参数中，配置指定的icon图片名称，为什么运行时胶囊实况窗中显示为应用的icon。
 
 

##### 解决方案

liveViewData.capsule中icon参数配置的图片，需保证在工程的“/resources/rawfile”路径下，如果“/resources/rawfile”路径下没有该文件，则会默认显示应用icon。
