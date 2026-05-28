# @cross-device-app-dev/sidebar-navigation

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_sidebar-navigation

对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@cross-device-app-dev/sidebar-navigation"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
@Entry
@Component
struct Index {
  build() {
    Tabs() {
      TabContent() {
      }.tabBar("tab1")

      TabContent() {
      }.tabBar("tab2")
    }.vertical(true)
  }
}
```
 
 

##### 反例

```text
@Entry
@Component
struct Index {
  build() {
    Tabs() {
      TabContent() {
      }.tabBar("tab1")

      TabContent() {
      }.tabBar("tab2")
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
