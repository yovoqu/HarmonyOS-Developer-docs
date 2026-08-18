# PC应用如何隐藏导航栏右上角三键

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-7

#### 问题现象

PC应用非全屏状态下或者自由多窗模式下如何不显示右上角三键？
 
 

#### 背景知识

[Window](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window)提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
 
 

#### 解决方案
1. 配置定时任务间隔，通过[onMouse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key#onmouse)事件判断鼠标在应用中是否保持静止。
2. 若鼠标静止，获取应用窗口实例，使用[setWindowDecorVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowdecorvisible11)主动隐藏状态栏。效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/djqORmjFTjqs-z3ygJXKbA/zh-cn_image_0000002628552364.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041034Z&HW-CC-Expire=86400&HW-CC-Sign=CAD2F1F0D23B50BE0DFBCCB1948AA32996010211A873BC3AA324001A8131A4AD)

3. 如上图窗口右上角三键此时未隐藏，使用[setWindowTitleButtonVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowtitlebuttonvisible14)主动隐藏三键，以获取沉浸式体验。效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/P5zJVprNQh-epkT-g19Lhg/zh-cn_image_0000002658911689.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041034Z&HW-CC-Expire=86400&HW-CC-Sign=F8510BA969F32D6956271A8B8CF715F3CE37DED116EE40BF8F5AF26D5C4634DC)

 
完整示例参考如下：
 
```text
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  preX: number = 0;
  preY: number = 0;
  curX: number = 0;
  curY: number = 0;
  context: Context | undefined = this.getUIContext().getHostContext();

  onPageShow(): void {
    // 设置定时任务检测一定时间内鼠标是否移动
    setInterval(() => {
      if (this.curX == this.preX && this.curY == this.preY) {
        // 设置导航栏不可见
        changeRight(this.context, false, false, false);
      } else {
        this.preX = this.curX;
        this.preY = this.curY;
      }
    }, 1000);
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .onMouse((event?: MouseEvent) => {
      // 设置页面的onMouse回调记录鼠标位置
      if (event) {
        this.curX = event.windowX;
        this.curY = event.windowY;
        // 设置导航栏可见
        changeRight(this.context, true, true, true);
      }
    })
    .height('100%')
    .width('100%')
  }
}

function changeRight(context: Context | undefined, max: boolean, min: boolean, isClose: boolean) {
  if (!context) {
    return;
  }
  let uiContext = context as common.UIAbilityContext;
  let mainWindow: window.Window | undefined = undefined;
  uiContext.windowStage.getMainWindow().then(
    data => {
      mainWindow = data;
      // setWindowDecorVisible用于隐藏图标、名称与状态栏
      mainWindow.setWindowDecorVisible(max);
      // setWindowTitleButtonVisible接口，隐藏主窗标题栏最大化、最小化、关闭按钮
      mainWindow.setWindowTitleButtonVisible(max, min, isClose);
    }
  ).catch((err: BusinessError) => {
    if (err.code) {
      console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
    }
  });
}
```
 
 

#### 常见FAQ

Q：setWindowSystemBarEnable等部分接口使用中发现在2in1模拟器中不生效是为什么？
 
A：Window部分接口虽然显示支持PC/2in1设备，文档中也有标识说明，接口在部分机型下不生效，在使用Window或者其他接口时需要注意接口适配性，避免影响开发效率。
