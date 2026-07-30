# WrappedBuilder报参数类型不匹配的错误如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1538

#### 问题现象

使用WrappedBuilder维护UI时，遇到WrappedBuilder泛型报错如何处理？
 
报错提示如下：
 
```text
Argument of type 'DialogCustomV2<T>' is not assignable to parameter of type 'MAPPER_VALUE'.
  The types of 'wrapped.builder' are incompatible between these types.
    Type '(args_0: T) => void' is not assignable to type '(args_0: BaseCustomDialogParam) => void'.
      Types of parameters 'args_0' and 'args_0' are incompatible.
        Type 'BaseCustomDialogParam' is not assignable to type 'T'.
          'BaseCustomDialogParam' is assignable to the constraint of type 'T', but 'T' could be instantiated with a different subtype of constraint 'BaseCustomDialogParam'.
```
 
解释：报错提示泛型参数类型不匹配，类型“DialogCustomV2&lt;T&gt;”不能分配给类型“DialogCustomV2&lt;BaseCustomDialogParam&gt;”。错误代码如下：
 
```text
import { ComponentContent, UIContext } from '@kit.ArkUI';

<em>// </em><em>定义基础接口</em>
namespace Param {
  export interface BaseDialogParamV2 {
    alignment?: DialogAlignment
    mask?: boolean
    cornerRadius?: Dimension,
    autoCancel?: boolean,
    width?: Dimension,
    height?: Dimension,
  }

  export interface BaseCustomDialogParam {
    dialogFunc?: () => boolean;
  }
}

function simpleUUID(): string {
  return 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = Math.random() * 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

<em>// </em><em>定义泛型类DialogCustomV2</em>
class DialogCustomV2<T extends Param.BaseCustomDialogParam> {
  uiContext: UIContext = new UIContext;
  wrapped: WrappedBuilder<[T]>;
  param: T;
  dialogParam: Param.BaseDialogParamV2;
  private _id: string;

  public get id(): string {
    return this._id;
  }

  constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
    this.wrapped = wrapped;
    this.param = param;
    this.dialogParam = dialogParam ?? {};
    this._id = simpleUUID();
  }

  open() {
    let view = new ComponentContent(this.uiContext, this.wrapped, this.param);
    this.uiContext.getPromptAction().openCustomDialog(view, this.dialogParam);
  }
}

export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[T]>, param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<T> = new DialogCustomV2<T>(wrapped, param, dialogParam);
  <em>// </em><em>缓存弹窗映射</em>
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
 <em> // 弹框堆栈</em>
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}

@Builder
function MyBuilder(param: Param.BaseCustomDialogParam) {
  Column() {
    Text('Hello from Dialog!')
      .fontSize(24)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 20 });

    Button('点此执行自定义方法')
      .onClick(() => {
        if (param.dialogFunc) {
          const shouldClose = param.dialogFunc();
          if (shouldClose) {
            console.info('自定义方法被执行');
          }
        }
      })
      .margin({ top: 10 });
  }
  .backgroundColor(Color.White)
  .borderRadius(32)
  .padding(20)
  .alignItems(HorizontalAlign.Center);
}

let globalBuilder: WrappedBuilder<[Param.BaseCustomDialogParam]> = wrapBuilder(MyBuilder);

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('打开弹窗')
        .onClick(() => {
         <em> // globalBuilder作为WrappedBuilder参数</em>
          const param: Param.BaseCustomDialogParam = {
            dialogFunc: () => {
           <em>   // 这里可以加逻辑，比如提示、上报等</em>
              console.info('这里可以执行自定义方法');
             <em> // 返回true表示允许关闭</em>
              return true;
            }
          };

          <em>// 弹窗样式参数</em>
          const dialogParam: Param.BaseDialogParamV2 = {
            width: 300,
            height: 200,
            cornerRadius: 16,
            mask: true,
            autoCancel: true,
            alignment: DialogAlignment.Center
          };

          <em>// 调用showCustomV2，传入globalBuilder和参数</em>
          showCustomV2(globalBuilder, param, dialogParam);
        });
    }
    .width('100%');
  }
}
```
 
 

#### 背景知识

[wrapBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder)作为全局@Builder的封装函数，返回一个WrappedBuilder对象，从而使得全局@Builder可以进行属性赋值和参数传递。
 
 

#### 问题定位

查看报错部分代码：
 
```text
export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[T]>, param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<T> = new DialogCustomV2<T>(wrapped, param, dialogParam);
 <em> // 缓存弹窗映射</em>
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
 <em> // 弹框堆栈</em>
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}
```
 
查看DialogCustomV2的构造函数：
 
```text
constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
  this.wrapped = wrapped;
  this.param = param;
  this.dialogParam = dialogParam ?? {};
  this._id = simpleUUID();
}
```
 
