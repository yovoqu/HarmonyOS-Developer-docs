# Hypium怎么在多台设备上并行执行测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-34

#### 问题现象

以下两种自动化测试场景，如何实现：
 
- 多份test.py在多台设备上测试不同的应用。
- 一份test.py脚本，同时测试多台设备。

 
 

#### 背景知识

[DevEco Testing Hypium(以下简称Hypium)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，提供**控件定位能力、模拟输入功能、多设备并行操作、生成用例执行报告**等功能。
 
Hypium支持多设备并行执行测试用例，使用前先参考[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)完成步骤1到步骤5的安装。
 
 

#### 解决方案
1. 场景一：多份test.py在多台设备上执行，新建多个main.py，通过main.py分别运行不同的test.py。
user_config.xml配置并行设备的sn。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/sPlcVFgBTqSGo6LODnwi4g/zh-cn_image_0000002658928845.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=AFBBB453411A1F55F7CEDCF24210B8887A6F9100BA62B45466B8456635479E48)

2. 配置用例的json文件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/h6fRHOZMTyqmHh6JvqVxFg/zh-cn_image_0000002628409636.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=28E829506D422AC12CBF2691E52600BDC6FEEB8F31CD1CD5894B2F37C84B50E4)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/I_5Z3P_zSUuVgJwRWk6BwA/zh-cn_image_0000002658808895.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=2BBE553C8F17F9A24961D3B1553EC8679AF3A60A038A3627158A1DE680785BB2)

3. 新建main2.py，配置main和main2，对应不同用例和设备。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/czQHm02KS4KXTWHSGDDwvw/zh-cn_image_0000002628569530.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=B866B69A8E519DF982B0301B24B29D39ECA503F6E20C6BFBEA01221D47056C2A)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Jkf_nHQbROShuo9h3Oc_eQ/zh-cn_image_0000002658928855.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=7881EDD9503B9C90FE96502C5CB14FD7A31B7C64B950ABD6889A7AE315EE8318)

4. 运行main.py和main2.py。
5. 场景二：单用例在多设备上执行。
新建项目时，点击左侧的DevEco Testing Hypium，选择双设备。或者用例里使用device1、device2区分设备。（如果大于2台设备，可以继续新增，如device3）
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/WjIme_CrQX-pxC_YEjw7SQ/zh-cn_image_0000002628409640.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=F267CC5F4D07CFAA05CF6B401F3F83B20B135C2C034E409E808783C8E290110D)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/acFI3ySnRqyLU90OWOsX8A/zh-cn_image_0000002658808899.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=C1AF57008A40D8FB8188DDB9FCC8D892A66C783E2BAADB47F7036C48B82FA85B)

6. 用例里面步骤分别对应不同设备（device1、device2）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/5r-80W4mRQin40kpcnsN6A/zh-cn_image_0000002628569532.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=E4DB3151A8EC24C05A67CE59D1A5361E9661DEC1873FC72715CB59DA26949828)

7. user_config.xml配置并行设备的sn。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/jnEWiL_BRC6giIwoAFpigg/zh-cn_image_0000002658928857.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=8B3F2C78C1950719B579FA5372966BAC68742BCCE21D813E346E1C2D214FDE6C)

8. 修改用例的json文件，增加设备（如果是新建项目选择双设备，默认已经配置2台设备）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NWOGteqHTMuz1_Ahm1egUw/zh-cn_image_0000002628409642.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=2EB04B5FD2EA6978E73CB5BA934596FF612B1ADCF6FED1FCD2C6BE96EF2DD206)

9. 配置main.py文件，指定运行设备sn号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Yj5yYiSeRF6lqCJf-TX8rw/zh-cn_image_0000002658808903.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=082258D128E57C96B84BEEA5BC7670AEE46A23EF0E052680046C1728DFE5D820)

10. 运行main文件。
 
 

#### 常见FAQ

Q：UiViewer如何实现多设备的连接和切换？
 
A：UiViewer最多支持同时对两个设备进行投屏，选中想连接的设备，设备编号一个设置为dev1，另外一个设置为dev2，点击确定，即可进行两个设备的投屏。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/J1HULcpDTz6F7-6fzIuZGQ/zh-cn_image_0000002628569536.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=9E06C0DE920D60D0D043887AA4139CA04B23E6935EB823AD9E0EB637CFD13739)

 
如果要进行设备切换，点击右上角的设备切换，回到设备选择页面，重新进行选择即可。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-8G2qb97QTG_XcHJyx1oIQ/zh-cn_image_0000002658928861.png?HW-CC-KV=V1&HW-CC-Date=20260723T014005Z&HW-CC-Expire=86400&HW-CC-Sign=E1041ED154C54FB013C70BF688E74F1D3E80398149013C4B111CE22F9DFFD5B4)

 
Q：如何测试不同的应用。
 
A：Hypium测试的对象是设备，而不是指定应用。针对特定应用的测试，可以编写测试用例，通过start_app打开指定应用，再执行对应的用例。
 
Q：Hypium是否支持选定模拟器进行测试？
 
A：支持，不管是模拟器还是真机，在user_config.xml指定设备的sn即可。
```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <em><!-- type: 设备连接方式,usb-hdc表示使用hdc命令控制设备(默认) --></em>
        <device type="usb-hdc">
            <em><!-- ip: 远端设备地址,ip和port为空时使用本地设备,非空时使用远端设备 --></em>
            <ip></ip> 
           <em> <!-- port: 远端设备端口号 --></em>
            <port></port> 
            <em><!-- sn: 设备SN号列表,SN之间用分号";"分隔,sn字段为空时使用所有本地设备,非空时使用指定的sn设备 --></em>
            <sn></sn> 
        </device>
    </environment>
    <testcases>
        <em><!-- 指定测试用例目录，为空则默认设置为当前项目下的testcase文件夹 --></em>
        <dir></dir>
    </testcases>
    <resource>
        <em><!-- 指定资源目录，为空则默认设置为当前项目下的resource文件夹 --></em>
        <dir></dir>
    </resource>
    <em><!-- 默认为INFO，如需更详细信息可设置为DEBUG --></em>
    <loglevel>DEBUG</loglevel>
    <devicelog>
       <em> <!--在测试用例结束后额外后拉取以下路径的日志到报告下--></em>
        <dir>/data/log/tee;/data/log/test</dir>
        <em><!--控制hilog日志等级，默认值为INFO--></em>
        <loglevel>DEBUG</loglevel>    
        <em><!--控制是否在拉取日志后设备端的日志，默认值为true--></em>
        <clear></clear>                
        <em><!--控制是否抓取设备日志，默认值为ON，OFF时候上述两个标签不生效--></em>
        <enable>ON</enable>            
    </devicelog>
</user_config>
```
 
 
Q：Hypium是否支持不输出日志？
 
A：框架会进行正常的日志打印，并会在测试工程的reports目录或者指定目录生成日志。但可以通过user_config.xml把日志等级调到最高（ERROR），并把设备日志关掉，从而减少报告内容。
```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <device type="usb-hdc">
            <sn></sn>
        </device>
    </environment>
    <testcases>
        <dir></dir>
    </testcases>
    <loglevel>ERROR</loglevel>
    <devicelog>OFF</devicelog>
</user_config>
```
