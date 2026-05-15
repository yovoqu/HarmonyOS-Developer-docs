# Image Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：ImageSource； API声明：getDelayTimeList(callback: AsyncCallback<Array<number>>): void; 差异内容：62980096,62980110,62980113,62980115,62980116,62980118,62980122,62980149 | 类名：ImageSource； API声明：getDelayTimeList(callback: AsyncCallback<Array<number>>): void; 差异内容：62980096,62980110,62980111,62980115,62980116,62980118,62980122,62980149 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType； API声明：GIF_METADATA = 5 差异内容：GIF_METADATA = 5 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：enum GifPropertyKey 差异内容：enum GifPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey； API声明：GIF_DELAY_TIME = 'GifDelayTime' 差异内容：GIF_DELAY_TIME = 'GifDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GifPropertyKey； API声明：GIF_DISPOSAL_TYPE = 'GifDisposalType' 差异内容：GIF_DISPOSAL_TYPE = 'GifDisposalType' | api/@ohos.multimedia.image.d.ts |
| 删除同名函数 | 类名：ImageCreator； API声明：queueImage(interface: Image, callback: AsyncCallback<void>): void; 差异内容：queueImage(interface: Image, callback: AsyncCallback<void>): void; | 类名：global； API声明： 差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 删除同名函数 | 类名：ImageCreator； API声明：queueImage(interface: Image): Promise<void>; 差异内容：queueImage(interface: Image): Promise<void>; | 类名：global； API声明： 差异内容：NA | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：ImageCreator； API声明：queueImage(image: Image, callback: AsyncCallback<void>): void; 差异内容：queueImage(image: Image, callback: AsyncCallback<void>): void; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：ImageCreator； API声明：queueImage(image: Image): Promise<void>; 差异内容：queueImage(image: Image): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：ImageSource； API声明：createPictureAtIndex(index: number): Promise<Picture>; 差异内容：createPictureAtIndex(index: number): Promise<Picture>; | api/@ohos.multimedia.image.d.ts |
