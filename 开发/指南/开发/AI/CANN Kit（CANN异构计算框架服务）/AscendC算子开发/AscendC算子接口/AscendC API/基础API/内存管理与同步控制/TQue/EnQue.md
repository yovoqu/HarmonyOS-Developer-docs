# EnQue

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-enque

## 功能说明

将Tensor push到队列。

## 函数原型

无需指定源和目的位置
```text
template
__aicore__ inline bool EnQue(const LocalTensor& tensor)
```

需要指定源和目的位置  通过[TQueBind](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview)绑定VECIN和VECOUT可实现VECIN和VECOUT内存复用，如下接口用于存在Vector计算的场景下实现复用，在入队时需要指定源和目的位置，不存在Vector计算的场景下可直接调用bool EnQue(LocalTensor& tensor)入队接口。
```text
template
__aicore__ inline bool EnQue(const LocalTensor& tensor)
```


## 参数说明

**表1** bool EnQue(LocalTensor& tensor)原型定义参数说明
| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 指定的Tensor。 |

**表2** template  bool EnQue(LocalTensor& tensor)原型定义参数说明
| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| srcUserPos | 输入 | 模板参数，开发者指定队列的src position，当前只支持如下通路：GM->VECIN/VECOUT->GM。 |
| dstUserPos | 输入 | 模板参数，开发者指定队列的dst position，当前只支持如下通路：GM->VECIN/VECOUT->GM。 |
| tensor | 输入 | 指定的Tensor。 |

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中
![](assets/EnQue/file-20260514132324884-0.png)

## 支持的型号

Kirin9020系列处理器 KirinX90系列处理器

## 注意事项

无

## 返回值

true：表示Tensor加入Queue成功。  false：表示Queue已满，入队失败。

## 调用示例


```text
// 接口: EnQue Tensor
AscendC::TPipe pipe;
AscendC::TQue que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor tensor1 = que.AllocTensor();
que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中
// 接口：EnQue指定特定的src/dst position，加入相应的队列
// template  bool EnQue(LocalTensor& tensor)
AscendC::TPipe pipe;
AscendC::TQueBind que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor tensor1 = que.AllocTensor();
que.EnQue(tensor1);// 将tensor加入VECIN的Queue中，实现内存复用
```
