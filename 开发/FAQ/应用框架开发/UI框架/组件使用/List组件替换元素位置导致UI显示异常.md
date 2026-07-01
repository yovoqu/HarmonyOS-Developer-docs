# List组件替换元素位置导致UI显示异常

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1281

## List组件替换元素位置导致UI显示异常
 


##### 问题现象

List组件替换元素位置导致UI显示异常，功能类似于歌曲置顶效果，问题代码示例参考如下：
 
```ArkTS
// Index.ets
import { JSON, util } from '@kit.ArkTS';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: string;
  icon: Resource;

  constructor(name: string, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
struct Index {
  @State private contacts: Array = [
    new Contact('小明', $r("app.media.startIcon")),
    new Contact('小红', $r("app.media.startIcon")),
    new Contact('小黑', $r("app.media.startIcon")),
    new Contact('小黄', $r("app.media.startIcon")),
    new Contact('小绿', $r("app.media.startIcon")),
  ];

  build() {
    Column({ space: 10 }) {
      List() {
        ForEach(this.contacts, (item: Contact, index: number) => {
          ListItem() {
            Row() {
              Image(item.icon)
                .width(40)
                .height(40)
                .margin(10)
              Text(item.name).fontSize(20)
            }
            .width('100%')
            .justifyContent(FlexAlign.Start)
          }.onClick(() => {
            // 将对应位置的元素移至首位
            if (this.contacts.length > 0) {
              const movedItem = this.contacts.splice(index, 1);
              this.contacts.unshift(movedItem) 
            }
          })
        }, (item: Contact) => JSON.stringify(item))
      }
      .width('100%')
    }
  }
}
```
 
实现类似于歌曲置顶操作，点击元素后，该元素从原位置消失但未正确显示在顶部，异常效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/9h66tY3eTI6rAsn2tBf4KA/zh-cn_image_0000002658837239.png?HW-CC-KV=V1&HW-CC-Date=20260701T025608Z&HW-CC-Expire=86400&HW-CC-Sign=87A801C5D644EABD357EC3B170E310E0F43671AEEF11BA09721430CFB98A1CD2)

 
 

##### 效果预览

实现效果，点击任意非首位元素，该元素即可实现置顶，其余元素顺次往下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/TkAIctNKSauT-RT6ydkD9A/zh-cn_image_0000002628597974.png?HW-CC-KV=V1&HW-CC-Date=20260701T025608Z&HW-CC-Expire=86400&HW-CC-Sign=8A5ADCBC9B7F44F850F976BA68EF40D3E2D2F5044226FFD9B984286D4F9A3D45)

 
 

##### 背景知识

- [splice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array#splice)：删除Array中指定位置的元素，需要时在Array的指定位置插入新元素。
- [unshift](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array#unshift)：在ArkTS Array的首端插入一个或多个元素，并返回新的Array长度。

 
 

##### 问题定位

根据问题现象以及代码分析可知删除元素操作实现了UI刷新，但新增元素未能实现UI刷新。
 
 

##### 分析结论

调试发现点击事件中代码行：this.contacts.unshift(movedItem)未能实现UI刷新，movedItem类型为Object。调试将movedItem更改为自定义class类型可以实现UI刷新。
 
 

##### 修改建议

修改参数contacts的类型为Array&lt;Contact&gt;，由于splice方法返回值为数组类型，而unshift的入参为数组中元素类型。因此需要取splice方法返回数组的首项值，代码修改如下：
 
```text
import { JSON, util } from '@kit.ArkTS';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: string;
  icon: Resource;

  constructor(name: string, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
struct Index {
  @State private contacts: Array = [
    new Contact('小明', $r('app.media.startIcon')),
    new Contact('小红', $r('app.media.startIcon')),
    new Contact('小黑', $r('app.media.startIcon')),
    new Contact('小黄', $r('app.media.startIcon')),
    new Contact('小绿', $r('app.media.startIcon')),
  ];

  build() {
    Column({ space: 10 }) {
      List() {
        ForEach(this.contacts, (item: Contact, index: number) => {
          ListItem() {
            Row() {
              Image(item.icon)
                .width(40)
                .height(40)
                .margin(10)
              Text(item.name).fontSize(20)
            }
            .width('100%')
            .justifyContent(FlexAlign.Start)
          }.onClick(() => {
            // 将对应位置的元素移至首位
            if (this.contacts.length > 0) {
              const movedItem = this.contacts.splice(index, 1);
              this.contacts.unshift(movedItem[0]);
            }
          })
        }, (item: Contact) => JSON.stringify(item))
      }
      .width('100%')
    }
  }
}
```
