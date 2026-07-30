# 通过colorFilter和颜色矩阵修改Image的颜色

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1353

#### 问题现象

在移动应用开发中，常遇到这样的典型场景：同一套图标素材需要根据用户主题、交互状态（如点击/禁用）或场景模式（如深色/浅色模式）呈现不同颜色。传统方案中，开发者往往通过准备多套资源文件或使用Canvas绘制来实现颜色变化，但这会导致安装包体积膨胀（资源冗余）和渲染性能损耗。
 
通过Image组件的colorFilter，只需单份原始图片配合颜色矩阵，即可实现运行时动态变色：
 
```text
<em>// </em><em>注入颜色变换矩阵</em>
Image($r('app.media.icon_toast_warning'))
  .colorFilter(
    [1, 1, 0, 0, 0,
      0, 1, 0, 0, 0,
      0, 0, 1, 0, 0,
      0, 0, 0, 1, 0])
```
 
但该方案面临一个问题：如何将人类可读的十六进制颜色（如#4f0f48db）转换为colorFilter所需的4×5颜色矩阵？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/oU_rCNXpSzW8x2xKaaAK5w/zh-cn_image_0000002628601520.png?HW-CC-KV=V1&HW-CC-Date=20260701T041331Z&HW-CC-Expire=86400&HW-CC-Sign=05CD756CBE597BDEFA84FDAA88222B1A7661ED9E08FC219BCD93D7C32793CB98)

 
 

#### 背景知识

在计算机图形学中，每个像素由四个维度的数据构成，可表示为四维向量：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/h9Gm8FTNSaOrUu-LcjdDeg/zh-cn_image_0000002658840793.png?HW-CC-KV=V1&HW-CC-Date=20260701T041331Z&HW-CC-Expire=86400&HW-CC-Sign=A8CB93422E280B250C47613BC11CF806F2F94C2CF7EAE8BC2F81593F4BD22331)

 
颜色矩阵本质是执行以下运算的线性变换器：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/gqvkhXqWS_aazTo7rh2JNw/zh-cn_image_0000002628761416.png?HW-CC-KV=V1&HW-CC-Date=20260701T041331Z&HW-CC-Expire=86400&HW-CC-Sign=3F433090F524BEA8603DC8A6986D55A847A1E8A5AB42F6B9026FAB8A1F3C88CC)

 
颜色矩阵M的参数语义：
 
- 行维度：每行单独控制红、绿、蓝、透明四个输出通道中一个通道的生成规则。
- 前四列：决定原始颜色中的红、绿、蓝、透明四个分量对当前输出通道的影响比例（权重系数）。
- 第五列：为输出通道直接添加一个固定值，用于整体调亮、调暗或颜色偏移。

 
运算时需将值归一化至0.0–1.0范围（1.0对应255）。
 
矩阵结构计算：
 
```text
<em>// </em><em>输出R通道的计算公式</em>
R' = m00*R + m01*G + m02*B + m03*A + m04
<em>// </em><em>输出G通道的计算公式</em>
G' = m10*R + m11*G + m12*B + m13*A + m14
<em>// </em><em>输出B通道同理</em>
<em>// Alpha通道独立处理</em>
A' = m30*R + m31*G + m32*B + m33*A + m34
```
 
**纯色替换矩阵**：将图像转换为目标色（如#2196F3）需满足：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/b8Kod9l-Q0GgBUa40WD54A/zh-cn_image_0000002658960741.png?HW-CC-KV=V1&HW-CC-Date=20260701T041331Z&HW-CC-Expire=86400&HW-CC-Sign=5181032599AC0FBD53F282672C0D5BC0FE08329391F72E0336A7D0F236DD953E)

 
对应矩阵：
 
```text
[
  0, 0, 0, 0, TargetR,
  0, 0, 0, 0, TargetG,
  0, 0, 0, 0, TargetB,
  0, 0, 0, 1, 0
]
```
 
