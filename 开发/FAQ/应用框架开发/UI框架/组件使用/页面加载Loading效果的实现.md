# 页面加载Loading效果的实现

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-825

#### 问题现象

页面加载时有时延，较长时会被感知到，如何解决该问题？
 
 

#### 背景知识

- [LoadingProgress()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress)是用于显示加载动效的组件。
- [rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation)用于设置组件旋转。
- [animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)属性动画实现渐变过渡效果。

 
 

#### 解决方案

根据业务场景，有三种方案实现该效果：
 1. 参考LoadingProgress()[示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress#示例1设置颜色)。
2. 通过图片旋转模拟Loading效果。
```text
@Entry
@Component
struct LoadingExample {
  @State loading: boolean = false;

  build() {
    Column({ space: 20 }) {
      LoadingView({ loading: this.loading })
      Row({ space: 20 }) {
        Button('开始').onClick(() => {
          this.loading = true;
        })

        Button('结束').onClick(() => {
          this.loading = false;
        })
      }
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct LoadingView {
  @Prop loading: boolean = false;
  <em>//图片旋转角度</em>
  @State angel: number = 0;

  build() {
    Image($r('app.media.startIcon'))  <em>// 图片资源自行替换</em>
      .width(30)
      .height(30)
      .rotate({
        centerX: "50%",
        centerY: "50%",
        angle: this.angel,
      })
      .draggable(false)
      .visibility(this.loading ? Visibility.Visible : Visibility.None)
      .onAppear(() => {
        this.getUIContext()?.animateTo({
          curve: Curve.Linear,
          playMode: PlayMode.Normal,
          iterations: -1, <em>// </em><em>设置-1表示动画无限循环</em>
          onFinish: () => {
          }
        }, () => {
          this.angel = 360;
        });
      })
  }
}
```
 代码运行效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/sUiS152zR-qciaaApdArog/zh-cn_image_0000002628398440.png?HW-CC-KV=V1&HW-CC-Date=20260701T041332Z&HW-CC-Expire=86400&HW-CC-Sign=F2CF69A5FBB8288C2CF7806B41D00103CF10D04A8DB8E548C44A8DEA7830A740)

