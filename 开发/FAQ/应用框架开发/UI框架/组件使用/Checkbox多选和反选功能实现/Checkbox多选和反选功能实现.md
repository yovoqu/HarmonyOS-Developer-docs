# Checkbox多选和反选功能实现

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1505

#### 问题现象

场景一：ArkUI中是否提供内置的一键反选功能的控件？
 
场景二：如何实现多选，并获取当前用户选择Checkbox的值？
 
 

#### 背景知识

- [Checkbox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox)多选框组件，它允许用户从一系列选项中选择多个项。无论是电子商务网站上的商品筛选，还是在线表单的数据收集，Checkbox都发挥着重要作用。
- 反选是指将当前所有已选中的Checkbox变为未选中状态，同时将所有未选中的Checkbox变为选中状态。
- [CheckboxGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup)：多选框群组，用于控制多选框全选或者不全选状态。

 
 

#### 解决方案

- **场景一**：目前Checkbox暂无内置一键反选的能力，可通过反转每一项中绑定于Checkbox的select属性的参数的状态值，实现变更Checkbox的选中状态，并利用响应式数据绑定自动更新界面以实现一键反选功能。
```json
@ObservedV2
class Person {
<em>  // 控制Checkbox的选中状态</em>
  @Trace public name: boolean;
  public value: number;

  constructor(name: boolean, value: number) {
    this.name = name;
    this.value = value;
  }
}

@ObservedV2
class Info {
  personList: Person[] = [];

  constructor() {
    this.personList = [new Person(false, 0), new Person(false, 1), new Person(false, 2)];
  }
}

@Entry
@Component
struct CheckboxPage {
  info: Info = new Info();

  build() {
    Column() {
      Row() {
        Text('反选');
      }
      .onClick(() => {
    <em>    // 反转Checkbox的选中状态，实现反选</em>
        for (let i = 0; i < this.info.personList.length; i++) {
          this.info.personList[i].name = !this.info.personList[i].name;
        }
      });

      List({ space: 0, initialIndex: 0 }) {
        ForEach(this.info.personList, (item: Person) => {
          ListItem() {
            Flex() {
              Checkbox({ name: item.value.toString() })
                .selectedColor('#027cff')
                .shape(CheckBoxShape.ROUNDED_SQUARE)
                .unselectedColor('#027cff')
                .select(item.name)
                .onChange((value: boolean) => {
             <em>     // 记录当前Checkbox的选中状态</em>
                  item.name = value;
                })
                .width(18)
                .height(18);
              Text(item.value.toString()).fontSize(15).margin({ top: 5 });
            };
          };
        }, (item: Person) => JSON.stringify(item));
      };
    }
    .width('100%')
    .height('100%')
    .margin({ top: 50 })
    .padding({ left: 24, right: 24 });
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/40M1HCKpR62bAtKYtrnPbg/zh-cn_image_0000002658965763.png?HW-CC-KV=V1&HW-CC-Date=20260730T072406Z&HW-CC-Expire=86400&HW-CC-Sign=9AE618400EFEC768D04F5ADB3D9659E730AB2057B6FAB15D08CB841534DACE9C)


 
- **场景二**：通过Checkbox的onChange方法对选中数据进行处理。
```json
class CheckName {
  public id: string;
  public productName: string;

  constructor(id: string, productName: string) {
    this.id = id;
    this.productName = productName;
  }
}

@Entry
@Component
struct CheckboxExample {
  @State services: CheckName[] = [
    new CheckName('1', 'checkbox1'),
    new CheckName('2', 'checkbox2'),
    new CheckName('3', 'checkbox3'),
    new CheckName('4', 'checkbox4'),
  ];
  @State clickIndex: string = '';
  @State clickName: string = '';
  @State selectIndexList: Array<string> = [];

  build() {
    Scroll() {
      Column() {
     <em>   // 全选按钮</em>
        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
          CheckboxGroup({ group: 'checkboxGroup' })
            .selectedColor('#007DFF')
            .onChange((itemName: CheckboxGroupResult) => {
              console.info('checkbox group content' + JSON.stringify(itemName));
            });
          Text('Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
        }.width('auto');

        ForEach(this.services, (item: CheckName) => {
          Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
            Checkbox({ name: item.productName, group: 'checkboxGroup' })
              .selectedColor('#007DFF')
              .onChange((value: boolean) => {
                this.clickIndex = item.id;
                this.clickName = item.productName;
                if (value == true) {
                  this.selectIndexList.push(item.productName);
                } else {
                  this.selectIndexList = this.selectIndexList.filter((element) => {
                    return element !== item.productName;
                <em>    // 返回不等于要删除元素的元素构成新数组</em>
                  });
                }
              });
            Text(item.productName).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
          }.width('auto').margin({ left: 36 });
        }, (item: CheckName) => item.id);
        Text(this.selectIndexList.toString())
          .fontSize(14)
          .lineHeight(20)
          .fontColor('#182431')
          .fontWeight(500)
          .alignSelf(ItemAlign.Center);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    };
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/DypLTRtbRvmR1p0lQ_fWYQ/zh-cn_image_0000002628606552.png?HW-CC-KV=V1&HW-CC-Date=20260730T072406Z&HW-CC-Expire=86400&HW-CC-Sign=C0A4B00D50BD5F9B7E88BCED082F60D53328CAF2EBE0DC7288269A4E0EF718A1)
