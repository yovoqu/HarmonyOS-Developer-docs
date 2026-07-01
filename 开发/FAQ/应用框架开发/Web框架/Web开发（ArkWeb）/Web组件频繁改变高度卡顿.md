# Web组件频繁改变高度卡顿

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-140

## Web组件频繁改变高度卡顿
 


##### 问题现象

频繁调整Web组件的高度导致卡顿？
 
 

##### 背景知识

[onScaleChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onscalechange9)：当前页面显示比例的变化时触发该回调。
 
 

##### 解决方案

- 由于高度更新过于频繁，触发了不必要的重渲染或布局计算。
- 可以使用节流或防抖来限制更新频率，减少性能消耗。

 
ArkTS代码如下：
 
```text
import { webview } from '@kit.ArkWeb';

@Component
struct Demo {
  public controller: webview.WebviewController = new webview.WebviewController();
  changeEvent: (event: OnScaleChangeEvent) => void = () => {
  };

  build() {
    Web({
      src: $rawfile('webScaleChange.html'),
      controller: this.controller
    })
      .zoomAccess(true)
      .fileAccess(false)
      .geolocationAccess(false)
      .onScaleChange((event) => {
        this.changeEvent(event);
      })
      .horizontalScrollBarAccess(false)
      .verticalScrollBarAccess(false);
  }
}

class Util {
  // 防抖，在一段时间内函数被多次触发，防抖让函数在一段时间内只执行一次
  static debounce(fun: (height: number) => void, delay?: number) {
    let timer: number;
    return (height: number) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        fun(height);
      }, delay ? delay : 300);
    };
  }
}

@Entry
@Component
struct Index {
  @State webHeight: number = 600; // 当前显示高度
  constWebHeight: number = 600; // 基础计算高度
  originScale: number = 100; // 初始比例
  webController: webview.WebviewController = new webview.WebviewController();
  // 创建防抖函数实例（300ms延迟）
  debouncedSetHeight: (height: number) => void = Util.debounce((newHeight: number) => {
    this.webHeight = newHeight;
    console.info(`防抖后高度：${this.webHeight}`);
  }, 300);

  build() {
    Column() {
      Demo({
        controller: this.webController,
        changeEvent: (event: OnScaleChangeEvent) => {
          const targetHeight = this.constWebHeight * event.newScale / this.originScale;
          this.debouncedSetHeight(targetHeight); // 此处触发防抖函数，替换成this.webHeight = targetHeight则表示不采用防抖函数
        }
      });
    }
    .height(this.webHeight)
    .width('100%');
  }
}
```
 
html代码如下：
 
```text


    
    
    复杂页面示例
    


    
        
            首页
            新闻
            联系我们
            关于我们
        
    


    
        欢迎来到我们的网站
        这是一个示例页面，展示了如何创建一个复杂的HTML页面。
    
    
        最新新闻
        
            新闻标题
            这里是新闻的详细内容。
        
    
    
        侧边栏
        这里是一些额外的信息或者广告。
    


    © 2023 公司名称. 保留所有权利。


    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    header {
        background: #333;
        color: #fff;
        padding: 10px 0;
    }
    nav ul {
        list-style: none;
        padding: 0;
    }
    nav ul li {
        display: inline;
        margin-right: 10px;
    }
    nav ul li a {
        color: #fff;
        text-decoration: none;
    }
    main {
        display: flex; /* 使用Flexbox布局 */
    }
    section, aside {
        padding: 20px;
    }
    section#home {
        flex: 3; /* 主内容区域占据更多空间 */
    }
    aside {
        flex: 1; /* 侧边栏占据较少空间 */
        background: #f4f4f4;
    }
    footer {
        text-align: center;
        padding: 10px 0;
        background: #333;
        color: #fff;
    }

```
 
可以通过双指捏动手机屏幕来实现页面的放大和缩小，对比观察是否采用防抖函数时的现象差。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/RS_WH2L9QDuGwhLcLifkNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025740Z&HW-CC-Expire=86400&HW-CC-Sign=F7DBEC4FEA632D0DDD35E9021B3AEB1DE269CCE2909811C401BD04129B8889D6)
 

防抖函数设置的时延delay指的是改变Column组件高度webHeight的间隔时间。
 

 
 

##### 常见FAQ

Q：使用Web组件页面时，在网页加载过程中，页面底部可能出现闪烁现象。
 
A：应用可以通过设置与网页背景色相同的Web组件的背景色，避免视觉闪烁。请参阅[闪烁原因](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-router-flash-optimization#闪烁原因)和[优化方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-router-flash-optimization#优化方法)了解详情。
