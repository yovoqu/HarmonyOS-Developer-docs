# Device Certificate Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：X509Cert； API声明：getSubjectName(): DataBlob; 差异内容：19020001,19020002,19030001 | 类名：X509Cert； API声明：getSubjectName(encodingType?: EncodingType): DataBlob; 差异内容：19020001,19020002,19030001,401 | api/@ohos.security.cert.d.ts |
| 函数变更 | 类名：X509Cert； API声明：getSubjectName(): DataBlob; 差异内容：NA | 类名：X509Cert； API声明：getSubjectName(encodingType?: EncodingType): DataBlob; 差异内容：encodingType?: EncodingType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明： enum EncodingType 差异内容： enum EncodingType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：EncodingType； API声明：ENCODING_UTF8 = 0 差异内容：ENCODING_UTF8 = 0 | api/@ohos.security.cert.d.ts |
