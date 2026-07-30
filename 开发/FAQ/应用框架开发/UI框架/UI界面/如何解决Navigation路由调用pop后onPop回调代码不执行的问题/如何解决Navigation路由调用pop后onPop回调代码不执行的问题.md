# 如何解决Navigation路由调用pop后onPop回调代码不执行的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-905

#### 问题现象

使用Navigation构建路由，从pageOne通过pushPath跳转到pageTwo，期望pageOne的onPop回调在pageTwo返回时被触发，但效果未达预期。
 
问题代码示例参考如下：
 
```json
class ParamWithOp {
  operation: number = 1
  count: number = 10
}

@Entry
@Component
struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  @State message: string = 'Hello World'

  @Builder
  pageMap(name: string, params: Object) {
    if (name === 'pageTwo') {
      PageTwo()
    }
  }

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
         <em>   // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。</em>
            this.pageInfo.pushPath({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message = `[pushPath]last page is: ${popInfo.info.name} result: ${JSON.stringify(popInfo.result)}`
              }
            });
          })
      }.width('100%').height('100%')
    }.navDestination(this.pageMap)
    .title('pageOne')
  }
}

@Component
struct PageTwo {
  pathStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
        <em>    // 回退到上一个页面，此处代码，在pop回pageOne页面时，未传参数</em>
            this.pathStack.pop();
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack
    })
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/L1st2PbJQN2h_zwlQFeIug/zh-cn_image_0000002628559672.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=9F57D3790062B9B4E1936D1961EBBFE980AC082C53414EDE4C6E233F93922757)

 
 

#### 背景知识

[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)组件是路由导航的根视图容器，结合导航控制器[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)可实现组件导航。
 
- [pushPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpath10)：将info指定的NavDestination页面信息入栈。可设置onPop回调函数来接收参数。
- [pop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pop11)：弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

 
 

#### 问题定位


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/gHjW6MhLRum804WO12pxMg/zh-cn_image_0000002658918979.png?HW-CC-KV=V1&HW-CC-Date=20260730T072442Z&HW-CC-Expire=86400&HW-CC-Sign=4D22C67E2AA4E2C53BD0F017C210A9EEC9A8FBDFD482221CC459AC33806B5DD5)

 
查阅官方文档关于pushPath方法的[NavPathInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathinfo10)入参说明，其中的onPop回调函数仅pop、[popToName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#poptoname11)、[popToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#poptoindex11)中设置result参数后触发。
 
 

#### 分析结论

onPop回调函数需要使用pop、popToName、popToIndex方法返回时设置result参数才会触发，否则不会执行onPop回调。
 
 

#### 修改建议

按上节所述，只需在pageTwo中调用pop方法时，传入result参数，即可在pageOne中成功收到onPop的回调。修改问题代码如下：
 
```text
<em>// 回退到上一个页面，随便传个result即可触发onPop回调</em>
this.pathStack.pop(1);
```
 
修改后的运行效果参见效果预览，可以看到，当pageTwo调用pop返回时传入了result参数，在pageOne成功执行了onPop回调，并接收到相关参数。
