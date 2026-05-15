# End

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-end

## 功能说明

单核内Matmul矩阵相乘计算结束后必须调用一次End函数。

## 函数原型


```text
__aicore__ inline void End()
```


## 参数说明

无

## 返回值

无

## 支持的型号

Kirin9020系列处理器

## 注意事项

无

## 调用示例


```text
mm.IterateAll(gm_c);
mm.End();
```
