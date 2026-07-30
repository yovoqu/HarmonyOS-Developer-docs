# 如何实现Canvas绘制刷新以及防止绘制丢失

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1049

#### 问题现象

Canvas动态绘制时，如何实现内容实时刷新与防止绘制丢失是两大核心问题，如何有效解决？
 
 

#### 背景知识

- [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)：提供画布组件，用于自定义绘制图形。
- [onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#onready)：Canvas组件初始化完成或者发生大小变化时的事件回调，当该事件被触发时画布被清空。
- [@Monitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor)：@Monitor装饰器用于监听状态变量修改，使得状态变量具有深度监听的能力。

 
 

#### 解决方案

- **场景一**：Canvas绘制如何刷新。Canvas无自动重绘机制，需要手动触发绘制刷新，共有4种实现方式，对比如下：

| 实现方式 | 触发机制 | 适用场景 |

| --- | --- | --- |

| 利用clearRect方法清空画布。 | 开发者手动调用。 | 局部刷新场景（如擦除部分区域）。 |

| 利用reset方法重置画布。 | 开发者手动调用。 | 全部重绘场景（如重置Canvas路径、样式）。 |

| 利用@Watch装饰器监听变量，根据变量变化刷新。 | 数据变量变更时自动触发。 | 数据驱动的动态内容（如实时进度条、图表）、需要与UI状态强绑定的场景，用状态管理V1实现。 |

| 利用@Monitor装饰器监听变量，根据变量变化刷新。 | 数据变量变更时自动触发。 | 数据驱动的动态内容（如实时进度条、图表）、需要与UI状态强绑定的场景，用状态管理V2实现。 |

  
**方式一**：利用[clearRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#clearrect)方法清空画布，进而重新绘制，代码示例如下：
```text
@Entry
@Component
struct CanvasClearRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Canvas(this.context)
        .width(300)
        .height(400)
        .onReady(() => {
          this.context.fillStyle = '#0097D4';
          this.context.fillRect(50, 100, 200, 100);
        })
        .backgroundColor('#f1f3f5');

      Button('Re Draw')
        .width('80%')
        .margin({ top: 20 })
        .onClick(() => {
          this.draw();
        });
    }
    .height('100%')
    .width('100%');
  }

  private draw() {
   <em> // 用clearRect清除画布中内容</em>
    this.context.clearRect(0, 0, 300, 400);
    this.context.fillStyle = '#0097D4';
    this.context.beginPath();
    this.context.arc(100, 100, 50, 0, 2 * Math.PI);
    this.context.fill();
  }
}
```
 实现效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/6sHJ8yvXTnOPFnsN15GY9Q/zh-cn_image_0000002628565454.png?HW-CC-KV=V1&HW-CC-Date=20260730T072516Z&HW-CC-Expire=86400&HW-CC-Sign=6E20AB768631230C61EE6F4FA2D9B3F22BA8A28C944C5AD847574CB6371FE1DD)

- **方式二**：利用[reset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#reset12)方法重置画布状态，清空绘制路径，代码示例如下：
```text
@Entry
@Component
struct CanvasReset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
 <em> // "common/images/example.png"需要替换为开发者所需的图像资源文件</em>
  private img: ImageBitmap = new ImageBitmap('common/images/example.png');
  private angle: number = Math.PI * 5 / 4;

  build() {
    Column() {
      Canvas(this.context)
        .width(300)
        .height(300)
        .onReady(() => {
          this.draw();
        })
        .backgroundColor('#f1f3f5');

      Button('Re Draw')
        .width('80%')
        .margin({ top: 20 })
        .onClick(() => {
          this.angle += Math.PI / 4;
          this.draw();
        });
    }
    .height('100%')
    .width('100%');
  }

  private draw() {
  <em>  // 这里clearRect无法清除路径，需要用reset重置画布状态</em>
    this.context.reset();
    let width = 300;
    this.context.beginPath();
    this.context.moveTo(width / 2, width / 2);
    this.context.arc(width / 2, width / 2, width / 2, Math.PI, this.angle);
    this.context.clip();
    this.context.drawImage(this.img, 0, 0, width, width);
  }
}
```
 实现效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/gPhGqc3IR76cUfCC1GgSQg/zh-cn_image_0000002658924761.png?HW-CC-KV=V1&HW-CC-Date=20260730T072516Z&HW-CC-Expire=86400&HW-CC-Sign=FAFE0678EF3059D11558B8D34608641BB119DA711E34EF0AECBFC44C2DD57822)

- **方式三**：利用[@Watch](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)装饰器监听状态变量，当数据刷新时，触发重新绘制逻辑，示例参考：[Canvas绘制内容如何动态更新](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-225)。
- **方式四**：利用@Monitor装饰器监听嵌套Class对象属性的变化，代码示例如下：
```text
@ObservedV2
class User {
  @Trace name: string;
  @Trace age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

@Entry
@ComponentV2
struct CanvasMonitor {
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
  @Local userArr: Array<User> = [new User('Tom', 24), new User('Jerry', 18)];

  @Monitor('userArr.length')
  draw() {
    this.context.clearRect(0, 0, 200, 500);
    for (let i = 0; i < this.userArr.length; i++) {
      this.context.fillText(this.userArr[i].name, 50, i * 30 + 50);
      this.context.fillText(this.userArr[i].age.toString(), 100, i * 30 + 50);
    }
  }

  build() {
    Column() {
      Canvas(this.context)
        .width(300)
        .height(400)
        .onReady(() => {
          this.context.font = '60px';
          this.draw();
        })
        .height('25%')
        .width('100%')
        .backgroundColor('#f1f3f5');

      Button('Change info property')
        .width('80%')
        .margin({ top: 20 })
        .onClick(() => {
          this.userArr.push(new User('Kitty', 12));
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
 实现效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/TPt5l8Z0RteXQSoTYYAwIQ/zh-cn_image_0000002628405556.png?HW-CC-KV=V1&HW-CC-Date=20260730T072516Z&HW-CC-Expire=86400&HW-CC-Sign=D360EB5DADDCEC1F1F74600E1B09CE37E37391487D0303F389A1DA5FED45927A)


 - **场景二**：Canvas绘制防止丢失。Canvas的onReady方法在Canvas组件初始化完成或者发生大小变化时会触发。比如折叠屏展开场景、横竖屏切换场景以及动态扩展Canvas组件宽高场景，可能会触发onReady方法，这时在onReady方法之外绘制的内容就会丢失，需要恢复绘制，共有2种实现方式，对比如下：

| 实现方式 | 触发机制 | 适用场景 |

| --- | --- | --- |

| 在onReady中恢复绘制。 | Canvas初始化完成时或者发生大小变化时。 | 绘制内容较少时，不涉及监听尺寸变化场景。 |

| 在onAreaChange事件恢复绘制。 | Canvas尺寸发生大小变化时。 | 需要精确根据尺寸变化进行绘制的场景。 |

  
**方式一**：在onReady方法中恢复画布绘制，示例参考：[横竖屏切换时，如何防止画布被清空](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-36)。
- **方式二**：绑定[onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)方法，Canvas大小发生变化时同样会触发onAreaChange事件，这时可以在onAreaChange中恢复绘制逻辑，代码示例如下：
```text
@Entry
@Component
struct CanvasOnAreaChange {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State myWidth: number = 300;

  build() {
    Column() {
      Canvas(this.context)
        .width(this.myWidth)
        .height(400)
        .onReady(() => {
          this.context.fillStyle = '#0097D4';
        })
        .onAreaChange(() => {
          <em>// 监听尺寸变化事件，重新绘制，恢复画布</em>
          this.draw();
        })
        .backgroundColor('#f1f3f5');

      Button('Change Size')
        .width('80%')
        .margin({ top: 20 })
        .onClick(() => {
          this.myWidth += 20;
        });
    }
    .height('100%')
    .width('100%');
  }

  private draw() {
    <em>// 用clearRect清除画布中内容</em>
    this.context.clearRect(0, 0, 300, 400);
    this.context.fillRect(50, 100, 200, 100);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/vSoI6FsZRTGd1FjKCxlbqA/zh-cn_image_0000002658804829.png?HW-CC-KV=V1&HW-CC-Date=20260730T072516Z&HW-CC-Expire=86400&HW-CC-Sign=3C200E97B488BDCCA363152CD672CA211D93503E7F53AAE939C1D30E5286EC64)


 
 
 

#### 常见FAQ

Q：在onReady方法中绘制了较多的内容，当Canvas尺寸变化时会触发重绘，引发闪烁如何解决？
 
A：这种情况可以避免在onReady方法中进行大量绘制，仅在其中设置Canvas属性，在外部方法中进行绘制；或者固定Canvas的宽高，防止触发onReady方法。
