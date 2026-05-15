# 测试结束后hilog日志一栏显示“-”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-16

用户手动停止任务后，Hypium进程会直接关闭，不会生成hilog。如果任务正常结束时缺少hilog，请确认test包中config文件夹下的user_config.xml文件中的devicelog参数设置为ON。如果没有，请添加该参数，重新打包即可解决。
