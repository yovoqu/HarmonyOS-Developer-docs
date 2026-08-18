# 怎么解决自定义Span组件在NavDestination下无法显示问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-895

#### 问题现象

包含Span组件的自定义组件，包含在Text组件下，让该Text组件置于NavDestination页面下，结果该自定义组件Span里的内容：Span自定义组件内容，没有显示。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/vekZBIQ5RqOsRB0s_UjIXQ/zh-cn_image_0000002658918867.png?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=6C07629A708EED55DCF184FF05DF5FDCFAA669A74AC86AE018C8EC7FABB9712F)

 
 

#### 背景知识

- [Text组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)：Text是文本组件，通常用于展示用户视图，如显示文章的文字。
- [NavDestination组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)：作为子页面的根容器，用于显示Navigation的内容区。

 
 

#### 问题定位

- Span内容不显示，依据文档排查该自定义子组件当前能力是否支持使用Span组件。
- 在NavDestination页面下不显示，单独抽离出来在Page页面查看是否显示。

 
 

#### 分析结论

- Page会把全部的自定义组件都展开，Text组件解析到自定义组件下。
- NavDestination机制下不会全部展开，自定义组件依赖后续组件内部自行展开，Text组件非容器组件，没有在解析子组件时做展开自定义操作。

 
 

#### 修改建议
1. Text不支持自定义组件，且Span组件作为Text、ContainerSpan组件的子组件，只能在这两个组件内使用，把Text和其下的Span抽离出来成单独的组件。
```text
@Component
export struct pageOne {
  build() {
    NavDestination() {
      Column() {
        Text() {
          Span('Text直接包含的Span子组件1\n');
          Span('Text直接包含的Span子组件2\n');
          Span('Span自定义组件内容');
        };
      }.height('100%')
      .justifyContent(FlexAlign.Center);
    };
  }
}

@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    console.info('nav index');
  }

  @Builder
  pages() {
    pageOne();
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('点击跳转到NavDestination页面')
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' });
          });
      }.height('100%')
      .justifyContent(FlexAlign.Center);

    }.navDestination(this.pages);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Wl3jZ8E6RfmIkhD35-GEsQ/zh-cn_image_0000002628399650.png?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=615BB73165ADAF5868E3690548E257D8AE978E7B3376C33F4BA1A14B51E3104D)

2. 如果Span组件是一组公共的特性，则可以通过@Builder装饰器把公共的部分抽取出来。
```text
@Component
export struct pageOne {
  build() {
    NavDestination() {
      Column() {
        Text() {
          this.newLocalBuilder();
        };
      }.height('100%')
      .justifyContent(FlexAlign.Center);
    };
  }

  @Builder
  newLocalBuilder() {
    Span('Text直接包含的Span子组件1\n');
    Span('Text直接包含的Span子组件2\n');
    Span('Span自定义组件内容');
  }
}

@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    console.info('nav index');
  }

  @Builder
  pages() {
    pageOne();
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('点击跳转到NavDestination页面')
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' });
          });
      }.height('100%')
      .justifyContent(FlexAlign.Center);

    }.navDestination(this.pages);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/okcsi1iGQ-6LJVVOisumwA/zh-cn_image_0000002658798917.png?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=010E5861A836EF366478F48AC461ED42BB574AA16ADBC5F1F6297944DB168D75)

3. 如果需要使用自定义组件，应该选择支持自定义子组件的组件，比如Column组件。
```text
@Component
export struct CustomSpan {
  aboutToAppear(): void {
    console.info('nav custom span');
  }

  build() {
    Text('Span自定义组件内容');
  }
}

@Component
export struct pageOne {
  build() {
    NavDestination() {
      Column() {
        Text() {
          Span('Text直接包含的Span子组件1\n');
          Span('Text直接包含的Span子组件2\n');
        };

        CustomSpan();
      }.height('100%')
      .justifyContent(FlexAlign.Center);
    };
  }
}

@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    console.info('nav index');
  }

  @Builder
  pages() {
    pageOne();
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('点击跳转到NavDestination页面')
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' });
          });
      }.height('100%')
      .justifyContent(FlexAlign.Center);

    }.navDestination(this.pages);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/zOcuOjfhQWuPgnUyaaBuxg/zh-cn_image_0000002628559556.png?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=AA63AC29EFCDC2D44004F4DB755AFBA009E7994FE3DC5A0060F7286C37795652)

 
 

#### 总结

- 组件下的子组件在使用时，首先要判断该组件支持的子组件类型，只有支持的子组件才能使用，才能保证所有场景都正确显示，比如Span组件只能在Text、ContainerSpan组件里使用。所以，最好按照组件规格说明来使用组件。
- 自定义组件在使用时，要判断其所在父组件是否支持自定义组件，如果不支持，则不应该包含自定义组件。比如Text组件不支持自定义组件，就不能在Text的子组件里使用自定义组件。否则，系统不能保证所有场景显示都符合预期。
- 自定义组件在使用时，也要判断自定义组件的最外层组件的使用范围。比如，自定义组件最外层是Span，而Span只能在Text和ContainerSpan里使用，如果用在Column里，则不会生效。
