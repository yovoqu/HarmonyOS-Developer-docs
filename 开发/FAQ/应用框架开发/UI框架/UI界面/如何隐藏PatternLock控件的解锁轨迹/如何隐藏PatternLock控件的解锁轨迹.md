# 如何隐藏PatternLock控件的解锁轨迹

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1332

#### 问题现象

HarmonyOS如何隐藏图案锁PatternLock控件的解锁轨迹。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/TX29rzy2T8m2aREsnR-1Vg/zh-cn_image_0000002628599896.png?HW-CC-KV=V1&HW-CC-Date=20260723T013053Z&HW-CC-Expire=86400&HW-CC-Sign=E40F1B9B755D07CDBEF9111DB6B998E7EA963242D2D8678B0AF6D1A02FA618DE)

 
 

#### 背景知识

HarmonyOS为图案密码锁提供了[PatternLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock)控件，以九宫格图案的方式输入密码，用于密码验证场景。
 
PatternLock控件默认情况下，点按会出现图案锁圆点变大、变色以及圆环波纹动效；连线时会产生轨迹并触发路径上圆点的特效。
 
简单实现可以参考以下组件代码：
 
```text
PatternLock()
  .sideLength(200)
  .circleRadius(9)
  .pathStrokeWidth(5)
  .activeColor('#707070')
  .selectedColor('#707070')
  .pathColor('#707070')
  .backgroundColor('#F5F5F5')
  .autoReset(true)
```
 
解锁效果如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/MMzjGOCVTGWINR-yAbnavA/zh-cn_image_0000002628759800.png?HW-CC-KV=V1&HW-CC-Date=20260723T013053Z&HW-CC-Expire=86400&HW-CC-Sign=FC141EABB14452C7413448DDC628827D99687ADCA78F0E9671F3A0C9947FF582)

 
 

#### 解决方案

隐藏圆点与轨迹动效，主要修改点如下：
 1. 为了隐藏连接线，需要将PatternLock控件的[pathStrokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#pathstrokewidth)属性设置为0或负数。
2. 为了隐藏圆点颜色、大小变化，需要将PatternLock控件的[regularColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#regularcolor)属性、[activateCircleStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#activatecirclestyle12)属性中options参数的[color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#circlestyleoptions12对象说明:~:text=说明-,color,-ResourceColor)属性设置为同一颜色，并将[selectedColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#selectedcolor)属性、[activeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#activecolor)属性设置为透明色'#00000000'。
3. 为了隐藏圆环大小变化，需要将PatternLock控件的[activateCircleStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#activatecirclestyle12)属性中options参数的radius属性与[circleRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#circleradius)属性设置为同一大小。
4. 为了隐藏圆点动效，需要将PatternLock控件的[activateCircleStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#activatecirclestyle12)属性中options参数的enableWaveEffect属性设置为false。
 
将原组件代码按上文修改后如下：
 
```text
import { LengthUnit } from '@kit.ArkUI';


@Entry
@Component
struct HiddenPatternLock {
  build() {
    RelativeContainer() {
      PatternLock()
        .sideLength(280)
        .circleRadius(10)
        .pathStrokeWidth(0)
        .regularColor('#707070')
        .activeColor('#00000000')
        .selectedColor('#00000000')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .autoReset(true)
        .activateCircleStyle({
          color: '#707070',
          radius: { value: 10, unit: LengthUnit.VP },
          enableWaveEffect: false
        })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onPatternComplete((indices: number[]) => {
          let numbers = indices.map(i => i + 1).join('-');
          console.info(`Selected numbers: ${numbers}`);
        });
    }
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor('#F5F5F5');
  }
}
```
 
在日志中会打印出选择的数字，截图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/LTCZu-XSSvyvC_-dMCGNvA/zh-cn_image_0000002658959115.png?HW-CC-KV=V1&HW-CC-Date=20260723T013053Z&HW-CC-Expire=86400&HW-CC-Sign=A5992DE3FD68DA4EC3F5DD0A91C5C51A6CD2A45A487F192A5F3D1289A2CE3CE4)

 
 

#### 常见FAQ

Q：将所有颜色修改一致后，图案锁解锁时圆点大小仍然会有略微放大，且颜色带透明度时，会出现颜色加深问题。
 
A：参考解决方案步骤2，将PatternLock控件的[selectedColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#selectedcolor)属性、[activeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock#activecolor)属性设置为透明色'#00000000'即可。
 
Q：PatternLock的激活和选定有什么区别？
 
A：激活：指组件处于可接收用户输入状态，即用户可以开始绘制图案；选定：指用户在激活的PatternLock上完成了单个点的选中或完整图案的确认，是对用户操作的即时反馈。
 
示例代码：
 
```text
import { LengthUnit } from '@kit.ArkUI';


@Entry
@Component
struct SelectedPatternLock {
  build() {
    RelativeContainer() {
      PatternLock()
        .circleRadius(6)
        .pathStrokeWidth(12)
      <em>  // 圆点在激活状态的填充颜色</em>
        .activeColor('rgba(0, 0, 0, 0.9)')
       <em> // 圆点在选中状态的填充颜色</em>
        .selectedColor('rgba(10, 89, 247, 1)')
        .pathColor('rgba(0, 0, 0, 0.2)')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .activateCircleStyle({
          color: 'rgba(0, 0, 0, 0.2)',
          radius: { value: 10, unit: LengthUnit.VP },
          enableWaveEffect: true
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
 
运行效果如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/yniu02UkQy-WNByieTE0TA/zh-cn_image_0000002658839165.png?HW-CC-KV=V1&HW-CC-Date=20260723T013053Z&HW-CC-Expire=86400&HW-CC-Sign=5AC02247AD2F4AEBE6A15CA2620EC44E9E19189B7B327645F6A1262B24A55DE9)
