# Scroll滚动回弹获取偏移位置不准确

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1428

#### 问题现象

设置edgeEffect为Spring的时候，在onWillScroll里面监听滑动的距离，快速滑动到边缘触发物理回弹时，回调的滑动距离不为0，即使最后通过惯性回到初始状态，滑动的距离也不为0。
 
参考问题代码如下：
 
```text
@Entry
@Component
struct ScrollerTest {
  arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];


  build() {
    Scroll() {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column() {
            Text(`item${item}`)
              .fontSize(16)
              .height(90)
              .width('100%')
              .border({ width: 1 })
              .fontColor(Color.Black);
          };
        }, (item: string) => item);
      };
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .onWillScroll((offsetX: number, offsetY: number, state: ScrollState) => {
      console.info(`滚动偏移量Y:${offsetY.toString()},X:${offsetX.toString()},state:${state.toString()}`);
    })
    .backgroundColor(Color.White)
    .width('100%')
    .height('100%');
  }
}
```
 
滚动到边缘无法判定为0，现象如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/owNecs7wSJOIdCNGp3bhzQ/zh-cn_image_0000002628763648.png?HW-CC-KV=V1&HW-CC-Date=20260730T072400Z&HW-CC-Expire=86400&HW-CC-Sign=B308ECE05AD879EE1662D45493C2D44D573E7E422E2B723364185B767A6D7087)

 
 

#### 背景知识

[onWillScroll事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onwillscroll12)：滚动事件回调，Scroll滚动前触发。该事件能回调组件下一步将要滚动的偏移量、当前滚动状态以及滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。
 
 

#### 问题定位

onWillScroll是滚动前触发的事件，滑动到边缘，触发弹性回弹也会触发该事件。也就是说最后打印的滚动位置信息是滑动停止后的前一帧位置到最后停止位置将要滑动的距离。最后打印的信息也就不为0。
 
延伸知识：当edgeEffect为None的时候能打印出0的原因是滑动组件不滑动的时候也能触发onWillScroll事件。意思是不滚动时，上下滑动滚动组件，将要偏移0。
 
设置edgeEffect为None，效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/oOKg8lcrRHiykQ90vCFFhA/zh-cn_image_0000002658962963.png?HW-CC-KV=V1&HW-CC-Date=20260730T072400Z&HW-CC-Expire=86400&HW-CC-Sign=9E630B7355E8124F0D6965C0818C2C98428A3D3EE3CE5695E77386A8452ACC27)

 
 

#### 分析结论

onWillScroll是滚动前触发的事件，不是滚动时或滚动后触发的事件，所以，在edgeEffect为Spring的时候，以onWillScroll事件的偏移量为0作为判定滚动组件滚动到边缘的条件会失效。
 
 

#### 修改建议

- 方案一：采用[onDidScroll事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#ondidscroll12)判定是否滚动到边缘，当偏移量为0时代表滚动到边缘。
```text
@Entry
@Component
struct OptionOne {
  arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];


  build() {
    Scroll() {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column() {
            Text(`item${item}`)
              .fontSize(16)
              .height(90)
              .width('100%')
              .border({ width: 1 })
              .fontColor(Color.Black);
          };
        }, (item: string) => item);
      };
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .onDidScroll((offsetX: number, offsetY: number, state: ScrollState) => {
      console.info(`滚动偏移量Y:${offsetY.toString()},X:${offsetX.toString()},state:${state.toString()}`);
    })
    .backgroundColor(Color.White)
    .width('100%')
    .height('100%');
  }
}
```


  效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/P7QS7z7jSSqmTQbx1LtwCA/zh-cn_image_0000002628603748.png?HW-CC-KV=V1&HW-CC-Date=20260730T072400Z&HW-CC-Expire=86400&HW-CC-Sign=5C08079874D679CFE5611EB537984D585C14D69709F60B146806F3758754F44C)

- 方案二：通过[onScrollEdge事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onscrolledge)与[onScrollStop事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onscrollstop9)判定是否滚动到边缘并停止：
```text
@Entry
@Component
struct OptionTwo {
  arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];


  build() {
    Scroll() {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column() {
            Text(`item${item}`)
              .fontSize(16)
              .height(90)
              .width('100%')
              .border({ width: 1 })
              .fontColor(Color.Black);
          };
        }, (item: string) => item);
      };
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .onScrollEdge(() => {
      console.info('To the top');
    })
    .onScrollStop(() => {
      console.info('Scroll Stop');
    })
    .backgroundColor(Color.White)
    .width('100%')
    .height('100%');
  }
}
```


  效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/g-XO_fkZTMeZcyL9h-8a-Q/zh-cn_image_0000002658843015.png?HW-CC-KV=V1&HW-CC-Date=20260730T072400Z&HW-CC-Expire=86400&HW-CC-Sign=8F0D1A7FC3C876F3BEDA90681EC49C671BF8A908ED7ED5489DEAB40A9F4DC98A)
