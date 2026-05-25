# core-vision-kit-object-detect — 物体检测

> 来源：https://gitcode.com/HarmonyOS_Samples/core-vision-kit-sample-code-ark-ts-object-detect-demo  
> 语言：ArkTS | 版本要求：HarmonyOS 5.0.5+, DevEco 6.1.0+

## 项目简介

基于 Core Vision Kit 的多物体检测 Demo，用户选择或拍摄照片后检测多种物体类型，输出类别、位置、置信度。

## 核心 API

| API | 用途 |
|-----|------|
| `objectDetection.ObjectDetector.create()` | 创建检测器 |
| `detector.process(request)` | 执行检测 |
| `detector.destroy()` | 销毁检测器释放资源 |

## 支持的 11 类物体

landscape, animal, plant, building, tree, face, form, text, human head, cat head, dog head

## 输出

- 类别标签 + 置信度 (0~1)
- 边界框 `{ left, top, width, height }`
- 多物体支持，每物体独立 ID

## 输入约束

- 分辨率：720p 以上推荐
- 尺寸：100px ~ 10000px
- 物体占比：> 0.1% 画面面积
