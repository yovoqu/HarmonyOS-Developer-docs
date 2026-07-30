# Swiper组件在删除数据时如何实现切换到前一个元素而非第一个

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-563

#### 问题现象

如何实现Swiper组件在删除数据时切换到前一个元素而非第一个？切换时的动画怎么实现？
 
 

#### 背景知识

- 使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)管理一个可以横滑切换的组件，发现在删除列表数据时Swiper会默认切到第一个元素。
- [pop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array#pop)从ArkTS Array中移除并返回最后一个元素。可以支持转场动画。[push](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array#push)在ArkTS Array的末尾添加元素，并返回新的Array长度。
- [showNext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#shownext)和[showPrevious](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#showprevious)方法分别可以使Swiper在数据源变化时翻至下一页和翻至上一页。翻页带动效切换过程，时长通过Swiper的duration属性设置。

 
 

#### 解决方案

- 场景一：实现Swiper组件在删除数据时切换到前一个元素而非第一个，无切换动画。

  通过绑定index属性，该属性支持通过$$双向绑定变量，使用数组管理Swiper的数据，删除操作通过pop()方法来实现。Swiper默认在数据源变化时会重置到第一个元素，需通过控制器强制指定目标位置。
```text
@Entry
@Component
struct SwiperDeletesDataToPreviousElementOne {
  private swiperController: SwiperController = new SwiperController();
  @State data: number[] = [];
  @State total: number = 2;
  @State index: number = 0;

  aboutToAppear(): void {
    for (let i = 0; i <= this.total; i++) {
      this.data.push(i);
    }
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        ForEach(this.data, (item: number) => {
          Text((item + 1) + '')
            .width('90%')
            .height(160)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .index($$this.index) <em>// </em><em>绑定索引状态变量</em>
      .indicator(Indicator.digit()
        .top(200)
        .fontColor(Color.Gray)
        .selectedFontColor(Color.Gray)
        .digitFont({ size: 20, weight: FontWeight.Bold })
        .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
      .displayArrow(true, false)
      .cachedCount(3)
      .loop(false);

      Row({ space: 10 }) {
        Button('Add').onClick(() => {
          this.data.push(++this.total);
          this.index = this.total; <em>// 修改索引，触发UI更新</em>
        });
        Button('Remove').onClick(() => {
          this.data.pop();
          this.index -= 1; <em>// </em><em>修改索引，触发UI更新</em>
        });
      };
    }
    .width('100%')
    .margin({ top: 5 });
  }
}
```


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/dpIP7reyRCeTRh4bqJ-upg/zh-cn_image_0000002658791415.png?HW-CC-KV=V1&HW-CC-Date=20260701T041249Z&HW-CC-Expire=86400&HW-CC-Sign=70C2E571ABDC1B4BE8C708EC42D8EA2AE3D63518D9D889675723D80CBAEF9E08)

- 场景二：实现Swiper组件在删除数据时切换到前一个元素而非第一个，有切换动画。

  可以通过使用Swiper组件的showNext和showPrevious方法解决，翻页默认带动效。
```text
@Entry
@Component
struct SwiperDeletesDataToPreviousElementTwo {
  private swiperController: SwiperController = new SwiperController();
  @State data: number[] = [];
  @State total: number = 2;
  index: number = 0;

  aboutToAppear(): void {
    for (let i = 0; i <= this.total; i++) {
      this.data.push(i);
    }
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        ForEach(this.data, (item: number) => {
          Text((item + 1) + '')
            .width('90%')
            .height(160)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .index($$this.index)<em> </em><em>// 绑定索引状态变量</em>
      .indicator(Indicator.digit()
        .top(200)
        .fontColor(Color.Gray)
        .selectedFontColor(Color.Gray)
        .digitFont({ size: 20, weight: FontWeight.Bold })
        .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
      .displayArrow(true, false)
      .cachedCount(3)
      .loop(false);

      Row({ space: 10 }) {
        Button('Add').onClick(() => {
          this.data.push(this.total++);
          this.swiperController.showNext();
        });
        Button('Remove').onClick(() => {
          this.data.pop();
          this.swiperController.showPrevious();
        });
      };
    }
    .width('100%')
    .margin({ top: 5 });
  }
}
```


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/PWQxazXqRliPgMb-IVucRA/zh-cn_image_0000002628552030.png?HW-CC-KV=V1&HW-CC-Date=20260701T041249Z&HW-CC-Expire=86400&HW-CC-Sign=9132FACC144F7D58C8DBB7FF99A411C37F27EA0E2B5D79F429BAB259CFB003DB)
