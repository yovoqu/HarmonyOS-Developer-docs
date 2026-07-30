# 获取ListItem组件的高度问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-584

#### 问题现象

**场景一**：想要实现在滑动距离到List底部一定高度时就加载更多，此时想要获取ListItem距离底部的高度，是否有什么方式可以实现？
 
**场景二**：假如List的高度设置了200vp，但当里面ListItem的高度大于200vp时，就会发生滚动，此时有什么方法或者事件可以获取内部ListItem的总高度呢？
 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)是很常用的滚动类容器组件，一般和子组件[ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)一起使用，List列表中的每一个列表项对应一个ListItem组件。List组件通常需要搭配如ForEach组件对ListItem组件进行循环渲染。
- List组件提供了[onScrollIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#onscrollindex)方法：列表滑动时触发，返回值分别为滑动起始位置索引值与滑动结束位置索引值。
- 组件区域变化事件[onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)可以在组件显示的尺寸、位置等发生变化时触发，获取相关参数。

 
 

#### 解决方案

- **场景一**：可以通过使用onScrollIndex方法来实现，在加载最后一个item之前发请求拿新数据。
```text
<em>// </em><em>模拟分页数据</em>
export class ListDataOne {
  data: Array<string> = [];
  totalCount: number = 100;

  constructor() {
    for (let index = 0; index < this.totalCount; index++) {
      this.data.push(index.toString());
    }
    console.info('data', `${this.data}`);
  }

  getData(page: number, pageSize: number) {
    let startIndex = (page - 1) * pageSize;
    return this.data.slice(startIndex, startIndex + pageSize);
  }
}

@Entry
@Component
struct GetTheHeightOfTheListItemOne {
  @State arr: Array<string> = [];
  @State page: number = 1;
  pageSize = 5;

  aboutToAppear(): void {
    let listData = new ListDataOne();
    let list = listData.getData(this.page, this.pageSize);
    list.forEach(item => {
      this.arr.push(item);
    });
  }

  build() {
    RelativeContainer() {
      List() {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(item.toString());
          }
          .height(200)
          .width(120)
          .margin({ bottom: 5 })
          .backgroundColor('#ace')
          .borderRadius(10);
        });
      }
      .alignListItem(ListItemAlign.Center)
      .cachedCount(2)
      .onScrollIndex((start: number, end: number, center: number) => {
        <em>// 加载最后一个item之前发请求拿新数据</em>
        if (end === this.page * this.pageSize - 1) {
          this.page++;
          let listData = new ListDataOne();
          let list = listData.getData(this.page, this.pageSize);
          list.forEach(item => {
            this.arr.push(item);
          });
          console.info('arr', `${this.arr}`);
        }
        console.info(`start ${start}`);
        console.info(`center ${center}`);
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/PZu9X3ThQlWzOBH6W5JMag/zh-cn_image_0000002628552386.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=D0A6DA064514CBFE44D5E28E6BFF71B7F8016B85D1815161F5CDB155279F7EFD)

- **场景二**：要想获取ListItem的总高度，可以通过获取List中每一个ListItem组件的高度，然后将所有高度进行相加。
```text
@Entry
@Component
struct GetTheHeightOfTheListItemTwo {
  @State list: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];
  @State isFlag: boolean = false;

  build() {
    Column() {
      List() {
        ForEach(this.list, (item: string, index: number) => {
          ListItem() {
            Text(item)
              .width('100%')
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .fontSize(30)
              .onAreaChange((newValue: Area) => {
                if (!this.isFlag) {
                  console.info(`${newValue.height}`); <em>// </em><em>获取每一个组件的高度</em>
                  console.info(`length  ${this.list.length}`); <em>// </em><em>获取总共有多少个组件</em>
                  console.info(`index ${index} -- ${newValue.height}`); <em>// </em><em>获取每个组件</em>
                  this.isFlag = !this.isFlag;
                  console.info(`sum: ${Number(newValue.height) * this.list.length}`);
                }
              });
          };
        }, (item: string) => item);
      }
      .width('100%')
      .backgroundColor('#DCDCDC')
      .height(200);
    }
    .width('100%')
    .height('100%');
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/gny8vZeFSOCt9FF5291MGA/zh-cn_image_0000002628392496.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=6812656768B9722E364A9F54E58F95BD1FCEFFDFE0E0D1453EDAB4F420696480)


  总共有12个组件，每个组件的高度是35，总和为420。

 
 

#### 常见FAQ

Q：有什么方法可以获取网页内容的高度呢？
 
A：可以参考官方文档[获取网页内容高度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-getpage-height)。
