# 解决冷启动picker选择器无权限问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-46

应用在冷启动后，系统可能不会自动授予之前通过picker等系统能力获取的URI的持续读取权限，直接使用这些URI会导致访问失败。可以在用户首次选择文件后，立即将文件复制到应用沙箱目录内，后续操作都基于沙箱内的副本进行。这样，在冷启动时，应用可以直接访问自己沙箱内的文件，无需再次申请权限。示例代码如下：
 
```json
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs, fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { preferences } from '@kit.ArkData';

const PREF_NAME = 'draft_pref';
const KEY_IMAGE_PATH = 'saved_image_path';

@Entry
@Component
struct ColdStartPickerSelector {
  @State imagePath: string = '';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  // When loading the page, attempt to read the last saved draft (cold start recovery logic).
  async aboutToAppear() {
    try {
      let pref = await preferences.getPreferences(this.context, PREF_NAME);
      let savedPath = await pref.get(KEY_IMAGE_PATH, '');

      if (savedPath && fs.accessSync(savedPath as string)) {
        this.imagePath = fileUri.getUriFromPath(savedPath as string);
        console.info('Cold start recovery draft successful: ' + this.imagePath);
      }
    } catch (err) {
      console.error('Reading draft configuration failed: ' + JSON.stringify(err));
    }
  }

  // Select image and save draft.
  async pickAndSaveDraft() {
    try {
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      let result = await photoPicker.select({ maxSelectNumber: 1 });

      if (result.photoUris.length > 0) {
        const tempUri = result.photoUris[0];

        // Open the temporary URI returned by Picker in read-only mode.
        let srcFile = fs.openSync(tempUri, fs.OpenMode.READ_ONLY);

        // Define the target save path in the sandbox.
        let destPath = `${this.context.cacheDir}/draft_image_${Date.now()}.jpg`;
        let destFile = fs.openSync(destPath, fs.OpenMode.CREATE | fs.OpenMode.WRITE_ONLY);

        // Execute file copying.
        fs.copyFileSync(srcFile.fd, destFile.fd);

        // Close file descriptor to free up resources.
        fs.closeSync(srcFile);
        fs.closeSync(destFile);

        // Persist the sandbox path locally.
        let pref = await preferences.getPreferences(this.context, PREF_NAME);
        await pref.put(KEY_IMAGE_PATH, destPath);
        await pref.flush();

        // Convert the file path in the application sandbox to a system recognizable file URI.
        this.imagePath = fileUri.getUriFromPath(destPath);
        console.info('Draft saved successfully, cache path: ' + destPath);
      }
    } catch (err) {
      console.error('Failed to select or save draft: ' + JSON.stringify(err));
    }
  }

  build() {
    Column({ space: 20 }) {
      Text('Demo')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)

      // Cold start read: directly render sandbox path.
      if (this.imagePath) {
        Image(this.imagePath)
          .width('100%')
          .height(300)
          .objectFit(ImageFit.Contain)
          .borderRadius(8)
        Text('Local draft loaded')
          .fontSize(14)
          .fontColor(Color.Green)
      } else {
        Text('No draft available')
          .fontSize(16)
          .fontColor(Color.Gray)
      }

      Button('Select image and save draft')
        .onClick(() => {
          this.pickAndSaveDraft();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .padding(20)
  }
}
```
 
**参考链接**
 
[fileIo.copyFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiocopyfile)
 
[应用沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)
