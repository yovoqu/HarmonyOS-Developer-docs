# 如何用Progress组件显示任务列表进度

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-795

#### 问题现象

使用Progress进度条组件展示任务进度时出现问题：
 1. 总任务数5，已完成任务数3，此时删除一条已完成的任务，进度条先增长再减少。这个问题是什么原因导致的，如何解决？问题代码如下：

  
```text
@Entry
@Component
struct TaskListPage1 {
  @State finishedTask: number = 0; <em>// 已完成任务数</em>
  @State totalTask: number = 0; <em>// 总任务数</em>
  @State tasks: TaskInfo[] = []; <em>// 任务列表</em>
  @State deleteButtonBgcolor: string | Color = '#E84026'; <em>// 删除按钮的颜色</em>


 <em> // 删除任务按钮</em>
  @Builder
  DeleteTask(index: number) {
    Stack() {
      Image($r('app.media.ic_public_trash'))<em> // 删除图标，可以更换其他资源</em>
        .draggable(false)
        .width(20);
    }
    .width(40)
    .height(40)
    .borderRadius('50%')
    .margin({ left: 16 })
    .backgroundColor(this.deleteButtonBgcolor)
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type === TouchType.Down) {
          this.deleteButtonBgcolor = '#AAE84026'; <em>// 按下时图标背景颜色</em>
        } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
          this.deleteButtonBgcolor = '#E84026'; <em>// 取消或抬起恢复图标背景颜色</em>
        }
      }
    })
    .onClick(() => {
      this.tasks.splice(index, 1); <em>// 任务列表删除当前索引的任务</em>
      this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; <em>// 重新获取已完成任务数</em>
      this.totalTask = this.tasks.length; /<em>/ 获取总任务数</em>
    });
  }


  build() {
    Column() {
  <em>    // 任务进度以及新增任务按钮</em>
      TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
      //<em> 任务列表</em>
      List({ space: 8 }) {
        ForEach(this.tasks, (item: TaskInfo, index: number) => {
          ListItem() {
            TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
          }.padding({ left: 16, right: 16 })
          .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); // <em>左滑出现删除按钮</em>
        });
      }
      .layoutWeight(1)
      .width('100%')
      .scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#f1f3f5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}


// <em>任务进度组件</em>
@Component
export struct TaskProgress {
  @Link finishedTask: number;
  @Link totalTask: number;
  @Link tasks: TaskInfo[];
  taskId: number = 0;


  build() {
    Column({ space: 20 }) {
      Row() {
        Text('任务进度：')
          .fontSize(25)
          .fontWeight(FontWeight.Bold);
      <em>  // 使用Stack堆叠容器，将进度条和进度展示层叠显示</em>
        Stack() {
        <em>  // Start solution1</em>
          Progress({
            value: this.finishedTask, <em>// 进度值，已完成数</em>
            total: this.totalTask, <em>// 进度总长，总任务数</em>
            type: ProgressType.Ring, <em>// 环形</em>
          }).width(90);
          <em>// End solution1</em>
          Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
        };
      }
      .borderRadius(10)
      .height(110)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.White)
      .width('100%');


      Button('新增任务')
        .width('60%')
        .onClick(() => {
          this.tasks.push(new TaskInfo(this.taskId++, false));
          this.totalTask = this.tasks.length;
        });
    }.width('100%');
  }
}


<em>// 任务项组件</em>
@Component
export struct TaskItem {
  @State item: TaskInfo = new TaskInfo(0, false);
  @Link finishedTask: number;
  @Link tasks: TaskInfo[];


  build() {
    Row() {
      Text(`ID:${this.item.id}`).fontSize(16);
      Checkbox()
        .width(30)
        .shape(CheckBoxShape.CIRCLE)
        .select(this.item.isFinished)
        .onClick(() => {
          if (this.item.isFinished === true) {
            this.finishedTask--;
          } else {
            this.finishedTask++;
          }
          this.item.isFinished = !this.item.isFinished;
        });
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .borderRadius(20)
    .padding({ left: 20, right: 20 })
    .backgroundColor(Color.White)
    .height(56)
    .width('100%');
  }
}


<em>// 任务信息，id和完成情况</em>
export class TaskInfo {
  id: number;
  isFinished: boolean;


  constructor(id: number, isFinished: boolean) {
    this.id = id;
    this.isFinished = isFinished;
  }
}
```


  现象效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/WoHIbE6wREOyLTIVZhp8Eg/zh-cn_image_0000002658916951.png?HW-CC-KV=V1&HW-CC-Date=20260811T005813Z&HW-CC-Expire=86400&HW-CC-Sign=823C4D86BD18EF1C6532A65E618D34F83F09676EC2A7285E17CD344570CBA0E6)

