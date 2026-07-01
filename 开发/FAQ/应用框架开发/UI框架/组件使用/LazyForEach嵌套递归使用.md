# LazyForEach嵌套递归使用

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1015

## LazyForEach嵌套递归使用
 


##### 问题现象

树形结构列表如何高效渲染？
 
 
- 数据量规模较大（4000+），如何保证页面渲染速度？
- 结构多层嵌套，且层级深度不确定，如何遍历数据并绘制界面？

 

##### 背景知识

- [LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件，可以保证数据加载以及绘制的流畅度，提升使用体验。
- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。它适合用于高效地显示结构化、可滚动的信息。

 
 

##### 解决方案

通过递归的形式，按层级实现每一个子树，最后组合为完整的树形结构列表。
 
- 单个层级实现：使用LazyForEach组件按需加载当前层级的数据，避免一次性渲染所有数据，提升性能。
- 多层级实现：
通过递归的方式遍历数据，动态生成子层级的树形结构。
- 每个层级的LazyForEach组件需嵌套在List容器中，且List容器需设置固定高度或使用constraintSize属性限制高度，以确保懒加载机制生效。

 - 性能优化：
当数据量较大时，使用cachedCount属性控制懒加载的缓冲区大小，提升渲染效率。
- 使用constraintSize属性限制层级高度，避免无限拉伸影响用户体验。

 
 
示例代码如下：
 
- 主逻辑代码：
使用aboutToAppear生命周期钩子生成模拟数据。
- 使用自定义递归函数Node遍历数据，每次递归使用LazyForEach组件渲染当前层级的数据项。
- 通过点击事件控制子层级的展开与折叠。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/m3Sdd3bRTyOK6ltdecizBA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025556Z&HW-CC-Expire=86400&HW-CC-Sign=671933D7FCB1005FBE5091FC69F83D6E83CE1E16BEECD142B28BFED4B97DC58D)
 

引用的数据类型参考后续“2.数据类型生成”。
 

 
```text
import { LazyDataSource, TreeData } from './LazyDataSource';


@Entry
@Component
struct Index {
  @State selections: boolean[] = []; // 各层级选中id
  result: ArrayTreeData> = [];
  @State treeData: LazyDataSourceTreeData> = new LazyDataSource();

  aboutToAppear(): void {
    // 准备数据
    let levelOneOneData = [
      new TreeData('11', '1', '层级-1-1', 2),
      new TreeData('12', '1', '层级-1-2', 2),
    ];
    for (let i = 3; i = 4000; i++) {
      levelOneOneData.push(new TreeData('1' + i, '1', '层级-1-' + i, 2));
    }
    let levelOneTwoData = [
      new TreeData('21', '2', '层级-2-1', 2),
    ];
    let levelOneTwoTwoData = [
      new TreeData('221', '22', '层级-2-2-1', 3),
    ];
    for (let i = 2; i = 4000; i++) {
      levelOneTwoTwoData.push(new TreeData('22' + i, '22', '层级-2-2-' + i, 3));
    }
    let levelOneTwoTwoTree: LazyDataSourceTreeData> = new LazyDataSource();
    let levelOneOneTree: LazyDataSourceTreeData> = new LazyDataSource();
    let levelOneTwoTree: LazyDataSourceTreeData> = new LazyDataSource();
    levelOneTwoTwoTree.dataArray = levelOneTwoTwoData;
    levelOneTwoData.push(new TreeData('22', '2', '层级-2-2', 2, levelOneTwoTwoTree));
    levelOneOneTree.dataArray = levelOneOneData;
    this.result = [
      new TreeData('1', '0', '层级-1', 1, levelOneOneTree)
    ];
    levelOneTwoTree.dataArray = levelOneTwoData;
    this.result.push(new TreeData('2', '0', '层级-2', 1, levelOneTwoTree));
    this.result.push(new TreeData('3', '0', '层级-3', 1));
    this.result.push(new TreeData('4', '0', '层级-4', 1));
    this.treeData.dataArray = this.result;
    this.treeData.notifyDataReload();
  }

  // 构建并根据是否展开绘制子节点
  @Builder
  Node(node: LazyDataSourceTreeData>, index: number) {
    Column() {
      List() {
        LazyForEach(node, (item: TreeData) => {
          ListItem() {
            Column() {
              Text(item.name + (item.childList ? (this.selections[item.id] ? '-' : '+') : ''))
                .width('100%')
                .fontSize(16)
                .margin({ left: 40 * index })
                .textAlign(TextAlign.Center)
                .backgroundColor(0xFFFFFF)
                .textAlign(TextAlign.Start)
                .onClick(() => {
                  const isSelection: boolean = this.selections[item.id];
                  if (isSelection) {
                    this.selections[item.id] = false;
                  } else {
                    this.selections[item.id] = true;
                  }
                });
              if (item.childList && this.selections[item.id]) {
                this.Node(item.childList, index + 1);
              }
            }
            .margin(5);
          };
        });
      }
      .cachedCount(20)
      .constraintSize({ maxHeight: node.totalCount() > 50 ? 400 : '100%' });
    };
  }

  build() {
    Column() {
      this.Node(this.treeData, 0);
    }
    .width('100%')
    .height('100%')
    .margin({ left: 20 });
  }
}
```
 - 数据类型生成：
自定义数据数组类型：
```text
// 自定义数据数组类型
@Observed
export class ObservedArrayT> extends ArrayT> {
  constructor(args?: T[]) {
    if (args instanceof Array) {
      super(...args);
    } else {
      super();
    }
  }
}
```

- LazyForEach基础数据继承类：
```text
// LazyForEach基础数据继承类
export class BasicDataSourceT> implements IDataSource {
  private listeners: DataChangeListener[] = [];

  public totalCount(): number {
    return 0;
  }

  public getData(index: number): T | undefined {
    console.warn(`Cannot read ${index}, please override getDate`);
    return undefined;
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener)  0) {
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }
}
```

- LazyForEach数据源类：
```text
//  LazyForEach数据源类
export class LazyDataSourceT> extends BasicDataSourceT> {
  dataArray: T[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): T {
    return this.dataArray[index];
  }

  public addData(index: number, data: T): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public pushData(data: T): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

  public pushArrayData(newData: ObservedArrayT>): void {
    this.clear();
    this.dataArray.push(...newData);
    this.notifyDataReload();
  }

  public pushDataPositionArray(index: number, newData: ObservedArrayT>): void {
    this.dataArray.splice(index, 0, ...newData);
    this.notifyDataReload();
  }

  public appendArrayData(addData: ObservedArrayT>): void {
    this.dataArray.push(...addData);
    this.notifyDataReload();
  }

  public deleteData(index: number): void {
    this.dataArray.splice(index, 1);
    this.notifyDataDelete(index);
  }

  public getDataList(): ObservedArrayT> {
    return this.dataArray;
  }

  public clear(): void {
    this.dataArray.splice(0, this.dataArray?.length);
  }

  public isEmpty(): boolean {
    return this.dataArray.length === 0;
  }
}
```

- 数据对象：
```text
// 数据对象
export class TreeData {
  id: string;
  parentId: string;
  name: string;
  level: number;
  childList?: LazyDataSourceTreeData>;

  constructor(id: string, parentId: string, name: string, level: number,
    childList?: LazyDataSourceTreeData>) {
    this.id = id;
    this.parentId = parentId;
    this.name = name;
    this.level = level;
    this.childList = childList;
  }
}
```


 
 
 

##### 总结

- LazyForEach需要关注[使用限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach#使用限制)。
- 相关UI界面限制，使用通用constraintSize配置，防止数据组件过多，降低交互性。
