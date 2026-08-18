# TextInput组件的下划线设置

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1413

#### 问题现象

开发者在使用TextInput组件时，对组件的下划线使用有以下几个经典场景：
 
- 场景一：如何实现TextInput组件下划线在文本输入时的动态显示和隐藏？
- 场景二：TextInput设置类型不是InputType.Normal类型时，如何设置下划线？
- 场景三：如何实现TextInput组件的下划线在获得焦点时闪烁的效果？

 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)是单行文本输入框组件，下划线只支持InputType.Normal类型，其他如Password或者Number类型时，设置[showUnderline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showunderline10)下划线不会生效。
- [outline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline#outline)属性（轮廓）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

 
 

#### 解决方案

- **场景一**：TextInput组件，可以按需配置显示还是隐藏下划线，可参考官方文档[设置下划线](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#示例2设置下划线)。
- **场景二**：当TextInput设置类型不是InputType.Normal类型时，可通过[outline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline#outline)属性来设置下划线。
```text
@Entry
@Component
struct PageOne {
  build() {
    Row() {
      Column() {
        TextInput({ placeholder: 'input your password...' })
          .width('95%')
          .height(40)
          .margin(20)
          .type(InputType.Password)
          .maxLength(9)
          .showPasswordIcon(true)
          .backgroundColor('#00000000')
          // 设置下划线
          .outline({
            width: { bottom: 1 },
            color: Color.Black,
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/u2fzfNJGQPahTeoJbT3RiA/zh-cn_image_0000002658962481.png?HW-CC-KV=V1&HW-CC-Date=20260811T005650Z&HW-CC-Expire=86400&HW-CC-Sign=BDC4C778C1230F194829CD51C0C017B2C499B8AD1EF5382D707332A8C58FD1A2)

- **场景三**：要添加闪烁效果，可以在输入框获得焦点时通过定时器来交替改变下划线的颜色。
```text
@Entry
@Component
struct PageTwo {
  @State bottomColor: Color = Color.Black;

  build() {
    Row() {
      Column() {
        TextInput({ placeholder: 'input your password...' })
          .type(InputType.Normal)
          .width('95%')
          .height(50)
          .showUnderline(true)
          .underlineColor({
            normal: this.bottomColor,

          })
          .onFocus(() => {
            setInterval(() => {
              this.bottomColor = this.bottomColor === Color.Red ? Color.Blue : Color.Red;
            }, 500); // 每500毫秒改变一次颜色
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Z6SsdU20SFmOjjLc77d56w/zh-cn_image_0000002628603270.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005650Z&HW-CC-Expire=86400&HW-CC-Sign=7399AF2A013A7A3D0CA1873BF0787EC9CD0FC369CC1B3986833EF35958DE7119)