2. 在问题一的场景中，删除任务后，如何实现进度条从0平滑增长到当前进度的动画效果？
 
 

#### 背景知识

[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)是进度条显示组件，显示内容为目标操作的当前进度。当进度条组件的样式[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress#style8)中enableSmoothEffect设置为true时（默认为true），表示开启平滑动效，进度值[value](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress#value)变化时会产生动画效果。
 
 

#### 解决方案

- **问题一****问题原因**：当删除一个任务项时会修改进度条当前进度值value和进度总长total，当前问题中的情况是3/5改为2/4。默认情况下Progress组件修改total不会产生动画效果，修改value才会展示动画，所以这里的效果是3/5首先因为total变化直接渲染成3/4，再产生3/4到2/4的动画效果。

  **修改方案**：可以将Progress组件的total值设定为一个固定值，只修改value值让任务进度变化。如将进度条total值设置为100，进度值设置为(完成数/任务总数)*100，任务总数为0时单独设置进度值为0。可以避免Progress组件的total变动导致进度条先增后减。

  核心代码如下：

  
```text
Progress({
  value: this.totalTask === 0 ? 0 : (this.finishedTask / this.totalTask) * 100, <em>// 当前进度值占总进度百分比</em>
  total: 100, /<em>/ 进度总长设置固定值100</em>
  type: ProgressType.Ring, //<em> 环形</em>
}).width(90);
```
 完整代码如下：

  
```text
@Entry
@Component
struct TaskListPage1 {
  @State finishedTask: number = 0; <em>// 已完成任务数</em>
  @State totalTask: number = 0; <em>// 总任务数</em>
  @State tasks: TaskInfo[] = []; <em>// 任务列表</em>
  @State deleteButtonBgcolor: string | Color = '#E84026'; <em>// 删除按钮的颜色</em>


  <em>// 删除任务按钮</em>
  @Builder
  DeleteTask(index: number) {
    Stack() {
      Image($r('app.media.ic_public_trash')) <em>// 删除图标，可以更换其他资源</em>
        .draggable(false)
        .width(20);
    }
    .width(40)
    .height(40)
    .borderRadius('50%')
    .margin({ left: 16 })
    .backgroundColor(this.deleteButtonBgcolor)
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type === TouchType.Down) {
          this.deleteButtonBgcolor = '#AAE84026'; <em>// 按下时图标背景颜色</em>
        } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
          this.deleteButtonBgcolor = '#E84026'; <em>// 取消或抬起恢复图标背景颜色</em>
        }
      }
    })
    .onClick(() => {
      this.tasks.splice(index, 1);<em> // 任务列表删除当前索引的任务</em>
      this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; <em>// 重新获取已完成任务数</em>
      this.totalTask = this.tasks.length; <em>// 获取总任务数</em>
    });
  }


  build() {
    Column() {
    <em>  // 任务进度以及新增任务按钮</em>
      TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
      <em>// 任务列表</em>
      List({ space: 8 }) {
        ForEach(this.tasks, (item: TaskInfo, index: number) => {
          ListItem() {
            TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
          }.padding({ left: 16, right: 16 })
          .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); <em>// 左滑出现删除按钮</em>
        });
      }
      .layoutWeight(1)
      .width('100%')
      .scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#f1f3f5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}


<em>// 任务进度组件</em>
@Component
export struct TaskProgress {
  @Link finishedTask: number;
  @Link totalTask: number;
  @Link tasks: TaskInfo[];
  taskId: number = 0;


  build() {
    Column({ space: 20 }) {
      Row() {
        Text('任务进度：')
          .fontSize(25)
          .fontWeight(FontWeight.Bold);
      <em>  // 使用Stack堆叠容器，将进度条和进度展示层叠显示</em>
        Stack() {
          Progress({
            value: this.totalTask === 0 ? 0 : (this.finishedTask / this.totalTask) * 100, <em>// 当前进度值占总进度百分比</em>
            total: 100,<em> // 进度总长设置固定值100</em>
            type: ProgressType.Ring, <em>// 环形</em>
          }).width(90);
          Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
        };
      }
      .borderRadius(10)
      .height(110)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.White)
      .width('100%');


      Button('新增任务')
        .width('60%')
        .onClick(() => {
          this.tasks.push(new TaskInfo(this.taskId++, false));
          this.totalTask = this.tasks.length;
        });
    }.width('100%');
  }
}


<em>// 任务项组件</em>
@Component
export struct TaskItem {
  @State item: TaskInfo = new TaskInfo(0, false);
  @Link finishedTask: number;
  @Link tasks: TaskInfo[];


  build() {
    Row() {
      Text(`ID:${this.item.id}`).fontSize(16);
      Checkbox()
        .width(30)
        .shape(CheckBoxShape.CIRCLE)
        .select(this.item.isFinished)
        .onClick(() => {
          if (this.item.isFinished === true) {
            this.finishedTask--;
          } else {
            this.finishedTask++;
          }
          this.item.isFinished = !this.item.isFinished;
        });
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .borderRadius(20)
    .padding({ left: 20, right: 20 })
    .backgroundColor(Color.White)
    .height(56)
    .width('100%');
  }
}


/<em>/ 任务信息，id和完成情况</em>
export class TaskInfo {
  id: number;
  isFinished: boolean;


  constructor(id: number, isFinished: boolean) {
    this.id = id;
    this.isFinished = isFinished;
  }
}
```


  运行效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/BzWjGUtaSR60OF6naomdMA/zh-cn_image_0000002628397742.png?HW-CC-KV=V1&HW-CC-Date=20260811T005813Z&HW-CC-Expire=86400&HW-CC-Sign=89117E029F39370451BD3B13246830BC292FBA3E6548708DA8A98834043D94D0)

