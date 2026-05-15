# menu开发指导

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-menu

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作，具体用法请参考[menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu)。


## 创建menu组件

在pages/index目录下的hml文件中创建一个menu组件，添加target、type、title属性。
```text


  show menu

    Item 1
    Item 2
    Item 3


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.title-text{
  font-size: 35px;
}
```

![](assets/menu开发指导/file-20260514130754320-0.png)
> [!NOTE]
> menu仅支持option子组件。 menu组件不支持focusable、disabled属性。


## 设置样式

为menu组件设置样式，例如字体颜色、大小、字符间距等。
```text


  show menu

    Item 1
    Item 2
    Item 3


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.title-text{
  font-size: 35px;
  background-color: #5a5aee;
  color: white;
  width: 70%;
  text-align: center;
  height: 85px;
  border-radius: 12px;
}
.menu{
  text-color: blue;
  font-size: 35px;
  letter-spacing: 2px;
}
option{
  color: #6a6aef;
  font-size: 30px;
}
```

![](assets/menu开发指导/file-20260514130754320-1.png)

## 绑定事件

为menu组件绑定oncancel事件（取消操作时触发）。
```text


  show menu

    Item 1
    Item 2
    Item 3


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  width: 100%;
}
.title-text{
  font-size: 35px;
  background-color: #5a5aee;
  color: white;
  width: 70%;
  text-align: center;
  height: 85px;
  border-radius: 12px;
  margin-top: 500px;
  margin-left: 15%;
}
menu{
  text-color: blue;
  font-size: 35px;
  letter-spacing: 2px;
}
option{
  color: #6a6aef;
  font-size: 30px;
}
```


```text
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  cancel() {
    promptAction.showToast({
      message: "cancel"
    })
  },
  textClick() {
    this.$element("menuId").show({ x: 175,y: 590 });
  }
}
```

![](assets/menu开发指导/file-20260514130754320-2.gif)
