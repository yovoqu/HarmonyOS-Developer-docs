# attach设置软键盘属性inputAttribute不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-784

#### 问题现象

inputAttribute属性用于设置enter键的功能类型，enterKeyType:5表示"下一步"。TextInput使用attach方法唤起的软键盘，设置的inputAttribute属性初次生效，enter键的功能为"下一步"，关闭键盘后再拉起键盘，inputAttribute属性失效，enter键的功能为"完成"。
 
问题代码示例参考如下：
 
```text
onFocus(() => {
  let textConfig: inputMethod.TextConfig = {
    inputAttribute: {
      textInputType: 0,
      enterKeyType: 5
    }
  };
  let inputMethodController = inputMethod.getController()
  inputMethodController.attach(true, textConfig, () => {
  });
})
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fT21AMxITBWIHP2sOIpAaw/zh-cn_image_0000002658916947.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072329Z&HW-CC-Expire=86400&HW-CC-Sign=4CD06171ECC3C1BC1CD8D41790F0DD221E3AF57F35DB9806DC53806B41B2ADF2)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/_TRTnWHNTN-bvrgtezPGmg/zh-cn_image_0000002628397738.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072329Z&HW-CC-Expire=86400&HW-CC-Sign=EF2B67F440DC8D6DB9706AA03DC1A63B49C802E932F3984D4850D51EDB245272)

 
 

#### 背景知识

- [attach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#attach10)：自绘控件绑定输入法。使用callback异步回调。
- [updateAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#updateattribute10)：更新编辑框属性信息。使用callback异步回调。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。

 
 

#### 解决方案

使用updateAttribute方法设置inputAttribute属性。
 
```text
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct CustomPopup {
  @State message: string = '';

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入正确内容' })
        .onChange((value: string) => {
          this.message = value;
        })
        .focusable(true)
        .margin({ top: 100, left: 10, right: 10 })
        .onFocus(() => {
          let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 5 };
          let inputMethodController = inputMethod.getController();
          inputMethodController.updateAttribute(inputAttribute, () => {
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
