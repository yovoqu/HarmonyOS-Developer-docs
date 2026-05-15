# 如何在App启动时让各种权限弹窗的申请自动弹出

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-92

将requestPermissionsFromUser接口放到EntryAbility.ets文件的loadContent回调中，参考代码如下：

```ts
windowStage.loadContent('pages/Index', (err) => {
  let atManager: abilityAccessCtrl.AtManager =
    abilityAccessCtrl.createAtManager();
  atManager
    .requestPermissionsFromUser(this.context, [
      'ohos.permission.ACCESS_BLUETOOTH',
    ])
    .then((data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
    .catch((err: BusinessError) => {
      console.error('data:' + JSON.stringify(err));
    });
});
```

在设置文件中声明目标权限：

```json
"requestPermissions": [
{
"name": "ohos.permission.ACCESS_BLUETOOTH",
"usedScene": {
"abilities": [
"EntryAbility"
],
"when": "inuse"
},
"reason": "$string:app_name"
}
],
```

参考链接

abilityAccessCtrl.createAtManager
