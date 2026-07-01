# 在RichEditor中格式化展示字符串文本

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1374

#### 问题现象

应用缓存的数据使用字符串保存，其中包含如：#话题、@好友这一类自定义样式的内容，如何回显到RichEditor组件中？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/eXGb2EBwQv2kiZRipBt-tA/zh-cn_image_0000002628602040.png?HW-CC-KV=V1&HW-CC-Date=20260701T041300Z&HW-CC-Expire=86400&HW-CC-Sign=113D432C5FDD4DA3E08E099FA837C49871C360A18A4D8F7E5071672F2A0D2ADA)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor)是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。可以通过[addTextSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan)添加文本内容以及[addBuilderSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addbuilderspan11)添加@Builder装饰器修饰的内容。
 
 

#### 解决方案

获取缓存数据时需要解析成对应格式后展示。用js正则匹配出需要的正常文本内容通过addTextSpan添加到输入框中，接着通过addBuilderSpan自定义样式内容插入后面。示例代码为：
 
```json
interface FormatText {
  'content': string;
  'sendFriend': SendFriendText[];
  'topic': TopicText;
}

interface SendFriendText {
  'name': string;
  'id': string;
}

interface TopicText {
  'topicContent': string;
}

@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      RichEditor(this.option)
        .onAppear(() => {
          let cacheData: string = `{
              "content": "哈哈哈&&topic&&&&at&&&&at&&",
              "sendFriend":
              [{
                "name": "测试名称1",
                "id": "1"
              },
              {
                "name": "测试名称2",
                "id": "2"
              }],
              "topic": {
                "topicContent": "测试话题'"
              }
            }`;
          const controller = this.controller;
          const regex = /&&(.*)&&/;
          let resolveData = JSON.parse(cacheData) as FormatText;
          let postContent = resolveData.content;
          let normalText: string = postContent.replace(regex, '');
          let topic = resolveData.topic.topicContent;
          let atNames: string[] = resolveData.sendFriend.map((item: SendFriendText) => item.name);
          controller.addTextSpan(normalText, { style: { fontColor: Color.Black, fontSize: 14 } });
          controller.addBuilderSpan(() => this.AtSpan(`#${topic}#`), {
            offset: controller.getCaretOffset()
          });
          atNames.map((name: string) => {
            controller.addBuilderSpan(() => this.AtSpan(`@${name}`), {
              offset: controller.getCaretOffset()
            });
          });
        })
    }
    .width('100%')
    .height('100%')
  }

  @Builder
  AtSpan(span: string) {
    Text(span)
      .fontSize(14)
      .fontColor('#007dff')
  }
}
```
