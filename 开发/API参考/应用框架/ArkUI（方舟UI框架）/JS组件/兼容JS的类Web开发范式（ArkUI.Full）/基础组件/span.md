# span

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-span
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
作为<[text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-text)>子组件提供文本修饰能力。
  

#### 权限列表

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。
 
> [!NOTE]
> 不支持focusable和disabled属性。

 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

仅支持如下样式：
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | &lt;color&gt; | - | 否 | 设置文本段落的文本颜色。 |
| font-size | &lt;length&gt; | 30px | 否 | 设置文本段落的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置文本段落的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | string | normal | 否 | 设置文本段落的字体样式，见text组件font-style的样式属性。 |
| font-weight | number \| string | normal | 否 | 设置文本段落的字体粗细，见text组件font-weight的样式属性。 |
| text-decoration | string | none | 否 | 设置文本段落的文本修饰，见text组件text-decoration样式属性。 |
| font-family | string | sans-serif | 否 | 设置文本段落的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |
 
 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

仅支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)中的click事件。
 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="container">
  <text class="title">
    <span class="spanTxt">span</span>
  </text>
</div>
```
 
```text
/* xxx.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.title {
  font-size: 30px;
  text-align: center;
  width: 100%;
  height: 100px;
}
.spanTxt{
  color: chartreuse;
  font-size: 80px;
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/UQchKBquQ_-Uh4gK0kdeyg/zh-cn_image_0000002611836171.png?HW-CC-KV=V1&HW-CC-Date=20260528T025438Z&HW-CC-Expire=86400&HW-CC-Sign=D4E7CB361C85331892620B30679A5581B65A5AD90B5FB615DDD7C5C5832E568E)
