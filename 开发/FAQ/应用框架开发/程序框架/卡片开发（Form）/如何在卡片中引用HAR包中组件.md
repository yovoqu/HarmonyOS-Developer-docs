# 如何在卡片中引用HAR包中组件

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-22

## 如何在卡片中引用HAR包中组件
 


##### 问题现象

为了提高自定义组件复用率，项目采用HAR包定义公共UI组件，如何在卡片页面中引用？
 
 

##### 背景知识

- [Form Kit（卡片开发服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/formkit-overview)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
- [HAR（Harmony Archive）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。

 
 

##### 解决方案

在项目中引用HAR，本文介绍采用从本地文件夹安装以及从本地压缩包安装两种方式。
 
- **场景一**：从本地文件夹安装。
参考[创建ArkTS卡片](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation)，在工程中创建动态卡片。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/-mD39QMBRoGhvng6ybkMmQ/zh-cn_image_0000002658990871.png?HW-CC-KV=V1&HW-CC-Date=20260701T025530Z&HW-CC-Expire=86400&HW-CC-Sign=6DE3A77A501815AE865C78E2A1613368CC7ED74A0A564065D1123B73E07806A1)

- 参考[构建HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har#section3761328124112)，在工程中创建名称为localFolderPack的HAR包。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/ejL-j72yRW-Xast0raw6cg/zh-cn_image_0000002628631660.png?HW-CC-KV=V1&HW-CC-Date=20260701T025530Z&HW-CC-Expire=86400&HW-CC-Sign=7F4FB336A553D258E80780FCABBE93409C2CE859937AC0781ADD2EB96680039F)

- 在localFolderPack的HAR包中自定义MainPage组件，并导出。
```text
@Component
export struct MainPage {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message = 'Welcome';
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

- 在主项目中配置对HAR的依赖，参考[引用及管理共享包-引用本地模块源码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import)。导入后oh-package.json5中会添加"localfolderpack": "file:../localFolderPack"。
- 在项目卡片页面WidgetCard.ets，引入HAR包并使用组件。
```text
import { MainPage } from 'localfolderpack';

@Entry
@Component
struct WidgetCard {
  build() {
    Row() {
      MainPage();
    }
    .width('100%')
    .height('100%')
    .backgroundColor($r('sys.color.comp_background_primary'));
  }
}
```


 - **场景二**：从本地压缩包安装。
参考创建ArkTS卡片，在工程中创建动态卡片。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/oxaRkI2tS7mJIBRWOQeHkQ/zh-cn_image_0000002658870933.png?HW-CC-KV=V1&HW-CC-Date=20260701T025530Z&HW-CC-Expire=86400&HW-CC-Sign=50DB9C079EEA46EE8AB93C50AA98493FDBFFD613E544CFA3247A084735D72143)

- 参考构建HAR，在工程中创建名称为localZipPack的HAR包。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/lYnmQBmyRjCC-uDMMIzpHw/zh-cn_image_0000002628791564.png?HW-CC-KV=V1&HW-CC-Date=20260701T025530Z&HW-CC-Expire=86400&HW-CC-Sign=6BDD68891455F052D8E4D3415AA6895138A66572AF245E5ADDD473BE30613A9B)

- 在localZipPack的HAR包中自定义MainPage组件，并导出。
```text
@Component
export struct MainPage {
  isShow: boolean = true;

  build() {
    Column() {
      if (this.isShow) {
        Row() {
          Text('localZipPack hello')
            .fontSize(20);
        };
      } else {
        Row() {
          Text('localZipPack hi')
            .fontSize(20);
        };
      }
    }
    .padding(16)
    .width('100%')
    .height('100%');
  }
}
```

- 参考[编译HAR模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har#section7892044183814)，进行编译，获取“build/default/outputs/default/localZipPack.har”。
- 在主项目中配置对HAR的依赖，参考[引用及管理共享包-引用本地HAR/HSP包](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import)。导入后oh-package.json5中会添加"localzippack": "file:../localZipPack.har"。
- 在项目卡片页面WidgetCard.ets，引入HAR包并使用组件。注意：从本地压缩包安装HAR包，编译器未能将HAR包自定义组件所使用的系统组件自动导入，需要手动将所使用的组件重新配置。本案例在MainPage组件中使用了Column、Row、Text、if组件，所以完整示例参考如下：
```text
import { MainPage } from 'localzippack';

@Entry
@Component
struct WidgetCard {
  build() {
    Row() {
      MainPage({ isShow: false });
    };
  }

  @Builder
  MainPageImport() {
    Column();
    Text();
    Row();
    if (true) {
    }
  }
}
```


 
 
 

##### 常见FAQ

Q：采用HAR包封装公共组件，将HAR包引入在卡片中复用时可能出现白屏，该如何解决？
 
A：采用源码编译的方式直接从本地文件夹安装HAR包不会出现问题，使用*.har压缩包安装引入出现该问题原因是二进制文件没有参与编译，导致打包的component_collection.json文件里不包含二进制文件内的组件信息。
