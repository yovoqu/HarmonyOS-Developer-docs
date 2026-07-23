# FrameNode自定义的TextArea节点如何实现自适应文本宽度

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1654

#### 问题现象

通过FrameNode自定义的TextArea节点后，如何配置可以使得TextArea宽度随文本宽度变化而变化？
 
 

#### 背景知识

- [FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode)表示组件树的实体节点，可以通过[appendChild()方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#appendchild12)在FrameNode最后一个子节点后添加新的子节点。
- [typeNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#typenode12)提供创建具体类型的FrameNode能力，可通过FrameNode的基础接口进行自定义的挂载，使用占位容器进行显示。
- [expandSafeArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea)控制组件扩展其安全区域。
设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高（包括设置'auto'）时，扩展安全区域的方向只支持[SafeAreaEdge.TOP, SafeAreaEdge.START]，扩展后的组件尺寸保持不变。
- expandSafeArea属性仅作用于当前组件，不会向父组件或子组件传递，因此使用过程中，所有相关组件均需配置。

 
 
 

#### 解决方案
1. 使用new FrameNode(uiContext)创建一个空的FrameNode作为整个动态组件树的根节点；
2. 通过typeNode.createNode动态创建Column和TextArea节点，利用width('auto')实现文本宽度自适应；
3. 同时通过commonAttribute.expandSafeArea设置安全区域避让，并使用appendChild组装节点树挂载至根FrameNode。
 
具体参考下列代码：
```text
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    let col = typeNode.createNode(uiContext, 'Column');
    col.initialize()
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .backgroundColor('rgba(241, 243, 245, 1)');
    node.appendChild(col);
    <em>// 创建textArea</em>
    let textArea = typeNode.createNode(uiContext, 'TextArea');
    textArea.initialize({ text: 'TextArea的内容是随文本宽度变化的' })
      .width('auto');
    <em>// 设置安全区域（沉浸式适配）</em>
    col.commonAttribute.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    col.appendChild(textArea);
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController);
    };
  }
}
```
