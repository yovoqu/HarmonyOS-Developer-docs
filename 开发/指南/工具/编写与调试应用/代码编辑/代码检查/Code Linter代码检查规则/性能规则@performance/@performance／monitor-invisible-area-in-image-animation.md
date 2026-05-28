# @performance/monitor-invisible-area-in-image-animation

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-monitor-invisible-area-in-image-animation

使用ImageAnimation实现帧动画时，建议显式调用monitorInvisibleArea接口。在动画组件不可见时，会停止动画播放，减少无效的冗余动画带来的负载恶化。
 

##### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/monitor-invisible-area-in-image-animation": "warn",
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
@Entry
@Component
struct ImageAnimatorTest {
  @State message: string = 'hello world';
  build() {
    Column() {
      ImageAnimator()
        .images([])
        .borderRadius(10)
        .monitorInvisibleArea(true)
      test1()
    }
    .width('100%')
  }
}
@Builder
function test1() {
  ImageAnimator()
    .monitorInvisibleArea(true)
}
```
 
 

##### 反例

```text
@Entry
@Component
struct ImageAnimatorTest {
  @State message: string = 'hello world';
  build() {
    Column() {
      ImageAnimator()
        .images([])
        .borderRadius(10)
      test1()
    }
    .width('100%')
  }
}
@Builder
function test1() {
  ImageAnimator()
    .images([])
    .borderRadius(10)
}
```
 
 

##### 规则集

```text
<span style="color: rgb(80,160,79);">plugin:@performance/</span><span style="color: rgb(0,0,255);">recommended</span>
<span style="color: rgb(80,160,79);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
