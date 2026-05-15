# AllocTensor

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-alloctensor

## 功能说明

从队列中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。
> [!NOTE]
> 分配的Tensor内容并非全0，可能会是随机值。


## 函数原型


```text
template
__aicore__ inline LocalTensor AllocTensor()
```


## 参数说明

无

## 支持的型号

Kirin9020系列处理器 KirinX90系列处理器

## 注意事项

无

## 返回值

LocalTensor对象。

## 调用示例


```text
// 使用AllocTensor分配Tensor
AscendC::TPipe pipe;
AscendC::TQueBind que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len); // InitBuffer分配内存块数为4，每块大小为1024Bytes
AscendC::LocalTensor tensor1 = que.AllocTensor(); // AllocTensor分配Tensor长度为1024Bytes
```
