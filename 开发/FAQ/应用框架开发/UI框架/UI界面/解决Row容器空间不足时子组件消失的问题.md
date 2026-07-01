# 解决Row容器空间不足时子组件消失的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-735

## 解决Row容器空间不足时子组件消失的问题
 


##### 问题现象

在Row组件中放置两个Text组件，左侧Text（动态标题）需自适应宽度，空间不足时末尾省略显示（TextOverflow.Ellipsis），右侧Text（如(99)）需始终完整显示，但实际效果中，空间不足时左侧Text直接消失，而非显示省略号。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct Index {
  @State title: string = '长标题文本长标题文本长标题文本';

  build() {
    Column() {
      Row() {
        Text(this.title)
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .textAlign(TextAlign.Center)
          .onClick(() => {
            this.title += '加加';
          })

        Text('(99)')
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .textAlign(TextAlign.Start)
          .displayPriority(2)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .margin({ top: 280 })
    }
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/JEjGgC4ZRWaOmlavUisnMw/zh-cn_image_0000002628395322.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025653Z&HW-CC-Expire=86400&HW-CC-Sign=DEC0867FE7E145ADCE50391AE41B5546C562839806511CEB0021E102BB762FE5)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/bmldBN1bSea-hHUh64_rDw/zh-cn_image_0000002658794597.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025653Z&HW-CC-Expire=86400&HW-CC-Sign=749904DB69E1BEE80C948B0D3DCEB1EE40759B55183097793F3009641F7CA214)

 
 

##### 背景知识

- [displayPriority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints#displaypriority)属性机制：当父容器空间不足时，系统按优先级隐藏子组件（值越小优先级越高），若某一优先级组件被隐藏，更低优先级的组件会全部被隐藏（即使空间足够），右侧Text设置displayPriority（低优先级），左侧未设置（默认0，高优先级），但隐藏逻辑导致左侧异常消失。
- 弹性布局压缩规则：Row基于Flex布局，子组件默认[flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink):0（禁止压缩），文本省略需同时满足：设置[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)和[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)，组件[flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink):1(允许压缩)且有明确宽度约束。

 
 

##### 问题定位

- 隐藏机制冲突：右侧displayPriority激活了隐藏逻辑，空间不足时触发低优先级组件隐藏链，导致左侧被连带隐藏，左侧虽设置省略样式，但flexShrink默认为0，未触发压缩流程，直接跳过省略进入隐藏。
- 布局约束缺失：左侧Text未明确允许压缩，右侧未禁止压缩，两者在空间争夺中行为未定义，justifyContent(FlexAlign.Center)强制居中分配空间，加剧宽度计算冲突。

 
 

##### 分析结论

根本矛盾在于：displayPriority的组件级隐藏机制与textOverflow的文本级压缩机制互斥，当空间不足时，系统优先触发displayPriority的隐藏逻辑，而非文本压缩。
 
 

##### 修改建议

核心方案：弃用displayPriority，改用弹性压缩控制。
 
```text
@Entry
@Component
struct LongText {
  @State title: string = '长标题文本长标题文本长标题文本';

  build() {
    Column() {
      // 关键修改1：使用Flex替代Row，明确弹性规则
      Flex({
        direction: FlexDirection.Row,
        alignItems: ItemAlign.Center,
        justifyContent: FlexAlign.Start // 左对齐
      }) {
        Text(this.title)
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .flexShrink(1) // 关键修改2：允许压缩
          .onClick(() => {
            this.title += '追加文本';
          })

        Text('(99)')
          .fontSize(17)
          .fontWeight(500)
          .flexShrink(0) // 关键修改3：禁止压缩
      }
      .width('100%')
      .margin({ top: 280 })
    }
  }
}
```
