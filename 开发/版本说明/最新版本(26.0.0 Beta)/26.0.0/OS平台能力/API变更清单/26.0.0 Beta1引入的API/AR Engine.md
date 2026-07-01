# AR Engine

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arengine-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：arEngine； API声明：enum ARRemoteSensorMode 差异内容：enum ARRemoteSensorMode | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARRemoteSensorMode； API声明：LOCAL_SENSOR = 0 差异内容：LOCAL_SENSOR = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARRemoteSensorMode； API声明：REMOTE_SENSOR_AI_GLASS = 1 差异内容：REMOTE_SENSOR_AI_GLASS = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFrame； API声明：acquireCameraImage(): ARImage; 差异内容：acquireCameraImage(): ARImage; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARConfig； API声明：remoteSensorMode?: ARRemoteSensorMode; 差异内容：remoteSensorMode?: ARRemoteSensorMode; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARViewContext； API声明：loadGSModel(resourcePath: spatialRender.GSImportSettings, location: arEngine.ARPose): Promise&lt;number&gt;; 差异内容：loadGSModel(resourcePath: spatialRender.GSImportSettings, location: arEngine.ARPose): Promise&lt;number&gt;; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext； API声明：removeGSModel(modelID: number): Promise&lt;boolean&gt;; 差异内容：removeGSModel(modelID: number): Promise&lt;boolean&gt;; | api/@hms.core.ar.arview.d.ets |
