# @correctness/listen-default-network-change

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-default-network-change

建议应用监听默认网络的变化，关闭原有网络的数据传输，并使用新网络建立数据传输。
 
该规则仅在联网类应用检查整个工程时才生效。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@correctness/listen-default-network-change": "suggestion"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
// With the ohos.permission.GET_NETWORK_INFO permission configured
import connection from '@ohos.net.connection';
export function test() {
  const defaultNet = connection.getDefaultNetSync();
  const netCapabilities = connection.getNetCapabilitiesSync(defaultNet);
  let bearerTypes = netCapabilities.bearerTypes;
  const netConnection = connection.createNetConnection();
  netConnection.on('netCapabilitiesChange', (netCap: connection.NetCapabilityInfo) => {
    const newBearTypes = netCap.netCap.bearerTypes;
    if (newBearTypes !== bearerTypes) {
      bearerTypes = newBearTypes;
    }
  });
}
```
 
 

##### 反例

```text
// With the ohos.permission.GET_NETWORK_INFO permission configured
// import connection from '@ohos.net.connection';
// The `on(type: 'netCapabilitiesChange', callback: Callback<connection.NetCapabilityInfo>)`, `getDefaultNet`/`getDefaultNetSync` and `getNetCapabilities`/`getNetCapabilitiesSync` functions are not called.
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@correctness/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
