# ArkGraphics 2D

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Path； API声明：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean; 差异内容：401 | 类名：Path； API声明：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas； API声明：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void; 差异内容：401 | 类名：Canvas； API声明：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas； API声明：clear(color: common2D.Color \| number): void; 差异内容：401 | 类名：Canvas； API声明：clear(color: common2D.Color \| number): void; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas； API声明：quickRejectPath(path: Path): boolean; 差异内容：401 | 类名：Canvas； API声明：quickRejectPath(path: Path): boolean; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas； API声明：quickRejectRect(rect: common2D.Rect): boolean; 差异内容：401 | 类名：Canvas； API声明：quickRejectRect(rect: common2D.Rect): boolean; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Typeface； API声明：static makeFromRawFile(rawfile: Resource): Typeface; 差异内容：401 | 类名：Typeface； API声明：static makeFromRawFile(rawfile: Resource): Typeface; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Font； API声明：createPathForGlyph(index: number): Path; 差异内容：401 | 类名：Font； API声明：createPathForGlyph(index: number): Path; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Font； API声明：getBounds(glyphs: Array&lt;number&gt;): Array<common2D.Rect>; 差异内容：401 | 类名：Font； API声明：getBounds(glyphs: Array&lt;number&gt;): Array<common2D.Rect>; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect； API声明：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect; 差异内容：401 | 类名：PathEffect； API声明：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect； API声明：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect; 差异内容：401 | 类名：PathEffect； API声明：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect； API声明：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect; 差异内容：401 | 类名：PathEffect； API声明：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Pen； API声明：setColor(color: number): void; 差异内容：401 | 类名：Pen； API声明：setColor(color: number): void; 差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：TextLine； API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine; 差异内容：401 | 类名：TextLine； API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine； API声明：getStringIndexForPosition(point: common2D.Point): number; 差异内容：401 | 类名：TextLine； API声明：getStringIndexForPosition(point: common2D.Point): number; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine； API声明：getOffsetForStringIndex(index: number): number; 差异内容：401 | 类名：TextLine； API声明：getOffsetForStringIndex(index: number): number; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine； API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void; 差异内容：401 | 类名：TextLine； API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine； API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number; 差异内容：401 | 类名：TextLine； API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run； API声明：getGlyphs(range: Range): Array&lt;number&gt;; 差异内容：401 | 类名：Run； API声明：getGlyphs(range: Range): Array&lt;number&gt;; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run； API声明：getPositions(range: Range): Array<common2D.Point>; 差异内容：401 | 类名：Run； API声明：getPositions(range: Range): Array<common2D.Point>; 差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run； API声明：getStringIndices(range?: Range): Array&lt;number&gt;; 差异内容：401 | 类名：Run； API声明：getStringIndices(range?: Range): Array&lt;number&gt;; 差异内容：NA | api/@ohos.graphics.text.d.ts |
