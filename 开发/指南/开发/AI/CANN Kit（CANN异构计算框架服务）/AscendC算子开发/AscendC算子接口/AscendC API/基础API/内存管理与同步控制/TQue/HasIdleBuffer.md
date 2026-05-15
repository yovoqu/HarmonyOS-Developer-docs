# HasIdleBuffer

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-hasidlebuffer

## 功能说明

查询队列中是否有空闲的内存块。

## 函数原型


```text
__aicore__ inline bool HasIdleBuffer()
```


## 参数说明

无

## 支持的型号

Kirin9020系列处理器 KirinX90系列处理器

## 注意事项

无

## 返回值

true：表示Queue中存在空闲内存。  false：表示Queue中不存在空闲内存。

## 调用示例


```text
// 当前Que中已经分配了4块内存
AscendC::TPipe pipe;
AscendC::TQue que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
bool ret = que.HasIdleBuffer(); // 没有AllocTensor的操作，返回值为true
AscendC::LocalTensor tensor1 = que.AllocTensor();
ret = que.HasIdleBuffer(); // AllocTensor了一块内存，返回值为true
AscendC::LocalTensor tensor2 = que.AllocTensor();
AscendC::LocalTensor tensor3 = que.AllocTensor();
AscendC::LocalTensor tensor4 = que.AllocTensor();
ret = que.HasIdleBuffer(); // AllocTensor了四块内存，当前无空闲内存，返回值为false，继续AllocTensor会报错
```
