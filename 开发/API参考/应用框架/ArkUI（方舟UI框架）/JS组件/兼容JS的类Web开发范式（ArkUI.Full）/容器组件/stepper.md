# stepper

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
步骤导航器。当完成一个任务需要多个步骤时，可以使用步骤导航器展示当前进展。
  

#### 权限列表

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

仅支持<stepper-item>子组件。
 
> [!NOTE]
> 步骤导航器内的步骤顺序按照子组件<stepper-item>的顺序进行排序。

 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：
  
| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| index | number | 0 | 设置步骤导航器步骤显示第几个stepper-item子组件，默认显示第一个stepper-item。 |
 
 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。
 
> [!NOTE]
> stepper组件默认占满父容器大小，建议父组件使用应用窗口大小（或者父组件为根节点）来优化体验。

 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：
  
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| finish | 无 | 当步骤导航器最后一个步骤完成时,触发该事件。 |
| skip | 无 | 当前步骤导航器下一步按钮状态为skip，即可跳过时，点击右侧跳过按钮触发该事件。 |
| change | { prevIndex: prevIndex, index: index} | 当用户点击步骤导航器的左边或者右边按钮进行步骤切换时触发该事件，prevIndex表示老步骤的序号，index表示新步骤的序号。 |
| next | { index: index, pendingIndex: pendingIndex } | 当用户点击下一步按钮时触发该事件，index表示当前步骤序号，pendingIndex表示将要跳转的序号，该事件有返回值，返回值格式为：{ pendingIndex: pendingIndex }，可以通过指定pendingIndex来修改下一个步骤使用哪个stepper-item子组件。 |
| back | { index: index, pendingIndex: pendingIndex } | 当用户点击上一步按钮时触发该事件，index表示当前步骤序号，pendingIndex表示将要跳转的序号，该事件有返回值，返回值格式为Object: { pendingIndex: pendingIndex }，可以通过指定pendingIndex来修改上一个步骤使用哪个stepper-item子组件。 |
 
 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)外，支持如下方法：
  
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| setNextButtonStatus | { status: string, label: label } | 设置当前步骤中下一步按钮的文本与状态，参数中label为指定按钮文本，status指定按钮状态，status可选值为： - normal：正常状态，下一步文本按钮正常显示，可点击进入下一个步骤； - disabled：不可用状态，下一步文本按钮灰度显示，不可点击进入下一个步骤； - waiting：等待状态，下一步文本按钮不显示，使用等待进度条，不可点击进入下一个步骤； - skip：跳过状态，下一步文本按钮显示跳过按钮，点击时会跳过剩下步骤。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="container">
    <stepper class="stepper" id="mystepper" onnext="nextclick" onback="backclick" onchange="statuschange"
             onfinish="finish" onskip="skip" style="height : 100%;">
        <stepper-item class="stepper-item" label="{{ label_1 }}">
            <div class="item">
                <text>Page One</text>
                <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
            </div>
        </stepper-item>
        <stepper-item class="stepper-item" label="{{ label_2 }}">
            <div class="item">
                <text>Page Two</text>
                <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
            </div>
        </stepper-item>
        <stepper-item class="stepper-item" label="{{ label_3 }}">
            <div class="item">
                <text>Page Three</text>
                <button type="capsule" class="button" value="change status" onclick="setRightButton"></button>
            </div>
        </stepper-item>
    </stepper>
</div>
```
 
```text
/* xxx.css */
.container {
    flex-direction: column;
    align-items: center;
    height: 100%;
    width: 100%;
    background-color: #f7f7f7;
}
.stepper{
    width: 100%;
    height: 100%;
}
.stepper-item {
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
}
.item{
    width: 90%;
    height: 86%;
    margin-top: 80px;
    background-color: white;
    border-radius: 60px;
    flex-direction: column;
    align-items: center;
    padding-top: 160px;
}
text {
    font-size: 78px;
    color: #182431;
    opacity: 0.4;
}
.button {
    width: 40%;
    margin-top: 100px;
    justify-content: center;
}
```
 
```text
// xxx.js
import prompt from '@ohos.promptAction';

export default {
    data: {
        label_1:
        {
            prevLabel: 'BACK',
            nextLabel: 'NEXT',
            status: 'normal'
        },
        label_2:
        {
            prevLabel: 'BACK',
            nextLabel: 'NEXT',
            status: 'normal'
        },
        label_3:
        {
            prevLabel: 'BACK',
            nextLabel: 'NEXT',
            status: 'normal'
        }
    },
    setRightButton(e) {
        this.$element('mystepper').setNextButtonStatus({
            status: 'waiting', label: 'SKIP'
        });
    },
    nextclick(e) {
        var index = {
            pendingIndex: e.pendingIndex
        }
        return index;
    },
    backclick(e) {
        var index = {
            pendingIndex: e.pendingIndex
        }
        return index;
    },
    statuschange(e) {
        prompt.showToast({
            message: '上一步序号' + e.prevIndex + '当前序号' + e.index
        })
    },
    finish() {
        prompt.showToast({
            message: '最后一步已完成'
        })
    },
    skip() {
        prompt.showToast({
            message: 'skip触发'
        })
    }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/VuIrQrPlQ8GRn-PO_v4bPw/zh-cn_image_0000002581276408.gif?HW-CC-KV=V1&HW-CC-Date=20260528T025444Z&HW-CC-Expire=86400&HW-CC-Sign=607EC730C6C2CBAA599CFDDD0FEBA9B1BBF4AE0E7788CE778A05ED307A07ED8D)
