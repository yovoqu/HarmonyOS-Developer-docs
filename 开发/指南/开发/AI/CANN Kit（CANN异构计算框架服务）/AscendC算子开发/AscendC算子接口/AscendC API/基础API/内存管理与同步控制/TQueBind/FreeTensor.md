# FreeTensor

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-freetensor

## 功能说明

释放队列中的指定Tensor，供Que后续使用。

## 函数原型


```text
template
__aicore__ inline void FreeTensor(LocalTensor& tensor)
```


## 参数说明


| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 待释放的Tensor。 |


## 支持的型号

Kirin9020系列处理器 KirinX90系列处理器

## 注意事项

无

## 返回值

无

## 调用示例


```text
// 使用FreeTensor释放通过AllocTensor分配的Tensor，注意配对使用
AscendC::TPipe pipe;
AscendC::TQueBind que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor tensor1 = que.AllocTensor();
que.FreeTensor(tensor1);
```
