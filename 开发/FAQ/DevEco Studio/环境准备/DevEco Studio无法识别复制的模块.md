# DevEco Studio无法识别复制的模块

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-28

#### 问题现象

- 复制一个模块到新项目，DevEco Studio无法识别模块，导致无法打包。
- 使用版本控制软件拉取他人代码到本地，未正确识别module，文件夹右下角没有蓝色角标，打包报错：
```text
<span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Try the </span><span style="color: rgb(181,106,1);">following</span><span style="color: rgb(181,106,1);">:</span>
<span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">Check whether the </span>module <span style="color: rgb(0,0,255);">which </span><span style="color: rgb(181,106,1);">D</span><span style="color: rgb(181,106,1);">:</span>\<span style="color: rgb(0,0,255);">xxx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ets belongs to is correctly configured</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">Check the corresponding file name is </span><span style="color: rgb(0,0,255);">correct</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">including case</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">sensitivity</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span>
```


 
 

#### 解决方案

- 如果是通过import形式导入模块，可以参考文档：[导入Module](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-module#section13771399184)。具体步骤如下：1. 在菜单栏单击File > New > Import... > Import Module。

2. 选择导入的模块。在指定路径下，选择导入的模块，单击OK。导入的模块可以为文件夹，也可以为zip格式。

 
- 若是从其他项目复制的/拉取他人代码的模块，在工程级别的build-profile.json5中，在app.modules数组中添加一个对象，其中name属性为实际模块名称、src属性为实际模块相对路径。如：{"name":"harlibrary","srcPath":"./harlibrary"}。
