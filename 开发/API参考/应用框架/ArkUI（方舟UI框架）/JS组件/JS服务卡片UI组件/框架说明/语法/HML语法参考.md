# HML语法参考

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-hml
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

HML是一套类HTML的标记语言，通过组件，事件构建出页面的内容。页面具备数据绑定、事件绑定、条件渲染和逻辑控制等高级能力。


## 页面结构
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
<!-- xxx.hml -->
<div class="item-container">
<text class="item-title">Image Show</text>
<div class="item-content">
<image src="/common/xxx.png" class="image"></image>
</div>
</div>
```


## 数据绑定
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
<!-- xxx.hml -->
<div class="item-container">
<text>{{content}}</text>            <!-- 输出：Hello World！-->
<text>{{key1}} {{key2}}</text>       <!-- 输出：Hello World-->
<text>key1 {{key1}}</text>           <!-- 输出：key1 Hello-->
<text>{{flag1 && flag2}}</text>      <!-- 输出：false-->
<text>{{flag1 || flag2}}</text>      <!-- 输出：true-->
<text>{{!flag1}}</text>              <!-- 输出：false-->
</div>
```

卡片hml文件中的变量需要在json文件的data字段下进行声明：


```json
{
  "data": {
    "content": "Hello World!",
    "key1": "Hello",
    "key2": "World",
    "flag1": true,
    "flag2": false
  }
}
```


> [!NOTE]
> 逻辑运算：
> 三元表达式
> 注意事项


## 事件绑定
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

卡片的事件需要在json文件的actions字段下进行声明。卡片仅支持click通用事件，事件的定义只能是直接命令式，事件定义必须包含action字段，用以说明事件类型。卡片支持两种事件类型：跳转事件(router)和消息事件(message)。跳转事件可以跳转到卡片提供方的应用，消息事件可以将开发者自定义信息传递给卡片提供方。事件参数支持变量，变量以"{{}}"修饰。跳转事件中若定义了params字段，则在被拉起应用的onStart的intent中，可用"params"作为key将跳转事件定义的params字段的值取到。


- 跳转事件格式  通过定义ability名称和携带的参数字段params直接跳转，可用"params"作为key提取到跳转事件定义的params字段值。   选择器 样例 默认值 样例描述   action string "router" 事件类型。 - "router"：用于应用跳转。 - "message"：自定义点击事件。   abilityName string - 跳转ability名。  params Object - 跳转应用携带的额外参数。      __PREBLOCK_3__
- 消息事件格式   选择器 样例 默认值 样例描述   action string message 表示事件类型。  params Object - 跳转应用携带的额外参数。      __PREBLOCK_4__
- 绑定路由事件和消息事件  __PREBLOCK_5__


## 列表渲染
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
<!-- xxx.hml -->
<div class="array-container">
<!-- div列表渲染 -->
<!-- 默认$item代表数组中的元素, $idx代表数组中的元素索引 -->
<div for="{{array}}" tid="id">
<text>{{$item.name}}</text>
</div>
<!-- 自定义元素变量名称 -->
<div for="{{value in array}}" tid="id">
<text>{{value.name}}</text>
</div>
<!-- 自定义元素变量、索引名称 -->
<div for="{{(index, value) in array}}" tid="id">
<text>{{value.name}}</text>
</div>
</div>
```


```json
{
  "data": {
    "array": [
      {
        "id": 1,
        "name": "jack",
        "age": 18
      },
      {
        "id": 2,
        "name": "tony",
        "age": 18
      }
    ]
  }
}
```

tid属性主要用来加速for循环的重渲染，旨在列表中的数据有变更时，提高重新渲染的效率。tid属性是用来指定数组中每个元素的唯一标识，如果未指定，数组中每个元素的索引为该元素的唯一id。例如上述tid="id"表示数组中的每个元素的id属性为该元素的唯一标识。for循环支持的写法如下：


- for="array"：其中array为数组对象，array的元素变量默认为\$item。
- for="v in array"：其中v为自定义的元素变量，元素索引默认为\$idx。
- for="(i, v) in array"：其中元素索引为i，元素变量为v，遍历数组对象array。


## 条件渲染
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

条件渲染分为2种：if/elif/else和show。

当使用if/elif/else写法时，节点必须是兄弟节点，否则编译无法通过。实例如下：


```text
<!-- xxx.hml -->
<div>
<text if="{{show}}"> Hello-TV </text>
<text elif="{{display}}"> Hello-Wearable </text>
<text else> Hello-World </text>
</div>
```


```json
{
  "data": {
    "show": false,
    "display": true
  }
}
```

当show为真时，节点正常渲染；当show为假时，节点不渲染，效果等同display样式为none。


```text
<!-- xxx.hml -->
<text show="{{visible}}"> Hello World </text>
```


```json
{
  "data": {
    "visible": false
  }
}
```


## 逻辑控制块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

<block>控制块使得循环渲染和条件渲染变得更加灵活；block在构建时不会被当作真实的节点编译。block标签只支持if属性。


```text
<!-- xxx.hml -->
<div>
<block if="{{show}}">
<text>Hello</text>
<text>World</text>
</block>
</div>
```


```json
{
  "data": {
    "show": true
  }
}
```
