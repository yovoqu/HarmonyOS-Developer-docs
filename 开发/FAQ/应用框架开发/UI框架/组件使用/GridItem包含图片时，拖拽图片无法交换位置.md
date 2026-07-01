# GridItem包含图片时，拖拽图片无法交换位置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1188

#### 问题现象

Grid拖拽场景中，如果GridItem中包含图片，则在拖拽图片时只有拖拽动画，没有交换元素功能。
 
现象如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hlg7aYFQR2mE9_q75EAfmA/zh-cn_image_0000002628592956.png?HW-CC-KV=V1&HW-CC-Date=20260701T041241Z&HW-CC-Expire=86400&HW-CC-Sign=FED3364BD845D894985F33D7D66CCA7A704AB6BDE57B19B5588DD2AEE31CAC6E)

 
 

#### 背景知识

- [onItemDragStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#onitemdragstart8)回调在开始拖拽网格元素时触发，[onItemDrop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#onitemdrop8)回调当GridItem停止拖拽时触发。
- [Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)的[draggable属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#draggable9)能够设置组件默认拖拽效果，默认值为true。

 
 

#### 解决方案

Grid拖拽场景需要调用onItemDragStart和onItemDrop回调，而Image组件的draggable属性默认值为true，在点击图片时，优先响应的是draggable属性，导致无法触发Grid组件的onItemDragStart回调，因此可以将Image组件的draggable属性改为false即可正常触发onItemDragStart回调，从而正常实现交换位置功能。完整示例代码如下：
 
```text
@Entry
@Component
struct Second {
  @State addedItems: string[] = ['1', '2', '3', '4', '5', '6', '7', '8'];
  private scroller: Scroller = new Scroller();


 <em> // 设置拖拽过程样式</em>
  @Builder
  dragItem(item: string) {
    Column() {
      Image($r('app.media.startIcon'))<em> // 仅供参考，需根据业务场景更换</em>
        .width(44)
        .height(44)
        .draggable(false)
        .objectFit(ImageFit.Contain);
      Text(`index:${item}`)
        .fontSize(12)
        .margin({ top: 5 });
    }
    .height('auto');
  }


  build() {
    Column() {
      Grid(this.scroller) {
        ForEach(this.addedItems, (item: string) => {
          GridItem() {
            Column() {
              Image($r('app.media.startIcon')) <em>// 仅供参考，需根据业务场景更换</em>
                .width(44)
                .height(44)
                .objectFit(ImageFit.Contain)
                .draggable(false); <em>// 将draggable属性设置为false</em>
              Text(`index:${item}`)
                .fontSize(12)
                .margin({ top: 5 });
            }
            .height(99);
          };
        });
      }
      .columnsGap(10)
      .rowsGap(0)
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .supportAnimation(true)
      .height(220)
      .width('100%')
      .padding({
        top: 30
      })
      .editMode(true) /<em>/ 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem</em>
      .onItemDragStart(((event: ItemDragInfo, index: number) => { /<em>/ 第一次拖拽此事件绑定的组件时，触发回调</em>
        console.log('onItemDragStart');
        return this.dragItem(this.addedItems[index]); <em>// 设置拖拽过程中显示的图片</em>
      }))
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number,
        isSuccess: boolean) => { <em>// 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调</em>
        console.log('onItemDrop');
      <em>  // isSuccess=false时，说明drop的位置在grid外部；insertIndex > length时，说明有新增元素的事件发生</em>
        if (!isSuccess || insertIndex >= this.addedItems.length) {
          return;
        }
        console.info( itemIndex + '', insertIndex + ''); <em>// itemIndex拖拽起始位置，insertIndex拖拽插入位置</em>
        this.changeIndex(itemIndex, insertIndex);
      });
    }
    .height('100%')
    .width('100%');
  }


<em>  // 交换数组位置</em>
  changeIndex(index1: number, index2: number) {
    let temp: string;
    temp = this.addedItems[index1];
    this.addedItems[index1] = this.addedItems[index2];
    this.addedItems[index2] = temp;
  }
}
```
 
效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/-hCYn01kRRKPNWfv2pvOtA/zh-cn_image_0000002658832209.png?HW-CC-KV=V1&HW-CC-Date=20260701T041241Z&HW-CC-Expire=86400&HW-CC-Sign=295B1D8D0248BC0AD62165F1253EFB33085A28BCEDF21125174939957A4A960D)
