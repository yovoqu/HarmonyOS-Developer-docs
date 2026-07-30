# 如何获取HarmonyOS手机系统版本信息

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-62

#### 问题现象

目前通过deviceInfo.displayVersion获取的手机系统版本是：ALN-AL00 6.0.0.110(SP97C00E110R4P8log)，如何获取软件版本号6.0.0.110，如何获取软件版本号中的"110"。
 
 

#### 解决方案

- **方案一**：直接通过正则表达式直接匹配点分十进制格式的版本号（如6.0.0.110），并捕获第四位数值"110"。
- **方案二**：先通过正则表达式直接匹配点分十进制格式的版本号（如6.0.0.110），再通过字符串分割取其中第四位数值"110"。

 
```text
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    this.getSysVersion();
  }

  getSysVersion() {
    let displayVersionStr: string = deviceInfo.displayVersion;
    console.info(`displayVersionStr :${displayVersionStr}`);
    <em>// </em><em>方案一：</em>
<em>    // 核心正则表达式为(\d+\.){3}(\d+)，其中(\d+)用于捕获第四位数值。</em>
<em>    // 匹配返回包含搜索结果的数组，其中索引为2的元素为您需要的字符串值。</em>
    const versionMatch = displayVersionStr.match(/(\d+\.){3}(\d+)/);
    console.info(`versionMatch :${versionMatch?.toString()}`);
    if (versionMatch != null) {
      console.info(`extractFourthValue1 is :${versionMatch[0]}`);
    <em>  // 输出结果：extractFourthValue1 is:6.0.0.110</em>
      console.info(`extractFourthValue2 is :${versionMatch[2]}`);
   <em>   // 输出结果：extractFourthValue2 is:110</em>
    }

   <em> // 方案二：</em>
<em>    // 先通过正则表达式直接匹配点分十进制格式的版本号（如 6.0.0.110），再通过字符串分割取其中第四位数值"110"。</em>
    const version = displayVersionStr.match(/\b\d+\.\d+\.\d+\.\d+\b/);
    console.info(`versionMatch :${version?.toString()}`);
    if (version != null) {
      let result: Array<string> = version[0].split('.');
      console.info(`extractFourthValue1 is :${version}`);
     <em> // 输出结果：extractFourthValue1 is:6.0.0.110</em>
      console.info(`extractFourthValue2 is :${result[3]}`);
    <em>  // 输出结果：extractFourthValue2 is:110</em>
    }
  }

  build() {
  }
}
```
 
可从日志中获取系统版本号信息：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/GJNNT1W4TTimWewtlFYnsQ/zh-cn_image_0000002628773844.png?HW-CC-KV=V1&HW-CC-Date=20260701T041419Z&HW-CC-Expire=86400&HW-CC-Sign=9D7BE4EDF8DA1AECA35744D2C5EA1992B8605ECBAC7BFF8FDD5481608E617B27)
