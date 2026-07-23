# 如何解决关闭bindSheet半模态窗口时退出动效执行两次的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-744

#### 问题现象

使用bindSheet半模态窗口实现应用分享的弹窗，在点击空白处或者拖动关闭bindSheet时，半模态窗口退出动效会执行两次。
 
问题现象图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/HWAh7jyTT1y-VrDwayaLug/zh-cn_image_0000002658914683.png?HW-CC-KV=V1&HW-CC-Date=20260723T012608Z&HW-CC-Expire=86400&HW-CC-Sign=A913FECD7DD6687A2E5F16C78AAEC304FAC788F09F4E1570F2D08C210E30C3FC)

 
效果预览:
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/1y5MfoNwQeOkgu61gK8Y-g/zh-cn_image_0000002658794733.png?HW-CC-KV=V1&HW-CC-Date=20260723T012608Z&HW-CC-Expire=86400&HW-CC-Sign=56ADC3D816D056946C6E2F9D022C64D56BA09107B5E73B0466733A693C9CDEA8)

 
复现问题示例代码如下：
 
```text
List() {
  ForEach(this.listObjs, (item: MenuObject, index: Number) => {
    ListItem() {
      MenuComponent({value: item}) <em>// 自定义组件</em>
        .width('100%')
        .onClick(() => {
          if (item.title === '分享给好友') {
            this.isShow = true
          } else {
           <em> // 跳转逻辑</em>
          }
        })
        .bindSheet($$this.isShow, this.ShareBuilder(), {
          detents: [SheetSize.FIT_CONTENT],
          dragBar: false,
          showClose: false,
          title: this.shareTitleBuilder,
        })
    }
  })
}
.width('100%')
.height('100%')
.divider({
  strokeWidth: 1,
  color: '#ffe9f0f0',
  startMargin: 20,
  endMargin: 20
})
```
 
 

#### 背景知识

- [半模态页面（bindSheet）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。用户可以通过bindSheet首参数控制半模态窗口的显示和退出，通过第二个参数设置[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)自定义半模态窗口显示的内容布局。
- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
- [ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)用来展示列表具体item，必须配合List来使用。

 
 

#### 问题定位

出现bindSheet半模态窗口退出动效执行两次，一般需要考虑bindSheet是否为多个组件绑定了半模态窗口。结合本案例问题分析如下：
 
- 案例使用了ForEach循环布局，循环创建多个ListItem。bindSheet绑定在ListItem的子节点上，所以会有多个循环子组件都绑定了半模态窗口，且设置了相同的ShareBuilder。
- 当点击“分享给好友”时，设置isShow为true，实际上同时弹出了多个半模态窗口叠加在一起。
- 当点击空白处关闭半模态窗口时，先关闭当前点击的窗口，关闭后通过双向绑定$$将isShow设置成false，这个时候剩余的半模态窗口都同时退出，触发退出的动效，所以从视觉上退出动效执行了两次。

 
 

#### 分析结论

本案例给多个子组件都绑定了半模态窗口，导致在退出半模态窗口时，触发多个窗口的退出动效。
 
 

#### 修改建议

为了避免出现bindSheet半模态窗口退出动效执行两次的问题，使用bindSheet半模态窗口时，只给指定的子组件绑定半模态窗口，其余子组件可以把bindSheet第二个参数CustomBuilder设置成undefined。示例代码如下：
 
```text
class MenuObject {
  title: string;

  constructor(title: string) {
    this.title = title;
  }
}

@Entry
@Component
struct BindSheetExample {
  pathStack: NavPathStack = new NavPathStack();
  @State isShow: boolean = false;
  private listObjs: MenuObject[] =
    [new MenuObject('账号管理'), new MenuObject('我的车辆'), new MenuObject('隐私政策'), new MenuObject('用户协议'),
      new MenuObject('分享给好友'), new MenuObject('关于')];

  @Builder
  title() {
    Row() {
      Text('分享至')
        .fontSize(20)
        .fontWeight(700)
        .fontColor(Color.Black);
      Image($r('app.media.close'))
        .width(42)
        .height(42)
        .onClick(() => {
          this.isShow = false;
        });
    }
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween);
  }

  @Builder
  ShareBuilder() {
    Column() {
    }
    .width('100%')
    .height(500)
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Navigation(this.pathStack) {
      Column() {
        List() {
          ForEach(this.listObjs, (item: MenuObject) => {
            ListItem() {
            <em>  // 自定义组件</em>
              MenuComponent({ value: item })
                .width('100%')
                .onClick(() => {
                  if (item.title === '分享给好友') {
                    this.isShow = true;
                  } else {
                   <em> // 跳转页面逻辑</em>

                  }
                })
             <em>   // 不需要bindSheet的子组件设置undefined</em>
                .bindSheet($$this.isShow, item.title === '分享给好友' ? this.ShareBuilder() : undefined,
                  {
                    detents: [SheetSize.FIT_CONTENT],
                    dragBar: false,
                    showClose: false,
                    title: this.title(),
                  });
            }
            .padding({
              top: 20,
              bottom: 20
            });
          });
        }
        .width('100%')
        .backgroundColor(Color.White)
        .borderRadius(16)
        .divider({
          strokeWidth: 1,
          color: '#ffe9f0f0',
          startMargin: 20,
          endMargin: 20
        });
      }
      .width('100%')
      .height('100%')
      .padding({
        left: 16,
        right: 16,
        top: 16
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#fff1f3f5');
  }
}

@Component
struct MenuComponent {
  @Prop value: MenuObject;

  build() {
    Row() {
      Text(this.value.title)
        .padding({ left: 15, top: 10, bottom: 10 });
    };
  }
}
```
