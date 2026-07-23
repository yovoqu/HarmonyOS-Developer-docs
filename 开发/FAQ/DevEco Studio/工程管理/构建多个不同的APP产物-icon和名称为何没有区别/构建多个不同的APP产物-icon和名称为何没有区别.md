# 构建多个不同的APP产物-icon和名称为何没有区别

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-31

#### 问题现象

需要在一个工程项目中，构建多个不同的APP，不同product拥有不同的bundleName、应用名称、应用图标。但是构建完后，并不能根据当前的product配置的信息替换AppScope文件下的app.json5里面的默认内容。
 
 

#### 背景知识

app.json5中的icon和label改变的是设置中显示的图标和名称。例如：
 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/gAOo_avISAONBxi6pQc5iw/zh-cn_image_0000002658807325.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=F32C7DA5A381FBC70953F44CDFAA98292A415E38ACA7B0F87F3C779BACAB4B9C)

 
正常使用DevEco Studio推送安装到手机的是HAP包，而HAP包里的icon和label是由module.json5文件决定的。例如：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/RzSwgEkSRuiwx4DCfJyryA/zh-cn_image_0000002628408064.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=6015FFC024EE8450BD5A5042CC86C02BF7B531AD57C0D193945F8C46ED56F58C)

 
要在工程级build-profile.json5文件products中配置不同的APP产物，并配置对应icon和label来覆盖app.json5里面的默认内容：
 
```json
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default_icon", <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义</span><span style="color: rgb(128,128,128);">default</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">icon</span></em>
        "label":"$string:default_name", <em>// </em><em><span style="color: rgb(128,128,128);">定义</span><span style="color: rgb(128,128,128);">default</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">label</span></em>
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productA_icon",<em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义</span><span style="color: rgb(128,128,128);">productA</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">icon</span></em>
        "label":"$string:productA_name", <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义</span><span style="color: rgb(128,128,128);">productA</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">label</span></em>
      },
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ],
    "modules": [
      {
        "name": "entry",
        "srcPath": "./entry",
        "targets": [
          {
            "name": "default",
            "applyToProducts": [
              "default"
            ]
          },
          {
            "name": "productA",
            "applyToProducts": [
              "productA"
            ]
          }
        ]
      }
    ]
  }
}
```
 
HAP包中模块级的build-profile.json5定制对应的target产物，来覆盖module.json5中的配置：
 
```text
{
  "apiType": 'stageMode',
  "buildOption": {
  },
  "targets": [
    {
      "name": "default",
      "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:default_icon",
            "label":"$string:default_name"
          }
        ]
      }
    },
    {
      "name": "productA",
      "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:productA_icon",
            "label":"$string:productA_name"
          }
        ]
      }
    }
  ]
}
```
 

#### 问题定位

HAP包中build-profile.json5是否定制对应的target产物，来覆盖module.json5中的配置。
 
 

#### 修改建议

针对HAP包也定制对应的target产物，并定制不同的icon、label。
 
 

#### 分析结论

product中的icon和label改变设置中显示的图标和名称，应用桌面的图标和名称是由HAP包的icon和label决定的。
 
可通过打包后的产物来检查是否配置正确：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7Uzub7JtQRu7uF72nYfanw/zh-cn_image_0000002628567960.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=DF487E0FD2A816BA08363A2597CE9BCC45977DBE20C5431A0DA1C3806BD63E2F)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/wAf_cV1ySEGcbrviipokCw/zh-cn_image_0000002658927283.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=DB90F30012EEECF2A899FA62E4C0091830ED5816A49C4BE89AD5C16D04A6B2EC)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/K_Kbh2KNRM6_l49yBvkzdA/zh-cn_image_0000002658807327.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=62E12BD48BEBDF71785BE6051B15B0C336C204663CD61C2B60C2F9B7EBF44FD6)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/AQF5q4xQRsmAO2jctZjuJg/zh-cn_image_0000002628408066.png?HW-CC-KV=V1&HW-CC-Date=20260723T013912Z&HW-CC-Expire=86400&HW-CC-Sign=8A5CA1B7F0C0C90DAEDBC4040A34F8A586BCB9BDA112C1109A780496207525E6)

 
附：配置多目标产物-[定义产物的icon、label、launchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides#section82111917125413)。
