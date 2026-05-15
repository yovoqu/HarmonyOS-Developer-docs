# 编译命令行中如何传递参数并且在Hvigor编译阶段扩展插件中获取到

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-79

使用hvigor命令：

```bash
> hvigorw -s -p key1=value2222
```

获取自定义参数代码：

```ts
// hvigorfile.ts
import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

export default {
  system: harTasks /* Built-in plugin of Hvigor. It cannot be modified. */,
  plugins: [] /* Custom plugin to extend the functionality of Hvigor. */,
};
console.log('value===', hvigor.getParameter().getExtParam('key1'));
```
