# 页面跳转后bindSheet不消失于原页面

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-583

#### 问题现象

在A页面打开bindSheet后跳转其他页面，希望返回A页面时bindSheet仍是打开状态。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/exZm3qYCQmyKccojDZJrMQ/zh-cn_image_0000002658791767.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041333Z&HW-CC-Expire=86400&HW-CC-Sign=40A74CBA96A2BBBA7F41304197E46B36403EB4D098017DFD57F73AC13CAED614)

 
 

#### 背景知识

- [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)为组件绑定半模态页面。
- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)用于页面间的路由导航组件，作为页面的根容器使用，[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)作为Navigation目的页面的根节点。
- [pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname11)用于跳转指定的NavDestination页面，同时可以使用onPop回调函数来处理新页面返回的结果。
- onPop的返回类型为[PopInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#popinfo11)，包含一个由开发者定义的对象result，[pop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pop11)方法可以触发onPop回调并传入页面处理结果。

 
 

#### 解决方案
1. 定义状态变量isShow控制bindSheet显隐。
2. 利用onPop回调函数的返回值PopInfo中的result的值决定isShow。在如下代码中，若传回的result的值为1，则令isShow=true。
3. 在子页面中使用pop方法传入result的值。
 
完整示例参考如下：
 
页面一：
 
```text
@Entry
@Component
struct PageOne {
<em>  // 定义状态变量isShow控制bindSheet显隐</em>
  @State isShow: Boolean = false;
  pageInfo: NavPathStack = new NavPathStack();

  @Builder
  myBuilder() {
    Column() {
      Button('ToSecondPage').fontSize(15).height(50).onClick(() => {
        this.isShow = false;
        this.pageInfo.pushPathByName('SecondPage', '', (onPop) => {
          this.isShow = (onPop.result as number) === 1;
        });
      });

    };
  }

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('bindSheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: SheetSize.MEDIUM,
            blurStyle: BlurStyle.Thick,
            showClose: true,
            title: { title: 'title', subtitle: 'subtitle' },
            preferType: SheetType.CENTER,
          });
      };
    };
  }
}
```
 
页面二：
 
```text
@Builder
export function SecondPageBulider() {
  SecondPage();
}

@Entry
@Component
export struct SecondPage {
  pageInfo = new NavPathStack();

  onBackPress(): boolean | void {
  }

  build() {
    NavDestination() {
      Column() {
        Button('ToSecondPage').fontSize(15).height(50).onClick(() => {
          this.pageInfo.pop(1);
        });
      };
    }
    .onReady((navctx) => {
      this.pageInfo = navctx.pathStack;
    })
    .width('100%')
    .height('100%');
  }
}
```
 
在“src/main”目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router_map"，并在“src/main/resources/base/profile”目录下新增router_map.json。
 
router_map.json：
 
```ArkTS
{
  "routerMap": [
    {
      "name": "SecondPage",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "SecondPageBulider"
    }
  ]
}
```
