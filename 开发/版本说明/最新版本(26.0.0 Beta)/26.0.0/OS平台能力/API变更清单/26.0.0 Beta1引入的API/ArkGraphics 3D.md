# ArkGraphics 3D

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-7001

## ArkGraphics 3D
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：RenderResourceFactory； API声明：createImageStream(params: SceneResourceParameters): Promise&lt;ImageStream&gt;; 差异内容：createImageStream(params: SceneResourceParameters): Promise&lt;ImageStream&gt;; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global； API声明：export declare abstract class SoftShadowConfig 差异内容：export declare abstract class SoftShadowConfig | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：SoftShadowConfig； API声明：get shadowAlgorithmType(): ShadowAlgorithmType; 差异内容：get shadowAlgorithmType(): ShadowAlgorithmType; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global； API声明：export declare class PCFConfig 差异内容：export declare class PCFConfig | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：PCFConfig； API声明：get shadowSampleRadius(): number \| undefined; 差异内容：get shadowSampleRadius(): number \| undefined; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：PCFConfig； API声明：get shadowSampleCount(): number \| undefined; 差异内容：get shadowSampleCount(): number \| undefined; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：RenderConfiguration； API声明：softShadowConfig?: SoftShadowConfig; 差异内容：softShadowConfig?: SoftShadowConfig; | api/graphics3d/Scene.d.ts |
| 新增API | NA | 类名：global； API声明：export interface ImageStream 差异内容：export interface ImageStream | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：ImageStream； API声明：readonly surfaceId: string; 差异内容：readonly surfaceId: string; | api/graphics3d/SceneResources.d.ts |
| 新增API | NA | 类名：global； API声明：export enum ShadowAlgorithmType 差异内容：export enum ShadowAlgorithmType | api/graphics3d/SceneTypes.d.ts |
| 新增API | NA | 类名：ShadowAlgorithmType； API声明：PCF = 0 差异内容：PCF = 0 | api/graphics3d/SceneTypes.d.ts |
