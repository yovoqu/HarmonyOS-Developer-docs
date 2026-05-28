# AR Engine

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arengine-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：arEngine； API声明：enum ARSemanticDenseMode 差异内容：enum ARSemanticDenseMode | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseMode； API声明：DISABLED = 0 差异内容：DISABLED = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseMode； API声明：NORMAL = 1 差异内容：NORMAL = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseMode； API声明：CUBE_VOLUME = 2 差异内容：CUBE_VOLUME = 2 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseMode； API声明：CUBE_SPACE = 3 差异内容：CUBE_SPACE = 3 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticPlaneLabel； API声明：PLANE_SPACE = 9 差异内容：PLANE_SPACE = 9 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticPlaneLabel； API声明：CUBE_VOLUME = 10 差异内容：CUBE_VOLUME = 10 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticPlaneLabel； API声明：CUBE_SPACE = 11 差异内容：CUBE_SPACE = 11 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine； API声明：interface ARSemanticDensePointData 差异内容：interface ARSemanticDensePointData | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDensePointData； API声明：readonly id: ArrayBuffer; 差异内容：readonly id: ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDensePointData； API声明：readonly position: ArrayBuffer; 差异内容：readonly position: ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDensePointData； API声明：readonly color: ArrayBuffer; 差异内容：readonly color: ArrayBuffer; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine； API声明：interface ARSemanticDenseCubeData 差异内容：interface ARSemanticDenseCubeData | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseCubeData； API声明：readonly id: number; 差异内容：readonly id: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseCubeData； API声明：readonly vertexSize: number; 差异内容：readonly vertexSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseCubeData； API声明：readonly vertexData: Array&lt;number&gt;; 差异内容：readonly vertexData: Array&lt;number&gt;; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseCubeData； API声明：readonly confidence: number; 差异内容：readonly confidence: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseCubeData； API声明：readonly label: ARSemanticPlaneLabel; 差异内容：readonly label: ARSemanticPlaneLabel; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：arEngine； API声明：class ARSemanticDenseData 差异内容：class ARSemanticDenseData | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：readonly timestamp: number; 差异内容：readonly timestamp: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：readonly pointDataSize: number; 差异内容：readonly pointDataSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：readonly cubeDataSize: number; 差异内容：readonly cubeDataSize: number; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：acquirePointData(): ARSemanticDensePointData; 差异内容：acquirePointData(): ARSemanticDensePointData; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：acquireCubeData(): Array&lt;ARSemanticDenseCubeData&gt;; 差异内容：acquireCubeData(): Array&lt;ARSemanticDenseCubeData&gt;; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARSemanticDenseData； API声明：release(): Promise&lt;void&gt;; 差异内容：release(): Promise&lt;void&gt;; | api/@hms.core.ar.arengine.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：ARFrame； API声明：acquireSemanticDense(): ARSemanticDenseData; 差异内容：acquireSemanticDense(): ARSemanticDenseData; | api/@hms.core.ar.arengine.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：ARConfig； API声明：semanticDenseMode?: ARSemanticDenseMode; 差异内容：semanticDenseMode?: ARSemanticDenseMode; | api/@hms.core.ar.arengine.d.ts |
