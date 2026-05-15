# Init

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-init

## 功能说明

初始化内存和用于同步流水事件的EventID的初始化。

## 函数原型


```text
__aicore__ inline void TPipe::Init()
```


## 支持的型号

Kirin9020系列处理器 KirinX90系列处理器

## 注意事项

重复申请释放TPipe，要与[Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-destroy)接口成对使用，TPipe如果要重复申请需要先Destroy释放后再Init。

## 返回值

无

## 调用示例


```text
template
class KernelAsin {
public:
    __aicore__ inline KernelAsin()
    {}
    __aicore__ inline void Init(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize, TPipe *pipe)
    {
        src_global.SetGlobalBuffer(reinterpret_cast(src_gm), srcSize);
        dst_global.SetGlobalBuffer(reinterpret_cast(dst_gm), srcSize);
        pipe->InitBuffer(inQueueX, 1, srcSize * sizeof(srcType));
        pipe->InitBuffer(outQueue, 1, srcSize * sizeof(srcType));
        bufferSize = srcSize;
    }
    __aicore__ inline void Process()
    {
        CopyIn();
        Compute();
        CopyOut();
    }
private:
    __aicore__ inline void CopyIn()
    {
        AscendC::LocalTensor srcLocal = inQueueX.AllocTensor();
        AscendC::DataCopy(srcLocal, src_global, bufferSize);
        inQueueX.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor dstLocal = outQueue.AllocTensor();
        AscendC::LocalTensor srcLocal = inQueueX.DeQue();
        int16_t scalar_value = 3;
        AscendC::Muls(dstLocal, srcLocal, (srcType)scalar_value, bufferSize);
        outQueue.EnQue(dstLocal);
        inQueueX.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut(uint32_t offset)
    {
        AscendC::LocalTensor dstLocal = outQueue.DeQue();
        AscendC::DataCopy(dst_global, dstLocal, bufferSize);
        outQueue.FreeTensor(dstLocal);
    }
private:
    AscendC::GlobalTensor src_global;
    AscendC::GlobalTensor dst_global;
    AscendC::TQue inQueueX;
    AscendC::TQue outQueue;
    uint32_t bufferSize = 0;
};
template
__aicore__ void kernel_Test_operator(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize)
{
    KernelAsin op;
    AscendC::TPipe pipeIn;
    for (uint32_t index =0; index
