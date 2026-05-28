# Destroy

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-destroy

#### 功能说明

释放资源。
 
  

#### 函数原型

```text
__aicore__ inline void Destroy()
```
 
  

#### 支持的型号

Kirin9020系列处理器
 
KirinX90系列处理器
 
  

#### 注意事项

用于重复申请释放TPipe，创建Tpipe对象后，可调用Destroy手动释放资源。
 
  

#### 返回值

无
 
  

#### 调用示例

```text
AscendC::TPipe pipe; // Pipe内存管理对象
// 输出数据Queue队列管理对象，QuePosition为VECOUT
AscendC::TQue<AscendC::TPosition::VECOUT, 2> que;
uint8_t num = 2;
uint32_t len = 128;
pipe.InitBuffer(que, num, len);
pipe.Destroy();
```
