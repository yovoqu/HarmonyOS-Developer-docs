# 取消订阅公共事件（C/C++）

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription

## 场景介绍

订阅者在完成业务需求之后，需要取消订阅公共事件。

## 接口说明

详细的API说明请参考[oh_commonevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h)。
| 接口名 | 描述 |
| --- | --- |
| [CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_unsubscribe) | 取消订阅公共事件。 |


## 开发步骤

引用头文件。
```text
#include "hilog/log.h"
#include "BasicServicesKit/oh_commonevent.h"
```

在CMake脚本中添加动态链接库。
```text
target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libohcommonevent.so
)
```

取消订阅公共事件。 订阅者订阅公共事件并完成业务需求后，可以通过[OH_CommonEvent_UnSubscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_unsubscribe)主动取消订阅事件。
```text
void Unsubscribe(CommonEvent_Subscriber *subscriber)
{
    // 通过传入订阅者来退订事件
    int32_t ret = OH_CommonEvent_UnSubscribe(subscriber);
    OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_UnSubscribe ret .", ret);
}
```
