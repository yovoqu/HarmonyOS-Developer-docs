# 不同APPID的应用如何实现应用接续

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/free-flow-faqs-2

#### 问题现象

HarmonyOS虽然能通过一多适配将一个功能发布到不同类型的设备上，由于不同设备（如手机、PC）的发布节奏和开发节奏不同，若将手机、PC拆分为2个不同的APPID，这种情况下，如何实现不同APPID的应用间应用接续功能呢？
 
 

#### 背景知识

- [应用接续](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue-cast)：指当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。
- 应用接续[支持同应用不同BundleName的Ability跨端迁移](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue-cast#section1610864011610)。

 
 

#### 解决方案

参考[支持同应用不同BundleName的Ability跨端迁移](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue-cast#section1610864011610)，不同APPID的应用需在module.json5配置文件中的abilities标签增加配置continueBundleName字段，指定当前ability需要接续的对端BundleName。
 1. 应用A（BundleName：com.hw.mycontinuea），入口ability为EntryAbility：
在module.json5的abilities标签中增加如下配置：
```json
"continuable": true,
"continueBundleName": [
  "com.hw.mycontinueb"
],
"continueType": [
  "mainAbility"
],
```

2. 在EntryAbility中补充onContinue事件：
```json
onContinue(wantParam: Record<string, Object>) {
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
  const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
  // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
  const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
  // 兼容性校验
  if (targetVersion < versionThreshold) {
    // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
    promptAction.openToast({
      message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
      duration: 2000
    });
    // 在兼容性校验不通过时返回MISMATCH
    return AbilityConstant.OnContinueResult.MISMATCH;
  }
  console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
  // 迁移数据保存
  const continueInput = '迁移的数据';
  if (continueInput) {
    // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
    wantParam['data'] = continueInput;
  }
  // ...
  return AbilityConstant.OnContinueResult.AGREE;
}
```

3. 在EntryAbility中补充onCreate和onNewWant事件：
```json
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  try {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    // 设置是否开启应用接续，可在各页面动态设置
    this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
      hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
    });
    // 判断是否为应用接续场景
    if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
      // 将上述的保存的数据取出恢复
      if (want.parameters !== undefined) {
        let continueInput = want.parameters.data as string;
        AppStorage.setOrCreate<string>('message', continueInput);
        console.info(`continue input ${continueInput}`);
      }
      // ...
      // 触发页面恢复
      this.context.restoreWindowStage(this.storage);
    }
    // ...
  } catch (err) {
    hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
  }
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
}

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
  if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
    // 将上述的保存的数据取出恢复
    if (want.parameters !== undefined) {
      let continueInput = want.parameters.data as string;
      AppStorage.setOrCreate<string>('message', continueInput);
      console.info(`continue input ${continueInput}`);
    }
    // ...
    // 触发页面恢复
    this.context.restoreWindowStage(this.storage);
  }
  // ...
}
```

4. 应用B（BundleName：com.hw.mycontinueb），入口ability为ProductAbility：
在module.json5的abilities标签中增加如下配置：
```json
"continuable": true,
"continueBundleName": [
  "com.hw.mycontinuea"
],
"continueType": [
  "mainAbility"
],
```

5. 在EntryAbility中补充onContinue事件：
```json
onContinue(wantParam: Record<string, Object>) {
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
  const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
  // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
  const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
  // 兼容性校验
  if (targetVersion < versionThreshold) {
    // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
    promptAction.openToast({
      message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
      duration: 2000
    });
    // 在兼容性校验不通过时返回MISMATCH
    return AbilityConstant.OnContinueResult.MISMATCH;
  }
  console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
  // 迁移数据保存
  const continueInput = '迁移的数据';
  if (continueInput) {
    // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
    wantParam['data'] = continueInput;
  }
  // ...
  return AbilityConstant.OnContinueResult.AGREE;
}
```

6. 在EntryAbility中补充onCreate和onNewWant事件：
```json
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  try {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    // 设置是否开启应用接续，可在各页面动态设置
    this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
      hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
    });
    // 判断是否为应用接续场景
    if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
      // 将上述的保存的数据取出恢复
      if (want.parameters !== undefined) {
        let continueInput = want.parameters.data as string;
        AppStorage.setOrCreate<string>('message', continueInput);
        console.info(`continue input ${continueInput}`);
      }
      // ...
      // 触发页面恢复
      this.context.restoreWindowStage(this.storage);
    }
    // ...
  } catch (err) {
    hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
  }
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
}

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
  if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
    // 将上述的保存的数据取出恢复
    if (want.parameters !== undefined) {
      let continueInput = want.parameters.data as string;
      AppStorage.setOrCreate<string>('message', continueInput);
      console.info(`continue input ${continueInput}`);
    }
    // ...
    // 触发页面恢复
    this.context.restoreWindowStage(this.storage);
  }
  // ...
}
```
