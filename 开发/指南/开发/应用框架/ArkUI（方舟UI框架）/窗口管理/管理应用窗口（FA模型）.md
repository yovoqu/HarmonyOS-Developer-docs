# 管理应用窗口（FA模型）

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa

##### 基本概念

窗口沉浸式能力：指对状态栏、导航栏等系统窗口进行控制，减少状态栏导航栏等系统界面的突兀感，从而使用户获得最佳体验的能力。

沉浸式能力只在应用主窗口作为全屏窗口时生效。通常情况下，应用子窗口、全局悬浮窗、模态窗口等辅助窗口和处于自由窗口下的应用主窗口无法使用沉浸式能力。

> [!NOTE]
> 当前沉浸式界面开发仅支持窗口级别的配置，暂不支持Page级别的配置。若有Page级别切换的需要，可以在页面生命周期开始，例如onPageShow中设置沉浸模式，然后在页面退出，例如onPageHide中恢复默认设置来实现。




##### 场景介绍

在FA模型下，管理应用窗口的典型场景有：

 - 设置应用子窗口属性及目标页面
 - 体验窗口沉浸式能力


以下分别介绍具体开发方式。



##### 接口说明

上述场景涉及的常用接口如下表所示。更多API说明请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window)。

| 实例名 | 接口名 | 描述 |
| --- | --- | --- |
| window静态方法 | createWindow(config: Configuration, callback: AsyncCallback&lt;Window&gt;): void | 创建子窗口。 -config：创建窗口时的参数。 |
| window静态方法 | findWindow(name: string): Window | 查找name所对应的窗口。 |
| Window | setUIContent(path: string, callback: AsyncCallback&lt;void&gt;): void | 根据当前工程中某个页面的路径为窗口加载具体的页面内容。 其中path为要加载到窗口中的页面内容的路径，在FA模型下该路径需添加到工程的config.json文件中。 |
| Window | moveWindowTo(x: number, y: number, callback: AsyncCallback&lt;void&gt;): void | 移动当前窗口位置。 |
| Window | setWindowBrightness(brightness: number, callback: AsyncCallback&lt;void&gt;): void | 设置屏幕亮度值。 |
| Window | resize(width: number, height: number, callback: AsyncCallback&lt;void&gt;): void | 改变当前窗口大小。 |
| Window | setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise&lt;void&gt; | 设置主窗口或子窗口的布局是否为沉浸式布局。true表示沉浸式布局；false表示非沉浸式布局。 |
| Window | setWindowSystemBarEnable(names: Array<'status'\|'navigation'>): Promise&lt;void&gt; | 设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果。 例如，该参数设置为['status', 'navigation']，则全部显示；设置为[]，则不显示。 |
| Window | setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise&lt;void&gt; | 设置窗口内导航栏、状态栏属性。 systemBarProperties：导航栏、状态栏的属性集合。 |
| Window | showWindow(callback: AsyncCallback&lt;void&gt;): void | 显示当前窗口。 |
| Window | on(type: 'touchOutside', callback: Callback&lt;void&gt;): void | 开启本窗口区域外的点击事件的监听。 |
| Window | destroyWindow(callback: AsyncCallback&lt;void&gt;): void | 销毁当前窗口。 |




##### 设置应用子窗口

开发者可以按需创建应用子窗口，如弹窗等，并对其进行属性设置等操作。

> [!NOTE]
> 以下几种场景不建议使用子窗口，建议优先考虑使用控件 overlay 能力实现。 移动设备（手机、在非自由模式下的平板设备）场景下子窗不能超出处于智慧多窗悬浮窗模式、分屏模式的应用主窗口范围，与控件一致。 分屏窗口与自由窗口模式下，主窗口位置大小发生改变时控件实时跟随变化能力优于子窗口。 部分设备平台下根据实际的系统配置限制，子窗只有系统默认的动效和圆角阴影，应用无法设置，自由度低。




##### 开发步骤
1. 创建/获取子窗口对象。

  
可以通过window.createWindow接口创建子窗口。

  非[自由窗口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#沉浸式布局)。

  自由窗口状态下，子窗口参数[decorEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#configuration9)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。
2. 也可以通过window.findWindow接口来查找已经创建的窗口从而得到子窗口。
3. 设置子窗口属性。

  子窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

  
```json
// 移动子窗口位置。
windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to move the window. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in moving the window.');
});
// 改变子窗口大小。
windowClass.resize(500, 500, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in changing the window size.');
});
```

4. 加载显示子窗口的具体内容。

  使用setUIContent和showWindow接口加载显示子窗口的具体内容。

  
```json
// 为子窗口加载对应的目标页面。
windowClass.setUIContent("pages/page2", (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  if (!windowClass) {
    console.error('windowClass is null');
    return;
  }
  // 显示子窗口。
  windowClass.showWindow((err: BusinessError) => {
    let errCode: number = err.code;
    if (errCode) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });
});
```

5. 销毁子窗口。

  当不再需要某些子窗口时，可根据场景的具体实现逻辑，使用destroyWindow接口销毁子窗口。

  
```json
// 销毁子窗口。当不再需要某些子窗口时，可根据场景的具体实现逻辑，使用destroy接口销毁子窗口。
windowClass.destroyWindow((err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to destroy the subwindow. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in destroying the subwindow.');
});
```




##### 体验窗口沉浸式能力

在看视频、玩游戏等场景下，用户往往希望隐藏状态栏、导航栏等不必要的系统窗口，从而获得更佳的沉浸式体验。此时可以借助窗口沉浸式能力（窗口沉浸式能力都是针对应用主窗口而言的），达到预期效果。从API version 10开始，沉浸式窗口默认配置为全屏大小并由组件模块控制布局，状态栏、导航栏背景颜色为透明，文字颜色为黑色；应用窗口调用setWindowLayoutFullScreen接口，设置为true表示由组件模块控制忽略状态栏、导航栏的沉浸式全屏布局，设置为false表示由组件模块控制避让状态栏、导航栏的非沉浸式全屏布局。



##### 开发步骤
1. 获取主窗口对象。

  
> [!NOTE]
> 沉浸式能力需要在成功获取应用主窗口对象的前提下进行。 确保应用内最后显示的窗口为主窗口，然后再使用window.getLastWindow接口来获取得到主窗口。


  
```json
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let mainWindowClass: window.Window | null = null;

// 获取主窗口。
class BaseContext {
  stageMode: boolean = false;
}

let context: BaseContext = { stageMode: false };
window.getLastWindow(context, (err: BusinessError, data) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to get the mainWindow. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in getting mainWindow. Data: ' + JSON.stringify(data));
  mainWindowClass = data;
  if (!mainWindowClass) {
   console.error('mainWindowClass is null');
   return;
  }
});
```

2. 实现沉浸式效果。有以下两种方式：

  
方式一：应用主窗口为全屏窗口时，调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
3. 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。
4. 加载显示沉浸式窗口的具体内容。

  使用setUIContent和showWindow接口加载显示沉浸式窗口的具体内容。

  
```json
// 为沉浸式窗口加载对应的目标页面。
mainWindowClass.setUIContent("pages/page3", (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  if (!mainWindowClass) {
   console.error('mainWindowClass is null');
   return;
  }
  // 显示沉浸式窗口。
  mainWindowClass.showWindow((err: BusinessError) => {
    let errCode: number = err.code;
    if (errCode) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });
});
```
