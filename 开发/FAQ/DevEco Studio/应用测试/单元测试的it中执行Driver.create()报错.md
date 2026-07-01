# 单元测试的it中执行Driver.create()报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-29

#### 问题现象

使用[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)进行脚本编写时，如果在it中定义driver = Driver.create()，执行时会报错：Error in connect_device, Can not connect to AAMS, RET_ERR_CONNECTION_EXIST。
 
 

#### 解决方案
1. it中不能放driver = Driver.create()，原因是：在执行测试套时，会自动进行设备的连接，也就是设备已处于连接状态。如果再次在it中执行连接会抛出异常，所以建议放在beforeAll中。如果it继续使用Driver.create()初始化的对象，需要把“let driver: Driver”定义在测试套中：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/74CMGP1vQ46UZD5G_t4nyg/zh-cn_image_0000002658808883.png?HW-CC-KV=V1&HW-CC-Date=20260701T041012Z&HW-CC-Expire=86400&HW-CC-Sign=B8E4FC5F94976DE59AE7A3C1E84F4BC9E95E6ACF1039389163C715918FDAD709)

2. 如果放在beforeAll中也报同样的错误，说明uitest进程已被占用，可以先kill掉uitest进程后再次尝试，具体操作步骤为：打开cmd，进入hdc shell模式，执行ps -ef |grep "uitest"命令查看被占用的进程号，然后执行“kill -9 进程号”。
