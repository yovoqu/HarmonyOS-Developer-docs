# DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-15

问题现象

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。


![](assets/DevEco%20Studio上使用生成NAPI功能时，%20提示“Could%20not%20find%20usage%20of%20napi_module_register%20in%20napi_init.cpp.”错误/file-20260515130027789-0.png)


解决措施

检查napi_init.cpp文件的RegisterEntryModule函数中是否调用了napi_module_register函数。napi_module_register的参数类型为napi_module*,   napi_module初始化示例代码如下图所示。然后重新生成NAPI。

字段含义：

nm_version:  N-API模块版本

nm_flags:  模块的属性标志

nm_filename:  N-API模块的文件名

nm_register_func:  注册函数

nm_modname:  模块名称

nm_priv: 私有数据指针

reserved: 保留字段


![](assets/DevEco%20Studio上使用生成NAPI功能时，%20提示“Could%20not%20find%20usage%20of%20napi_module_register%20in%20napi_init.cpp.”错误/file-20260515130027789-1.png)


![](assets/DevEco%20Studio上使用生成NAPI功能时，%20提示“Could%20not%20find%20usage%20of%20napi_module_register%20in%20napi_init.cpp.”错误/file-20260515130027789-2.png)
