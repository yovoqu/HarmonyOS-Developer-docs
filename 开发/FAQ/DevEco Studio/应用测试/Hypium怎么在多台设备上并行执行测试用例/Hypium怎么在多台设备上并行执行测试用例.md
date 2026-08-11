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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/sPlcVFgBTqSGo6LODnwi4g/zh-cn_image_0000002658928845.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=BE6FC3B66546630E182FB33C014849EAB63368D95AC94CCB939290276F892AF0)

2. 配置用例的json文件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/h6fRHOZMTyqmHh6JvqVxFg/zh-cn_image_0000002628409636.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=0639F69FBC32B324AC5C4E51654E4CC39040784DA66784B2ADF0B92AF59DEA51)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/I_5Z3P_zSUuVgJwRWk6BwA/zh-cn_image_0000002658808895.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=162B9548E74219AB4C199B3C01E1FA66CC26812F3939C7C451005E2DE115419D)

3. 新建main2.py，配置main和main2，对应不同用例和设备。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/czQHm02KS4KXTWHSGDDwvw/zh-cn_image_0000002628569530.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=B075C6D96DC82673C1200584615AD2BEB503AD205966D4EBC30A08F17E93C4AE)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Jkf_nHQbROShuo9h3Oc_eQ/zh-cn_image_0000002658928855.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=73C66CAC025E4B9A1757191AA3D62243FD4E87CC2BF24788572DDECF5A08C062)

4. 运行main.py和main2.py。
5. 场景二：单用例在多设备上执行。
新建项目时，点击左侧的DevEco Testing Hypium，选择双设备。或者用例里使用device1、device2区分设备。（如果大于2台设备，可以继续新增，如device3）
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/WjIme_CrQX-pxC_YEjw7SQ/zh-cn_image_0000002628409640.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=E4708DAFA27EEB2717B8A18EB9142DD798B8EBAB01A05F6FA636294633CBD905)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/acFI3ySnRqyLU90OWOsX8A/zh-cn_image_0000002658808899.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=1899C26F6A91919566ABE640BE1981C46A7607A5A5793FE23ABFC339BFEAAE44)

6. 用例里面步骤分别对应不同设备（device1、device2）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/5r-80W4mRQin40kpcnsN6A/zh-cn_image_0000002628569532.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=84F944EF7AFD410DD5AB6967DB9D0EE5A34E91054853962F1D12F53F58705D5C)

7. user_config.xml配置并行设备的sn。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/jnEWiL_BRC6giIwoAFpigg/zh-cn_image_0000002658928857.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=08D569C995C9A9798659A3525164FA3077CBF0EA70315361074A73D04B56E5AC)

8. 修改用例的json文件，增加设备（如果是新建项目选择双设备，默认已经配置2台设备）。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NWOGteqHTMuz1_Ahm1egUw/zh-cn_image_0000002628409642.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=053A18038776C5CA5BE0A161E11752210EF282357E5BDA2784A25F96E3CC22E7)

9. 配置main.py文件，指定运行设备sn号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Yj5yYiSeRF6lqCJf-TX8rw/zh-cn_image_0000002658808903.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=986FF611CFA7ADCED10886E6E57B5AC580542512C8CD5D5E3256161797EA1D68)

10. 运行main文件。
 
 

#### 常见FAQ

Q：UiViewer如何实现多设备的连接和切换？
 
A：UiViewer最多支持同时对两个设备进行投屏，选中想连接的设备，设备编号一个设置为dev1，另外一个设置为dev2，点击确定，即可进行两个设备的投屏。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/J1HULcpDTz6F7-6fzIuZGQ/zh-cn_image_0000002628569536.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=097E7882125C69600E11438FEF645C59C35B90AD94C2CA20AEAF0737F0FFDCCB)

 
如果要进行设备切换，点击右上角的设备切换，回到设备选择页面，重新进行选择即可。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-8G2qb97QTG_XcHJyx1oIQ/zh-cn_image_0000002658928861.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=408203993B80629BF466FD2DD5D383A0376B5E83C55A4CADE4A8429BD81DBEAD)

 
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
