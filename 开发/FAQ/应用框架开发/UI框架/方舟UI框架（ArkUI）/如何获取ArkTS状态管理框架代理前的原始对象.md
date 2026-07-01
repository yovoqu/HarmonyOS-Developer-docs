# 如何获取ArkTS状态管理框架代理前的原始对象

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-367

使用getTarget接口获取状态管理框架代理前的原始对象。
 
参考示例如下：
 
```text
import { UIUtils } from '@kit.ArkUI';

@Observed
class UserInfo {
  name: string = 'Tom';
}

@Entry
@Component
struct GetTargetDemo {
  @State info: UserInfo = new UserInfo();

  build() {
    Column() {
      Text(`info.name: ${this.info.name}`)
      Button('Change the properties of the proxy object')
        .onClick(() => {
          this.info.name = 'Alice';<em> // The Text component can refresh</em>
        })
      Button('更改原始对象的属性')
        .onClick(() => {
          let rawInfo: UserInfo = UIUtils.getTarget(this.info);
          if (rawInfo) {
            rawInfo.name = 'Bob';<em> // The Text component cannot be refreshed</em>
          }
        })
    }
  }
}
```
 
参考链接
 
[getTarget接口：获取状态管理框架代理前的原始对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-gettarget)
