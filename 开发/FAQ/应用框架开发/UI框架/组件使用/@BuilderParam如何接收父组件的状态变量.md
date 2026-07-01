# @BuilderParam如何接收父组件的状态变量

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-826

#### 问题现象

如何通过@BuilderParam装饰器传递@State装饰的状态变量？
 
 

#### 背景知识

[@BuilderParam装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam)用于装饰指向[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)方法的变量，能够声明任意UI描述的元素。@BuilderParam装饰器初始化的值必须为@Builder，否则编译时就会输出报错信息。
 
 

#### 解决方案

@State装饰器装饰的变量不可直接传递给@BuilderParam装饰器，可以使用@Builder装饰器当做桥梁，在@Builder装饰的构建函数中使用状态变量，实现状态变量的传递，具体实现如下：
 
- 在build方法中，调用MyCustomContainer子组件，通过箭头函数将带有状态变量的自定义构建函数传递给子组件。
```text
@Entry
@Component
struct TransmitBuilderParam {
  @State message: string = '状态变量';

  @Builder
  customParBuilder() {
    Text(this.message);
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        MyCustomContainer({
          customView: () => {
            this.customParBuilder();
          }
        });
        Button('修改状态变量')
          .onClick(() => {
            this.message = '12345';
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

- 在MyCustomContainer组件中，定义空自定义构建函数customViewBuild。使用@BuilderParam装饰器接收父组件传递过来的自定义构建函数，并且在子组件中调用this.customView()就能看到父组件的自定义内容，状态变量改变时也能更新。
```text
@Component
struct MyCustomContainer {
  @Builder
  customViewBuild() {
  }

  @BuilderParam customView: () => void = this.customViewBuild;

  build() {
    Column() {
      Text('childText');
      this.customView();
    };
  }
}
```


 
完整示例代码如下：
 
```text
@Entry
@Component
struct TransmitBuilderParam {
  @State message: string = '状态变量';

  @Builder
  customParBuilder() {
    Text(this.message);
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        MyCustomContainer({
          customView: () => {
            this.customParBuilder();
          }
        });
        Button('修改状态变量')
          .onClick(() => {
            this.message = '12345';
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}

@Component
struct MyCustomContainer {
  @Builder
  customViewBuild() {
  }

  @BuilderParam customView: () => void = this.customViewBuild;

  build() {
    Column() {
      Text('childText');
      this.customView();
    };
  }
}
```
 
运行效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/3kM5LZpWQtyyTgzKIcgTYQ/zh-cn_image_0000002628558356.png?HW-CC-KV=V1&HW-CC-Date=20260701T041238Z&HW-CC-Expire=86400&HW-CC-Sign=5BA48739F047EC914034CD845F913FCCE5162BD66581485AEB42F914110C56DA)
