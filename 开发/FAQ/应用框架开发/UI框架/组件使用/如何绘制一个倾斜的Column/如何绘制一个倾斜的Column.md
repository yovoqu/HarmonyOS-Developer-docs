# 如何绘制一个倾斜的Column

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1185

#### 问题现象

UI开发中，如何绘制一个倾斜指定角度的Column？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/n9u7Cm1LRJ-vaQq10RJOFA/zh-cn_image_0000002628752850.png?HW-CC-KV=V1&HW-CC-Date=20260730T072344Z&HW-CC-Expire=86400&HW-CC-Sign=C3894A3E69D27F66C912D3705F1C093107CDBBE70CAFF1B84788042373CC1683)

 
 

#### 背景知识

[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)：可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform3d20)接口。参数可设置当前组件的变换矩阵。object当前仅支持[Matrix4Transit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4#matrix4transit)矩阵对象类型。[matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4)：提供矩阵变换功能，支持对图形进行平移、旋转和缩放等。
 
 

#### 解决方案

通过给对应的[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)添加transform属性，根据倾斜的角度计算出弧度，使用matrix4.[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4#matrix4init)创建一个四阶矩阵，将创建的四阶矩阵对象作为transform的参数传入，即可得到一个倾斜指定角度的Column。
 
```text
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private matrix1: matrix4.Matrix4Transit | undefined = undefined;

  aboutToAppear(): void {
   <em> // 将角度转换为弧度（Math.tan需要弧度制）</em>
    const angleRad = -14 * Math.PI / 180;
 <em>   // 计算倾斜角度对应的tan值</em>
    const tanValue = Math.tan(angleRad);
 <em>   // 使用matrix4.init创建一个4x4的变换矩阵</em>
    this.matrix1 = matrix4.init([
      1, tanValue, 0, 0, <em>// 第一行：x方向倾斜</em>
      0, 1, 0, 0, <em>// 第二行：保持y不变</em>
      0, 0, 1, 0, <em>// 第三行：z不变</em>
      0, 0, 0, 1<em> // </em><em>第四行：齐次坐标</em>
    ]);
  }

  build() {
    Column() {
      Column() {
        Text('Column倾斜')
          .fontSize(16)
          .textAlign(TextAlign.Center);
      }
      .width(200)
      .height(400)
      .border({ width: 1, color: Color.Black })
      .transform(this.matrix1);
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
