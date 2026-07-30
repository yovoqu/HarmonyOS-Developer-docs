# PC应用内组件如何实现悬浮样式Hover效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-754

#### 问题现象

PC应用如何实现鼠标悬停在组件上时，组件UI效果变更？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/hC5wTvM6T6CXMLIWueaSSA/zh-cn_image_0000002628395472.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=B158BA05AA996E5E047C4879214913AF429DF9E7CE3AD69A522C83273D5618F9)

 
 

#### 背景知识

- [@Styles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style)：@Styles装饰器可以将多条样式设置提炼成一个方法，直接在组件声明的位置调用。通过@Styles装饰器可以快速定义并复用自定义样式，仅仅应用于静态页面的样式复用。
- [stateStyles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles)：stateStyles可以依据组件的内部状态的不同，快速设置不同样式。stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下五种状态：focused、normal、pressed、disabled、selected。

 
 

#### 解决方案

例如按钮的默认状态、按下状态、禁用状态可以将@Styles与stateStyles组合使用来实现对应效果，悬浮状态还需要结合[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover)事件来实现。
 
```text
<em>// </em><em>定义在全局的Button样式</em>
@Styles
function globalButtonStyle() {
  .width(160)
  .height(80)
  .borderRadius(16);
}

@Entry
@Component
struct CustomerButton {
  @State isHover: boolean = false;

  <em>// </em><em>定义在组件内的@Styles封装的样式</em>
<em>  // Disable</em>
  @Styles
  disabledStyle(){
    .backgroundColor('#A8B8F7');
  }

  <em>// normal</em>
  @Styles
  normalStyle() {
    .backgroundColor('#0A59F7');
  }

 <em> // pressed</em>
  @Styles
  pressedStyle() {
    .backgroundColor('#0950DE');
  }

  <em>// hover</em>
  @Styles
  hoverStyle() {
    .backgroundColor(this.isHover ? '#0954EA' : '#0A59F7');
  }

  build() {
    Column() {
      Row() {
        Text('Default')
          .width(120)
          .fontSize(30);
        Button('默认状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .stateStyles({
            normal: this.normalStyle
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Pressed')
          .width(120)
          .fontSize(30);
        Button('按下状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .stateStyles({
            normal: this.normalStyle,
            pressed: this.pressedStyle,
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Hover')
          .width(120)
          .fontSize(30);
        Button('悬浮状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .onHover((isHover: boolean) => {
            console.info(`${isHover}`);
            this.isHover = !this.isHover;
          })
          .stateStyles({
            normal: this.hoverStyle
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Disable')
          .width(120)
          .fontSize(30);
        Button('禁用状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .enabled(false)
          .stateStyles({
            disabled: this.disabledStyle
          });
      }
      .margin({
        bottom: 20
      });
    }
    .padding({ top: 20 })
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
