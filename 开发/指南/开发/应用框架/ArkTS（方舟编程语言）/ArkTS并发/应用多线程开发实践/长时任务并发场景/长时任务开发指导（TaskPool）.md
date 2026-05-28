# 长时任务开发指导（TaskPool）

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-guide

此处提供使用TaskPool进行长时任务的开发指导，以定期采集传感器数据为例。
  

#### 使用TaskPool进行传感器数据监听
1. 导入所需的模块。

  
```ArkTS
import { sensor } from '@kit.SensorServiceKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError, emitter } from '@kit.BasicServicesKit';
```

2. 定义长时任务，内部监听sensor数据，并通过emitter注册销毁通知。

  
```ArkTS
@Concurrent
async function sensorListener(): Promise<void> {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
    emitter.emit({ eventId: 0 }, { data: data });
  }, { interval: 1000000000 });

  emitter.on({ eventId: 1 }, () => {
    sensor.off(sensor.SensorId.ACCELEROMETER)
    emitter.off(1)
  })
}
```

3. 给sensor添加ohos.permission.ACCELEROMETER权限。

  
```json
"requestPermissions": [
  {
    "name": "ohos.permission.ACCELEROMETER"
  }
]
```

4. 宿主线程定义注册及销毁的行为。

  
注册：发起长时任务，并通过emitter接收监听数据。
5. 销毁：发送取消传感器监听的事件，并结束长时任务。
