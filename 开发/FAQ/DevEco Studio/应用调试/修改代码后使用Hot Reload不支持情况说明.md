# 修改代码后使用Hot Reload不支持情况说明

更新时间：2026-03-12 12:31:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20

**问题现象**
 
执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。
 

![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-0.png)

 
**解决措施**
 
DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hot-reload#section995453874915)。
 
**常见不支持代码场景**
 
- 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-1.png)

- 不支持@Entry入口文件内class成员函数的新增。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-10.png)

- 不支持@Entry入口文件内枚举的修改。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-11.png)

- 不支持import未加载的模块的新增、修改。若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-12.png)


  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-2.png)

- 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-3.png)

- 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-4.png)

- 不支持@Entry入口文件内大部分装饰器的修改。当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-5.png)

- 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-6.png)

- 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-7.png)

- 不支持修改非ets/ts代码文件。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-8.png)

- 不支持修改worker线程文件。
![](assets/修改代码后使用Hot%20Reload不支持情况说明/file-20260515130311682-9.png)
