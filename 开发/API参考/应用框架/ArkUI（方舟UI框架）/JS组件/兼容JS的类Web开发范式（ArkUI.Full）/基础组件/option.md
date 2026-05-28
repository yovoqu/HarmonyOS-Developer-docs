# option

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
当作为<[select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select)>的子组件时用来展示下拉选择的具体项目。
 
当作为<[menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu)>的子组件时用来展示弹出菜单的具体项目。
  

#### 权限列表

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| selected | boolean | - | 否 | 选择项是否为下拉列表的默认项，仅在父组件是select时生效。true表示该选项是下拉列表的默认项，false表示该选项不是下拉列表的默认项。 |
| value | string | - | 是 | 该属性定义选项值，将作为父组件select/menu的selected事件回调参数。 option选项的UI展示值需要放在标签内，如： <option value="10">十月</option> |
| icon | string | - | 否 | 图标资源路径，该图标展示在选项文本前，图标格式为jpg，png和svg。 |
 
 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持如下样式。
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | &lt;color&gt; | #e6000000 | 否 | 选择项的文本颜色。 |
| font-size | &lt;length&gt; | 16px | 否 | 选择项的文本尺寸。 |
| allow-scale | boolean | true | 否 | 选择项的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-weight | number \| string | normal | 否 | 选择项的字体粗细，见text组件font-weight的样式属性。 |
| text-decoration | string | none | 否 | 选择项的文本修饰，见text组件text-decoration的样式属性。 |
| font-family | string | sans-serif | 否 | 选择项的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |
 
 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

详见[menu示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu#示例)。
