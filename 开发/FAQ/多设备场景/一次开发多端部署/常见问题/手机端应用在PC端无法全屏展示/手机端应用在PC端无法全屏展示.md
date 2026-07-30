# 手机端应用在PC端无法全屏展示

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-2

#### 问题现象

手机端应用在PC上仍显示为手机样式UI，无法打开全屏。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/NNPxFT8bTHGrLmtnp5SuZg/zh-cn_image_0000002628392502.png?HW-CC-KV=V1&HW-CC-Date=20260730T072245Z&HW-CC-Expire=86400&HW-CC-Sign=D95A907A4FFFC2C3565AD4048A2D59238273CA50CBE5CC8A63F8E676D2133108)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/JeCojTLsQUihbF0EnxK-PQ/zh-cn_image_0000002658791773.png?HW-CC-KV=V1&HW-CC-Date=20260730T072245Z&HW-CC-Expire=86400&HW-CC-Sign=EC7B419480B11DDF2560288EEC5C2427CF22F1AC625A6C4CDE3C154A691378DC)

 
PC上进行全屏展示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/wLgUV1wUTiOnTYf3bs74bA/zh-cn_image_0000002628552392.png?HW-CC-KV=V1&HW-CC-Date=20260730T072245Z&HW-CC-Expire=86400&HW-CC-Sign=4625EE38EE48A379876AE5885719A33DAD0D396EA3FA49E33936A8BFC7C24D35)

 
 

#### 背景知识

[一多适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-overview)提供帮助开发者快速开发出适配多种类型设备的应用的能力。一多适配开发使用的布局能力包括以下两种方式：
 
- [自适应布局](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-adaptive-layout)：开发框架提供了拉伸，均分，占比，缩放，延伸，隐藏，折行等七种自适应布局能力。这些布局能力可以独立使用，也可多种布局叠加使用。
- [响应式布局](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout)：基于响应式设计方法论进行布局的方法，核心思想是页面根据不同屏幕尺寸，进行不同的UI展示，以此自动调整布局。

 
 

#### 问题定位
1. 排查项目代码中所有module.json5配置文件中的deviceTypes配置项，是否包含了'2in1'选项。
2. 排查项目代码中UI相关的代码，是否针对PC端使用自适应布局和响应式布局，做了一多适配的逻辑。
 
 

#### 分析结论
1. 项目代码中的module.json5配置文件中的deviceTypes配置项，未包含'2in1'。
2. 项目代码中未使用响应式布局逻辑进行设备屏幕的尺寸的监听，导致页面UI在PC端展示变形。
 
 

#### 修改建议
1. 修改项目中的所有module.json5配置文件中的deviceTypes配置项，新增'2in1'项。如果项目中包含多个模块，每个模块的module.json5都需要修改deviceTypes配置。
2. 监听屏幕尺寸，获取相应的断点进行保存。
```text
smListener: mediaquery.MediaQueryListener =
  this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
mdListener: mediaquery.MediaQueryListener =
  this.getUIContext().getMediaQuery().matchMediaSync('(520vp<=width<840vp)');
lgListener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(840vp<=width)');

<em>// 注册媒体属性变更回调事件，监听屏幕尺寸在页面初始化的时候完成注册。</em>
public register() {
  this.smListener = this.getUIContext().getMediaQuery().matchMediaSync('(320vp<=width<520vp)');
  this.smListener.on('change', this.isBreakpointSM);
  this.mdListener = this.getUIContext().getMediaQuery().matchMediaSync('(520vp<=width<840vp)');
  this.mdListener.on('change', this.isBreakpointMD);
  this.lgListener = this.getUIContext().getMediaQuery().matchMediaSync('(840vp<=width)');
  this.lgListener.on('change', this.isBreakpointLG);
}

<em>// 保存屏幕尺寸的断点</em>
private updateCurrentBreakpoint(breakpoint: string) {
  if (this.currentBreakpoint !== breakpoint) {
    this.currentBreakpoint = breakpoint;
    AppStorage.set<string>('currentBreakpoint', this.currentBreakpoint);
  }
}

private isBreakpointSM = (mediaQueryResult: mediaquery.MediaQueryResult) => {
  if (mediaQueryResult.matches) {
    this.updateCurrentBreakpoint('sm');
  }
};

private isBreakpointMD = (mediaQueryResult: mediaquery.MediaQueryResult) => {
  if (mediaQueryResult.matches) {
    this.updateCurrentBreakpoint('md');
  }
};

private isBreakpointLG = (mediaQueryResult: mediaquery.MediaQueryResult) => {
  if (mediaQueryResult.matches) {
    this.updateCurrentBreakpoint('lg');
  }
};
```

3. 通过判断断点，刷新UI页面。以下代码片段以tab元素为例。
```text
@StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';<em> // 初始化默认为手机</em>

build() {
  Column() {
    Tabs({
      barPosition: this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG ? BarPosition.Start : BarPosition.End,
    }) {
    <em>  // tab内容</em>

    }
    .barWidth(this.currentBreakpoint === 'lg' ?
      $r('app.float.barWidth') : StyleConstants.FULL_WIDTH)
    .barHeight(this.currentBreakpoint === 'lg' ?
      StyleConstants.SIXTY_HEIGHT : $r('app.float.back_width'))
    .vertical(this.currentBreakpoint === 'lg')
  }
}
```

4. 对页面其他元素或组件，采用相应的自适应布局或响应式布局进行相应的改造。
