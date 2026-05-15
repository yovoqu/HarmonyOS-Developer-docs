# Core Vision Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：faceComparator； API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>; 差异内容：1008400001,1008400002,401 | 类名：faceComparator； API声明：function compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>; 差异内容：1008400001,1008400002,200,401 | api/@hms.ai.face.faceComparator.d.ts |
| 错误码变更 | 类名：faceDetector； API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>; 差异内容：1008800001,1008800002,401 | 类名：faceDetector； API声明：function detect(visionInfo: VisionInfo): Promise<Array<Face>>; 差异内容：1008800001,1008800002,200,401 | api/@hms.ai.face.faceDetector.d.ts |
| 错误码变更 | 类名：subjectSegmentation； API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>; 差异内容：1011000001,1011000002,401 | 类名：subjectSegmentation； API声明：function doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>; 差异内容：1011000001,1011000002,200,401 | api/@hms.ai.vision.subjectSegmentation.d.ts |
