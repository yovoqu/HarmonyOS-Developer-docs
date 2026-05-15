# 如何获取router.back传递的参数

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-164

在 onPageShow 回调方法中使用 Router模块的getParams方法来获取传递过来的参数。参考代码如下：

```text
class InfoTmp {
age: number = 0
}

class RouTmp {
id: object = () => {
}
info: InfoTmp = new InfoTmp()
}

const context = AppStorage.get("context") as UIContext;
const params: RouTmp = context.getRouter().getParams() as RouTmp; // Get the parameter object passed
const id: object = params.id // Get the value of the id property
const age: number = params.info.age // Get the value of the age property
```

参考链接

页面跳转
