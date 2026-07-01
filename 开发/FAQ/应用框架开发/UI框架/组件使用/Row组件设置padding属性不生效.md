# Row组件设置padding属性不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1295

## Row组件设置padding属性不生效
 


##### 问题现象

Row组件中存放一个Text组件和一个TextInput组件，给Row组件设置padding并未生效，该如何解决？
 
```text
@Entry
@Component
struct PageOne {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3');
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/RM7IhLiMQMefXTb8EJbYaA/zh-cn_image_0000002658837245.png?HW-CC-KV=V1&HW-CC-Date=20260701T025609Z&HW-CC-Expire=86400&HW-CC-Sign=71AEDFC7E63B7F948302E1D44837C21779ACFE741D7A2289C6B62BE4FDAC0CD7)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/kFIzd8mfTKmjqVQIe2UOCA/zh-cn_image_0000002628597982.png?HW-CC-KV=V1&HW-CC-Date=20260701T025609Z&HW-CC-Expire=86400&HW-CC-Sign=589B71152824C80213D2B26C664F564192C91C32EA7526540566AA5446B45890)

 
 

##### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)：单行文本输入框组件。
- [layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)：设置组件的布局权重，使组件在父容器（[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)/[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)/[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）的主轴方向按照权重分配尺寸。

 
 

##### 解决方案

针对padding属性未生效问题，给TextInput组件设置layoutWeight(1)属性即可。
 
```text
@Entry
@Component
struct PageTwo {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3')
          .layoutWeight(1);
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```