关键问题在于如何将目标色的十六进制值转换为TargetR、TargetG、TargetB。得到颜色矩阵后，即可通过[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性实现颜色滤镜效果。
 
 

#### 解决方案

实现图片动态变色，可使用Image的colorFilter。其参数所需的颜色矩阵，可通过以下封装方法将十六进制颜色值转换得到：
 1. 输入验证：使用正则表达式验证输入格式，只接受#RRGGBB或#AARRGGBB格式，格式错误时抛出明确异常。
2. 通道提取：移除#符号，6位颜色自动补全为8位（添加FF表示完全不透明）。
3. 解析通道和归一化：将每2位十六进制字符串转换为十进制整数，解析顺序：A→R→G→B，并将0-255范围映射到0.0-1.0。
4. 矩阵构建：RGB通道前四列的系数设为0（忽略原始颜色值），第五列设为目标颜色值，而Alpha通道需要混合透明度计算。
 
```text
class ColorUtils {
  <em>/**</em>
<em>   * 将十六进制颜色值转换为4x5颜色矩阵</em>
<em>   * @param hexColor 十六进制颜色字符串，支持格式：#RRGGBB, #AARRGGBB</em>
<em>   * @returns 4x5颜色矩阵数组 (20个元素的number数组)</em>
<em>   */</em>
  static hexToColorMatrix(hexColor: string): number[] {
   <em> // 验证输入格式</em>
    if (!/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$/.test(hexColor)) {
      throw new Error('Invalid hex color format. Expected #RRGGBB or #AARRGGBB');
    }

   <em> // 提取颜色通道值</em>
    let rgba = hexColor.substring(1);
    if (rgba.length === 6) {
      rgba = 'FF' + rgba; <em>// 添加默认Alpha通道</em>
    }

   <em> // 解析ARGB通道值(含归一化处理)</em>
    const alpha = parseInt(rgba.substring(0, 2), 16) / 255;
    const red = parseInt(rgba.substring(2, 4), 16) / 255;
    const green = parseInt(rgba.substring(4, 6), 16) / 255;
    const blue = parseInt(rgba.substring(6, 8), 16) / 255;

  <em>  /**</em>
<em>     * 构造纯色替换矩阵：</em>
<em>     * [0, 0, 0, 0, red,    → 输出R通道 = 0*R + 0*G + 0*B + 0*A + 目标R</em>
<em>     *  0, 0, 0, 0, green,  → 输出G通道 = 0*R + 0*G + 0*B + 0*A + 目标G</em>
<em>     *  0, 0, 0, 0, blue,   → 输出B通道 = 0*R + 0*G + 0*B + 0*A + 目标B</em>
<em>     *  0, 0, 0, alpha, 0]  → 输出A通道 = 0*R + 0*G + 0*B + alpha*A + 0</em>
<em>     */</em>
    return [
      0, 0, 0, 0, red,
      0, 0, 0, 0, green,
      0, 0, 0, 0, blue,
      0, 0, 0, alpha, 0
    ];
  }
}

@Entry
@Component
struct Example {
 <em> // 图片资源</em>
  @State imageRes: Resource = $r('app.media.ic_pause'); <em>// 运行时需替换为实际的图片资源</em>

  build() {
    Column() {
     <em> // 未使用</em>
      Image(this.imageRes)
        .width(200)
        .height(200)
        .margin(16);

    <em>  // 使用colorFilter添加滤镜</em>
      Image(this.imageRes)
        .width(200)
        .height(200)
        .colorFilter(ColorUtils.hexToColorMatrix('#66666666'));
    }.justifyContent(FlexAlign.Center).width('100%').height('100%')
  }
}
```
 
 

#### 常见FAQ

Q：如何改变一个颜色的亮度？
 
A：通过矩阵，将三个颜色通道统一做颜色偏移，实现亮度调节。矩阵如下，其中N是用来调整三通道的亮度。
 
```text
[ 1  0  0  0  N
  0  1  0  0  N
  0  0  1  0  N
  0  0  0  1  0 ]
```
