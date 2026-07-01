# Hypium怎么在多台设备上并行执行测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-34

## Hypium怎么在多台设备上并行执行测试用例
 


##### 问题现象

以下两种自动化测试场景，如何实现：
 
- 多份test.py在多台设备上测试不同的应用。
- 一份test.py脚本，同时测试多台设备。

 
 

##### 背景知识

[DevEco Testing Hypium(以下简称Hypium)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，提供**控件定位能力、模拟输入功能、多设备并行操作、生成用例执行报告**等功能。
 
Hypium支持多设备并行执行测试用例，使用前先参考[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)完成步骤1到步骤5的安装。
 
 

##### 解决方案

- 场景一：多份test.py在多台设备上执行，新建多个main.py，通过main.py分别运行不同的test.py。
user_config.xml配置并行设备的sn。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/sPlcVFgBTqSGo6LODnwi4g/zh-cn_image_0000002658928845.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=248B96C524D1C8AC819A31CECDDBF5A7BB07DA69C08340B05F41889F67F22721)

- 配置用例的json文件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/h6fRHOZMTyqmHh6JvqVxFg/zh-cn_image_0000002628409636.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=DA7471F0C864B7653D08C56218168F0AF68CC934681052B9F11DF755F2F216F7)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/I_5Z3P_zSUuVgJwRWk6BwA/zh-cn_image_0000002658808895.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=C7E87182F55D68246B07625A50A1BF29497DC4821FC3C4078BE9CFFBBFB0A82A)

- 新建main2.py，配置main和main2，对应不同用例和设备。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/czQHm02KS4KXTWHSGDDwvw/zh-cn_image_0000002628569530.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=C42886D745384605B9A97F8313887AE859BD9617CE2AE72D1D7C6122234D4F62)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Jkf_nHQbROShuo9h3Oc_eQ/zh-cn_image_0000002658928855.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=FB9CCC2E4764F0C75C9479038F5AA974F0A1F30364DB004CE3B1661E5B1B9D82)

- 运行main.py和main2.py。

 - 场景二：单用例在多设备上执行。
新建项目时，点击左侧的DevEco Testing Hypium，选择双设备。或者用例里使用device1、device2区分设备。（如果大于2台设备，可以继续新增，如device3）
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/WjIme_CrQX-pxC_YEjw7SQ/zh-cn_image_0000002628409640.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=AC6C2867D23DB3695F5386BD8E4AA2B81D0AEAFC24AE92FF8527E85C3AC05969)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/acFI3ySnRqyLU90OWOsX8A/zh-cn_image_0000002658808899.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=C9A679FB3AB45AB3A2F05833CE72CB867E63917D533D92A834001E8909CDC788)

- 用例里面步骤分别对应不同设备（device1、device2）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/5r-80W4mRQin40kpcnsN6A/zh-cn_image_0000002628569532.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=319693789BB7993B20AD484C13177ADC074654F6D69A2965F216F54B80D6525A)

- user_config.xml配置并行设备的sn。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/jnEWiL_BRC6giIwoAFpigg/zh-cn_image_0000002658928857.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=00FBDEEE259849147F0BE3670B7AE610B50B3D6246B62BE633091FAF669C676D)

- 修改用例的json文件，增加设备（如果是新建项目选择双设备，默认已经配置2台设备）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NWOGteqHTMuz1_Ahm1egUw/zh-cn_image_0000002628409642.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=2AFFA9A257C7E8563953FF8CC31964CE6CAD1D539C6BF7102C8E9FC490108D9C)

- 配置main.py文件，指定运行设备sn号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Yj5yYiSeRF6lqCJf-TX8rw/zh-cn_image_0000002658808903.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=BC7AF086B3E8223C9805D5253D208A3D290FA079A4715E60B3E755BF6A85F86B)

- 运行main文件。

 
 
 

##### 常见FAQ

Q：UiViewer如何实现多设备的连接和切换？
 
A：UiViewer最多支持同时对两个设备进行投屏，选中想连接的设备，设备编号一个设置为dev1，另外一个设置为dev2，点击确定，即可进行两个设备的投屏。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/J1HULcpDTz6F7-6fzIuZGQ/zh-cn_image_0000002628569536.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=E9ED29E24684A8BF10D69689556412DB15A65B249EC0CAEF8C3A250FF88AE78E)

 
如果要进行设备切换，点击右上角的设备切换，回到设备选择页面，重新进行选择即可。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-8G2qb97QTG_XcHJyx1oIQ/zh-cn_image_0000002658928861.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=203ED19CBEC00F1C9436B52CBFFDFA1DEA562A8427C9D2EFA357B77D8B7B078A)

 
Q：如何测试不同的应用。
 
A：Hypium测试的对象是设备，而不是指定应用。针对特定应用的测试，可以编写测试用例，通过start_app打开指定应用，再执行对应的用例。
 
Q：Hypium是否支持选定模拟器进行测试？
 
A：支持，不管是模拟器还是真机，在user_config.xml指定设备的sn即可。
```text


    
        
        
            
             
            
             
            
             
        
    
    
        
        
    
    
        
        
    
    
    DEBUG
    
        
        /data/log/tee;/data/log/test
        
        DEBUG    
        
                        
        
        ON            
    

```
 
 
Q：Hypium是否支持不输出日志？
 
A：框架会进行正常的日志打印，并会在测试工程的reports目录或者指定目录生成日志。但可以通过user_config.xml把日志等级调到最高（ERROR），并把设备日志关掉，从而减少报告内容。
```text


    
        
            
        
    
    
        
    
    ERROR
    OFF

```
