# 如何实现Flex组件的宽高自适应子组件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1493

#### 问题现象

问题1：Flex方向为Column时，默认高度会撑满Flex的父容器。如何让Flex的高度自适应子组件的高度？
 
问题2：Flex方向为Row时，默认宽度会撑满Flex的父容器，如何让Flex宽度自适应子组件的宽度？
 
问题1效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/iOsHcGtvQUS3o8AX5y3gjg/zh-cn_image_0000002658845079.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=798A54E6526239BA97E0032CCE6257FFC66FF565F26D96289A08F8A3E8B39256)

 
问题2效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ceUlwK5ESE6pAny9PMaHlg/zh-cn_image_0000002628765708.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=2425232B574DEA1B5B05ADF8822A0CFD275D797994E13E5D007F9E55F7DB079E)

 
 

#### 背景知识

- [Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。
- Flex主轴不设置长度时默认撑满父容器。主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)属性以及父容器传递的最大最小长度限制，且constraintSize属性优先级更高。
- [组件区域变化事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event)，组件显示的尺寸、位置等发生变化时触发[onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)，仅会响应由布局变化所导致的组件大小、位置发生变化时的回调，可以获取组件位置和尺寸信息。
- [组件尺寸变化事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-size-change-event)，组件显示的尺寸发生变化时触发[onSizeChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-size-change-event#onsizechange)，仅会响应由布局变化所导致的组件尺寸发生变化时的回调，可以获取组件尺寸信息。

 
 

#### 解决方案

- **方案一**：参考背景知识，Flex组件主轴方向设置长度为auto时，Flex自适应子组件布局。问题1：Flex方向为Column，可以将Flex组件高度设置为auto，使Flex自适应子组件布局的高度。

  
```text
@Entry
@Component
struct FlexExample1 {
  build() {
    Column({ space: 10 }) {
      Text('Flex方向为Column');
      Flex({ direction: FlexDirection.Column }) {
        Text('Flex的子组件\nHello World!')
          .backgroundColor('#330a59f7')
          .textAlign(TextAlign.Center)
          .borderRadius(30)
          .padding(20);
      }
      .backgroundColor('#f1f3f5')
      .height('auto');
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/RxhwmEbEQ2-KXHD7I4JXWg/zh-cn_image_0000002658965033.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=42A3EA5811D592204DEDBA632106DE7A0AB73F0DFFE4BB810152B94DDABB10D7)


  问题2：Flex方向为Row时同理，设置宽度为auto，使Flex自适应子组件布局的宽度。

  
```text
@Entry
@Component
struct FlexExample2 {
  build() {
    Column({ space: 10 }) {
      Text('Flex方向为Row');
      Flex({ direction: FlexDirection.Row }) {
        Text('Flex的子组件\nHello World!')
          .backgroundColor('#330a59f7')
          .textAlign(TextAlign.Center)
          .borderRadius(30)
          .padding(20);
      }
      .backgroundColor('#f1f3f5')
      .width('auto');
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/AqnucAeOQPmnZultTIqxAA/zh-cn_image_0000002628605828.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=12EF12DB01E584038EBD394AA1AD32937C00D621E74C7DD29212B51F188B253A)

- **方案二**：Flex主轴方向长度默认设置'100%'，子组件布局完成时通过onSizeChange/onAreaChange获取尺寸信息，根据子组件尺寸设置Flex主轴方向长度。问题1：Flex方向为Column时，通过onSizeChange获取子组件高度，设置Flex高度。

  
```text
@Entry
@Component
struct FlexExample3 {
  @State flexHeight: number | string = '100%'; <em>// 默认情况主轴占满</em>

  build() {
    Column({ space: 10 }) {
      Text('Flex方向为Column');
      Flex({ direction: FlexDirection.Column }) {
        Text('Flex的子组件\nHello World!')
          .backgroundColor('#330a59f7')
          .textAlign(TextAlign.Center)
          .borderRadius(30)
          .padding(20)
          .onSizeChange((oldSize, newSize) => { <em>// 也可以使用onAreaChange</em>
            this.flexHeight = newSize.height as number; <em>// 获取子组件高</em>
          });
      }
      .backgroundColor('#f1f3f5')
      .height(this.flexHeight);
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/p-eTNGliQ16fM4H1R9rlEQ/zh-cn_image_0000002658845081.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=8F23217F48E3273EBA54F95005EC5077C644528C4C2FADD37ACCA320732D43BB)


  问题2：Flex方向为Row时，通过onSizeChange获取子组件宽度，设置Flex宽度。

  
```text
@Entry
@Component
struct FlexExample4 {
  @State flexWidth: number | string = '100%';<em> // 默认情况主轴占满</em>

  build() {
    Column({ space: 10 }) {
      Text('Flex方向为Row');
      Flex({ direction: FlexDirection.Row }) {
        Text('Flex的子组件\nHello World!')
          .backgroundColor('#330a59f7')
          .textAlign(TextAlign.Center)
          .borderRadius(30)
          .padding(20)
          .onSizeChange((oldSize, newSize) => { <em>// 也可以使用onAreaChange</em>
            this.flexWidth = newSize.width as number;<em> // 获取子组件宽</em>
          });
      }
      .backgroundColor('#f1f3f5')
      .width(this.flexWidth);
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/i3jifXYhQCud2muvSI2Gmw/zh-cn_image_0000002628765710.png?HW-CC-KV=V1&HW-CC-Date=20260730T072404Z&HW-CC-Expire=86400&HW-CC-Sign=C34FFEC267407E7D269B5C95EBB12BA53A77D844E2D4497D661D0D2D146334E6)
