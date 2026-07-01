# 构建多个不同的APP产物-icon和名称为何没有区别

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-31

#### 问题现象

需要在一个工程项目中，构建多个不同的APP，不同product拥有不同的bundleName、应用名称、应用图标。但是构建完后，并不能根据当前的product配置的信息替换AppScope文件下的app.json5里面的默认内容。
 
 

#### 背景知识

app.json5中的icon和label改变的是设置中显示的图标和名称。例如：
 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/gAOo_avISAONBxi6pQc5iw/zh-cn_image_0000002658807325.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=FDDBDF8E06B804766F9650E01CBC313AADCE743A14A96DE042E978189C1ECA56)

 
正常使用DevEco Studio推送安装到手机的是HAP包，而HAP包里的icon和label是由module.json5文件决定的。例如：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/RzSwgEkSRuiwx4DCfJyryA/zh-cn_image_0000002628408064.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=6A73774E3B61424B144732935742083A86F73F10BFA4857243B659681E71B118)

 
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7Uzub7JtQRu7uF72nYfanw/zh-cn_image_0000002628567960.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=0AF8AA9C13768E227C77CECDAAF2B1585357C68F0FC75CC6A806ECE90C8E20F2)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/wAf_cV1ySEGcbrviipokCw/zh-cn_image_0000002658927283.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=25883E0BD256836911895335002EC73E6EF0EA969E0F502FF83763591F641F8C)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/K_Kbh2KNRM6_l49yBvkzdA/zh-cn_image_0000002658807327.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=BAD600A3CED28B967106BCD3EBB8552D3EB1CFBF9B23F40C32B0B08D35C02E62)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/AQF5q4xQRsmAO2jctZjuJg/zh-cn_image_0000002628408066.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=C6C679A0E5D1280E9B85AB80A1D42469B1B6CA8B0AE8136C410E569B705E0BE6)

 
附：配置多目标产物-[定义产物的icon、label、launchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides#section82111917125413)。
