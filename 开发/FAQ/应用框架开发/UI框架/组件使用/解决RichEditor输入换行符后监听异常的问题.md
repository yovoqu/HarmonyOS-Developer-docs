# 解决RichEditor输入换行符后监听异常的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1398

#### 问题现象

正常输入文字如'1，2，3'等，inputStr都能准确获取，如果先输入一个换行符，再输入文字,如'1，2，3'，'1'这个文字就获取不到，再次输入'2'，'3'能监听到，如何解决该问题？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct StackExample {
  private controller: RichEditorController = new RichEditorController()

  build() {
    Row() {
     <em> // 输入框</em>
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
          event.keepEditableState() <em>// 保持输入状态</em>
        })
        .onIMEInputComplete((value: RichEditorTextSpanResult) => {
       <em>   // 监听文字输入</em>
          const start = value.offsetInSpan[0]
          const end = value.offsetInSpan[1]
        <em>  // 获取输入的字符串</em>
          const inputStr = value.value.substring(start, end)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/bjIl7yT1RWGd8CGk9Y6EfQ/zh-cn_image_0000002628763130.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=6861D70653843F3EEA94219CDFE810FF16D715778E2C4C965031F0FD5131C50B)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nBDxk65oQguHx2oT_S2X5A/zh-cn_image_0000002658962443.png?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=A418B1B61BA8878CD6B3585E7BE4956940F3794ABE71A425F7F6323E2192625A)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/22B3MPGGTiSXb3pPpylDNA/zh-cn_image_0000002628603234.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=0DE34774A806FA9F02B964A2F55D8C5048557B5E7A19924DC74E2C9DB3103E5D)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JIQwt60CQcScmzsMmLKbUg/zh-cn_image_0000002658842497.png?HW-CC-KV=V1&HW-CC-Date=20260701T041329Z&HW-CC-Expire=86400&HW-CC-Sign=2E69440269DD91C33CFA65D207A3B526D7363BFA8C4EC136F7A8A0C63E8C57B1)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)支持图文混排和文本交互式编辑的组件。
 
- [onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onsubmit12)按下软键盘输入法回车键触发该回调。
- [onDidIMEInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#ondidimeinput12)输入法完成输入时，触发回调。
- [getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)获取span信息。
- [onIMEInputComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onimeinputcomplete)：输入法完成输入后，触发回调。

 
 

#### 解决方案

onIMEInputComplete接口仅支持返回一个文本span的信息，存在\n会触发span分裂，所以换行后监听异常。
 1. 使用onDidIMEInput代替onIMEInputComplete，获取当前输入内容的范围。
2. 使用getSpans获取当前输入的内容并打印，实现监听。
 
```text
@Entry
@Component
struct StackExample {
  private controller: RichEditorController = new RichEditorController();

  build() {
    Row() {
    <em>  // 输入框</em>
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
          event.keepEditableState(); <em>// 保持输入状态</em>
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
