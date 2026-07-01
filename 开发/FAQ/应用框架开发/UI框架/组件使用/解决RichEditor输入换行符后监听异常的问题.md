# 解决RichEditor输入换行符后监听异常的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1398

## 解决RichEditor输入换行符后监听异常的问题
 


##### 问题现象

正常输入文字如'1，2，3'等，inputStr都能准确获取，如果先输入一个换行符，再输入文字,如'1，2，3'，'1'这个文字就获取不到，再次输入'2'，'3'能监听到，如何解决该问题？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct StackExample {
  private controller: RichEditorController = new RichEditorController()

  build() {
    Row() {
      // 输入框
      RichEditor({ controller: this.controller })
        .backgroundColor(Color.Gray)
        .enterKeyType(EnterKeyType.NEW_LINE)
        .width('100%')
        .constraintSize({
          maxHeight: 100,
          minHeight: 35
        })
        .defaultFocus(true)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          event.keepEditableState() // 保持输入状态
        })
        .onIMEInputComplete((value: RichEditorTextSpanResult) => {
          // 监听文字输入
          const start = value.offsetInSpan[0]
          const end = value.offsetInSpan[1]
          // 获取输入的字符串
          const inputStr = value.value.substring(start, end)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/bjIl7yT1RWGd8CGk9Y6EfQ/zh-cn_image_0000002628763130.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025613Z&HW-CC-Expire=86400&HW-CC-Sign=CC3D8A018738076C662780256AD57C7EBA1F5315ABC5C1BAAE0C90E64BCD9646)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nBDxk65oQguHx2oT_S2X5A/zh-cn_image_0000002658962443.png?HW-CC-KV=V1&HW-CC-Date=20260701T025613Z&HW-CC-Expire=86400&HW-CC-Sign=0B337C94774400BFE4F840B2FA7476751F88781B42A2E88B3B54A1C4E46BFFB4)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/22B3MPGGTiSXb3pPpylDNA/zh-cn_image_0000002628603234.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025613Z&HW-CC-Expire=86400&HW-CC-Sign=D8A4625305646BDA024ED1E293DF6DC7B4243F85C819A621562833550CE51C74)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JIQwt60CQcScmzsMmLKbUg/zh-cn_image_0000002658842497.png?HW-CC-KV=V1&HW-CC-Date=20260701T025613Z&HW-CC-Expire=86400&HW-CC-Sign=97E19F4D9517EC131EB8B7BCBDD95D2EE011683316367C529E131B19BC278098)

 
 

##### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)支持图文混排和文本交互式编辑的组件。
 
- [onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onsubmit12)按下软键盘输入法回车键触发该回调。
- [onDidIMEInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#ondidimeinput12)输入法完成输入时，触发回调。
- [getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)获取span信息。
- [onIMEInputComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onimeinputcomplete)：输入法完成输入后，触发回调。

 
 

##### 解决方案

onIMEInputComplete接口仅支持返回一个文本span的信息，存在\n会触发span分裂，所以换行后监听异常。
 
- 使用onDidIMEInput代替onIMEInputComplete，获取当前输入内容的范围。
- 使用getSpans获取当前输入的内容并打印，实现监听。

 
```text
@Entry
@Component
struct StackExample {
  private controller: RichEditorController = new RichEditorController();

  build() {
    Row() {
      // 输入框
      RichEditor({ controller: this.controller })
        .backgroundColor(Color.Gray)
        .enterKeyType(EnterKeyType.NEW_LINE)
        .width('100%')
        .constraintSize({
          maxHeight: 100,
          minHeight: 35
        })
        .defaultFocus(true)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          event.keepEditableState(); // 保持输入状态
        })
        .onDidIMEInput((value: TextRange) => {
          const start = value.start;
          const end = value.end;
          const curSpans = this.controller.getSpans({
            start: start,
            end: end
          });
          curSpans.forEach(item => {
            if (typeof (item as RichEditorTextSpanResult)) {
              const cur = item as RichEditorTextSpanResult;
              console.info("输入的字符: " + cur.value.substring(cur.offsetInSpan[0], cur.offsetInSpan[1]));
            }
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
