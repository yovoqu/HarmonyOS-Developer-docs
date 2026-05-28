# 编译报错“The path XX is not writable. please choose a new location”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-118

**问题现象**
 
在Mac上，通过打开DMG文件中的DevEco Studio图标启动DevEco Studio时，如果构建报错“The path XX is not writable. please choose a new location”，请选择一个新的位置。
 

![](assets/编译报错“The%20path%20XX%20is%20not%20writable.%20please%20choose%20a%20new%20location”/file-20260515130144166-0.png)

 
**问题原因**
 
在Mac上直接通过DMG中的DevEco Studio图标打开DevEco Studio，会以只读方式打开。内置在DevEco Studio中的文件没有写权限。
 
**解决措施**
 
将“DevEco-Studio.app”拖拽到“Applications”文件夹中，安装后再使用。
