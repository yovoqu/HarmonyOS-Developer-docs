# 实现Slider进度和滑块解耦

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1653

#### 问题现象

如何实现类似Slider组件，且要求滑块和进度解耦。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/6PfqO3TZRP2g15TlQPELew/zh-cn_image_0000002628820888.png?HW-CC-KV=V1&HW-CC-Date=20260723T012825Z&HW-CC-Expire=86400&HW-CC-Sign=5C4D59E9B0D8F7FD6B7A29E2E09A57DACC2617DA2AA74ACF73C6D9FA71A5D0B2)

 
 

#### 背景知识

- [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
- [DataPanel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel)：数据面板组件，用于将多个数据占比情况使用占比图进行展示。

 
 

#### 解决方案

为了实现滑块和进度解耦，在堆叠容器中通过DataPanel组件实现进度效果，并使用Circle组件模拟可拖动的滑块。
 
- 在DataPanel组件中通过values属性来设置进度条的值，并绑定点击事件来更新滑块的位置selectValue。
```text
<em>// 使用DataPanel模拟进度条</em>
DataPanel({ values: this.valueArr, max: 1000, type: DataPanelType.Line })
  .width(300)
  .height(10)
  .borderRadius('50%')
 <em> // DataPanel点击事件，将滑块重置于点击位置</em>
  .onClick((event: ClickEvent) => {
   <em> // 判断点击位置是否超过进度条长度，+8为滑块半径，并重新计算赋值selectValue</em>
    if ((event.x + 8) * 1000 / 300 > 1000) {
      this.selectValue = 1000;
    } else {
      this.selectValue = (event.x + 8) * 1000 / 300;
    }
  })
```

- 滑块Circle组件的位置与变量selectValue绑定，并在滑动手势中更新滑块位置。为了防止滑块脱离进度，对两侧边界进行判断。
```text
<em>// 模拟滑块</em>
Circle({ width: 16, height: 16 })
  .fill('#fff')
  .borderRadius('50%')
<em>  // 滑块的位置为selectValue在总体的占比乘以300，减8防止滑块溢出边界</em>
  .position({ left: (this.selectValue) / 1000 * 300 - 8, top: 0 })
  .shadow({ radius: 10, color: Color.Gray })
  .gesture(
    PanGesture({ direction: PanDirection.Horizontal, distance: 1 })
      .onActionStart(() => {
     <em>   // 初始化滑块左边界坐标</em>
        this.lastOffsetX = 0;
      })
      .onActionUpdate((even) => {
     <em>   // 在滑动手势更新回调中，通过手势坐标减去上次左边界坐标计算偏移距离，通过偏移距离在总长度（300）占比乘以1000更新selectValue</em>
        this.selectValue = this.selectValue + (even.offsetX - this.lastOffsetX) / 300 * 1000;
      <em>  // 对滑块左边界进行判断</em>
        if (this.selectValue < 0) {
          this.selectValue = 0;
     <em>     // 对滑块的右边界进行判断</em>
        } else if (this.selectValue > 1000) {
          this.selectValue = 1000;
        }
   <em>     // 更新滑块左边界坐标</em>
        this.lastOffsetX = even.offsetX;
      })
  )
```


 
通过上述DataPanel组件和Circle组件实现了类似Slider组件的功能，并且滑块和进度解耦。
 
```text
@Entry
@Component
struct SliderDecouple {
<em>  // 滑块位置值</em>
  @State selectValue: number = 120;
  @State valueArr: number[] = [120];
  lastOffsetX: number = 0;

  build() {
    Column({ space: 10 }) {
      Stack() {
    <em>    // 使用DataPanel模拟进度条</em>
        DataPanel({ values: this.valueArr, max: 1000, type: DataPanelType.Line })
          .width(300)
          .height(10)
          .borderRadius('50%')
     <em>     // DataPanel点击事件，将滑块重置于点击位置</em>
          .onClick((event: ClickEvent) => {
        <em>    // 判断点击位置是否超过进度条长度，+8为滑块半径，并重新计算赋值selectValue</em>
            if ((event.x + 8) * 1000 / 300 > 1000) {
              this.selectValue = 1000;
            } else {
              this.selectValue = (event.x + 8) * 1000 / 300;
            }
          })

   <em>     // 模拟滑块</em>
        Circle({ width: 16, height: 16 })
          .fill('#fff')
          .borderRadius('50%')
     <em>     // 滑块的位置为selectValue在总体的占比乘以300，减8防止滑块溢出边界</em>
          .position({ left: (this.selectValue) / 1000 * 300 - 8, top: 0 })
          .shadow({ radius: 10, color: Color.Gray })
          .gesture(
            PanGesture({ direction: PanDirection.Horizontal, distance: 1 })
              .onActionStart(() => {
             <em>   // 初始化滑块左边界坐标</em>
                this.lastOffsetX = 0;
              })
              .onActionUpdate((even) => {
          <em>      // 在滑动手势更新回调中，通过手势坐标减去上次左边界坐标计算偏移距离，通过偏移距离在总长度（300）占比乘以1000更新selectValue</em>
                this.selectValue = this.selectValue + (even.offsetX - this.lastOffsetX) / 300 * 1000;
             <em>   // 对滑块左边界进行判断</em>
                if (this.selectValue < 0) {
                  this.selectValue = 0;
            <em>      // 对滑块的右边界进行判断</em>
                } else if (this.selectValue > 1000) {
                  this.selectValue = 1000;
                }
             <em>   // 更新滑块左边界坐标</em>
                this.lastOffsetX = even.offsetX;
              })
          )
      }

  <em>    // 模拟进度条变化</em>
      Button('add')
        .onClick(() => {
     <em>     // 模拟每次进度条增加50</em>
          this.valueArr[0] = this.valueArr[0] + 50;
     <em>     // 进度条不能超越滑块</em>
          if (this.valueArr[0] > this.selectValue) {
            this.valueArr[0] = this.selectValue;
          } else if (this.valueArr[0] < 0) {
            this.valueArr[0] = 0;
          }
        })
      Text('进度：' + Math.round((this.valueArr[0]) / 10) + '%')
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width(400)
  }
}
```
