# @ohos.net.sharing (网络共享管理)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

网络共享管理模块用于将设备网络连接共享给其他连接设备。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { sharing } from '@kit.NetworkKit';
```
 
  

#### NetHandle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type NetHandle = connection.NetHandle
 
数据网络的句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。
 
**系统能力**：SystemCapability.Communication.NetManager.Core
  
| 类型 | 说明 |
| --- | --- |
| connection.NetHandle | 网络链路信息。 |
