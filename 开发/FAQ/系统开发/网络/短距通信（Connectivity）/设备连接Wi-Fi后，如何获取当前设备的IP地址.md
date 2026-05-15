# 设备连接Wi-Fi后，如何获取当前设备的IP地址

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4

使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET_WIFI_INFO。

参考代码如下：

```ts
import { wifiManager } from '@kit.ConnectivityKit';

let ipAddress = wifiManager.getIpInfo().ipAddress;
let ip =
  (ipAddress >>> 24) +
  '.' +
  ((ipAddress >> 16) & 0xff) +
  '.' +
  ((ipAddress >> 8) & 0xff) +
  '.' +
  (ipAddress & 0xff);
```
