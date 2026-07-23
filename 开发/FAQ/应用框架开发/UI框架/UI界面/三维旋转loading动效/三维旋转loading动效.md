# 三维旋转loading动效

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-648

#### 问题现象

如何实现具有三维旋转效果的加载动画界面？
 
 

#### 背景知识

- [animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)提供接口来指定由于闭包代码导致的状态变化插入过渡动效。
- [rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)是一种通用属性，可用于设置组件的旋转。

 
 

#### 解决方案
1. 调用animateTo动画函数，将旋转参数从初始值过渡到目标值并通过设置iterations:-1，实现无限循环。
```text
this.getUIContext()?.animateTo({
  duration: 2000,
  // 动画播放次数，设置为-1时表示无限次播放
  iterations: -1,
  curve: Curve.Linear
}, () => {
  this.num = 360;
  this.numZ = 470;
  this.twonum = 450;
  this.twonumZ = 470;
  this.treenum = 480;
  this.treenumZ = 450;
  this.formnum = 610;
  this.formnumZ = 630;
});
```

2. 通过rotate方法设置x/y/z轴旋转分量和旋转中心点(centerX/Y)，实现空间错位效果。
```text
.rotate({
  x: 50,
  y: 0,
  z: this.numZ,
  angle: this.num,
  centerX: 80,
  centerY: 80,
});
```

3. 完整示例参考如下：
```text
@Entry
@Component
struct RotatingAnimationDemo {
  @State num: number = 0;
  @State numZ: number = 100;
  @State twonum: number = 90;
  @State twonumZ: number = 90;
  @State treenum: number = 180;
  @State treenumZ: number = 90;
  @State formnum: number = 270;
  @State formnumZ: number = 270;


  onDidBuild(): void {
    this.getUIContext()?.animateTo({
      duration: 2000,
    <em>  // 动画播放次数，设置为-1时表示无限次播放</em>
      iterations: -1,
      curve: Curve.Linear
    }, () => {
      this.num = 360;
      this.numZ = 470;
      this.twonum = 450;
      this.twonumZ = 470;
      this.treenum = 480;
      this.treenumZ = 450;
      this.formnum = 610;
      this.formnumZ = 630;
    });
  };


  build() {
    Stack() {
      Row() {
      }
      .width(190)
      .height(190)
      .border({ width: { bottom: 8 }, color: 'rgb(255, 141, 249)', style: BorderStyle.Solid })
      .borderRadius(90)
      .rotate({
        x: 50,
        y: 0,
        z: this.numZ,
        angle: this.num,
        centerX: 80,
        centerY: 80,
      });
      Row() {
      }
      .width(190)
      .height(190)
      .border({ width: { bottom: 8 }, color: 'rgb(255, 65, 106)', style: BorderStyle.Solid })
      .borderRadius(90)
     <em> // 设置组件的旋转参数</em>
      .rotate({
        x: 20, <em>// 旋转轴向量x坐标</em>
        y: 50, <em>// 旋转轴向量y坐标</em>
        z: this.twonumZ,
        angle: this.twonum, <em>// 旋转角度</em>
        centerX: 80,<em> // 变换中心点x轴坐标</em>
        centerY: 80,
      });


      Row() {
      }
      .width(190)
      .height(190)
      .border({ width: { bottom: 8 }, color: 'rgb(0, 255, 255)', style: BorderStyle.Solid })
      .borderRadius(90)
      .rotate({
        x: 40,
        y: 150,
        z: this.treenumZ,
        angle: this.treenum,
        centerX: 80,
        centerY: 80,
      });


      Row() {
      }
      .width(190)
      .height(190)
      .border({ width: { bottom: 8 }, color: 'rgb(252, 183, 55)', style: BorderStyle.Solid })
      .borderRadius(90)
      .rotate({
        x: 70,
        y: 0,
        z: this.formnumZ,
        angle: this.formnum,
        centerX: 80,
        centerY: 80,
      });
      Row() {
        Text('loading...')
          .fontColor(Color.White);
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#212121')
  }
}
```
 效果图为：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/_5iN7d2eRaOI5lOG40Utsg/zh-cn_image_0000002628394516.png?HW-CC-KV=V1&HW-CC-Date=20260723T013135Z&HW-CC-Expire=86400&HW-CC-Sign=DD75618CFEBAA0C8E64CB1174846A670611107FE6D5F35D792499A16D60AA295)
