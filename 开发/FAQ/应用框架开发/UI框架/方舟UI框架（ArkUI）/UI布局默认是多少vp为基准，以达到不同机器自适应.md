# UI布局默认是多少vp为基准，以达到不同机器自适应

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-129

无论屏幕分辨率或密度如何，组件的视觉效果保持一致。

vp具体计算公式为：vp= px/(DPI/160)

px 是屏幕的真实物理像素值，densityDPI 通常指系统屏幕密度，densityPixels是屏幕密度与标准DPI的比率，常见取值有 0.75、1.0、1.5、2.0、3.0 等。在HarmonyOS中，标准DPI为160。以华为Mate 40 Pro为例，densityDPI为 560，densityPixels为3.5。要查看真机的DPI，可以调用屏幕属性中的display接口查询。

```ts
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
} catch (exception) {
  console.error(
    'Failed to obtain the default display object. Code: ' +
      JSON.stringify(exception),
  );
}
```

如果原型图没有提供vp单位的布局，开发者可以根据densityPixels把px转为vp，HarmonyOS也封装了现成的接口px2vp()和vp2px()供开发者直接调用。

参考链接

像素单位，@ohos.display (屏幕属性)
