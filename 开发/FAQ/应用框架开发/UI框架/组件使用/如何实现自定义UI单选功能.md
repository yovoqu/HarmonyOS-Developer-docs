# 如何实现自定义UI单选功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-677

## 如何实现自定义UI单选功能
 


##### 问题现象

实现一个单选组件，要求：①绘制指示图标，②选中项需显示高亮状态。
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pgh2B1e6QyCCgQFDE8Q0oQ/zh-cn_image_0000002658914057.png?HW-CC-KV=V1&HW-CC-Date=20260701T025541Z&HW-CC-Expire=86400&HW-CC-Sign=D22E2794FE779C09A599D0EA5FDE4CF25FF684CAA34F7DA10053571AD64BF151)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/lNYZA2K7T2OyTwCcCkcLxg/zh-cn_image_0000002658794107.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025541Z&HW-CC-Expire=86400&HW-CC-Sign=9D14B548DE43BDCB028CCE0CA1FEA857510DCBC8D9B47B2B0813FCD11F243E88)

 
 

##### 背景知识

- [Polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon)：多边形绘制组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

##### 解决方案

采用Stack容器实现层叠布局，通过@State变量控制Polygon绘制的三角形指示图标显示与隐藏状态，结合条件渲染，实现选中时的高亮切换效果。
 
```text
@Entry
@Component
struct RadioPage {
  @State select: string = 'SELECT_OPTION_1'; // SELECT_OPTION_1为选项一，SELECT_OPTION_2为选项二

  @Builder
  commonUI(selectValue:string,imageUrl:string,context:string) {
    Stack() {
      Row() {
        Image($r(imageUrl))
          .width(40)
          .height(40)
        Text(context)
      }
      .width(150)
      .padding(5)
      .borderRadius(5)
      .border({ width: 1, color: this.select === selectValue ? '#ff5892de' : '#ffc4cac7' }) // 根据select变量判断选中的border颜色
      .backgroundColor(this.select === selectValue? '#ff5892de' : '#ffc4cac7') // 根据select变量判断选中的backgroundColor颜色
      .justifyContent(FlexAlign.Center)

      if (this.select === selectValue) {
        // 三角形指示图标
        Polygon({ width: 20, height: 20 })
          .points([[10, 10], [15, 0], [20, 10]])
          .fill('#ff5892de')
          .position({ top: -10, left: 10 })
      }
    }
    .onClick(() => {
      this.select = selectValue;
    })
  }

  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        // 选项一
        this.commonUI('SELECT_OPTION_1','app.media.startIcon','选项一');
        // 选项二
        this.commonUI('SELECT_OPTION_2','app.media.startIcon','选项二');
      }
      .padding(10)
      .height(100)
      .width('100%')
    }
  }
}
```
