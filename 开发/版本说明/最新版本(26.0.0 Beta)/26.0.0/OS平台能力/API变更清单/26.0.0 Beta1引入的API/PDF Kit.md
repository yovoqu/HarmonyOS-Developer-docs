# PDF Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-7001

## PDF Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：PdfDocument； API声明：loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult; 差异内容：401 | 类名：PdfDocument； API声明：loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：saveDocument(path: string, onProgress?: (progress: number) => number): boolean; 差异内容：401 | 类名：PdfDocument； API声明：saveDocument(path: string, onProgress?: (progress: number) => number): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：createDocument(width: number, height: number): boolean; 差异内容：401 | 类名：PdfDocument； API声明：createDocument(width: number, height: number): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：isEncrypted(path: string): boolean; 差异内容：401 | 类名：PdfDocument； API声明：isEncrypted(path: string): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：getPage(index: number): PdfPage; 差异内容：401 | 类名：PdfDocument； API声明：getPage(index: number): PdfPage; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：insertBlankPage(index: number, width: number, height: number): PdfPage; 差异内容：401 | 类名：PdfDocument； API声明：insertBlankPage(index: number, width: number, height: number): PdfPage; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：insertPageFromDocument(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage; 差异内容：401 | 类名：PdfDocument； API声明：insertPageFromDocument(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：deletePage(index: number, count: number): void; 差异内容：401 | 类名：PdfDocument； API声明：deletePage(index: number, count: number): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：movePage(index: number, dest: number): boolean; 差异内容：401 | 类名：PdfDocument； API声明：movePage(index: number, dest: number): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：setFontWeight(weight: number): void; 差异内容：401 | 类名：PdfDocument； API声明：setFontWeight(weight: number): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：convertToImage(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean; 差异内容：401 | 类名：PdfDocument； API声明：convertToImage(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：removeBookmark(bookmark: Bookmark): boolean; 差异内容：401 | 类名：PdfDocument； API声明：removeBookmark(bookmark: Bookmark): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：insertBookmark(bookmark: Bookmark, parent: Bookmark, position: number): boolean; 差异内容：401 | 类名：PdfDocument； API声明：insertBookmark(bookmark: Bookmark, parent: Bookmark, position: number): boolean; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：addHeaderFooter(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：401 | 类名：PdfDocument； API声明：addHeaderFooter(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：addWatermark(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：401 | 类名：PdfDocument； API声明：addWatermark(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfDocument； API声明：addBackground(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：401 | 类名：PdfDocument； API声明：addBackground(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfAnnotation； API声明：moveTo(x: number, y: number): void; 差异内容：401 | 类名：PdfAnnotation； API声明：moveTo(x: number, y: number): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：addAnnotation(annotationInfo: PdfAnnotationInfo): PdfAnnotation; 差异内容：401 | 类名：PdfPage； API声明：addAnnotation(annotationInfo: PdfAnnotationInfo): PdfAnnotation; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：setAnnotation(annotation: PdfAnnotation, annotationInfo: PdfAnnotationInfo): void; 差异内容：401 | 类名：PdfPage； API声明：setAnnotation(annotation: PdfAnnotation, annotationInfo: PdfAnnotationInfo): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：removeAnnotation(annotation: PdfAnnotation): void; 差异内容：401 | 类名：PdfPage； API声明：removeAnnotation(annotation: PdfAnnotation): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：setBox(boxtype: BoxType, rect: PdfRect): void; 差异内容：401 | 类名：PdfPage； API声明：setBox(boxtype: BoxType, rect: PdfRect): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：getBox(boxtype: BoxType): PdfRect; 差异内容：401 | 类名：PdfPage； API声明：getBox(boxtype: BoxType): PdfRect; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：setRotation(rotation: RotationAngle): void; 差异内容：401 | 类名：PdfPage； API声明：setRotation(rotation: RotationAngle): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：getCustomPagePixelMap(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap; 差异内容：401 | 类名：PdfPage； API声明：getCustomPagePixelMap(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap; 差异内容：401 | 类名：PdfPage； API声明：getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：getAreaPixelMapWithOptions(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap; 差异内容：401 | 类名：PdfPage； API声明：getAreaPixelMapWithOptions(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：addTextObject(text: string, x: number, y: number, style: TextStyle): void; 差异内容：401 | 类名：PdfPage； API声明：addTextObject(text: string, x: number, y: number, style: TextStyle): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：addImageObject(path: string, x: number, y: number, width: number, height: number): void; 差异内容：401 | 类名：PdfPage； API声明：addImageObject(path: string, x: number, y: number, width: number, height: number): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：PdfPage； API声明：deleteGraphicsObject(object: GraphicsObject): void; 差异内容：401 | 类名：PdfPage； API声明：deleteGraphicsObject(object: GraphicsObject): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：Bookmark； API声明：setDestInfo(info: DestInfo): void; 差异内容：401 | 类名：Bookmark； API声明：setDestInfo(info: DestInfo): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 删除错误码 | 类名：Bookmark； API声明：setBookmarkInfo(info: BookmarkInfo): void; 差异内容：401 | 类名：Bookmark； API声明：setBookmarkInfo(info: BookmarkInfo): void; 差异内容：NA | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：PdfDocument； API声明：getPixelMapWithPages(pageIndices: number[], matrices: PdfMatrix[], bitmapWidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap; 差异内容：getPixelMapWithPages(pageIndices: number[], matrices: PdfMatrix[], bitmapWidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap; | api/@hms.officeservice.pdfservice.d.ts |
