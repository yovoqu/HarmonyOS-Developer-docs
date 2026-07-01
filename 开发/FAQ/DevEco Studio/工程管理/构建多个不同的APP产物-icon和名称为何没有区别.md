# 构建多个不同的APP产物-icon和名称为何没有区别

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-31

## 构建多个不同的APP产物-icon和名称为何没有区别
 


##### 问题现象

需要在一个工程项目中，构建多个不同的APP，不同product拥有不同的bundleName、应用名称、应用图标。但是构建完后，并不能根据当前的product配置的信息替换AppScope文件下的app.json5里面的默认内容。
 
 

##### 背景知识

app.json5中的icon和label改变的是设置中显示的图标和名称。例如：
 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/gAOo_avISAONBxi6pQc5iw/zh-cn_image_0000002658807325.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=8225CD7EE36F54E1D5C3532533C5E4B33B8F674411E9500D9B6E198698598122)

 
正常使用DevEco Studio推送安装到手机的是HAP包，而HAP包里的icon和label是由module.json5文件决定的。例如：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/RzSwgEkSRuiwx4DCfJyryA/zh-cn_image_0000002628408064.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=9E49B750B98950AA7A7F3966EC6D07B9794E10300A8C7700936964194D251BCA)

 
要在工程级build-profile.json5文件products中配置不同的APP产物，并配置对应icon和label来覆盖app.json5里面的默认内容：
 
```text
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default_icon", // 定义default的icon
        "label":"$string:default_name", // 定义default的label
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productA_icon", // 定义productA的icon
        "label":"$string:productA_name", // 定义productA的label
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
 

##### 问题定位

HAP包中build-profile.json5是否定制对应的target产物，来覆盖module.json5中的配置。
 
 

##### 修改建议

针对HAP包也定制对应的target产物，并定制不同的icon、label。
 
 

##### 分析结论

product中的icon和label改变设置中显示的图标和名称，应用桌面的图标和名称是由HAP包的icon和label决定的。
 
可通过打包后的产物来检查是否配置正确：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7Uzub7JtQRu7uF72nYfanw/zh-cn_image_0000002628567960.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=8C7CC0F8001B067F5A37146CB4EEA2B1F759AB7F79B93AC62BB61B533F47CE9A)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/wAf_cV1ySEGcbrviipokCw/zh-cn_image_0000002658927283.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=8CA5C163206F854363A561372CB95465B1E81ABE0F7B253197AF6B7256AC0C5C)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/K_Kbh2KNRM6_l49yBvkzdA/zh-cn_image_0000002658807327.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=CA3090DD318D6B700CA81A05ACC5E4D99AF86A2EB90C8E6170C82F7BE1431B3E)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/AQF5q4xQRsmAO2jctZjuJg/zh-cn_image_0000002628408066.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=E9E959B705ECD2ADB8D9336AB3D48734974A093C01DE427275E1BF5671C41765)

 
附：配置多目标产物-[定义产物的icon、label、launchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides#section82111917125413)。
