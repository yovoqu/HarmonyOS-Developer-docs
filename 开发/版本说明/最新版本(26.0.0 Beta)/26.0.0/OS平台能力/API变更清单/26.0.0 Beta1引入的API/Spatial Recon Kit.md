# Spatial Recon Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-spatialreconkit-7001

## Spatial Recon Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace spatialImage 差异内容：declare namespace spatialImage | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：export enum SpatialImageStatus 差异内容：export enum SpatialImageStatus | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_SUCCESS = 0 差异内容：STATUS_SUCCESS = 0 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_NOT_SUPPORT = 1023710001 差异内容：STATUS_NOT_SUPPORT = 1023710001 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_AIMODEL_NOT_EXIST = 1023710002 差异内容：STATUS_AIMODEL_NOT_EXIST = 1023710002 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_AIMODEL_DOWNLOAD_FAILED = 1023710003 差异内容：STATUS_AIMODEL_DOWNLOAD_FAILED = 1023710003 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_GENERATE_CANCELLED = 1023710004 差异内容：STATUS_GENERATE_CANCELLED = 1023710004 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageStatus； API声明：STATUS_GENERATE_FAILED = 1023710005 差异内容：STATUS_GENERATE_FAILED = 1023710005 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：export enum SpatialImageModelType 差异内容：export enum SpatialImageModelType | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageModelType； API声明：MODELTYPE_GS = 0 差异内容：MODELTYPE_GS = 0 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageModelType； API声明：MODELTYPE_MESH = 1 差异内容：MODELTYPE_MESH = 1 | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：export interface CameraPose 差异内容：export interface CameraPose | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：CameraPose； API声明：position: Vec3; 差异内容：position: Vec3; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：CameraPose； API声明：rotation: Quaternion; 差异内容：rotation: Quaternion; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：type ProgressCallback = (progress: number) => void; 差异内容：type ProgressCallback = (progress: number) => void; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：export class SpatialImageGenerator 差异内容：export class SpatialImageGenerator | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageGenerator； API声明：static isSupport(): SpatialImageStatus; 差异内容：static isSupport(): SpatialImageStatus; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageGenerator； API声明：prepareEnv(callback: ProgressCallback): Promise&lt;SpatialImageStatus&gt;; 差异内容：prepareEnv(callback: ProgressCallback): Promise&lt;SpatialImageStatus&gt;; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageGenerator； API声明：cancelPrepare(): Promise&lt;SpatialImageStatus&gt;; 差异内容：cancelPrepare(): Promise&lt;SpatialImageStatus&gt;; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageGenerator； API声明：generate(image: image.PixelMap, type: SpatialImageModelType, uri: string): Promise&lt;SpatialImageStatus&gt;; 差异内容：generate(image: image.PixelMap, type: SpatialImageModelType, uri: string): Promise&lt;SpatialImageStatus&gt;; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageGenerator； API声明：cancelGenerate(): Promise&lt;SpatialImageStatus&gt;; 差异内容：cancelGenerate(): Promise&lt;SpatialImageStatus&gt;; | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：spatialImage； API声明：export class SpatialImageController 差异内容：export class SpatialImageController | api/@hms.graphics.spatialImage.d.ts |
| 新增API | NA | 类名：SpatialImageController； API声明：calcRenderPos(response: sensor.GyroscopeResponse): CameraPose; 差异内容：calcRenderPos(response: sensor.GyroscopeResponse): CameraPose; | api/@hms.graphics.spatialImage.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.graphics.spatialImage.d.ts 差异内容：SpatialReconKit | api/@hms.graphics.spatialImage.d.ts |