可以看到，DialogCustomV2包含了一个WrappedBuilder类型的成员wrapped，而使用WrappedBuilder时需要指定一个明确的类型。
 
 

#### 分析结论

上述代码是由于类型不匹配导致报错，虽然BaseCustomDialogParam能够满足T的约束条件，但是由于T是一个泛型类型，它可以被实例化为任何符合该约束的类型，这导致了类型不兼容的情况。目前WrappedBuilder不支持上述代码的用法。
 
 

#### 修改建议

使用WrappedBuilder时为了确保类型安全和正确的功能实现，需要将DialogCustomV2中的T设置为实际要操作的数据类型的精确类型。在这个例子中，应该将DialogCustomV2&lt;T&gt;和wrapped: WrappedBuilder<[T]>中的T设置为BaseCustomDialogParam，而不是更宽泛的类型。
 
完整示例参考如下：
 
```text
import { ComponentContent, UIContext } from '@kit.ArkUI';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

<em>// </em><em>定义基础接口</em>
namespace Param {
  export interface BaseDialogParamV2 {
    alignment?: DialogAlignment
    mask?: boolean
    cornerRadius?: Dimension,
    autoCancel?: boolean,
    width?: Dimension,
    height?: Dimension,
  }

  export interface BaseCustomDialogParam {
    dialogFunc?: () => boolean;
  }
}

function simpleUUID(): string {
  let rand = cryptoFramework.createRandom();
  let randData = rand.generateRandomSync(1);
  return 'xxxx'.replace(/[xy]/g, (str) => {
    const temp = randData.data[0] * 16 / 255 | 0;
    const value = str === 'x' ? temp : (temp & 0x3 | 0x8);
    return value.toString(16);
  });
}

<em>// </em><em>定义泛型类DialogCustomV2</em>
class DialogCustomV2<T extends Param.BaseCustomDialogParam> {
  uiContext: UIContext = new UIContext;
  wrapped: WrappedBuilder<[T]>;
  param: T;
  dialogParam: Param.BaseDialogParamV2;
  private _id: string;

  public get id(): string {
    return this._id;
  }

  constructor(wrapped: WrappedBuilder<[T]>, param: T, dialogParam?: Param.BaseDialogParamV2) {
    this.wrapped = wrapped;
    this.param = param;
    this.dialogParam = dialogParam ?? {};
    this._id = simpleUUID();
  }

  open() {
    let view = new ComponentContent(this.uiContext, this.wrapped, this.param);
    this.uiContext.getPromptAction().openCustomDialog(view, this.dialogParam);
  }
}

export function showCustomV2<T extends Param.BaseCustomDialogParam>(wrapped: WrappedBuilder<[Param.BaseCustomDialogParam]>,
  param: T,
  dialogParam?: Param.BaseDialogParamV2) {
  const dialog: DialogCustomV2<Param.BaseCustomDialogParam> =
    new DialogCustomV2<Param.BaseCustomDialogParam>(wrapped, param, dialogParam);
 <em> // 缓存弹窗映射</em>
  type MAPPER_VALUE = DialogCustomV2<Param.BaseCustomDialogParam>;
  const MAPPER = new Map<string, MAPPER_VALUE>();
 <em> // 弹框堆栈</em>
  const STACK: Array<string> = [];
  MAPPER.set(dialog.id, dialog);
  STACK.push(dialog.id);
  dialog.open();
}

@Builder
function MyBuilder(param: Param.BaseCustomDialogParam) {
  Column() {
    Text('Hello from Dialog!')
      .fontSize(24)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 20 });

    Button('点此执行自定义方法')
      .onClick(() => {
        if (param.dialogFunc) {
          const shouldClose = param.dialogFunc();
          if (shouldClose) {
            console.info('自定义方法被执行');
          }
        }
      })
      .margin({ top: 10 });
  }
  .backgroundColor(Color.White)
  .borderRadius(32)
  .padding(20)
  .alignItems(HorizontalAlign.Center);
}

let globalBuilder: WrappedBuilder<[Param.BaseCustomDialogParam]> = wrapBuilder(MyBuilder);

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('打开弹窗')
        .onClick(() => {
         <em> // globalBuilder作为WrappedBuilder参数</em>
          const param: Param.BaseCustomDialogParam = {
            dialogFunc: () => {
             <em> // 这里可以加逻辑，比如提示、上报等</em>
              console.info('这里可以执行自定义方法');
           <em>   // 返回true表示允许关闭</em>
              return true;
            }
          };

         <em> // 弹窗样式参数</em>
          const dialogParam: Param.BaseDialogParamV2 = {
            width: 300,
            height: 200,
            cornerRadius: 16,
            mask: true,
            autoCancel: true,
            alignment: DialogAlignment.Center
          };

        <em>  // 调用showCustomV2，传入globalBuilder和参数</em>
          showCustomV2(globalBuilder, param, dialogParam);
        });
    }
    .width('100%');
  }
}
```
