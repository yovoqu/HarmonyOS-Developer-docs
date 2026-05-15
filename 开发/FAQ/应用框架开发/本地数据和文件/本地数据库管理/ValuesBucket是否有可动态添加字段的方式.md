# ValuesBucket是否有可动态添加字段的方式

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-48

解决措施

ValuesBucket的实现如下：

```ts
export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;
```

若要动态添加字段，可以参考以下方法。

```ts
function set(): void {
  let value: ValuesBucket = {};
  let name: string = 'NAME';
  value[name] = 'cxx';
  value['AGE'] = 18;
  value['SALARY'] = 20000;
}
```
