# ArkGraphics 2D

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：uiEffect； API声明：function createEffect(): VisualEffect; 差异内容：NA | 类名：uiEffect； API声明：function createEffect(): VisualEffect; 差异内容：form | api/@ohos.graphics.uiEffect.d.ts |
| 函数变更 | 类名：Matrix； API声明：isEqual(matrix: Matrix): Boolean; 差异内容：Boolean | 类名：Matrix； API声明：isEqual(matrix: Matrix): boolean; 差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Matrix； API声明：invert(matrix: Matrix): Boolean; 差异内容：Boolean | 类名：Matrix； API声明：invert(matrix: Matrix): boolean; 差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Matrix； API声明：isIdentity(): Boolean; 差异内容：Boolean | 类名：Matrix； API声明：isIdentity(): boolean; 差异内容：boolean | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Canvas； API声明：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array&lt;number&gt;, vertOffset: number, colors: Array&lt;number&gt;, colorOffset: number): void; 差异内容：colors: Array&lt;number&gt; | 类名：Canvas； API声明：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array&lt;number&gt;, vertOffset: number, colors: Array&lt;number&gt; \| null, colorOffset: number): void; 差异内容：colors: Array&lt;number&gt; \| null | api/@ohos.graphics.drawing.d.ts |
