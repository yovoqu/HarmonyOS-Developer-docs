# Push Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：pushService； API声明：export function receiveMessage(pushType: 'IM' \| 'VoIP' \| 'BACKGROUND' \| 'EMERGENCY', ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void; 差异内容：pushType: 'IM' \| 'VoIP' \| 'BACKGROUND' \| 'EMERGENCY' | 类名：pushService； API声明：export function receiveMessage(pushType: PushType, ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void; 差异内容：pushType: PushType | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService； API声明：export type PushType = 'DEFAULT' \| 'IM' \| 'VoIP' \| 'BACKGROUND' \| 'EMERGENCY'; 差异内容：export type PushType = 'DEFAULT' \| 'IM' \| 'VoIP' \| 'BACKGROUND' \| 'EMERGENCY'; | api/@hms.core.push.pushService.d.ts |