- **问题二**可以将style中enableSmoothEffect设置为false取消进度条本身的动效，自定义删除任务时的动画效果实现该场景。在删除任务时首先设置进度值为0，再通过[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)展示进度从0回到当前进度的动画效果。

  核心代码如下：

  
```text
.onClick(() => {
  this.tasks.splice(index, 1);<em> // 任务列表删除当前索引的任务</em>
  this.finishedTask = 0; <em>// 删除后先把进度设为0</em>
  this.totalTask = this.tasks.length; <em>// 获取总任务数</em>
  this.uiContext.animateTo({}, () => { <em>// 展示0到当前进度的动画</em>
    this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; <em>// 重新获取已完成任务数</em>
  });
});
```
 完整代码如下：

  
```text
@Entry
@Component
struct TaskListPage2 {
  @State finishedTask: number = 0; /<em>/ 已完成任务数</em>
  @State totalTask: number = 0; /<em>/ 总任务数</em>
  @State tasks: TaskInfo[] = []; <em>// 任务列表</em>
  @State deleteButtonBgcolor: string | Color = '#E84026'; <em>// 删除按钮的颜色</em>
  uiContext: UIContext = this.getUIContext();


 <em> // 删除任务按钮</em>
  @Builder
  DeleteTask(index: number) {
    Stack() {
      Image($r('app.media.ic_public_trash')) <em>// 删除图标，可以更换其他资源</em>
        .draggable(false)
        .width(20);
    }
    .width(40)
    .height(40)
    .borderRadius('50%')
    .margin({ left: 16 })
    .backgroundColor(this.deleteButtonBgcolor)
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type === TouchType.Down) {
          this.deleteButtonBgcolor = '#AAE84026'; /<em>/ 按下时图标背景颜色</em>
        } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
          this.deleteButtonBgcolor = '#E84026'; //<em> 取消或抬起恢复图标背景颜色</em>
        }
      }
    })
    .onClick(() => {
      this.tasks.splice(index, 1); // <em>任务列表删除当前索引的任务</em>
      this.finishedTask = 0; //<em> 删除后先把进度设为0</em>
      this.totalTask = this.tasks.length; // <em>获取总任务数</em>
      this.uiContext.animateTo({}, () => { // <em>展示0到当前进度的动画</em>
        this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; //<em> 重新获取已完成任务数</em>
      });
    });
  }


  build() {
    Column() {
     <em> // 任务进度以及新增任务按钮</em>
      TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
    <em>  // 任务列表</em>
      List({ space: 8 }) {
        ForEach(this.tasks, (item: TaskInfo, index: number) => {
          ListItem() {
            TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
          }.padding({ left: 16, right: 16 })
          .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); <em>// 左滑出现删除按钮</em>
        });
      }
      .layoutWeight(1)
      .width('100%')
      .scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#f1f3f5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}


<em>// 任务进度组件</em>
@Component
export struct TaskProgress {
  @Link finishedTask: number;
  @Link totalTask: number;
  @Link tasks: TaskInfo[];
  taskId: number = 0;


  build() {
    Column({ space: 20 }) {
      Row() {
        Text('任务进度：')
          .fontSize(25)
          .fontWeight(FontWeight.Bold);
     <em>   // 使用Stack堆叠容器，将进度条和进度展示层叠显示</em>
        Stack() {
          Progress({
            value: this.finishedTask, <em>// 进度值，已完成数</em>
            total: this.totalTask, <em>// 进度总长，总任务数</em>
            type: ProgressType.Ring, /<em>/ 环形</em>
          }).style({ enableSmoothEffect: false }) <em>// 禁用进度条动画</em>
            .width(90);
          Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
        };
      }
      .borderRadius(10)
      .height(110)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.White)
      .width('100%');


      Button('新增任务')
        .width('60%')
        .onClick(() => {
          this.tasks.push(new TaskInfo(this.taskId++, false));
          this.totalTask = this.tasks.length;
        });
    }.width('100%');
  }
}


<em>// 任务项组件</em>
@Component
export struct TaskItem {
  @State item: TaskInfo = new TaskInfo(0, false);
  @Link finishedTask: number;
  @Link tasks: TaskInfo[];
  uiContext: UIContext = this.getUIContext();


  build() {
    Row() {
      Text(`ID:${this.item.id}`).fontSize(16);
      Checkbox()
        .width(30)
        .shape(CheckBoxShape.CIRCLE)
        .select(this.item.isFinished)
        .onClick(() => {
          this.uiContext.animateTo({ duration: 200 }, () => {
            if (this.item.isFinished === true) {
              this.finishedTask--;
            } else {
              this.finishedTask++;
            }
            this.item.isFinished = !this.item.isFinished;
          });
        });
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .borderRadius(20)
    .padding({ left: 20, right: 20 })
    .backgroundColor(Color.White)
    .height(56)
    .width('100%');
  }
}


<em>// 任务信息，id和完成情况</em>
export class TaskInfo {
  id: number;
  isFinished: boolean;


  constructor(id: number, isFinished: boolean) {
    this.id = id;
    this.isFinished = isFinished;
  }
}
```


  运行效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/mqnKsYYEQiKoOcvyqbwO1g/zh-cn_image_0000002658797005.png?HW-CC-KV=V1&HW-CC-Date=20260811T005813Z&HW-CC-Expire=86400&HW-CC-Sign=C9EAA6E7F12B76499C4CD35FADB8E1F39CB9329CB04E5310BB508CE29E874DC0)


 
 

#### 常见FAQ

Q：Progress组件显示完成进度时，如何不展示动画？
 
A：可以将Progress组件style中enableSmoothEffect设置为false，关闭进度值变化时的动效。
 
 

#### 总结

默认情况下Progress组件修改进度值value会触发动画效果，修改进度总长total会直接渲染。如果在未关闭进度平滑动效时修改total和value，会出现预期外的视觉表现（如进度先增后减）。建议设置total值为100，通过进度完成情况百分比计算value更新进度值，避免直接修改total。
