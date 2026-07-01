# Radio组件通过ContentModifier实现自定义样式后如何实现单选

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-721

## Radio组件通过ContentModifier实现自定义样式后如何实现单选
 


##### 问题现象

当Radio设置通过ContentModifier设置自定义内容后，Radio无法实现单选功能。
 
问题代码如下：
 
```text
class DiRadio implements ContentModifier {
  applyContent(): WrappedBuilder {
    return wrapBuilder(buildDiRadio);
  }
}


@Builder
function buildDiRadio(config: RadioConfiguration) {
  Column() {
    Image(config.checked ? $r('app.media.checked_true') : $r('app.media.checked_false'))
      .width(24).height(24)
  };
}


@Entry
@Component
struct CustomRadio {
  build() {
    Column({ space: 15 }) {
      Column({ space: 5 }) {
        Text('Radio1');
        Radio({ value: 'Radio1', group: 'radioGroup' }).contentModifier(new DiRadio());
      };


      Column({ space: 5 }) {
        Text('Radio2');
        Radio({ value: 'Radio2', group: 'radioGroup' }).contentModifier(new DiRadio());
      };


      Column({ space: 5 }) {
        Text('Radio3');
        Radio({ value: 'Radio3', group: 'radioGroup' }).contentModifier(new DiRadio());
      };
    }
    .height('100%')
    .width('100%');
  }
}
```
 
问题效果预览:
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/AXeLT94VSSmpMMIb3suaCw/zh-cn_image_0000002658914533.png?HW-CC-KV=V1&HW-CC-Date=20260701T025544Z&HW-CC-Expire=86400&HW-CC-Sign=A903411C9101F45FB50418DE961A3B299BDFCFCCBE4A548E4193C49FE68E4E5F)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BM71IsMDT1-Ad8FR4WThKQ/zh-cn_image_0000002628395308.png?HW-CC-KV=V1&HW-CC-Date=20260701T025544Z&HW-CC-Expire=86400&HW-CC-Sign=F42EFBB1792E10B63067E90E01B3742BA042497C5972B60A1FAB2F061E4F68F4)

 
 

##### 背景知识

- [ContentModifier接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-attributes-content-modifier)：内容修改器，提供自定义绘制组件内容区的能力。
- [Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)：单选框，提供相应的用户交互选择项。[contentModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio#contentmodifier18)，在Radio组件上，定制内容区的方法。modifier，内容修改器，开发者需要自定义class实现ContentModifier接口。当modifier的值为undefined时，不使用内容修改器。

 
 

##### 问题定位

Radio组件添加了ContentModifier后，当选择Radio时没有修改checked的值。
 
 

##### 分析结论

目前Radio组件添加了ContentModifier后，内容、样式和触发条件需要自己定义。
 
 

##### 修改建议

在ContentModifier的基础上，给自定义内容添加点击事件。当checked的值为false时，通过triggerChange方法修改当前Radio的checked值为true（同group的其他Radio的checked值会自动变为false），可以解决该问题。
 
代码示例如下：
 
```text
class DiRadio implements ContentModifier {
  applyContent(): WrappedBuilder {
    return wrapBuilder(buildDiRadio);
  }
}


@Builder
function buildDiRadio(config: RadioConfiguration) {
  Column() {
    Image(config.checked ? $r('app.media.startIcon') : $r('app.media.background'))
      .width(24).height(24)
      .onClick(() => {
        if (!config.checked) {
          config.triggerChange(true);
        }
      });
  };
}


@Entry
@Component
struct CustomRadio {
  build() {
    Column({ space: 15 }) {
      Column({ space: 5 }) {
        Text('Radio1');
        Radio({ value: 'Radio1', group: 'radioGroup' }).contentModifier(new DiRadio());
      };


      Column({ space: 5 }) {
        Text('Radio2');
        Radio({ value: 'Radio2', group: 'radioGroup' }).contentModifier(new DiRadio());
      };


      Column({ space: 5 }) {
        Text('Radio3');
        Radio({ value: 'Radio3', group: 'radioGroup' }).contentModifier(new DiRadio());
      };
    }
    .height('100%')
    .width('100%');
  }
}
```
