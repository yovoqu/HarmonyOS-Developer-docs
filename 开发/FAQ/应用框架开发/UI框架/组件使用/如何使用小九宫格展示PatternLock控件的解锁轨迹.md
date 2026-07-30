# 如何使用小九宫格展示PatternLock控件的解锁轨迹

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1219

#### 问题现象

在开发PatternLock功能时，为了增强用户体验，通常会在图形界面的上方展示一个九宫格的缩略图，这个缩略图能够反映用户绘制的手势密码路径。本文将介绍如何使用小九宫格展示PatternLock控件的解锁轨迹。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/SUbeyIf6TMmb_jAfXubHmg/zh-cn_image_0000002658953227.png?HW-CC-KV=V1&HW-CC-Date=20260701T041302Z&HW-CC-Expire=86400&HW-CC-Sign=7A27F7FED6D1518726C058CB01AF61FB72D1F7B88143AD2A62F3277FEBB7548A)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/M0K1DZHbQzmLMXYrvTv0pQ/zh-cn_image_0000002658833269.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041302Z&HW-CC-Expire=86400&HW-CC-Sign=D38A15DDB774267646638638308C85302802C5622618FBA5BB19F66E4B33E60A)

 
 

#### 背景知识

- [PatternLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock)是一种图案密码锁组件，以九宫格图案的方式输入密码，常用于密码验证场景。密码输入选中宫格圆点时触发[onDotConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#ondotconnect11)回调，密码输入结束时触发[onPatternComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#onpatterncomplete)回调。
- [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)组件为网格容器，通过指定项目所在的单元格做出各种各样的布局，其中容器内各条目对应一个[GridItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem)组件。

 
 

#### 解决方案
1. 在PatternLock手势路径经过的地方使用current存储。
```text
<em>// </em><em>最高层</em>
PatternLock(this.patternLockController)
  .activateCircleStyle({
    color: '#331D9CDF',
    radius: { value: 30, unit: LengthUnit.VP },
    enableWaveEffect: true
  })
  .sideLength(320)
  .circleRadius(8)
  .pathStrokeWidth(5)
  .regularColor('#ffbebebe')
  .activeColor('#FF1D9CDF')
  .selectedColor('#FF1D9CDF')
  .pathColor('#cc05a9f7')
  .onDotConnect((index: number) => {
    console.info(`${index}查看手势路径`);
    this.current.push(index);
  })
```

2. 定义小九宫格时，判断当前的位置是否在current中来确认展示对应的样式。
```text
<em>// </em><em>手势路径：小九宫格</em>
Grid() {
  ForEach(this.circularItems, (item: string, index) => {
    GridItem() {
      Row() {
      }
      .width(10)
      .height(10)
      .backgroundColor(this.current.includes(index) ? Color.Black : Color.Grey) <em>// </em><em>根据当前选中的点进行改色</em>
      .borderRadius(10);
    };
  }, (item: string) => item);
}
.width('11%')
.columnsTemplate('1fr 1fr 1fr')
.maxCount(3)
.columnsGap(6)
.rowsGap(4);
```

 
完整示例参考如下：
 
```text
import { LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct PatternLockExample {
  @State passwords: Number[] = [];
  @State message: string = '请输入不小于5位数的手势密码！';
  @State circularItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  @State current: number[] = []; <em>// </em><em>当前手势密码所选点</em>
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
   <em>   // 手势路径：小九宫格</em>
      Grid() {
        ForEach(this.circularItems, (item: string, index) => {
          GridItem() {
            Row() {
            }
            .width(10)
            .height(10)
            .backgroundColor(this.current.includes(index) ? Color.Black : Color.Grey) <em>// </em><em>根据当前选中的点进行改色</em>
            .borderRadius(10);
          };
        }, (item: string) => item);
      }
      .width('11%')
      .columnsTemplate('1fr 1fr 1fr')
      .maxCount(3)
      .columnsGap(6)
      .rowsGap(4);


      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20);
      Stack() {
    <em>    // 最底层</em>
        PatternLock(this.patternLockController)
          .activateCircleStyle({
            color: '#661D9CDF',
            radius: { value: 30, unit: LengthUnit.VP },
            enableWaveEffect: true
          })
          .sideLength(320)
          .circleRadius(30)
          .pathStrokeWidth(5)
          .regularColor('#ffe0e0e0') <em>// 设置未选择时颜色</em>
          .activeColor('#661D9CDF') <em>// </em><em>设置经过还未离开时颜色</em>
          .selectedColor('#661D9CDF'); <em>// </em><em>设置已选择后颜色</em>
     <em>   // 中间层</em>
        PatternLock(this.patternLockController)
          .activateCircleStyle({
            color: '#B3FFFFFF',
            radius: { value: 30, unit: LengthUnit.VP },
            enableWaveEffect: true
          })
          .sideLength(320)
          .circleRadius(28)
          .pathStrokeWidth(5)
          .regularColor(Color.White)
          .activeColor('#B3FFFFFF')
          .selectedColor('#B3FFFFFF')
          .pathColor('#cc05a9f7');
     <em>   // 最高层</em>
        PatternLock(this.patternLockController)
          .activateCircleStyle({
            color: '#331D9CDF',
            radius: { value: 30, unit: LengthUnit.VP },
            enableWaveEffect: true
          })
          .sideLength(320)
          .circleRadius(8)
          .pathStrokeWidth(5)
          .regularColor('#ffbebebe')
          .activeColor('#FF1D9CDF')
          .selectedColor('#FF1D9CDF')
          .pathColor('#cc05a9f7')
          .onDotConnect((index: number) => {
            console.info(`${index}查看手势路径`);
            this.current.push(index);
          })

          .onPatternComplete((input: Array<number>) => {
            <em>// </em><em>输入的密码长度小于5时，提示重新输入</em>
            if (input.length < 5) {
              this.current = [];
              this.message = '密码需要超过五位';
              return;
            }
           <em> // 判断密码长度是否大于0</em>
            if (this.passwords.length > 0) {
             <em> // 判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入</em>
              if (this.passwords.toString() === input.toString()) {
                this.current = [];
                this.passwords = input;
                this.message = '设置密码成功: ' + this.passwords.toString();
                this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT);
              } else {
                this.current = [];
                this.message = '密码不一致，请重新输入。';
                this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG);
              }
            } else {
             <em> // 提示第二次输入密码</em>
              this.passwords = input;
              this.message = '请再次输入';
              this.current = [];
            }
          });
      };

      Button('重置').margin(30).onClick(() => {
       <em> // 重置密码锁</em>
        this.patternLockController.reset();
        this.passwords = [];
        this.message = '请输入不小于5位数的手势密码！';
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
