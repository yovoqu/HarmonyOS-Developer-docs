# UI测试中如何在feature模块启动当前模块的ability

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-32

## UI测试中如何在feature模块启动当前模块的ability
 


##### 问题现象

使用DevEco Studio进行UI测试，在feature模块下启动ability如何实现？
 
 

##### 背景知识

UI测试框架（UITest）为开发者提供UI界面查找和模拟操作能力，可覆盖UI自动化测试的关键场景，包括界面控件精准查找、UI交互操作（如点击、滑动、文本输入等），参考：[UI测试框架使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uitest-guidelines)。
 
 

##### 解决方案

- 在项目工程中新建feature模块：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/BZrTzMaOTXyFMhaDRays0A/zh-cn_image_0000002658808887.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=19CB563D11C059AC1AA2988164DE915F36C8C53FBF6CF3E78137369AC563BECA)

- 打开feature\src\main\module.json5，查看abilities标签的name属性值，确认需要启动的abilityName：
```ArkTS
"abilities": [
  {
  "name": "FeatureAbility",
  "srcEntry": "./ets/featureability/FeatureAbility.ets",
  "description": "$string:FeatureAbility_desc",
  "icon": "$media:layered_image",
  "label": "$string:FeatureAbility_label",
  "startWindowIcon": "$media:startIcon",
  "startWindowBackground": "$color:start_window_background",
  "exported": true
  }
],
```

- 在feature\src\ohosTest\ets\test\Ability.test.ets编写测试用例启动测试页面，代码示例如下：
```text
import { describe, it, expect } from '@ohos/hypium';
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
const bundleName = abilityDelegatorRegistry.getArguments().bundleName;

function sleep(time: number) {
  return new Promisevoid>((resolve: Function) => setTimeout(resolve, time));
}

export default function abilityTest() {
  describe('AbilityTest', () => {

    it('testStartFeatureTest', 0, async (done: Function) => {
      const want: Want = {
        bundleName: bundleName,
        abilityName: 'FeatureAbility'
      };
      try {
        await delegator.startAbility(want);
        await sleep(1000);

        const ability = await delegator.getCurrentTopAbility();
        expect(ability.context.abilityInfo.name).assertEqual('FeatureAbility');

        done();
      } catch (error) {
        console.error(`startAbility error. Code is ${error.code}, message is ${error.message}.`);
      }
    });
  });
}
```
