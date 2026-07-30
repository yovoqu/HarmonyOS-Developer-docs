# @Builder和@Component的区别与嵌套使用场景

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1657

#### 问题现象

- 场景一：如何使@Builder装饰的自定义构建函数内UI具备生命周期？
- 场景二：@Builder装饰的自定义构建函数内嵌套@Component自定义组件时，如何传递参数？

 
 

#### 背景知识

[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)和[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)的区别总结如下：
  
| 特性 | @Component/@ComponentV2 | @Builder |
| --- | --- | --- |
| 本质 | 定义独立组件 | 定义UI构建函数（代码片段） |
| 生命周期 | 具备生命周期，详见：自定义组件生命周期 | 无生命周期函数 |
| 状态管理 | 支持状态变量声明 | 仅支持参数传递 |
| 复用方式 | 作为组件实例化 | 作为函数调用 |
| 嵌套限制 | 可嵌套其它组件或@Builder | 可嵌套其它@Builder，也可嵌套@Component组件 |
| 典型场景 | 封装带逻辑/状态的复杂UI单元 | 封装无状态的纯UI结构片段 |
 
 
 

#### 解决方案

- 场景一：如何使@Builder装饰的自定义构建函数内UI具备生命周期？在@Builder函数中嵌套@Component修饰的自定义组件，可以依靠@Component组件的生命周期给PromptAction弹窗增加生命周期函数。

  
```text
import { ComponentContent } from '@kit.ArkUI';

@Entry
@Component
struct SceneOne {
  build() {
    Column() {
      Button('创建builder的弹窗').onClick(() => {
        let dialogContentNode = new ComponentContent(this.getUIContext(), wrapBuilder(childComp));
        this.getUIContext().getPromptAction().openCustomDialog(dialogContentNode);
      })
        .margin({ bottom: 12 });
    }.width('100%');
  }
}

@Builder
export function childComp() {
  Child();
}

@Component
struct Child {
  aboutToAppear(): void {
    console.info('执行了aboutToAppear');
  }

  onDidBuild(): void {
    console.info('执行了onDidBuild');
  }

  build() {
    Column() {
      Text(`弹窗`);
    };
  }
}
```
 实现效果：

  
```text
03-26 17:16:13.614   4363-4363     A03d00/JSAPP                    com.examp...05632611  I     执行了aboutToAppear
03-26 17:16:13.615   4363-4363     A03d00/JSAPP                    com.examp...05632611  I     执行了onDidBuild
```


 
 
- 场景二：@Builder装饰的自定义构建函数内嵌套@Component自定义组件时，如何传递参数？在V1版本可以通过@Prop接收，V2版本通过@Param接收参数，V1版本完整示例代码如下：

  
```text
import { ComponentContent } from '@kit.ArkUI';

@Entry
@Component
struct SceneTwo {
  @State name: string = '弹窗示例';

  build() {
    Column() {
      Button('创建builder的弹窗并传递参数').onClick(() => {
        let dialogContentNode = new ComponentContent(this.getUIContext(), wrapBuilder(childCompTwo), this.name);
        this.getUIContext().getPromptAction().openCustomDialog(dialogContentNode);
      })
        .margin({ bottom: 12 });
    }.width('100%');
  }
}

@Builder
export function childCompTwo(name: string) {
  ChildTwo({ name: name });
}

@Component
struct ChildTwo {
  @Prop name: string = ''; <em>// 使用@Prop装饰器接收，@Link接收不满足使用限制会报错</em>

  build() {
    Column() {
      Text(this.name);
    }
    .justifyContent(FlexAlign.Center)
    .borderRadius(25)
    .backgroundColor(Color.White)
    .width('90%')
    .height(100);
  }
}
```
 场景二实现效果：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/LnclSKPPSLu-Nz3MO5oeUQ/zh-cn_image_0000002628661002.png?HW-CC-KV=V1&HW-CC-Date=20260730T072416Z&HW-CC-Expire=86400&HW-CC-Sign=BBB1BE645377B6D2F6247575E249C8FAA0B8E83AFC3BA7BF32A8BDCBF30922E6)


 

#### 常见FAQ

Q：@BuilderParam能传递@Component组件吗？
 
A：@BuilderParam只能接收@Builder、@LocalBuilder装饰的自定义组件，不能接收@Component装饰的组件，若想要传递@Component组件，可以在外部嵌套一个@Builder装饰的自定义组件。
 
Q：@Builder嵌套@Component组件，@Component组件使用@Prop装饰器接收参数时，UI不刷新？
 
A：需要使用引用传递刷新，详情参考官网示例：[在@Builder内创建自定义组件传递参数不刷新问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#在builder内创建自定义组件传递参数不刷新问题)。