1. 自定义LoadingView，供全局调用。
自定义LoadingView.ets。
```text
export class LoadingTime {
<em>  // 显示时间为baseTime+msg.length*wordTime</em>
  static baseTime: number = 400; <em>// 消息显示基本时间</em>
  static wordTime: number = 90; <em>// </em><em>每个字增加显示的时间</em>

 <em> // 最终显示时间为上面计算结果限制到最短与最长之间</em>
  static minTime: number = 1600; <em>// 最短显示时间</em>
  static maxTime: number = 4200; <em>// 最长显示时间</em>
};

export enum LoadingType {
  Loading = 0,
  Info,
  Success,
  Error,
  Length
};

interface LoadingParam {
  msg: string,
  cancelCallBack?: () => void,
  alignment?: DialogAlignment,
  offset?: Offset,
  showInSubWindow?: boolean,
  isModal?: boolean,
  tmpHUDNum?: number,<em> </em><em>// 缓存HUD的数量，用于多层返回HUD不显示情况</em>
};

@Entry
@CustomDialog
struct _LoadingView {
  controller: CustomDialogController;
  close: () => void = () => {
  };
  type: LoadingType = LoadingType.Loading;
  image: ResourceStr | undefined = undefined;
  @State angle: number = 0;
  msg: string = '';

  aboutToAppear() {
    if (this.type === LoadingType.Loading) {
      setTimeout(() => {
        this.angle = 360;
      }, 100);
    }
  }

  build() {
    Column() {
      if (this.type === LoadingType.Loading) {
        Row()
          .width(this.getUIContext().px2vp(200))
          .height(this.getUIContext().px2vp(200))
          .sweepGradient({
            center: [this.getUIContext().px2vp(100), this.getUIContext().px2vp(100)],
            rotation: 280,
            start: 0,
            end: 360,
            colors:
            [['rgba(255, 255, 255, 0.0)', 0.0], ['rgba(255, 255, 255, 0.0)', 0.18], ['rgba(255, 255, 255, 1.0)', 1.0]]
          })
          .clipShape(new Path({
            width: 100, height: 100, commands:
            `M100 10 A90 90 0 1 0 190 100 A2 8 0 1 0 182 100 A82 82 0 1 1 100 18 A4 4 0 0 0 100 10 Z`
          }))
          .rotate({
            z: 1,
            angle: this.angle
          })
          .animation({
            duration: 1000,
            curve: Curve.Linear,
            iterations: -1,
            expectedFrameRateRange: {
              min: 20,
              max: 60,
              expected: 60,
            }
          })
          .scale({ x: 0.9, y: 0.9 })
      } else if (this.image) {
        Image(this.image)
          .fitOriginalSize(true)
          .objectFit(ImageFit.None)
      }
      if (this.msg) {
        Text(this.msg)
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .padding({ top: this.type === LoadingType.Loading || this.image ? 10 : 0 })
      }
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .padding(12)
    .margin(30)
    .backgroundColor(Color.Black)
    .borderRadius(10)
    .shadow({
      radius: 10,
      color: Color.Gray,
      offsetX: 3,
      offsetY: 0
    })
  }
}

let _dialogController: CustomDialogController | null;
let _cancelCallBack: (() => void) | undefined;

let tmpHUDArray: LoadingView[] = [];

@Component
export struct LoadingView {
  showLoading(
    msg: string | LoadingParam = '',
    cancelCallBack?: () => void,
    alignment?: DialogAlignment,
    offset?: Offset,
    showInSubWindow?: boolean,
    isModal?: boolean,
    tmpHUDNum: number = 1, <em>// </em><em>缓存HUD的数量，用于多层返回HUD不显示情况</em>
  ): void {
    if (typeof msg === 'string') {
      this.showType(LoadingType.Loading, undefined, msg, cancelCallBack, alignment, offset, showInSubWindow, isModal);
    } else {
      this.showType(LoadingType.Loading, undefined, msg.msg, msg.cancelCallBack, msg.alignment, msg.offset,
        msg.showInSubWindow, msg.isModal);
      tmpHUDNum = msg.tmpHUDNum ?? 1;
    }

   <em> // 用于解决网络返回或者其它情况下不显示的问题</em>
    if (tmpHUDArray.length < tmpHUDNum) {
      for (let index = 0; index < tmpHUDNum; index++) {
        tmpHUDArray.push(new LoadingView());
      }
    }
  }

  showInfo(
    msg: string | LoadingParam = '',
    cancelCallBack?: () => void,
    alignment?: DialogAlignment,
    offset?: Offset,
    showInSubWindow?: boolean,
    isModal?: boolean,
  ): void {
    if (typeof msg === 'string') {
      this.showType(LoadingType.Info, undefined, msg, cancelCallBack, alignment, offset, showInSubWindow, isModal);
    } else {
      this.showType(LoadingType.Info, undefined, msg.msg, msg.cancelCallBack, msg.alignment, msg.offset,
        msg.showInSubWindow, msg.isModal);
    }
  }

  showSuccess(
    msg: string | LoadingParam = '',
    cancelCallBack?: () => void,
    alignment?: DialogAlignment,
    offset?: Offset,
    showInSubWindow?: boolean,
    isModal?: boolean,
  ): void {
    if (typeof msg === 'string') {
      this.showType(LoadingType.Success, $r('app.media.startIcon'), msg, cancelCallBack, alignment, offset,
        showInSubWindow, isModal);
    } else {
      this.showType(LoadingType.Success, $r('app.media.startIcon'), msg.msg, msg.cancelCallBack, msg.alignment,
        msg.offset, msg.showInSubWindow, msg.isModal);
    }
  }

  showError(
    msg: string | LoadingParam = '',
    cancelCallBack?: () => void,
    alignment?: DialogAlignment,
    offset?: Offset,
    showInSubWindow?: boolean,
    isModal?: boolean,
  ): void {
    if (typeof msg === 'string') {
      this.showType(LoadingType.Error, $r('app.media.startIcon'), msg, cancelCallBack, alignment, offset,
        showInSubWindow, isModal);
    } else {
      this.showType(LoadingType.Error, $r('app.media.startIcon'), msg.msg, msg.cancelCallBack, msg.alignment,
        msg.offset, msg.showInSubWindow, msg.isModal);
    }
  }

  showType(
    type: LoadingType,
    image: Resource | undefined,
    msg: string,
    cancelCallBack?: () => void,
    alignment: DialogAlignment = DialogAlignment.Center,
    offset: Offset = { dx: 0, dy: 0 },
    showInSubWindow: boolean = false,
    isModal: boolean = false,
    useTmpHUD: boolean = true <em>// 是否使用缓存的HUD</em>
  ): void {
    let self: LoadingView | undefined = this;
    if (useTmpHUD && tmpHUDArray.length > 0) {
      self = tmpHUDArray.shift();
    };
    self?.showTypeReal(type, image, msg, cancelCallBack, alignment, offset, showInSubWindow, isModal);
  }

  private showTypeReal(
    type: LoadingType,
    image: Resource | undefined,
    msg: string,
    cancelCallBack?: () => void,
    alignment: DialogAlignment = DialogAlignment.Center,
    offset: Offset = { dx: 0, dy: 0 },
    showInSubWindow: boolean = false,
    isModal: boolean = false,
  ): void {
    this.hide();

    _cancelCallBack = cancelCallBack;

    let animate: AnimateParam = {
      duration: 90,
      delay: 0,
      curve: Curve.EaseInOut
    };

    _dialogController = new CustomDialogController({
      builder: _LoadingView({ type: type, image: image, msg: msg }),
      autoCancel: false,
      cancel: () => {
        _dialogController = null;
        if (_cancelCallBack) {
          _cancelCallBack();
        };
      },
      customStyle: true,
      alignment: alignment,
      offset: offset,
      maskColor: 0x33000000,
      openAnimation: animate,
      closeAnimation: animate,
      showInSubWindow: showInSubWindow,
      isModal: isModal, <em>// api11是否有蒙层</em>
    });
    _dialogController.open();
    if (type !== LoadingType.Loading) {
      let time: number = LoadingTime.baseTime;
      if (msg) {
        time += msg.length * LoadingTime.wordTime;
      }
      time = Math.max(time, LoadingTime.minTime);
      time = Math.min(time, LoadingTime.maxTime);
      setTimeout(() => {
        this.hide();
      }, time);
    }
  }

  hide() {
    if (_dialogController) {
      _dialogController.close();
      _dialogController = null;
      if (_cancelCallBack) {
        _cancelCallBack();
      }
    }
  }

  build() {
  }
}
```

