# aa命令拉起hipreview应用并预览本地文件失败

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-51

## aa命令拉起hipreview应用并预览本地文件失败
 


##### 问题现象

使用hdc命令拉起hipreview应用并传入本地文件直接预览失败。
 
```text
hdc shell aa start -b com.huawei.hmos.hipreview -a MainAbility -U file://storage/media/100/local/files/Docs/Documents/1.pdf
```
 
其中文件路径是通过Device File Browser获取的文件真实路径，也叫物理路径。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/I_S71TkHQ0GLpub-q71g_A/zh-cn_image_0000002628554892.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=7DFE3E9648BFEE7F3DBD1D61B82EE3661121F6700E2C704152BE1B425448FDDA)

 
命令行执行效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TAU76V0kQgCceIh8MxxvBA/zh-cn_image_0000002628394990.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=0DEF9E2D90DBF4DD98C1A8565A7597958A8C58779B8E17960FFCEA43FF125EEE)

 
 

##### 背景知识

- [Ability assistant（Ability助手，简称为aa）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool)是用于启动应用和启动测试用例的工具，为开发者提供基本的应用调试和测试能力，例如启动应用组件、强制停止进程、打印应用组件相关信息等。
- [用户文件URI](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro)是文件的唯一标识，在对用户文件进行访问与修改等操作时往往都会使用到URI。

 
 

##### 解决方案

-U参数传递错误，-U参数对应的是URI参数，而不是文件物理路径。
 
```text
hdc shell aa start -b com.huawei.hmos.hipreview -a MainAbility -U file://docs/storage/Users/currentUser/Documents/1.pdf
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/kM0DXnVkSs6YXlWQK5dNKA/zh-cn_image_0000002658914209.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=1F47115A3358B4EFC3195C9D7BA0DB116AEA9441C1987B79238922D0F904F265)

 
 

##### 常见FAQ

Q：aa命令传入URI参数（-U）为文件的物理路径预览失败。
 
A：URI参数（-U）对应的是[URI的类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#uri的类型)。
 
Q：aa命令中-U参数携带query参数，但query参数丢失，命令如下：
 
```text
hdc shell aa start -a MainAbility -b {bundleName} -A ohos.want.action.viewData -U "url?param1=v1&param2=v2"
```
 
A：参数丢失是因为hdc shell会去掉最外层双引号，shell读到&时会当做特殊字符，后面的参数不能透传，正确的写法是：
 
```text
hdc shell aa "start -a MainAbility -b xxx -A ohos.want.action.viewData -U 'url?param1=v1&param2=v2'"
```
 
Q：aa start命令行拉起app，-U命令后跟的URI解析成want中的URI参数丢失，命令如下：
 
```text
hdc shell aa start -A action.system.home -U 'miguvideo://miguvideotv?action={"params":{"extra":{"detail_type":"JUMP_NEW_PAY_PAGE","deepLinkType":"launch er"},"pageID":"98ab1e76e24c4472a9018408ca0087f4"},"type":"JUMP_INNER_NEW_PAGE"}'
```
 
A：传参方式不正确，参考官网文档aa工具[启动命令（start）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool#启动命令start)，可尝试换成下面这种传参方式：
 
```text
aa start -U myscheme://www&#46;test.com:8080/path --pi paramNumber 1 --pb paramBoolean true --ps paramString teststring --psn paramNullString
```
