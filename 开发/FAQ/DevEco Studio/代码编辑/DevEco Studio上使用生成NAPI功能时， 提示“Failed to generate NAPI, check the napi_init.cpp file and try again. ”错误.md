# DevEco Studio上使用生成NAPI功能时， 提示“Failed to generate NAPI, check the napi_init.cpp file and try again. ”错误

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-14

**问题现象**
 
右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。
 

![](assets/DevEco%20Studio上使用生成NAPI功能时，%20提示“Failed%20to%20generate%20NAPI,%20check%20the%20napi_init.cpp%20file%20and%20try%20again.%20”错误/file-20260515130026963-0.png)

 
**解决措施**
 
检查napi_init.cpp文件的Init函数中是否初始化了napi_property_descriptor变量。没有初始化请添加napi_property_descriptor desc[] = {}; 然后重新生成NAPI。
 

![](assets/DevEco%20Studio上使用生成NAPI功能时，%20提示“Failed%20to%20generate%20NAPI,%20check%20the%20napi_init.cpp%20file%20and%20try%20again.%20”错误/file-20260515130026963-1.png)