2. Index引入使用。
```text
import { LoadingView } from './LoadingView';

@Entry
@Component
struct Index {
  loadingView: LoadingView = new LoadingView();

  build() {
    NavDestination() {
      Column({ space: 30 }) {
        Button('Toast提示有文案')
          .onClick(() => {
            this.loadingView.showLoading({ msg: '数据加载中' });
            setTimeout(() => {
              this.loadingView.hide();
            }, 1000);
          })
        Button('loading有蒙层')
          .onClick(() => {
            this.loadingView.showLoading({ msg: '数据加载中', isModal: true });
            setTimeout(() => {
              this.loadingView.hide();
            }, 1000);
          })
        Button('信息提示')
          .onClick(() => {
            this.loadingView.showInfo('这里是Toast提示信息');
          })
        Button('成功')
          .onClick(() => {
            this.loadingView.showSuccess('数据加载成功');
          })
        Button('失败')
          .onClick(() => {
            this.loadingView.showError('数据加载失败');
          })
        Button('Toast')
          .onClick(() => {
            this.loadingView.showLoading();
            setTimeout(() => {
              this.loadingView.hide();
            }, 1000);
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```
 代码运行效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/4RwYKHaHT3SdY3ptX_k2tg/zh-cn_image_0000002658797721.png?HW-CC-KV=V1&HW-CC-Date=20260701T041332Z&HW-CC-Expire=86400&HW-CC-Sign=57B4A9CA7E71B5446201F5247A3EFC50BE5F716B6D15FDA60F604DA8E2F88155)
