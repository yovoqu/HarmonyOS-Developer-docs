# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：safetyDetect； API声明：function checkUrlThreat(req: UrlCheckRequest): Promise&lt;UrlCheckResponse&gt;; 差异内容：NA | 类名：safetyDetect； API声明：function checkUrlThreat(req: UrlCheckRequest): Promise&lt;UrlCheckResponse&gt;; 差异内容：1010800005,1010800006,1010800007,1010800008,801 | api/@hms.security.safetyDetect.d.ts |
| 新增错误码 | 类名：safetyDetect； API声明：function checkSysIntegrity(req: SysIntegrityRequest): Promise&lt;SysIntegrityResponse&gt;; 差异内容：NA | 类名：safetyDetect； API声明：function checkSysIntegrity(req: SysIntegrityRequest): Promise&lt;SysIntegrityResponse&gt;; 差异内容：1010800005,1010800006,1010800007,1010800008,801 | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：function checkSysIntegrityOnLocal(): Promise&lt;string&gt;; 差异内容：function checkSysIntegrityOnLocal(): Promise&lt;string&gt;; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：AttestType； API声明：ATTEST_TYPE_SECIMAGE_PROCESS = 3 差异内容：ATTEST_TYPE_SECIMAGE_PROCESS = 3 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：AttestExceptionErrCode； API声明：ATTEST_ERROR_SIGNATURE_VERIFICATION_FAILED = 1011500017 差异内容：ATTEST_ERROR_SIGNATURE_VERIFICATION_FAILED = 1011500017 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：AttestExceptionErrCode； API声明：ATTEST_ERROR_SECIMAGE_PROCESS_FAILED = 1011500018 差异内容：ATTEST_ERROR_SECIMAGE_PROCESS_FAILED = 1011500018 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export enum SecImageProcFormat 差异内容：export enum SecImageProcFormat | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat； API声明：SECIMAGE_FORMAT_INVALID = 0 差异内容：SECIMAGE_FORMAT_INVALID = 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat； API声明：SECIMAGE_FORMAT_YUV_NV21 = 1 差异内容：SECIMAGE_FORMAT_YUV_NV21 = 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcFormat； API声明：SECIMAGE_FORMAT_JPEG = 2 差异内容：SECIMAGE_FORMAT_JPEG = 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export enum SecImageProcOperation 差异内容：export enum SecImageProcOperation | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation； API声明：SECIMAGE_COMPRESSION = 0 差异内容：SECIMAGE_COMPRESSION = 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation； API声明：SECIMAGE_CROPPING = 1 差异内容：SECIMAGE_CROPPING = 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcOperation； API声明：SECIMAGE_COMPRESSION_AND_CROPPING = 2 差异内容：SECIMAGE_COMPRESSION_AND_CROPPING = 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export interface SecImageBuffer 差异内容：export interface SecImageBuffer | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageBuffer； API声明：secImage: ArrayBuffer; 差异内容：secImage: ArrayBuffer; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export interface CropRegion 差异内容：export interface CropRegion | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion； API声明：x: number; 差异内容：x: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion； API声明：y: number; 差异内容：y: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion； API声明：width: number; 差异内容：width: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：CropRegion； API声明：height: number; 差异内容：height: number; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export enum SecImageProcTag 差异内容：export enum SecImageProcTag | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_INVALID = AttestTagType.ATTEST_TAG_TYPE_INVALID \| 0 差异内容：SECIMAGE_TAG_INVALID = AttestTagType.ATTEST_TAG_TYPE_INVALID \| 0 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_SRC_IMAGE_FORMAT = AttestTagType.ATTEST_TAG_TYPE_UINT \| 1 差异内容：SECIMAGE_TAG_SRC_IMAGE_FORMAT = AttestTagType.ATTEST_TAG_TYPE_UINT \| 1 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_DEST_IMAGE_FORMAT = AttestTagType.ATTEST_TAG_TYPE_UINT \| 2 差异内容：SECIMAGE_TAG_DEST_IMAGE_FORMAT = AttestTagType.ATTEST_TAG_TYPE_UINT \| 2 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_PROC_OPERATION = AttestTagType.ATTEST_TAG_TYPE_UINT \| 3 差异内容：SECIMAGE_TAG_PROC_OPERATION = AttestTagType.ATTEST_TAG_TYPE_UINT \| 3 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_COMPRESSION_QUALITY = AttestTagType.ATTEST_TAG_TYPE_UINT \| 4 差异内容：SECIMAGE_TAG_COMPRESSION_QUALITY = AttestTagType.ATTEST_TAG_TYPE_UINT \| 4 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcTag； API声明：SECIMAGE_TAG_CROP_REGION = AttestTagType.ATTEST_TAG_TYPE_UINT \| 5 差异内容：SECIMAGE_TAG_CROP_REGION = AttestTagType.ATTEST_TAG_TYPE_UINT \| 5 | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export interface SecImageProcParams 差异内容：export interface SecImageProcParams | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParams； API声明：tag: SecImageProcTag; 差异内容：tag: SecImageProcTag; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParams； API声明：value: number \| CropRegion; 差异内容：value: number \| CropRegion; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：export interface SecImageProcParamsArray 差异内容：export interface SecImageProcParamsArray | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：SecImageProcParamsArray； API声明：properties: Array&lt;SecImageProcParams&gt;; 差异内容：properties: Array&lt;SecImageProcParams&gt;; | api/@hms.security.trustedAppService.d.ts |
| 新增API | NA | 类名：trustedAppService； API声明：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise&lt;SecImageBuffer&gt;; 差异内容：function procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise&lt;SecImageBuffer&gt;; | api/@hms.security.trustedAppService.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：FraudDetectionRequest； API声明：version?: number; 差异内容：version?: number; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
