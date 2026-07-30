# 如何实现在class函数中直接调用自定义弹窗API

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-791

#### 问题现象

如何实现可以在class类函数中直接调用的类似promptAction.showDialog()功能的自定义弹窗。当前需要在class函数中自定义显示loading转圈。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/MB7aM4yVTtWIIwCCFWRI_A/zh-cn_image_0000002628557636.png?HW-CC-KV=V1&HW-CC-Date=20260730T072329Z&HW-CC-Expire=86400&HW-CC-Sign=968A2A0E5AB60ECBDD8C3F4E3AD0A58B5EA7764C10C4E9B85FA6A4CA73FC7341)

 
 

#### 背景知识

[getPromptAction().openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12)：打开自定义弹窗。需使用UIContext中的getPromptAction获取PromptAction对象，再通过此对象调用替代方法openCustomDialog。
 
 

#### 解决方案

自定义loading动效的弹窗样式，再封装一个单实例可调出弹窗的openCustomDialog静态方法。只需在全局调用此方法即可唤出弹窗。
 
```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent } from '@kit.ArkUI';

@Entry
@Component
struct DialogLoadingProgress {
  ctx: UIContext = this.getUIContext();

  build() {
    Column() {
      Button('测试').onClick(() => {
        ShowTest.getIns().openDialog(this.ctx);
      });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}

@Builder
function dialogStyle() {
  Column() {
    LoadingProgress()
      .color(Color.Black)
      .width(80).height(80);
  }
  .height(200)
  .padding(5)
  .justifyContent(FlexAlign.Center)
  .width('94%')
  .borderRadius(32)
  .backgroundColor(Color.White);
}

export class ShowTest {
  private static ins: ShowTest; <em>// 单例模式去调用</em>
  constructor() {
    ShowTest.ins = this;
  }

  public static getIns() {
    if (!ShowTest.ins) {
      ShowTest.ins = new ShowTest();
    }
    return ShowTest.ins;
  }

  openDialog(ctx: UIContext) {
    let contentNode: ComponentContent<[]> | null = null;
    contentNode = new ComponentContent(ctx, wrapBuilder(dialogStyle));
    ctx.getPromptAction().openCustomDialog(contentNode).catch((e: BusinessError) => {
      console.error(`e: ${e}`);
    });
  }
}
```
 
 

#### 总结

效果与常规的自定义弹窗无太大区别。问题需求是封装全局导出的弹窗类，不再依赖UI页面创建自定义弹窗。在需要时可直接调用弹窗类并传入页面的UIContext以创建弹窗，再通过@Builder函数自定义弹窗内容。相比于常规的[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)自定义弹窗，用法更加方便，无需再在当前页面中定义弹窗组件。
