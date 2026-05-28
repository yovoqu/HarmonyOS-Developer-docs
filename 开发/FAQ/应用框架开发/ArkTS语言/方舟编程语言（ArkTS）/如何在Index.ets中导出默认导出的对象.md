# 如何在Index.ets中导出默认导出的对象

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-145

**问题现象**
 
```ArkTS
// src/main/ets/api/AppInterfaces.ets
import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
export default new AppInterfaces() as AppInterfaces;
// Index.ets
export AppInterfaces from './src/main/ets/api/AppInterfaces';
```
 
报错提示：Cannot find name 'AppInterfaces'. &lt;ArkTSCheck&gt;
 
**解决措施**
 
```ArkTS
import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
let test = new AppInterfaces()
export default test;
```
