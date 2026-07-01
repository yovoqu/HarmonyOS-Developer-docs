# 打开PhotoViewPicker时默认选中上次选中的图片

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-9

#### 问题现象

通过Media Library Kit的PhotoViewPicker实现选择系统相册图片，之前选择的图片没有默认选中。
 
预期效果：选择图片->完成提交->下次进入标记选中状态（不完成提交下次进入不选中）。
 
实际效果：选择图片->完成提交->下次进入未标记选中状态。
 
 

#### 背景知识

通过[PhotoViewPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker)选择系统相册图片时，可以使用PhotoSelectOptions属性控制选择的媒体文件类型、数量、预选择文件数据、推荐的媒体文件等。
 
 

#### 解决方案

PhotoViewPicker选择图片时不会对选择结果进行记录，建议可以自行保存每次选择的图片uri，再通过PhotoSelectOptions属性设置预选的图片数据。
 1. 将每次选择的图片uri缓存到数组preSelected中。
2. 通过PhotoSelectOptions中preselectedUris属性，将缓存的uri设置为预选择的图片。
 
完整示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">photoAccessHelper </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MediaLibraryKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">preSelected</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Select'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">photoSelectOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoSelectOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxSelectNumber </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">preselectedUris </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">preSelected</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MIMEType </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoViewMIMETypes</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">IMAGE_VIDEO_TYPE</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">photoViewPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoViewPicker</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoSelectResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">preSelected </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">photoUris</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Invoke photoViewPicker.select failed, code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
如果preselectedUris中预选择的图片已被删除，select接口不会报异常，也不会影响未删除的图片被默认选中。
 
目前PhotoViewPicker不支持将预选择的图片集中显示在列表头部，如果上次选中的图片是分散的，再次进入默认选中的图片仍然是分散的。
