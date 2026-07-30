# 通过页面跳转将CardRecognition控件拍照界面关闭

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-2

#### 问题现象

通过设置了两个[setTimeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#settimeout)定时器控制[CardRecognition（卡证识别控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition)实现拍照界面关闭，预期效果是进入页面五秒后，会渲染CardRecognition控件，在进入页面十秒后，会销毁CardRecognition控件。
 
 

#### 背景知识

当前系统已支持卡证识别控件提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。CardRecognition控件会拉起的是一个系统的全模态弹窗，页面组件的显隐状态无法关闭该弹窗。
 
 

#### 解决方案

将CardRecognition控件单独放在一个页面，设置定时器通过页面路由跳转来实现自主关闭卡证识别拍摄功能。核心代码参考如下：
 
- Index.ets：
```text
@Entry
@Component
struct Index {
  pathStack: NavPathStack = new NavPathStack();

  <em>// </em><em>卡证识别入口按钮</em>
  build() {
    Navigation(this.pathStack) {
      Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
        .width('50%')
        .height(40)
        .onClick(() => {
          this.pathStack.pushPathByName('cardDemoPage', null);
        });
    }.title('卡证识别控件demo')
    .mode(NavigationMode.Stack);
  }
}
```


 
- CardDemoPage.ets
```json
import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'CardRecognitionPage';

@Builder
export function CardDemoPageBuilder() {
  CardDemoPage();
}

<em>// </em><em>卡证识别页，用于加载uiExtensionAbility</em>
@Component
export struct CardDemoPage {
  pathStack: NavPathStack = new NavPathStack();
  timerId: number = -1;

  aboutToDisappear(): void {
  <em>  // 子页面销毁时清除定时器</em>
    if (this.timerId !== -1) {
      clearTimeout(this.timerId);
    }
  }

  build() {
    NavDestination() {
      CardRecognition({
      <em>  // 此处选择身份证类型作为示例</em>
        supportType: CardType.CARD_ID,
        cardSide: CardSide.DEFAULT,
        cardRecognitionConfig: {
          defaultShootingMode: ShootingMode.MANUAL,
          isPhotoSelectionSupported: true
        },
        onResult: ((params: CardRecognitionResult) => {
          hilog.info(0x0001, TAG, `params code: ${params.code}`);
          hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
          hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
         <em> // 手动返回或扫描到结果返回上个页面</em>
          this.goBack();
        })
      });
    }
    .width('100%')
    .height('100%')
    .hideTitleBar(true)
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
      hilog.info(0x0001, TAG, `current page config info is ${JSON.stringify(context.getConfigInRouteMap())}`);
    })
    .onShown(() => {
    <em>  // 当该NavDestination页面显示时设置定时器，定时触发路由返回</em>
      this.timerId = setTimeout(() => {
        this.goBack();
      }, 5000);
    });
  }

 <em> /**</em>
<em>   * 1.如果返回的是Navigation根页面需要使用getRouter()返回</em>
<em>   * 2.如果返回的是NavDestination子页面可使用NavPathStack返回</em>
<em>   */</em>
  goBack() {
    this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' });
  }
}
```

- router_map.json：
```ArkTS
{
  "routerMap": [
    {
      "name": "cardDemoPage",
      "pageSourceFile": "src/main/ets/pages/CardDemoPage.ets",
      "buildFunction": "CardDemoPageBuilder",
      "data": {
        "description": "this is cardDemoPage"
      }
    }
  ]
}
```


 
> [!NOTE]
> 不要在同一界面设置两个定时器，否则第二个定时器执行后也不会关闭拍照界面。
