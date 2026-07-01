# 动态生成多个CheckboxGroup并设置全选

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1267

#### 问题现象

如何动态生成多个CheckboxGroup并设置其全选？
 
 

#### 背景知识

[Checkbox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox)多选框组件，通常用于某选项的打开或关闭。[CheckboxGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup)多选框群组，用于控制多选框全选或者不全选状态。多组CheckboxGroup要设置不同的群组名称，多个相同群组名称的CheckboxGroup，仅第一个CheckboxGroup生效。
 
 

#### 解决方案

- 可以将需要展示的数据源整理成类似格式，根据数据源动态生成多组CheckboxGroup，用boolean类型的数组保存每个CheckboxGroup的状态，用来刷新选择框的选择状态，参考示例代码如下：
```json
interface DataModel {
  groupName: string;
  items: string[];
  selectAll: boolean;
}

@Entry
@Component
struct CheckboxGroupExample {
  <em>// 数据源</em>
  groups: Array<DataModel> = [
    { groupName: '第一章', items: ['1.1', '1.2', '1.3', '1.4'], selectAll: false },
    { groupName: '第二章', items: ['2.1', '2.2', '2.3'], selectAll: false }
  ];
  @State groupSelect: boolean[] = [false, false]; <em>// 每个CheckBoxGroup选择状态</em>
  @State selectAll: boolean = false; <em>// 全选按钮的状态</em>
  @State selectItem: Array<Array<string>> = [[], []]; <em>// 保存已选的数据</em>

  @Builder
  createGroup(data: DataModel, index: number) {
    Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
      CheckboxGroup({ group: data.groupName })
        .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
        .selectedColor('#007DFF')
        .selectAll(this.groupSelect[index])
        .onChange((event: CheckboxGroupResult) => {
          this.groups[index].selectAll = (event.status === SelectStatus.All);

          this.selectAll = true;
          for (let item of this.groups) {
            this.selectAll = (this.selectAll && item.selectAll);
          }
       <em>   // 保存当前分组所选数据</em>
          this.selectItem[index] = event.name;
        });
      Text(data.groupName).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
    };

    ForEach(data.items, (item: string) => {
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        Checkbox({ name: item, group: data.groupName })
          .selectedColor('#007DFF')
          .shape(CheckBoxShape.ROUNDED_SQUARE)
          .onChange((value: boolean) => {
            console.info(`Checkbox1 change is ${value}`);
          });
        Text(item).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
      }.margin({ left: 36 });
    }, (item: string) => item);
  }

  build() {
    Column() {
      ForEach(this.groups, (item: DataModel, index: number) => {
        this.createGroup(item, index);
      }, (item: DataModel) => JSON.stringify(item));
      Flex({ alignItems: ItemAlign.Center }) {
        Checkbox({ name: '全选' })
          .select(this.selectAll)
          .selectedColor('#007DFF')
          .shape(CheckBoxShape.ROUNDED_SQUARE)
          .onClick(() => {
          <em>  // 点击全选按钮，改变每个CheckBoxGroup选择状态</em>
            this.selectAll = !this.selectAll;
            for (let i = 0; i < this.groupSelect.length; i++) {
              this.groupSelect[i] = !this.groupSelect[i];
              this.groupSelect[i] = this.selectAll;
            }
          });
        Text('全选');
      };

      Text(`当前所选数据${this.selectItem}`);
    }
    .padding(16);
  }
}
```
 效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/_c3D34FrTMeOGOgDAkp3AQ/zh-cn_image_0000002658955329.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041259Z&HW-CC-Expire=86400&HW-CC-Sign=6A1E0011935868009ED7EC15D67169B680299E8C9EB261750C21C9C4F55A7F3C)

- CheckboxGroup还可以和List组件组合使用，点击“全选”后实现全部选中，参考示例代码如下：
```text
@Entry
@Component
struct Index {
  @State dataList: string[] = [];
  @State selectedItemInGroup: boolean = false;<em> // group是否存在被选中item</em>
  @State notSelectedItemInGroup: boolean = true;<em> // group是否存在未被选中item</em>

  aboutToAppear(): void {
    for (let i = 0; i < 300; i++) {
      this.dataList.push(i + '');
    }
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Row() {
          CheckboxGroup({ group: 'checkboxGroup' })
            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
            .selectedColor(Color.Orange)
            .onChange((itemName: CheckboxGroupResult) => {
              console.info(`checkbox itemName.status:${itemName.status}`);
             <em> // 关键代码</em>
              if (itemName.status === SelectStatus.All) {
                this.selectedItemInGroup = true;
                this.notSelectedItemInGroup = false;
              } else if (itemName.status === SelectStatus.None) {
                this.notSelectedItemInGroup = true;
                this.selectedItemInGroup = false;
              }
              console.info(`checkbox group content: ${itemName}`);
            })
            .mark({
              strokeColor: Color.Black,
              size: 40,
              strokeWidth: 5
            })
            .unselectedColor('#39a2db')
            .width(30)
            .height(30);
          Text('Select All').fontSize(20);
        };

        List({ space: 20 }) {
          ForEach(this.dataList,
            (item: string, index: number) => {
              ListItem() {
                Row() {
                  Checkbox({ name: 'checkbox' + index, group: 'checkboxGroup' })
                    .selectedColor('#39a2db')
                    .select(this.selectedItemInGroup)
                    .shape(CheckBoxShape.ROUNDED_SQUARE)
                    .onChange((value: boolean) => {
                      console.info(`Checkbox ${index} change is ${value}`);
                    })
                    .mark({
                      strokeColor: Color.Black,
                      size: 50,
                      strokeWidth: 5
                    })
                    .unselectedColor('#ffbebebe')
                    .width(30)
                    .height(30);
                  Text('Checkbox' + index).fontSize(20);
                };
              }
              .backgroundColor(Color.White);
            }
          );
        }
        .cachedCount(100)
        .layoutWeight(1);
      }
      .padding(16)
      .height('100%')
      .alignItems(HorizontalAlign.Start);
    }
    .height('100%');
  }
}
```
 效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/8XZNk6XdTwu-3T66IJWHRg/zh-cn_image_0000002628596112.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041259Z&HW-CC-Expire=86400&HW-CC-Sign=DB76F7E70C4DCF644738A0A45F49AE59E3D0D577B489344E729D348723DF8494)
