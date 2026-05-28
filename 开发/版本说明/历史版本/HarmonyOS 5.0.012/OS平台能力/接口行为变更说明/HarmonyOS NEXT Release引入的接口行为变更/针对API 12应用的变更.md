# 针对API 12应用的变更

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b071

##### ArkUI

 

##### Navigation嵌套使用时的生命周期行为优化

**变更原因**
 
在嵌套使用Navigation的场景下,如果内层Navigation处于不可见的状态，不应该触发对应的onShown生命周期。
 
**变更影响**
 
此变更涉及应用适配。
 
变更前：在嵌套Navigation的场景下如果内层的Navigation不可见，此时如果应用对不可见的Navigation进行栈操作，会触发对应的onShown生命周期。
 
变更后：在嵌套Navigation的场景下如果内层的Navigation不可见，此时如果应用对不可见的Navigation进行栈操作，不会触发对应的onShown生命周期。
 
**起始API Level**
 
12
 
**变更的接口/组件**
 
onShown生命周期。
 
**适配指导**
 
默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。
