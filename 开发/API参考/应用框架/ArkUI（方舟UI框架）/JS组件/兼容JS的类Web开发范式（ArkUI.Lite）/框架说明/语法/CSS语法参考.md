# CSS语法参考

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-css
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

CSS是描述HML页面结构的样式语言。所有组件均存在系统默认样式，也可在页面CSS样式文件中对组件、页面自定义不同的样式。


## 样式导入
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

为了模块化管理和代码复用，CSS样式文件支持 @import 语句，导入 CSS 文件。


## 声明样式
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

每个页面目录下存在一个与布局hml文件同名的css文件，用来描述该hml页面中组件的样式，决定组件应该如何显示。


1. 内部样式，支持使用style、class属性来控制组件的样式。例如：  __PREBLOCK_0__  __PREBLOCK_1__
2. 文件导入，合并外部样式文件。例如，在common目录中定义样式文件style.css，并在index.css文件首行中进行导入：  __PREBLOCK_2__  __PREBLOCK_3__


## 选择器
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

css选择器用于选择需要添加样式的元素，支持的选择器如下表所示：


| 选择器 | 样例 | 样例描述 |
| --- | --- | --- |
| .class | .container | 用于选择class="container"的组件。 |
| #id | #titleId | 用于选择id="titleId"的组件。 |
| , | .title, .content | 用于选择class="title"和class="content"的组件。 |


示例：


```text
<!-- 页面布局xxx.hml -->
<div id="containerId" class="container">
<text id="titleId" class="title">标题</text>
<div class="content">
<text id="contentId">内容</text>
</div>
</div>
```


```text
/* 页面样式xxx.css */
/* 对class="title"的组件设置样式 */
.title {
font-size: 30px;
}
/* 对id="contentId"的组件设置样式 */
#contentId {
font-size: 20px;
}
/* 对所有class="title"以及class="content"的组件都设置padding为5px */
.title, .content {
padding: 5px;
}
```


## 伪类
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

css伪类是选择器中的关键字，用于指定要选择元素的特殊状态。


| 名称 | 支持组件 | 描述 |
| --- | --- | --- |
| :active | input[type="button"] | 表示被用户激活的元素，如：被用户按下的按钮。轻量级智能穿戴上伪类选择器上仅支持background-color 和background-image 的样式设置。 |
| :checked | input[type="checkbox"、type="radio"] | 表示checked属性为true的元素。轻量级智能穿戴上伪类选择器上仅支持background-color 和background-image 的样式设置。 |


伪类示例如下，设置按钮的:active伪类可以控制被用户按下时的样式：


```text
<!-- index.hml -->
<div class="container">
<input type="button" class="button" value="Button"></input>
</div>
```


```text
/* index.css */
.button:active {
background-color: #888888;/*按钮被激活时，背景颜色变为#888888 */
}
```


## 样式预编译
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

预编译提供了利用特有语法生成css的程序，可以提供变量、运算等功能，令开发者更便捷地定义组件样式，目前支持less、sass和scss的预编译。使用样式预编译时，需要将原css文件后缀改为less、sass或scss，如index.css改为index.less、index.sass或index.scss。


- 当前文件使用样式预编译，例如将原index.css改为index.less：  __PREBLOCK_8__
- 引用预编译文件，例如common中存在style.scss文件，将原index.css改为index.scss，并引入style.scss：  __PREBLOCK_9__  在index.scss中引用：  __PREBLOCK_10__  ![](assets/CSS语法参考/file-20260514164245963-0.png)    引用的预编译文件建议放在common目录进行管理。
