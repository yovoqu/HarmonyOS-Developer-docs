# Navigation自定义标题栏不生效问题如何修改

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-906

#### 问题现象

使用Navigation时，自定义了一个标题栏布局，使用其中的title方法无效。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/tri6awaVTkOYHr-eEUEa2w/zh-cn_image_0000002628399758.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=2957AC81D60444924798F40B22DD9E88295ED5DA790F0068286FE0E1A1F2A7DB)

 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct Index {
  text: string = '标题';
  customTitle: NavigationCustomTitle = {
    builder: this.customTitleBuilder(),
    height: TitleHeight.MainOnly
  };

  @Builder
  customTitleBuilder() {
    Row() {
      Text(this.text);
    };
  }

  build() {
    Navigation() {
      Column() {
        Text('首页')
          .fontSize(40);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .title(this.customTitle);
  }
}
```
 
 

#### 背景知识

[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)是路由容器组件，一般作为首页的根容器。其内部默认包含了标题栏、内容区和工具栏。其中内容区默认首页显示导航内容，标题栏和工具栏均支持传入自定义样式。
 
 

#### 解决方案

使用ArkUI Inspector查看应用布局，发现TitleBar不可见，标题栏未创建。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Ji6AST-WSoe94WQ6chcO8Q/zh-cn_image_0000002658799027.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=54F39C45935576C18A35B5A7FA96DF8CD3D13D2EB7ED2A8287C5EE3635213BD4)

 
查看[title](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#title)传入参数类型，其中NavigationCustomTitle和CustomBuilder这两种类型均支持自定义标题栏样式。
 
代码中使用的NavigationCustomTitle类型变量，自定义标题的方法在传入时，没有绑定当前上下文。在执行时，this指向了NavigationCustomTitle对象，找不到相应的方法，因而无法渲染绘制标题栏。
 
- **方案一**：NavigationCustomTitle里builder传入方法需要bind(this)。
```text
@Entry
@Component
struct NavTitleSolution1 {
  text: string = '标题';
  customTitle: NavigationCustomTitle = {
    builder: this.customTitleBuilder.bind(this),
    height: TitleHeight.MainOnly
  };

  @Builder
  customTitleBuilder() {
    Row() {
      Text(this.text)
        .fontSize(20);
    }.margin({ left: 18, top: 28 });
  }

  build() {
    Navigation() {
      Column() {
        Text('首页')
          .fontSize(40);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .title(this.customTitle);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/rMk62wiUToC76vrcmLw15Q/zh-cn_image_0000002628559674.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=6F323A8852BB27C51C2AA67B514DCF5CD8356063A213898A977974AD96CFAB0A)

- **方案二**：在title中直接传入自定义布局的方法。
```text
@Entry
@Component
struct NavTitleSolution2 {
  text: string = '标题';

  @Builder
  customTitleBuilder() {
    Row() {
      Text(this.text)
        .fontSize(20);
    }.margin({ left: 18, top: 28 });
  }

  build() {
    Navigation() {
      Column() {
        Text('首页')
          .fontSize(40);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .hideBackButton(true)
    .titleMode(NavigationTitleMode.Mini)
    .title(this.customTitleBuilder());
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2CquOetPTdOMgtO70jb4ag/zh-cn_image_0000002658918981.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=56C8924FB12543E5ADEBACE5CB7C23A4A36008334B229B5F6108E57FC66E9833)


 
 

#### 常见FAQ

Q：NavDestination怎么修改单个页面标题文字颜色？
 
A：参考上述解决方案，在title中传入@Builder构建函数实现自定义标题栏，可以指定文字颜色。
