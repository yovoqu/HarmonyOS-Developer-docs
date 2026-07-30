# 如何解决photoAccessHelper.getAssets获取竖向视频宽高不正确问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-12

#### 问题现象

图库显示宽高1080*1920。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/b2cMaQ8nR9qBYAk2RxHPGA/zh-cn_image_0000002659258335.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=E2341E7660A9D3CC3AD9B2E9674168739307779E6391F909B7A6F0E223D304D3)

 
通过API获取到的视频高为1080，宽为1920，API获取的值宽高与实际相反。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/71SQX3vZSI2Z27z4uIrOyA/zh-cn_image_0000002628899116.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=3592C52E053672953F4BA8542580276A974E917ED2B470FC18AE75307D8FEAD8)

 
 

#### 背景知识

- 使用[PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1)获取媒体资源。
- 使用[PhotoAsset.get](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset#get)获取图片和视频文件关键信息。

 
 

#### 问题定位

获取横屏视频做对比，两个视频在手机上显示的尺寸宽高数值相反。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/gWioWTP2S_Gz16anACcOFw/zh-cn_image_0000002659138385.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=E230EBA6DE2DE6A0ED1B720CBCD0171CAF8364F9729AB87F7C779C3BCED1D40E)

 
通过API获取到的两个视频同样高为1080，宽为1920，但是竖向视频有90°旋转，因此怀疑是旋转导致的问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/NOl-0ePSRDmkf1To2dO8Qg/zh-cn_image_0000002629059034.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=20B8BA30B41EB572BADCB90D9250EE24CD885F0AB7E0E5457999999E525A6786)

 
再对比下旋转180°和270°的情况，旋转度数除以180余数为90的时候，需要长宽的数值互换，才能得出手机上看到的结果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/DyQkbZNERii-TkJHccLSpQ/zh-cn_image_0000002659258337.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=E808A8F077B226088A13B59D90D576BE0A7CAEC566CA57C8219BC1CAD09E4468)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9Olw1LV1S_idw072dZ5yUQ/zh-cn_image_0000002628899118.png?HW-CC-KV=V1&HW-CC-Date=20260730T072527Z&HW-CC-Expire=86400&HW-CC-Sign=F1F9B157DE29E51B4199F66C4363E148691FFF5BEAF7EDE5C1D0C5726DD57FC7)

 
 

#### 分析结论

获取视频或图片长宽时，还需要判断是否有旋转，如果旋转度数除以180余数为90即视频是竖屏时，需要长宽的数值互换，才能得出手机上看到的结果。
 
 

#### 修改建议

通过photoAsset.get('orientation')判断视频是否旋转，来判断视觉效果上的长宽和参数的对应关系：
 
```bash
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PhAccessHelperGetAssets {
  @State phName: string = '';
  @State phHeight: number = 0;
  @State phWidth: number = 0;
  @State phOrientation: number = 0;

  async testMethod() {
    const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE; <em>// 过滤选择媒体文件类型为IMAGE</em>
    photoSelectOptions.maxSelectNumber = 1;<em> </em><em>// 选择媒体文件的最大数目</em>
    let uris: Array<string> = [];
    const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
   <em> // 拉起相册</em>
    photoViewPicker.select(photoSelectOptions).then(async (photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      uris = photoSelectResult.photoUris;
      console.info('photoViewPicker.select to file succeed and uris are:' + uris);
      if (uris.length === 0) {
        return;
      }
      let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      let uri = uris[0];<em> </em><em>// 需保证此uri已存在</em>
      predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri.toString());
      let fetchOptions: photoAccessHelper.FetchOptions = {
        fetchColumns: [
          'title',
          photoAccessHelper.PhotoKeys.WIDTH,<em> </em><em>// 图片宽度</em>
          photoAccessHelper.PhotoKeys.HEIGHT, <em>// 图片高度</em>
          photoAccessHelper.PhotoKeys.DURATION,<em> </em><em>// 持续时间</em>
          photoAccessHelper.PhotoKeys.SIZE, <em>// </em><em>文件大小</em>
          photoAccessHelper.PhotoKeys.DISPLAY_NAME, <em>// 显示名字</em>
          photoAccessHelper.PhotoKeys.ORIENTATION, <em>// </em><em>图片文件的方向</em>
          photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE], <em>// </em><em>媒体文件的子类型</em>
        predicates: predicates
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await phAccessHelper.getAssets(fetchOptions);
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      let title: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.TITLE;
      let paTitle = photoAsset.get(title.toString());
      this.phName = paTitle.toString();
      this.phOrientation = photoAsset.get('orientation') as number; <em>// 获取旋转角度</em>
      if (this.phOrientation % 180 == 90) {
        this.phName = paTitle.toString();
        this.phWidth = photoAsset.get('height') as number;
        this.phHeight = photoAsset.get('width') as number;
        this.phOrientation = photoAsset.get('orientation') as number;
      } else {
        this.phWidth = photoAsset.get('width') as number;
        this.phHeight = photoAsset.get('height') as number;
      }
     <em> // 释放FetchResult实例并使其失效</em>
      fetchResult.close();
      return photoAsset;
    }).catch((err: BusinessError) => {
      console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
    });
    return;
  }

  build() {
    Column() {
      Button('选择图片或视频')
        .id('PhAccessHelperGetAssetsHelloWorld')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.testMethod();
        });
      Text(`图片：${this.phName},属性长：${this.phHeight}宽：${this.phWidth}角度：${this.phOrientation}`);
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}
```
