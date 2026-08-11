# 如何实现全局层级的自定义UI控件

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-617

#### 问题现象

如何开放UI实现到组件外部，由外部自由定制一个或多个封装好的UI内容，使其可以被跨组件或跨页面调用？
 
 

#### 背景知识

- [@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)：@Builder装饰器用于封装可复用的UI结构，通过提取重复的布局代码提高开发效率。
- [wrapBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder)：当在一个struct内使用多个全局@Builder函数实现UI的不同效果时，代码维护将变得非常困难，且页面不够整洁。此时，可以使用wrapBuilder封装全局@Builder。

 
 

#### 解决方案

实现思路如下：UI内容由全局@Builder自定义构建函数进行封装。通过注册表注册一个WrappedBuilder数组来管理UI，在组件中通过ForEach的方式渲染这个WrappedBuilder数组，这样可以通过管理该WrappedBuilder数组来动态渲染定制的UI内容。
 1. 采用单例模式管理全局UI组件注册表（EllaBookUIView）。
通过IBookUIComponent（书籍UI组件接口）规范组件实现，通过getUIBuilder获取组件构建器实现解耦。
```text
export interface IBookUIComponent {
 <em> // 获取UI构建器</em>
  getUIBuilder: WrappedBuilder<[]>;
 <em> // 组件名称</em>
  componentName?: string;
}
```

2. 通过全局UI组件注册表（EllaBookUIView）实现动态扩展组件注册机制。
```text
export class EllaBookUIView {
  private static instance: EllaBookUIView | null = null;
  private components: IBookUIComponent[] = [];

  private constructor() {
  }

<em>  // 获取单例</em>
  public static getInstance(): EllaBookUIView {
    if (!EllaBookUIView.instance) {
      EllaBookUIView.instance = new EllaBookUIView();
    }
    return EllaBookUIView.instance;
  }

 <em> // 注册组件</em>
  public registerComponent(component: IBookUIComponent): void {
    this.components.push(component);
    console.info(`[BookUIRegistry] 组件注册成功: ${component.componentName || '未命名组件'}`);
  }

<em>  // 获取所有组件构建器</em>
  public getAllBuilders(): WrappedBuilder<[]>[] {
    return this.components.map(component => component.getUIBuilder);
  }

 <em> // 清除所有组件</em>
  public clearComponents(): void {
    this.components = [];
    console.info('[BookUIRegistry] 所有组件已清除');
  }
}
```

3. 控制组件实现：ControlButtons结构体实现书籍基础控制功能。
顶部控制栏：退出按钮+播放/暂停按钮。
4. 底部控制栏：翻页按钮组。
```text
@Component
struct ControlButtons {
  @State isPlaying: boolean = true;<em> // 播放状态</em>

 <em> // 退出书籍</em>
  private exitBook() {
    console.info('退出书籍');
  }

 <em> // 切换播放状态</em>
  private togglePlay() {
    this.isPlaying = !this.isPlaying;
    console.info(this.isPlaying ? '播放中' : '已暂停');
  }

 <em> // 上一页</em>
  private prevPage() {
    console.info('上一页');
  }

 <em> // 下一页</em>
  private nextPage() {
    console.info('下一页');
  }

  build() {
    Stack({ alignContent: Alignment.BottomStart }) {
    <em>  // 顶部控制栏</em>
      Row() {
      <em>  // 1.顶部最左侧---退出按钮</em>
        Button() {
          Image($r('app.media.xmark'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(20)
        .onClick(() => {
        <em>  // 退出逻辑</em>
          this.exitBook();
        });

        Blank();
      <em>  // 2.顶部最右侧---播放/暂停按钮</em>
        Button() {
          if (this.isPlaying) {
            Image($r('app.media.pause'))
              .objectFit(ImageFit.Contain);
          } else {
            Image($r('app.media.play'))
              .objectFit(ImageFit.Contain);
          }
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(20)
        .onClick(() => {
          this.togglePlay();
        });
      }
      .width('100%')
      .padding(10)
      .position({ x: 0, y: 0 });

    <em>  // 底部控制栏</em>
      Row() {
     <em>   // 3.底部最左侧---上一页按钮</em>
        Button() {
          Image($r('app.media.chevron_left'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(25)
        .onClick(() => {
          this.prevPage();
        });

        Blank();
     <em>   // 4.底部最右侧---下一页按钮</em>
        Button() {
          Image($r('app.media.chevron_right'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(25)
        .onClick(() => {
          this.nextPage();
        });
      }
      .width('100%')
      .padding(10);
    }
    .width('100%')
    .height('100%');
  };
}

<em>// 创建UI构建器</em>
@Builder
function controlBuilder() {
  ControlButtons();
}
```

5. BookUIComponents类实现接口规范，将构建器包装为可注册单元。
```text
export class BookUIComponents implements IBookUIComponent {
  componentName: string = '书籍控制组件';
  getUIBuilder: WrappedBuilder<[]> = wrapBuilder(controlBuilder);
}
```

6. 页面调用：通过ForEach动态渲染注册的构建器，BuilderComponent作为通用容器解析并执行构建器逻辑。
```text
Stack({ alignContent: Alignment.TopStart }) {
  Column({ space: 16 }) {
    Button('打开书籍控制器控件')
      .onClick(() => {
        ellaBookUIView.registerComponent(new BookUIComponents());
        this.uiBuilders = ellaBookUIView.getAllBuilders();
      });
    Button('关闭书籍控制器控件')
      .onClick(() => {
        ellaBookUIView.clearComponents();
        this.uiBuilders = ellaBookUIView.getAllBuilders();
      });
  }.height('100%').width('100%');

  ForEach(this.uiBuilders,
    (builder: WrappedBuilder<[]>) => {
     <em> // 使用公共属性传递索引</em>
      BuilderComponent({ builder: builder })
        .hitTestBehavior(HitTestMode.Transparent);
    }
  );
};
```

 
完整示例如下：
 
