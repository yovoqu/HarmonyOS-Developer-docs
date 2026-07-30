# PC应用如何隐藏导航栏右上角三键

更新时间：2026-07-30 01:24:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-7

#### 问题现象

PC应用非全屏状态下或者自由多窗模式下如何不显示右上角三键？
 
 

#### 背景知识

[Window](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window)提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
 
 

#### 解决方案
1. 配置定时任务间隔，通过[onMouse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key#onmouse)事件判断鼠标在应用中是否保持静止。
2. 若鼠标静止，获取应用窗口实例，使用[setWindowDecorVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowdecorvisible11)主动隐藏状态栏。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/q8YT7SveSUePqrsocquaVA/zh-cn_image_0000002680372243.png?HW-CC-KV=V1&HW-CC-Date=20260730T072243Z&HW-CC-Expire=86400&HW-CC-Sign=85DDE762191EC40D8C1441FA11FDC0304F032F5DC947D8B48BE8D56FA973A59B)

3. 如上图窗口右上角三键此时未隐藏，使用[setWindowTitleButtonVisible](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowtitlebuttonvisible14)主动隐藏三键，以获取沉浸式体验。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/M1OAl2AVSsCleGqfH7d6_Q/zh-cn_image_0000002680212499.png?HW-CC-KV=V1&HW-CC-Date=20260730T072243Z&HW-CC-Expire=86400&HW-CC-Sign=6E22048ACCB5E75FC1A5FBA426C399178CA2070DFDE82AC71149E9517CFD5E19)


  
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
  <em>  // 设置定时任务检测一定时间内鼠标是否移动</em>
    setInterval(() => {
      if (this.curX == this.preX && this.curY == this.preY) {
     <em>   // 设置导航栏不可见</em>
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
   <em>   // 设置页面的onMouse回调记录鼠标位置</em>
      if (event) {
        this.curX = event.windowX;
        this.curY = event.windowY;
       <em> // 设置导航栏可见</em>
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
     <em> // setWindowDecorVisible用于隐藏图标、名称与状态栏</em>
      mainWindow.setWindowDecorVisible(max);
     <em> // setWindowTitleButtonVisible接口，隐藏主窗标题栏最大化、最小化、关闭按钮。</em>
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
 
Q：深色模式下PC应用窗口右上角的三键颜色不够清晰，如何处理？
 
A：将设备系统版本升级至最新Release版本。系统在新版本中已优化深色模式下右上角三键的显示颜色，升级后三键将显示为白色，提升视觉清晰度。
