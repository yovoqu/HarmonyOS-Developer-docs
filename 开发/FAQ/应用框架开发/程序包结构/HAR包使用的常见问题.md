# HAR包使用的常见问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-72

## HAR包使用的常见问题
 


##### 问题现象

HAR包作为静态共享包，时常作为二方/三方SDK使用，但在HAR包构建或引用中常遇到版本冲突、包体积过大等问题。
 
 

##### 背景知识

[HAR包的构建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har)：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。[构建的具体方法可见官网](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har)。
 
[HAR包的引用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import)：可以引用本地HAR包或OHPM仓中的HAR包。
 
[ohpm uninstall](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-uninstall)：卸载三方库，uninstall命令后面配置--no-save参数，卸载的三方库信息不会从oh-package.json5文件中删除。
 
 

##### 解决方案

- **场景一：每次是否都要先打包成HAR包再引用？**不需要每次先打包成HAR包再引用，可以直接引用源码，如entry模块需要依赖foo模块的源码方式如下。
 在需要引入本地模块源码的模块的oh-package.json5中设置源码依赖项，即entry模块的oh-package.json5中，添加如下配置：
 
```text
"dependencies": {
  "foo": "file:path/to/foo"  // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
},
```

- **场景二：****是否可以将java或jar文件打包成HAR包？**当前不支持将java或jar打包成HAR包。HAR包是静态共享包，可以包含ArkTs/ts代码、C++库、资源和配置文件。
- **场景三：HAR包会被重复打包如HAR包中有so库，引用此HAR包的每个module都会拷贝一份此so库，造成包体积非常大，如何优化？**推荐将公共资源替换成HSP动态共享包。
 在多包场景下，如果应用的多个HAP或HSP包使用HAR包实现代码和资源的共享，那么打包后的每个HAP或HSP包中都会存在一份共享HAR包的拷贝，导致APP包中存在冗余代码和资源。如下图示例，应用模块HAP1和HAP2/HSP1都引用了HAR2和HAR3，打包后，APP包中HAR2和HAR3存在多份重复拷贝，体积较大。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/igz4_K26SWGz_qtZJ98LPQ/zh-cn_image_0000002628788114.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=3AC0B0ACDA4BB85378390F1B564E9D381B35376A2D2FF8C9895C87B738781BDD)

 这种场景下，推荐开发者使用HSP代替HAR实现代码和资源共享。如下图示例，使用HSP2对原应用进行升级改造，打包后，APP包中HAR2和HAR3只存在一份拷贝，HAR2、HAR3总大小大于HSP时，可以减小应用包大小。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/eSKv1_UdTCqgDOWkut1nfA/zh-cn_image_0000002658987435.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=376D384265F23ECA86821C704581C4ACB736A58A1D816FA2F224FA1E98F6ABDC)

- **场景四：一个应用有多个模块，多个模块中引用同一个HAR包的不同版本是否有影响，怎么指定统一的版本？**没有影响，每个模块都会将各自的HAR包拷贝到自己的模块，不会影响其它模块。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/nvfDWoCgQ9OA_Y2uS1HpMA/zh-cn_image_0000002628628218.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=6937CB1448403481285ED2B5B0ED1CB19EC8ED90300362307536545DA2097734)

 
ohpm客户端在1.4.0版本开始支持[Override机制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-oh-package-json5#zh-cn_topic_0000001792256137_overrides)，可以在项目级别的oh-package.json5（即项目根目录下的oh-package.json5）文件中添加overrides配置，可以将HAR包指定统一的版本。替换的版本既可以是一个具体的版本号，也可以是一个模糊版本，还可以是本地存在的HAR包或源码目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/bVxvf9_PTIGZs7RsLkjcGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=0FE5CB98F531117867BD724C8B5E396CD16DE4211989A2D10FABDA953AD1E653)
 
overrides必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。
- 如项目指定foo统一版本为1.0.1，在项目级的oh-package.json5中配置如下：
```text
"overrides": {
  "foo": "1.0.1"
},
```

- 若本地存在foo的源码或者HAR包，想确保foo始终使用您本地的版本，可以在项目级的oh-package.json5中如下配置：
```text
"overrides": {
  // 本地存在"foo"的源码目录，如项目根目录下的foo目录
  // "foo": "file:./foo"
  // 本地存在"foo"的HAR文件，如项目根目录下的libs目录中的foo.har
  "foo": "file:./libs/foo.har"
},
```

- **场景五：一个应用存在多个HAR模块，例如存在模块HARA、模块HARB、模块HARC和模块HARD，HARB中依赖并引用了HARA，HARC中依赖并引用了HARB和HARA，HARD中依赖并引用了HARC、HARB和HARA，现在希望打包完成后的包中只包含一份HARA、HARB、HARC、HARD，避免生成的HAR包冗余重复，该如何实现？**
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/zmYHieC3QcOMP0beKBhkEw/zh-cn_image_0000002658867497.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=3FF13E4783AB717622C8BFCB33425193E13315829AB2C99A820297B6EB685293)
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/uVlakH4rQ7WOW8gqZJPdnw/zh-cn_image_0000002628788118.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=0C91075F6DD8E2638F4659826D8959CCE3CA10B2E67A65EBF79C0DF884933136)

- 由于存在多个HAR模块，这些模块之间又存在重复依赖和引用的关系，由于同一个工程下，不同HAR模块之间存在继承依赖的关系，即对于工程下的模块HARA、模块HARB、模块HARC和模块HARD，先将模块中的方法、类和接口等通过export方式暴露出去，使得工程下其他模块能够访问。
- 让HARB中依赖HARA，HARC中依赖HARB，HARD中依赖HARC，从而使四个模块构成继承依赖的关系，就可以实现在HARD引用HARC、HARB和HARA，在HARC中引用HARB和HARA，在HARB中引用HARA，这样就避免生成重复HAR包的情况。
- 将最外层的HAR模块HARD先转化成HSP模块，参考链接进行相关配置[HAR转HSP指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-to-hsp)。由于HSP模块只能供应用内其他HAP模块或HSP模块引用，如果需要共其他应用的模块使用，还需要将HSP模块转化成[集成态HSP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/integrated-hsp)，参考链接进行相关配置集成态HSP。
- 对集成态HSP模块HARD进行打包，提供给其他应用使用。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/wme5QV0EQKiJrXC-ZC1FTg/zh-cn_image_0000002658987441.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=9E565387A6BA1FFE8F8577CD517AC5A2EE07C3D25A124F8E6A91C8EBC651880A)
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Ed4DXvRbTKGCtT7POB09ig/zh-cn_image_0000002628628220.png?HW-CC-KV=V1&HW-CC-Date=20260701T025517Z&HW-CC-Expire=86400&HW-CC-Sign=4278F767C0AE2F5FBBDF275B87BD7750E39DC82E16DE737F2D23A861E4554405)
