# 如何解决单个状态变量绑定多个@Watch监听器时部分监听器失效的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1579

#### 问题现象

在HarmonyOS开发中，当一个状态变量@State绑定了两个@Watch监听器时，观察到其中一个监听器生效，而另一个监听器未生效。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct S20250403171354570182 {
  @State @Watch('change1') @Watch('change2') num: number = 0;

  // 监听不生效
  change1() {
    console.info('watch1 ');
  }

  // 监听生效
  change2() {
    console.info('watch2');
  }

  build() {
    RelativeContainer() {
      Text(this.num.toString())
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.num++;
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
 
change1()函数未执行，change2()函数被执行，问题现象如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/HmJfKy9DQr2m8Y_x7NAZlw/zh-cn_image_0000002628770192.png?HW-CC-KV=V1&HW-CC-Date=20260811T005819Z&HW-CC-Expire=86400&HW-CC-Sign=134A9DA9320C95465FA829B3CA71B25235357031F9A997AB6F934E8671944EA9)

 
 

#### 解决方案

状态变量的变化无法被多个[@Watch](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)监听器同时监听。因此，需要将所有需要在状态变量变化时执行的操作合并到一个@Watch回调方法中，删除多余的@Watch和回调方法。
 
 

#### 总结

多个@Watch不能用于一个状态变量，如果使用多个会导致后面的监听器覆盖前面，导致出现多余的代码。如果想要使用一个监听器监听多个变量可以使用状态管理V2中的[@Monitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor)装饰器，其差异详见官方文档[@Monitor与@Watch对比](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor#monitor与watch对比)。
