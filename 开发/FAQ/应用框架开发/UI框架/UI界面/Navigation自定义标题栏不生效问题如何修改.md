# Navigation自定义标题栏不生效问题如何修改

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-906

#### 问题现象

使用Navigation时，自定义了一个标题栏布局，使用其中的title方法无效。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/tri6awaVTkOYHr-eEUEa2w/zh-cn_image_0000002628399758.png?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=9CFA63A6201B2E01C37FD81039028DCF5F776862589313B60F651DDD79292735)

 
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Ji6AST-WSoe94WQ6chcO8Q/zh-cn_image_0000002658799027.png?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=DD41FCABCB76CE3A9EA8C2267852B8618C2D1AEE366F8F0AB9B592841161C521)

 
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

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/rMk62wiUToC76vrcmLw15Q/zh-cn_image_0000002628559674.png?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=E8BFD69D66F0781CCF06B674E6633BA51B5C9CF2B601D3D55580FA1B9A617CA8)

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

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2CquOetPTdOMgtO70jb4ag/zh-cn_image_0000002658918981.png?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=13199F3E9682418D420FBD1ECF52FD8D3D1F722A355BF0E00D358DCB843F2EE1)


 
 

#### 常见FAQ

Q：NavDestination怎么修改单个页面标题文字颜色？
 
A：参考上述解决方案，在title中传入@Builder构建函数实现自定义标题栏，可以指定文字颜色。
