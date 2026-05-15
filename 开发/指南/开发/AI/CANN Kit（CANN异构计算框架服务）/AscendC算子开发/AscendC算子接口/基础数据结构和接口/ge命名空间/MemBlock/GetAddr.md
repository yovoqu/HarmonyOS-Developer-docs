# GetAddr

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-memblock-getaddr

## 函数功能

获取只读的device内存地址。  获取可读写的device内存地址。

## 函数原型

获取只读的device内存地址场景：
```text
const void *GetAddr() const
```

获取可读写的device内存地址场景：
```text
void *GetAddr()
```


## 参数说明

无

## 返回值

获取只读的device内存地址场景：
| 类型 | 描述 |
| --- | --- |
| void* | 只读的device内存地址。 |

获取可读写的device内存地址场景：
| 类型 | 描述 |
| --- | --- |
| void* | 可读写的device内存地址。 |


## 异常处理

无

## 约束说明

无
