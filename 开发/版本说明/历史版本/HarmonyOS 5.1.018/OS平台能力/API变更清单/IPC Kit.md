# IPC Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ipckit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MessageSequence； API声明：setSize(size: number): void; 差异内容：NA | 类名：MessageSequence； API声明：setSize(size: number): void; 差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence； API声明：setCapacity(size: number): void; 差异内容：NA | 类名：MessageSequence； API声明：setCapacity(size: number): void; 差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence； API声明：rewindRead(pos: number): void; 差异内容：NA | 类名：MessageSequence； API声明：rewindRead(pos: number): void; 差异内容：1900010 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence； API声明：rewindWrite(pos: number): void; 差异内容：NA | 类名：MessageSequence； API声明：rewindWrite(pos: number): void; 差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence； API声明：readAshmem(): Ashmem; 差异内容：NA | 类名：MessageSequence； API声明：readAshmem(): Ashmem; 差异内容：1900010 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：IRemoteObject； API声明：registerDeathRecipient(recipient: DeathRecipient, flags: number): void; 差异内容：NA | 类名：IRemoteObject； API声明：registerDeathRecipient(recipient: DeathRecipient, flags: number): void; 差异内容：1900005 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：IRemoteObject； API声明：unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void; 差异内容：NA | 类名：IRemoteObject； API声明：unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void; 差异内容：1900005 | api/@ohos.rpc.d.ts |
| 删除错误码 | 类名：MessageSequence； API声明：readByteArray(): number[]; 差异内容：401 | 类名：MessageSequence； API声明：readByteArray(): number[]; 差异内容：NA | api/@ohos.rpc.d.ts |
| 删除错误码 | 类名：MessageSequence； API声明：readAshmem(): Ashmem; 差异内容：1900004,401 | 类名：MessageSequence； API声明：readAshmem(): Ashmem; 差异内容：NA | api/@ohos.rpc.d.ts |
| 错误码变更 | 类名：MessageSequence； API声明：writeAshmem(ashmem: Ashmem): void; 差异内容：1900003,401 | 类名：MessageSequence； API声明：writeAshmem(ashmem: Ashmem): void; 差异内容：1900009,401 | api/@ohos.rpc.d.ts |