```text
<em>// 书籍UI组件接口</em>
export interface IBookUIComponent {
 <em> // 获取UI构建器</em>
  getUIBuilder: WrappedBuilder<[]>;
 <em> // 组件名称</em>
  componentName?: string;
}

<em>// 全局UI组件注册表</em>
export class EllaBookUIView {
  private static instance: EllaBookUIView | null = null;
  private components: IBookUIComponent[] = [];

  private constructor() {
  }

 <em> // 获取单例</em>
  public static getInstance(): EllaBookUIView {
    if (!EllaBookUIView.instance) {
      EllaBookUIView.instance = new EllaBookUIView();
    }
    return EllaBookUIView.instance;
  }

 <em> // 注册组件</em>
  public registerComponent(component: IBookUIComponent): void {
    this.components.push(component);
    console.info(`[BookUIRegistry] 组件注册成功: ${component.componentName || '未命名组件'}`);
  }

 <em> // 获取所有组件构建器</em>
  public getAllBuilders(): WrappedBuilder<[]>[] {
    return this.components.map(component => component.getUIBuilder);
  }

 <em> // 清除所有组件</em>
  public clearComponents(): void {
    this.components = [];
    console.info('[BookUIRegistry] 所有组件已清除');
  }
}
<em>// 导出全局单例</em>
export const ellaBookUIView = EllaBookUIView.getInstance();

@Component
struct ControlButtons {
  @State isPlaying: boolean = true; <em>// 播放状态</em>

 <em> // 退出书籍</em>
  private exitBook() {
    console.info('退出书籍');
  }

<em>  // 切换播放状态</em>
  private togglePlay() {
    this.isPlaying = !this.isPlaying;
    console.info(this.isPlaying ? '播放中' : '已暂停');
  }

 <em> // 上一页</em>
  private prevPage() {
    console.info('上一页');
  }

 <em> // 下一页</em>
  private nextPage() {
    console.info('下一页');
  }

  build() {
    Stack({ alignContent: Alignment.BottomStart }) {
     <em> // 顶部控制栏</em>
      Row() {
      <em>  // 1.顶部最左侧---退出按钮</em>
        Button() {
          Image($r('app.media.xmark'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(20)
        .onClick(() => {
        <em>  // 退出逻辑</em>
          this.exitBook();
        });

        Blank();
     <em>   // 2.顶部最右侧---播放/暂停按钮</em>
        Button() {
          if (this.isPlaying) {
            Image($r('app.media.pause'))
              .objectFit(ImageFit.Contain);
          } else {
            Image($r('app.media.play'))
              .objectFit(ImageFit.Contain);
          }
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(20)
        .onClick(() => {
          this.togglePlay();
        });
      }
      .width('100%')
      .padding(10)
      .position({ x: 0, y: 0 });

    <em>  // 底部控制栏</em>
      Row() {
      <em>  // 3.底部最左侧---上一页按钮</em>
        Button() {
          Image($r('app.media.chevron_left'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(25)
        .onClick(() => {
          this.prevPage();
        });

        Blank();
      <em>  // 4.底部最右侧---下一页按钮</em>
        Button() {
          Image($r('app.media.chevron_right'))
            .objectFit(ImageFit.Contain);
        }
        .height(24)
        .width(24)
        .backgroundColor(Color.Transparent)
        .borderRadius(25)
        .onClick(() => {
          this.nextPage();
        });
      }
      .width('100%')
      .padding(10);
    }
    .width('100%')
    .height('100%');
  };
}

<em>// 创建UI构建器</em>
@Builder
function controlBuilder() {
  ControlButtons();
}

export class BookUIComponents implements IBookUIComponent {
  componentName: string = '书籍控制组件';
  getUIBuilder: WrappedBuilder<[]> = wrapBuilder(controlBuilder);
}

@Entry
@Component
struct Page {
  @State uiBuilders: WrappedBuilder<[]>[] = [];

  build() {
    Column() {
      Stack({ alignContent: Alignment.TopStart }) {
        Column({ space: 16 }) {
          Button('打开书籍控制器控件')
            .onClick(() => {
              ellaBookUIView.registerComponent(new BookUIComponents());
              this.uiBuilders = ellaBookUIView.getAllBuilders();
            });
          Button('关闭书籍控制器控件')
            .onClick(() => {
              ellaBookUIView.clearComponents();
              this.uiBuilders = ellaBookUIView.getAllBuilders();
            });
        }.height('100%').width('100%');

        ForEach(this.uiBuilders,
          (builder: WrappedBuilder<[]>) => {
         <em>   // 使用公共属性传递索引</em>
            BuilderComponent({ builder: builder })
              .hitTestBehavior(HitTestMode.Transparent);
          }
        );
      };
    };
  }
}

@Component
struct BuilderComponent {
  builder?: WrappedBuilder<[]>;

  build() {
    if (this.builder) {
      this.builder.builder();
    } else {
      Text('暂无构建');
    }
  }
}
```
 
实现效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/skbtsio9S66CmsXsx3YjUA/zh-cn_image_0000002628554166.png?HW-CC-KV=V1&HW-CC-Date=20260811T005704Z&HW-CC-Expire=86400&HW-CC-Sign=A298255FAD5675556E96535C9252A2B0051E70E9B6397AC5CB1A8196BB3EB88F)
