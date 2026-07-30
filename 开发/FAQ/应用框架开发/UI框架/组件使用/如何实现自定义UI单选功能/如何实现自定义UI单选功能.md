# 如何实现自定义UI单选功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-677

#### 问题现象

实现一个单选组件，要求：①绘制指示图标，②选中项需显示高亮状态。
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pgh2B1e6QyCCgQFDE8Q0oQ/zh-cn_image_0000002658914057.png?HW-CC-KV=V1&HW-CC-Date=20260730T072324Z&HW-CC-Expire=86400&HW-CC-Sign=5A0DA3FD1136E4212AE4C0410E28C4AC3C4B6C60C0132D220A2008B84AE60DAB)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/lNYZA2K7T2OyTwCcCkcLxg/zh-cn_image_0000002658794107.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072324Z&HW-CC-Expire=86400&HW-CC-Sign=054BD33DC0AD436F2B5673A6CEB0A867B1C31258457DB4A6B3107FF0066893BA)

 
 

#### 背景知识

- [Polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon)：多边形绘制组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

采用Stack容器实现层叠布局，通过@State变量控制Polygon绘制的三角形指示图标显示与隐藏状态，结合条件渲染，实现选中时的高亮切换效果。
 
```text
@Entry
@Component
struct RadioPage {
  @State select: string = 'SELECT_OPTION_1'; <em>// SELECT_OPTION_1</em><em>为选项一，SELECT_OPTION_2为选项二</em>

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
      .border({ width: 1, color: this.select === selectValue ? '#ff5892de' : '#ffc4cac7' }) <em>// </em><em>根据select变量判断选中的border颜色</em>
      .backgroundColor(this.select === selectValue? '#ff5892de' : '#ffc4cac7') <em>// </em><em>根据select变量判断选中的backgroundColor颜色</em>
      .justifyContent(FlexAlign.Center)

      if (this.select === selectValue) {
      <em>  // 三角形指示图标</em>
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
      <em>  // 选项一</em>
        this.commonUI('SELECT_OPTION_1','app.media.startIcon','选项一');
     <em>   // 选项二</em>
        this.commonUI('SELECT_OPTION_2','app.media.startIcon','选项二');
      }
      .padding(10)
      .height(100)
      .width('100%')
    }
  }
}
```
