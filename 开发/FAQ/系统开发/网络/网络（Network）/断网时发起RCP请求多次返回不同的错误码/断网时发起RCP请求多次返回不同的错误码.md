# 断网时发起RCP请求多次返回不同的错误码

更新时间：2026-07-02 07:18:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-90

#### 问题现象

问题一：测试机A开启热点，测试机B连接后，测试机A断网，然后测试机B在同一个时间段对同一个地址进行访问时，会分别返回三种不同的错误码，是什么原因？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ufg5Zn0rQuu_VQKPmFSeKQ/zh-cn_image_0000002661423817.png?HW-CC-KV=V1&HW-CC-Date=20260730T072547Z&HW-CC-Expire=86400&HW-CC-Sign=EDC5CF6B7E5C6AC6E00C8B38D3ACA939C51B56BDD8A07425F8D979FA16C3D467)

 
问题二：错误码1007900056要怎么排查？
 
问题三：弱网情况下进行网络请求，返回了错误码1007900052，这种情况是正常的吗？
 
 

#### 解决方案

问题一方案：
 
- 如果有DNS缓存，那么就直接进入TCP阶段，TCP阶段两种可能：
连接超时，[错误码1007900028](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900028-操作超时)。
- 连接直接被拒绝，[错误码1007900007](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900007-无法连接到服务器)。

 - 如果没有DNS缓存，首先进行DNS解析，就是[错误码1007900006](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900006-域名解析失败)。

 
断网后短时间内DNS缓存还在，所以会直接进入TCP请求，过了一会DNS缓存被清除了，所以直接就报1007900006；DNS解析属于内部业务逻辑。
 
问题二方案：排查下是否使用了代理、出错时是否切换了网络、出错时应用是否切换了前后台。
 
问题三方案：正常，但是错误码1007900052一般是服务器的配置或实现不当导致的，可进行以下操作排查问题：排查服务器配置异常（服务器未正确处理请求，导致返回空响应）、网络传输中断（请求或响应过程中网络中断，导致数据未完整传输）、请求参数不合法（参数格式错误或缺失，导致服务器拒绝响应）。
