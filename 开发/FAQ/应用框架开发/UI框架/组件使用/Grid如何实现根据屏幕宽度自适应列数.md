# Grid如何实现根据屏幕宽度自适应列数

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1465

## Grid如何实现根据屏幕宽度自适应列数
 


##### 问题现象

如何实现一个能够上拉加载更多的Grid列表，并且可以根据不同的屏幕大小适配不同展示列数？
 
 

##### 背景知识

- [栅格容器组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)(GridRow)仅可以和[栅格子组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)(GridCol)在栅格布局场景中使用。栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。
- 可通过GridCol的span属性设置占用列数，xs、sm、md、lg分别对应不同栅格大小设备上栅格容器组件的栅格列数。

 
 

##### 解决方案

- 可以通过栅格布局来实现Grid组件对不同屏幕大小的适配，具体实现方式及示例代码如下：
配置栅格容器组件(GridRow)的columns参数，即设定栅格布局的列数，默认API version 20之前为12列。
- 配置栅格子组件(GridCol)的span参数，设定不同栅格大小设备对应的栅格列数，可根据屏幕越大对应显示的列数越多来设定xs、sm、md、lg的值。
- 通过[onScrollStop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onscrollstop9)回调，触发加载更多数据。

 
```text
let tmpData: number[] =
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,];

@Entry
@Component
struct GridRowAdaptiveColumnCount {
  @State data: number[] = tmpData;
  scroller: Scroller = new Scroller();

  build() {
    Column({ space: 5 }) {
      Scroll(this.scroller) {
        GridRow({
          columns: 12,
          gutter: 5,
        }) {
          ForEach(this.data, (item: number) => {
            GridCol({
              span: {
                xs: 12,
                sm: 6,
                md: 3,
                lg: 2
              }
            }) {
              Row() {
                Text(item.toString())
                  .fontSize(20)
                  .fontWeight(400)
                  .fontColor(Color.White)
                  .textAlign(TextAlign.Center)
                  .width('100%')
                  .height('100%');
              }.width('100%').height(80).backgroundColor('#0D5AF5');
            };
          });
        }.margin({ top: 5 })
        .onBreakpointChange((breakpoint: string) => {
          console.info(breakpoint);
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(`onAreaChange, oldValue: ${oldValue}, newValue: ${newValue}`);
        });
      }
      .backgroundColor('#F1F3F5')
      .height('100%')
      .scrollSnap({
        snapAlign: ScrollSnapAlign.START,
        snapPagination: 400,
        enableSnapToStart: true,
        enableSnapToEnd: true
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
        tmpData = tmpData.map(item => item + 30);
        this.data = this.data.concat(tmpData);
        console.info(String(this.data));
      });
    }.width('100%').height('100%');
  }
}
```
 - 在三种不同屏幕下的运行效果图如下：
手机设备下对应span参数值为sm，可显示两列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/IvZ83Nd1R-uZmp6DX-xZvA/zh-cn_image_0000002658964565.png?HW-CC-KV=V1&HW-CC-Date=20260701T025616Z&HW-CC-Expire=86400&HW-CC-Sign=14DF6BCCF030CBF0232A6F06B57BAC9A19ADAE865CD2FBCF87FA8778661B6058)

- 折叠屏设备下对应span参数值为md，可显示四列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Gb9rm8NzSZyuVJIVkW2GVw/zh-cn_image_0000002628605356.png?HW-CC-KV=V1&HW-CC-Date=20260701T025616Z&HW-CC-Expire=86400&HW-CC-Sign=17665F04A246C84EC5561E38673832CC4F5A4228CC722E65E94E9CD17726ABCC)

- 平板设备下对应span参数值为lg，可显示六列：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mWxjnUeXQEuAsMGvsj_6jA/zh-cn_image_0000002658844613.png?HW-CC-KV=V1&HW-CC-Date=20260701T025616Z&HW-CC-Expire=86400&HW-CC-Sign=1DF169CAA34D3BF6C5AF7B820DA0DF6F11ABB605BADF2D2A8C1D17D16B5BD11E)
