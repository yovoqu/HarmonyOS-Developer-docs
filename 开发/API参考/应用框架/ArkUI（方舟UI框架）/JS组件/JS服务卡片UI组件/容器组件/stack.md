# stack

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
 
> [!NOTE]
> 从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持。
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)。
 
  

##### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)。
 
  

##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events)。
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<stack class="stack-parent">
  <div class="back-child bd-radius"></div>
  <div class="positioned-child bd-radius"></div>
  <div class="front-child bd-radius"></div>
</stack>
```
 
```text
/* xxx.css */
.stack-parent {
  width: 400px;
  height: 400px;
  margin: 50px;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
}
.back-child {
  width: 300px;
  height: 300px;
  background-color: #3f56ea;
}
.front-child {
  width: 100px;
  height: 100px;
  background-color: #00bfc9;
}
.positioned-child {
  width: 100px;
  height: 100px;
  left: 50px;
  top: 50px;
  background-color: #47cc47;
}
.bd-radius {
  border-radius: 16px;
}
```
 
**4×4卡片**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/vMDJDrX9Skaav9ivOM2QNw/zh-cn_image_0000002581436566.png?HW-CC-KV=V1&HW-CC-Date=20260528T024056Z&HW-CC-Expire=86400&HW-CC-Sign=AFAF19D137523BF7D0C09E1DFAB761A40803FD52EF099CE0734B320A32B2EDC6)
