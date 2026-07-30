# 使用bindPopup实现气泡占用全屏时TextInput可以输入文本的效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1331

#### 问题现象

使用TextInput和bindPopup如何实现带动态提示的输入框。需要实现以下效果：
 
- Popup的背景为透明，Popup显示时占用整个窗口。
- 当点击TextInput输入框时可以获取焦点输入文本，并且输入框失去焦点时隐藏Popup。

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/EORzekH6QxWKvTVkpjTVHA/zh-cn_image_0000002658839163.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072450Z&HW-CC-Expire=86400&HW-CC-Sign=7A0078F3CECB5D34498D600202E135C31C34E532BBBDD74FAF4BF5714B4A4075)

 
 

#### 背景知识

- [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)为[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)等组件绑定Popup气泡，可以设置[PopupOptions类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)下的backgroundBlurStyle属性为BlurStyle.NONE用来关闭气泡的模糊背景，可以使气泡变为透明。
- TextInput主要用于获取用户输入的信息，并将信息处理成数据进行上传，[添加事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input#添加事件)可以获取输入框内改变的文本内容。

 
 

#### 解决方案

实现气泡占用全屏时TextInput可以输入文本的效果，参考以下步骤：
 1. 定义message存储TextInput组件当前的文本内容，并且使用@State装饰。
```text
@State message: string = '';
```

2. 定义customPopup控制弹出框(Popup)的显示和隐藏状态。当customPopup为true时，弹出框显示，为false时，弹出框隐藏。
```text
@State customPopup: boolean = false;
```

3. 将弹出框(Popup)的尺寸设置为其可用空间的100%宽度和100%高度。
```text
@Builder
popupBuilder() {
  Row({ space: 2 }) {
    Text(this.tips).fontSize(15);
  }
  .alignItems(VerticalAlign.Center)
  .justifyContent(FlexAlign.Center)
  .width('100%')
  .height('100%') <em>// popup显示时占用整个窗口</em>
  .padding(5);
}
```

4. 创建TextInput输入框，使用onEditChange事件控制弹出框(Popup)的显示和隐藏，设置backgroundBlurStyle: BlurStyle.NONE禁用弹出框(Popup)弹出背景的模糊效果。
```text
build() {
  Column() {
    TextInput({ text: this.message, placeholder: '请输入姓名' })
      .margin({
        top: 50,
        left: 15,
        right: 15
      })
      .enableAutoFill(false)
      .bindPopup(this.customPopup, {
        builder: this.popupBuilder,
        placement: Placement.Bottom,
        mask: { color: '#33000000' },
        backgroundBlurStyle: BlurStyle.NONE,<em> </em><em>// 去除模糊背景填充效果</em>
        enableArrow: false, <em>// </em><em>隐藏箭头</em>
        autoCancel: true,
        showInSubWindow: false,
        onStateChange: (e) => {
          if (!e.isVisible) {
            this.customPopup = false; <em>// </em><em>点击了弹出框外部的区域，及时地将@State变量同步更新为false</em>
          }
        }
      })
      .onChange((value: string) => {
        this.message = value;
        if (value.length == 0) {
          this.tips = '';
          return;
        }

        if (!isChineseCharByRegex(value)) {
          this.tips = '您的输入有误，姓名只能为汉字';
        } else {
          this.tips = '';
        }
      })
      .onEditChange((isEditing: boolean) => {
      <em>  // isEditing为true表示输入框获得了焦点</em>
        if (isEditing) { <em>// </em><em>只有获得焦点才显示</em>
          this.customPopup = true;
        } else {
          this.customPopup = false; <em>// 输入框失去焦点时隐藏</em>
        }
      });
  }
  .width('100%')
  .height('100%');
}
```

 
完整示例参考如下：
 
```text
@Entry
@Component
struct BindPopUpDemo {
  @State message: string = '';
  @State customPopup: boolean = false;
  @State tips: string = '';

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Text(this.tips).fontSize(15);
    }
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')<em> </em><em>// popup显示时占用整个窗口</em>
    .padding(5);
  }

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入姓名' })
        .margin({
          top: 50,
          left: 15,
          right: 15
        })
        .enableAutoFill(false)
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Bottom,
          mask: { color: '#33000000' },
          backgroundBlurStyle: BlurStyle.NONE, <em>// 去除模糊背景填充效果</em>
          enableArrow: false,<em> </em><em>// 隐藏箭头</em>
          autoCancel: true,
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false; <em>// </em><em>点击了弹出框外部的区域，及时地将@State变量同步更新为false</em>
            }
          }
        })
        .onChange((value: string) => {
          this.message = value;
          if (value.length == 0) {
            this.tips = '';
            return;
          }

          if (!isChineseCharByRegex(value)) {
            this.tips = '您的输入有误，姓名只能为汉字';
          } else {
            this.tips = '';
          }
        })
        .onEditChange((isEditing: boolean) => {
        <em>  // isEditing为true表示输入框获得了焦点</em>
          if (isEditing) {<em> </em><em>// 只有获得焦点才显示</em>
            this.customPopup = true;
          } else {
            this.customPopup = false; <em>// </em><em>输入框失去焦点时隐藏</em>
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}

function isChineseCharByRegex(char: string): boolean {
  return /^[\u4e00-\u9fa5\u3400-\u4dbf\ud840-\ud87f\udc00-\udfff\uF900-\uFAFF]+$/.test(char);
}
```
