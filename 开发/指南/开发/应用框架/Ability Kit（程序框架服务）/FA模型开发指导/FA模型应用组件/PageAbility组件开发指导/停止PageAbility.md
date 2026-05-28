# 停止PageAbility

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stop-pageability

停止PageAbility通过featureAbility中的terminateSelf接口实现。
 
 **表1** featureAbility接口说明
  
| 接口名 | 接口描述 |
| --- | --- |
| terminateSelf() | 停止Ability。 |
| terminateSelfWithResult(parameter: AbilityResult) | 设置该PageAbility停止时返回给调用者的结果及数据并停止Ability。 |
 
 
如下示例展示了停止Ability的方法。
 
```text
import featureAbility from '@ohos.ability.featureAbility';
import hilog from '@ohos.hilog';

const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
```
 
```text
// ...
(async (): Promise<void> => {
  try {
    hilog.info(domain, TAG, 'Begin to terminateSelf');
    await featureAbility.terminateSelf();
    hilog.info(domain, TAG, 'terminateSelf succeed');
  } catch (error) {
    hilog.error(domain, TAG, 'terminateSelf failed with ' + error);
  }
})()
// ...
```
