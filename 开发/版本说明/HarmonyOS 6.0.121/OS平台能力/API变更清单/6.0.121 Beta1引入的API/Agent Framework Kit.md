# Agent Framework Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-agentframeworkkit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ButtonType； API声明：ICON_ABOVE_TITLE = 2 差异内容：ICON_ABOVE_TITLE = 2 | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export declare class AgentController 差异内容：NA | 类名：global； API声明：export declare class AgentController 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：AgentController； API声明：isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>; 差异内容：NA | 类名：AgentController； API声明：isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：AgentController； API声明：on(type: 'agentDialogOpened', callback: Callback<void>): void; 差异内容：NA | 类名：AgentController； API声明：on(type: 'agentDialogOpened', callback: Callback<void>): void; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：AgentController； API声明：off(type: 'agentDialogOpened', callback?: Callback<void>): void; 差异内容：NA | 类名：AgentController； API声明：off(type: 'agentDialogOpened', callback?: Callback<void>): void; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：AgentController； API声明：on(type: 'agentDialogClosed', callback: Callback<void>): void; 差异内容：NA | 类名：AgentController； API声明：on(type: 'agentDialogClosed', callback: Callback<void>): void; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：AgentController； API声明：off(type: 'agentDialogClosed', callback?: Callback<void>): void; 差异内容：NA | 类名：AgentController； API声明：off(type: 'agentDialogClosed', callback?: Callback<void>): void; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export declare class FunctionController 差异内容：NA | 类名：global； API声明：export declare class FunctionController 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export declare interface BaseOptions 差异内容：NA | 类名：global； API声明：export declare interface BaseOptions 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：BaseOptions； API声明：title?: string; 差异内容：NA | 类名：BaseOptions； API声明：title?: string; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：BaseOptions； API声明：titleFontSize?: number; 差异内容：NA | 类名：BaseOptions； API声明：titleFontSize?: number; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：BaseOptions； API声明：iconSize?: number; 差异内容：NA | 类名：BaseOptions； API声明：iconSize?: number; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：BaseOptions； API声明：iconColors?: ResourceColor[]; 差异内容：NA | 类名：BaseOptions； API声明：iconColors?: ResourceColor[]; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export declare interface FunctionOptions 差异内容：NA | 类名：global； API声明：export declare interface FunctionOptions 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：queryText?: string; 差异内容：NA | 类名：FunctionOptions； API声明：queryText?: string; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：controlSize?: ControlSize; 差异内容：NA | 类名：FunctionOptions； API声明：controlSize?: ControlSize; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：buttonType?: ButtonType; 差异内容：NA | 类名：FunctionOptions； API声明：buttonType?: ButtonType; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：isShowShadow?: boolean; 差异内容：NA | 类名：FunctionOptions； API声明：isShowShadow?: boolean; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：backgroundColor?: ResourceColor; 差异内容：NA | 类名：FunctionOptions； API声明：backgroundColor?: ResourceColor; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionOptions； API声明：titleColors?: ResourceColor[]; 差异内容：NA | 类名：FunctionOptions； API声明：titleColors?: ResourceColor[]; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export enum ButtonType 差异内容：NA | 类名：global； API声明：export enum ButtonType 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：ButtonType； API声明：CIRCLE = 0 差异内容：NA | 类名：ButtonType； API声明：CIRCLE = 0 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：ButtonType； API声明：CAPSULE = 1 差异内容：NA | 类名：ButtonType； API声明：CAPSULE = 1 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：global； API声明：export declare struct FunctionComponent 差异内容：NA | 类名：global； API声明：export declare struct FunctionComponent 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionComponent； API声明：agentId: string; 差异内容：NA | 类名：FunctionComponent； API声明：agentId: string; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionComponent； API声明：onError: ErrorCallback; 差异内容：NA | 类名：FunctionComponent； API声明：onError: ErrorCallback; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionComponent； API声明：options?: FunctionOptions; 差异内容：NA | 类名：FunctionComponent； API声明：options?: FunctionOptions; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionComponent； API声明：controller?: FunctionController; 差异内容：NA | 类名：FunctionComponent； API声明：controller?: FunctionController; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
| API从不支持元服务到支持元服务 | 类名：FunctionComponent； API声明：build(): void; 差异内容：NA | 类名：FunctionComponent； API声明：build(): void; 差异内容：atomicservice | api/@hms.ai.AgentFramework.d.ets |
