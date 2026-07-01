# Tabs和同方向滑动的子组件的滑动动作隔离

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1310

#### 问题现象

如何设置在横向拖动子组件中的第三方图标时，禁止触发Tabs的切换功能。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/IkeT1TvPRI69HfQ4YYKeEQ/zh-cn_image_0000002658838299.png?HW-CC-KV=V1&HW-CC-Date=20260701T041145Z&HW-CC-Expire=86400&HW-CC-Sign=A132A27772BF2494F8EE4207807D84C11CFD48834D154B7BC1EAB679314118C2)

 
 

#### 背景知识

- [!!双向绑定语法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding)：在状态管理V2中，提供!!语法糖统一处理双向绑定。
- [Tabs.scrollable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#scrollable)：设置是否可以通过滑动页面进行页面切换。
- [TouchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#touchtype)：触摸事件的类型。
- [@ohos/mpchart](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmpchart)：MPChart是一个包含各种类型图表的图表库，主要用于业务数据汇总，包括线形图、柱状图、饼状图、蜡烛图、气泡图、雷达图、瀑布图等自定义图表库。

 
 

#### 解决方案
1. 该方案基于@ohos/mpchart，执行ohpm i @ohos/mpchart命令安装MPChart三方库。
2. 使用!!语法，把判断Tabs是否可以通过滑动页面进行页面切换的isAllowScroll属性，在主页面和子组件中关联。
3. 子组件中图表触摸时，设置isAllowScroll属性为false，触摸结束手指抬起时，设置isAllowScroll属性为true。
 
```text
import {
  JArrayList, <em>// 工具类：数据集合</em>
  EntryOhos,<em>/</em><em>/ 图表数据结构基础类</em>
  LineDataSet, <em>//线形图数据集合</em>
  ILineDataSet,<em> // 线形图数据集合的操作类</em>
  LineData, <em>//线形图数据包</em>
  LineChart, <em>// 线形图图表类</em>
  LineChartModel,<em>// 线形图配置构建类</em>
  MarkerView, <em>//图例形状</em>
} from '@ohos/mpchart';


@Entry
@ComponentV2
struct Index {
  @Local fontColor: string = '#182431';
  @Local selectedFontColor: string = '#007DFF';
  @Local currentIndex: number = 0;
  @Local selectedIndex: number = 0;
  @Local isAllowScroll: boolean = true;
  private controller: TabsController = new TabsController();


  private model: LineChartModel = new LineChartModel();
 <em> // 构造数据选择监听器</em>


  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.selectedIndex === index ? 1 : 0)
    }.width('100%')
  }


  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.selectedIndex, controller: this.controller }) {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar(this.tabBuilder(0, 'blue'))


        TabContent() {
          Star({ isAllowScroll: this.isAllowScroll!! })
        }.tabBar(this.tabBuilder(1, 'LineChart'))


        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar(this.tabBuilder(2, 'yellow'))
      }
      .scrollable(this.isAllowScroll)
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(56)
      .animationDuration(400)
      .animationMode(AnimationMode.CONTENT_FIRST)
      .onChange((index: number) => {
        console.log(`onChange index:${index}`);
        this.selectedIndex = index;
      })
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5')
    }.width('100%')
  }


}




@ComponentV2
struct Star {
  private model: LineChartModel = new LineChartModel();
  @Param isAllowScroll: boolean = true;
  @Event $isAllowScroll: (val: boolean) => void = () => {};


<em>  // 图表数据初始化</em>
  aboutToAppear() {


  <em>  // 初始化图表配置构建类</em>
    this.model = new LineChartModel();
    this.model.setDragEnabled(true);
    this.model.setScaleEnabled(true);
   <em> // 为图表设置markerView</em>
    let normalMarker = new MarkerView();
    this.model.setMarker(normalMarker);
    <em>// 也可设置定义图表MarkerView</em>
<em>    // 生成图表数据</em>
    let lineData: LineData = this.getLineData();
    <em>// 将数据与图表配置类绑定</em>
    this.model.setData(lineData);
   <em> // 设置图表最大的X轴显示范围，如不设置，则默认显示全部数据</em>
    this.model.setVisibleXRangeMaximum(20);
  }


  private getLineData(): LineData {


    let start: number = 1;
    let values: JArrayList<EntryOhos> = new JArrayList<EntryOhos>();
    for (let i = start; i < 30; i++) {
      values.add(new EntryOhos(i, i));
    }
    let dataSet = new LineDataSet(values, 'DataSet');
    let dataSetList: JArrayList<ILineDataSet> = new JArrayList<ILineDataSet>();
    dataSetList.add(dataSet);


    let lineData: LineData = new LineData(dataSetList);
    return lineData;
  }


  build() {
    Column() {
      LineChart({ model: this.model })
        .width('100%')
        .height('30%')
        .onTouch((event) => {
          if (event.type === TouchType.Down || event.type === TouchType.Move) {
            this.$isAllowScroll(false);
          } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            this.$isAllowScroll(true);
          }
        })
    }


  }
}
```
