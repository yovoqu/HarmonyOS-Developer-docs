# bindSheet如何在跳转后返回，仍保持原样

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-741

#### 问题现象

bindSheet的内容是个List，点击某个ListItem跳转至其他页面，如何实现从其他页面返回后bindSheet仍是打开状态，且List仍保持原样？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/5rEyeVgiTxaIT8iSgSqQig/zh-cn_image_0000002628555360.png?HW-CC-KV=V1&HW-CC-Date=20260723T012608Z&HW-CC-Expire=86400&HW-CC-Sign=4F4436BF3BAEDDDFE4B0661BD7243B5315522DAE049B31BC56184153D6D8746A)

 
 

#### 背景知识

- [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sheet-page)：默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。
- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)：AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。

 
 

#### 解决方案

在[onPageShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow)生命周期中，通过AppStorage获取当前bindSheet显示状态以及List滑动距离，在跳转其他页面时记录当前List滑动距离，当目标页面返回时将bindSheet显隐状态绑定的变量设置为true，且在List的onAppear中通过Scroller滑动至之前保存的位置，实现保持原样的效果。参考代码如下：
 
```text
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct BindSheetOnePage {
  @StorageProp('isTrue') isShow: boolean = false;
  @State numArr: number[] = [];
  private scrollerForList: Scroller = new Scroller();
  @State currentY: number = 0;

  onPageShow(): void {
   <em> // 全局获取半模态的状态</em>
    this.isShow = AppStorage.get('isTrue') as boolean;
   <em> // 全局获取List当前位置</em>
    this.currentY = AppStorage.get('currentY') as number;
   <em> // 设置沉浸式</em>
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      console.error(`err: ${err}`);
      win.setWindowLayoutFullScreen(true);
    });
  }

  aboutToAppear(): void {
    <em>// 插入list数据</em>
    for (let index = 0; index < 20; index++) {
      this.numArr.push(index);
    }
  }

  @Builder
  myBuilder() {
    List({ scroller: this.scrollerForList }) {
      ForEach(this.numArr, (item: number) => {
        ListItem() {
          Column() {
            Text(item.toString());
          }
          .justifyContent(FlexAlign.Center)
          .height('20%')
          .width('100%')
          .backgroundColor('#F3F3F3')
          .onClick(() => {
           <em> // 全局存储当前List滑动距离</em>
            AppStorage.setOrCreate('currentY', this.scrollerForList.currentOffset().yOffset);
          <em>  // 跳转到下一个页面</em>
            this.getUIContext().getRouter().pushUrl({
              url: 'pages/BindSheetTwoPage'
            }).catch((e: BusinessError) => {
              console.error(`e: ${e}`);
            });
          });
        };
      });
    }
    .margin({
      left: 16,
      right: 16
    })
    .onAppear(() => {
     <em> // 通过Scroller滑动至之前保存的位置，实现保持原样的效果</em>
      this.scrollerForList.scrollTo({ xOffset: 0, yOffset: this.currentY });
    })
    .height('100%');
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
        <em>  // 点击打开半模态</em>
          this.isShow = true;
        <em>  // 全局存储半模态状态</em>
          AppStorage.setOrCreate('isTrue', true);
        })
        .fontSize(20)
        .margin(10)
       <em> // $$双向同步半模态的状态</em>
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: 600,
          title: { title: "title" },
          onAppear: () => {
            console.info('BindSheet onAppear.');
          },
          onDisappear: () => {
            console.info('BindSheet onDisappear.');
          }
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
 
路由目标页面代码如下：
 
```text
@Entry
@Component
struct BindSheetTwoPage {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
      <em>    // 点击返回上个页面</em>
          this.getUIContext().getRouter().back();
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
