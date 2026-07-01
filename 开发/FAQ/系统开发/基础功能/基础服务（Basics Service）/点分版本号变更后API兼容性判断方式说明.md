# 点分版本号变更后API兼容性判断方式说明

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-19

## 点分版本号变更后API兼容性判断方式说明
 

**问题描述**
 
7.0版本支持点分版本号，使用点分版本号时，API兼容性判断方式与之前有差异，如新增的API兼容性判断方式、@[Available](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-annotation#available)注解等差异。
 
**解决措施**
 
- 新增的API兼容性判断方式
ArkTS语言新增的API兼容性判断方式。
apiAvailable()接口使用方式。
```text
getTestData(): void {
  if (deviceInfo.sdkApiVersion >= 24 && deviceInfo.apiAvailable('26.0.0')) {
    // Calling APIs of 26.0.0
  } else {
    // Downgrade Scheme
  }
}
```

- C/C++语言新增的API兼容性判断方式。
APIAVAILABLE()接口使用方式。
```text
void testFunction(){
    if(APIAVAILABLE(24, 0, 0)){
        // method invocation
    }
}
```


 
 
- 通过@[Available](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-annotation#available)注解进行API兼容性判断的差异
在点分版本号变更后，可支持使用三位数字的版本号参数。（仅支持ArkTS，从API 22版本开始支持。）
```text
// HarmonyOS
@Available({ minApiVersion: 'HarmonyOS 7.0.0' })
function  func2(){}
```
 
 

```text
// OpenHarmony
@Available({ minApiVersion: '26' })
function  func1(){
  func2()
}
```
