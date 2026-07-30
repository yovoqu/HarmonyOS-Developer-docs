# 如何解决TextInput限制输入异常问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1464

#### 问题现象

为TextInput组件添加限制条件，只能输入某个范围内的数字，在onChange回调里实现具体逻辑，运行后没有生效，有两个问题：
 1. 回调里设置了输入范围，但还是能够输入超出范围的数字，且无法输入负数。
2. 给文本添加$$双向绑定后，仍无法输入负数，正整数范围生效，但无法再输入小数点。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct TextInputPage {
  @State inputValue: string = '';

  build() {
    Column() {
      TextInput({
        text: this.inputValue, <em>// </em><em>加上双向绑定符号$$之后就无法再输入小数点</em>
        placeholder: '请输入-50~150之间的数字'
      })
        .type(InputType.NUMBER_DECIMAL)
        .onChange((value: string) => {
        <em>  // 转换为数字进行范围判断</em>
          let numValue = parseFloat(value) ;
          if (numValue <= -50) {
            console.info('numValue小于50')
            this.inputValue = '-50';
          }else if (numValue >= 150) {
            console.info('numValue大于150')
            this.inputValue = '150';
          }else {
            this.inputValue = numValue.toString()
          }
        })
    }
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/vQfr8r0ZTXubDFK-JynhCQ/zh-cn_image_0000002628605354.png?HW-CC-KV=V1&HW-CC-Date=20260701T041316Z&HW-CC-Expire=86400&HW-CC-Sign=480F655B6E4D57856440D724572B619D63957EC24D3FBEC40602190BF4042F10)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/N8B5vNrVRJ6WyPIs8nLVBQ/zh-cn_image_0000002658844611.png?HW-CC-KV=V1&HW-CC-Date=20260701T041316Z&HW-CC-Expire=86400&HW-CC-Sign=04E471B54DB8C770AE0434464E91445BF48ACD526AD872994450EB75F218566D)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/I-LYJhvJStmGU_59fqV-dg/zh-cn_image_0000002628765244.png?HW-CC-KV=V1&HW-CC-Date=20260701T041316Z&HW-CC-Expire=86400&HW-CC-Sign=D5DB1D8AC84462D2BA52FACA320EC505251069B7212C39942E8EA83334A579B3)

 
 

#### 背景知识

在HarmonyOS中，[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定符号可以实现将状态变量和系统组件的内部状态保持同步。在使用[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input)组件进行文本输入时，可以在[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)事件中对输入的内容进行限制等操作。
 
 

#### 问题定位
1. 排查在向TextInput组件的text参数传值时，是否使用$$双向绑定符号。
2. 追溯最终展示的数字值来源，排查是否有限制小数点输入的操作或者是否在数据转换过程中造成小数点丢失。
 
 

#### 分析结论
1. 向TextInput组件的text参数传值时没有使用$$双向绑定符号，导致状态变量的变化无法同步传递给TextInput组件。
2. 小数点在经过parseFloat()方法以及toString()方法的转换之后丢失，导致输入失败。
 
 

#### 修改建议
1. 为TextInput组件的text参数添加$$双向绑定符号。
2. onChange事件的value值本身就是string类型，除开进行范围判断时需要用到整数，进行文本展示时直接用value值就好，不需要再将用parseFloat()方法转化的整数转成string类型。
3. 当type属性的值设置为InputType.NUMBER_DECIMAL时，不支持负数小数。更换使用inputFilter实现输入负数小数。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct TextInputPage {
  @State inputValue: string = '';

  build() {
    Column() {
      TextInput({
        text: $$this.inputValue,
        placeholder: '请输入-50~150之间的数字'
      })
        .onChange((value: string) => {
       <em>   // 转换为数字进行范围判断</em>
          let numValue = parseFloat(value);
          if (numValue <= -50) {
            console.info('numValue小于50');
            this.inputValue = '-50';
          } else if (numValue >= 150) {
            console.info('numValue大于150');
            this.inputValue = '150';
          } else {
            this.inputValue = value;
          }
        })
        .inputFilter('^-?\\d*\\.?\\d{0,2}$', (val) => {<em> </em><em>// 使用正则表达式对输入内容进行限制</em>
          console.info(`限制输入两位小数 ： ${val}`);
          return 0;
        })
    }
  }
}
```
