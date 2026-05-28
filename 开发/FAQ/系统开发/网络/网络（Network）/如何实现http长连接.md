# 如何实现http长连接

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-48

可使用定时HTTP请求模拟长连接。参考代码如下：
 
```ArkTS
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
// 设置5秒轮询一次
setTimeout(() => {
  httpRequest.request("EXAMPLE_URL", {
    method: http.RequestMethod.GET,
    connectTimeout: 60000,
    readTimeout: 60000
  }, (err, data) => {
    if (!err) {
      console.info('Received data:', JSON.stringify(data.result));
    } else {
      console.info('Polling error:', JSON.stringify(err));
    }
  })
}, 5000)
```
