# AddrSanitizer（地址越界）检测

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-guidelines

## 简介

地址越界问题是指访问了不合法的地址，导致程序运行出现异常，通常表现为应用崩溃（Crash），其故障原因为释放后使用（use after free）、重复释放（double-free）、栈溢出（stack-overflow）、堆溢出（heap-overflow）等。由于应用崩溃日志信息有限且非崩溃第一现场，地址越界问题定位较为困难，一般依赖ASan、HWASan、GWP-ASan等检测工具以获取更多内存操作信息。从API13开始推荐[使用HWASan检测工具](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-hwasan-detection)进行地址越界问题的分析。

## 常见越界类型与影响

常见地址越界类型和影响可参看[地址越界经典问题类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-catagory)。

## 地址越界检测原理

检测原理和使用方法可参看[地址越界类问题检测](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ram-detection)。

## 日志获取方式

地址越界日志和进程崩溃日志一致，都是由Faultlogger模块进行管理，可通过以下方式获取： **方式一：通过DevEco Studio获取日志** DevEco Studio会收集设备/data/log/faultlog/faultlogger/路径下的进程崩溃故障日志到FaultLog下，根据进程名和故障和时间分类显示。获取日志的方法参见：[DevEco Studio使用指南-FaultLog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log)。 **方式二：通过HiAppEvent接口订阅** HiAppEvent给开发者提供了故障订阅接口，详见[HiAppEvent介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-intro)。参考[订阅地址越界事件（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-arkts)或[订阅地址越界事件（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-ndk)完成地址越界事件订阅，并通过事件的[external_log](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events#params字段说明)字段读取故障日志文件内容。 **方式三：通过hdc获取日志，需打开开发者选项** 在运行态，日志默认都落盘至 /data/log/faultlog/faultlogger 下。在开发者选项打开的情况下，开发者可以通过hdc file recv /data/log/faultlog/faultlogger D:\命令导出故障日志到本地，故障日志文件名格式为[检测器类型]-[bundleName]-[uid]-[happenedTime].log。

## 日志规格


## ASan日志规格

ASan日志规格如下，标题头会展示设备信息，故障发生时间，故障进程和故障原因等。日志详细描述了越界访问的地址（0x007fffd59768）、访问大小（WRITE of size 4）、发生的线程和进程信息。通过调用栈，展现了导致此次越界的函数调用路径，列出各个调用层的地址及对应的模块和偏移，帮助开发者快速定位代码位置。日志还提供影子内存（Shadow bytes）跟踪内存状态，帮助确认访问是否合法。同时，日志列出了进程的内存空间映射，帮助分析越界地址所处的具体内存区域。 以下为具体示例：
```text
Device info:XXX 0x001ffffab2e0: 00 00 00 00 f1 f1 f1 f1 00 00 00 00 00[f3]f3 f3
  0x001ffffab2f0: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x001ffffab300: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x001ffffab310: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x001ffffab320: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x001ffffab330: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==appspawn==11766==ABORTING

==appspawn==11766==Process memory map follows:

## HWASan日志规格

HWASan日志在格式上与ASan相近，也会在标题中展示设备信息、故障发生时间、故障进程及触发原因等关键信息。日志会详细记录越界访问的地址（如0x0002013c0100）和访问大小（如WRITE of size 4）。同时会记录发生时的线程和进程信息。完整的调用栈会展示触发越界的函数执行路径，列出各层地址、所属模块及偏移，便于开发者快速定位代码位置。不同于ASan的是，HWASan还会输出指针与内存块的标签（tags），并通过对比标签来辅助判断是否存在非法访问。
```text
Device info:XXX 0x005c2013c010:[11] 11  08  00  a5  a5  08  00  13  13  08  00  2e  2e  08  00
0x005c2013c020: 09  09  08  00  68  68  08  00  df  df  08  00  17  17  08  00
0x005c2013c030: 24  24  08  00  5f  5f  08  00  f9  f9  08  00  05  05  08  00
0x005c2013c040: 02  02  08  00  78  78  08  00  50  50  08  00  33  33  08  00
0x005c2013c050: 57  57  08  63  4a  4a  08  4b  a8  a8  08  00  cd  cd  08  00
0x005c2013c060: e6  e6  08  00  0d  0d  08  00  3c  3c  3c  08  83  83  83  08
0x005c2013c070: 62  62  62  08  08  08  08  08  35  35  35  08  b5  b5  b5  08
0x005c2013c080: 87  87  87  08  4d  4d  4d  08  46  46  46  08  0e  0e  0e  08
0x005c2013c090: 6d  6d  6d  08  7a  7a  7a  08  11  11  11  08  af  af  af  08
Tags for short granules around the buggy address (one tag corresponds to 16 bytes):
0x005c2013c000: ..  ..  56  ..  ..  ..  ad  ..  97  00  02  ..  ..  ..  94  ..
=>0x005c2013c010:[..] ..  11  ..  ..  ..  a5  ..  ..  ..  13  ..  ..  ..  2e  ..
0x005c2013c020: 13  00  09  ..  ..  ..  68  ..  ..  ..  df  ..  ..  ..  17  ..
See https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html#short-granules for a description of short granule tags
Registers where the failure occurred (pc 0x00651a5c0fa0):
x0  ec00000201e4ee88  x1  3c000004004c6b38  x2  0000000000000000  x3  0000000000000000
x4  6e0000652737ff79  x5  e600000201f631b9  x6  3e000002016b0d10  x7  0000056d1a495b07
x8  0200005bffffffff  x9  0000006527380ff0  x10 0000006527380f18  x11 0000000000000000
x12 073e000002016b0d  x13 000000056d1a495b  x14 000000000000006e  x15 0000000000000000
x16 0000005a3f867ef0  x17 000000651a5c0f64  x18 0000000000000005  x19 d2000002013c0100
x20 0200005c00000000  x21 3c000004004c6b38  x22 ec00000201e4ee80  x23 0000000000000000
x24 b800000000000000  x25 c8000065273804b0  x26 3e000002016b0d08  x27 b8000065273803a0
x28 1700000400263f80  x29 000000652737ffa0  x30 000000651a5c0fa4   sp 000000652737ffa0

SUMMARY: HWAddressSanitizer: tag-mismatch (/data/storage/el1/bundle/libs/arm64/libijk.so+0x2c0fa0) (BuildId: 84383086df874d94fa191ddbbc25091cc14992c5)

Memory near registers:

## MemDebug日志规格

MemDebug采用隔离区加投毒填充的机制，并复用HWASan的Tag校验的检测工具，对于Double Free类问题，其日志规格和HWASan一致。
```text
Device info:XXX 0x005c100945e0: 96  08 [e9] e7  c9  c9  36  36  18  08  ef  d9  80  08  8e  08
  0x005c100945f0: ba  08  98  98  b6  1b  63  63  08  00  bb  52  74  08  84  08
  ...
Tags for short granules around the buggy address (one tag corresponds to 16 bytes):
  0x005c100945d0: ..  ea  ..  ..  ..  ..  ..  cb  ..  ..  ..  64  ..  ..  ..  ..
=>0x005c100945e0: ..  96 [..] ..  ..  ..  ..  ..  ..  18  ..  ..  ..  80  ..  8e
  0x005c100945f0: ..  ba  ..  ..  ..  ..  ..  ..  64  ..  ..  ..  ..  74  ..  84
See https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html#short-granules for a description of short granule tags
SUMMARY: HWAddressSanitizer: invalid-free (/system/lib64/xxxxxx.xxxxx.so+0xxxxxx) (BuildId: xxxxxxxxxxxxxxxxxxxxxxxxxxx)

进程maps信息
==appspawn==62642==Process memory map follows:
        0x000000010000-0x000100020000
        0x000100020000-0x000100030000   [anon:SizeClassAllocator: region data]
        0x000100030000-0x000100040000   [anon:SizeClassAllocator: region data]
        ...
```

 对于Use-After-Free（Write）类问题，日志在问题概述部分会有所不同。示例输出如下：
```text
ptrBeg was re-written after free 0x000100946540[1], 0x000100946548 5555555500000009:5555555555555555
```

 其中，0x000100946540问题内存块起始地址，[1]为检测出问题的内存基于起始地址的8字节偏移数，0x000100946548为实际被修改的地址，5555555500000009:5555555555555555表示内存中的内容被修改后的实际值和预期值的对比。在该信息之后，日志还会输出对应内存块的释放堆栈和分配堆栈，调用栈的格式与HWASan日志一致，此处不再赘述。

## GWP-ASan日志规格

GWP-ASan的日志格式较为简洁，以下示例为典型的Use-After-Free问题日志，包含内存块的分配、释放及违规访问的调用栈信息。
```text
Device info:XXX

## AddrSanitizer聚类


## 聚类简介

应用程序在不同版本或同一版本的不同时间，AddrSanitizer可能因同一原因产生故障，但AddrSanitizer故障日志中的大部分信息会随版本、时间等因素变化，导致难以快速判断是否为重复问题。此外，AddrSanitizer故障信息中包含系统侧和应用侧的调用栈，这不利于开发者快速定位和排查应用侧的问题。 因此，为避免重复分析多份故障信息，提高应用故障问题的分析效率，需要对AddrSanitizer故障信息进行聚类；同时，聚类也能帮助开发者对不同原因问题进行分类统计。 判断多份日志是否属于同一问题，主要基于以下两个维度： 地址越界的故障类型。业务相关调用栈，过滤基础库后的栈顶前两帧。 通过上述信息可对问题进行初步定界。

## 提取聚类信息

**提取故障类型**   不同类型日志的故障类型提取方式如下：  GWP-ASan  在[GWP-ASan日志](#gwp-asan日志规格)中，故障类型根据原始日志中包含"at"的行提取。可能的故障类型包括Use After Free、Double Free、Invalid (Wild) Free等，详细类型说明可参考[GWP-ASan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-gwpasan-detection#section73731529454)。  ASan/HWASan/MemDebug  在[ASan](#asan日志规格)、[HWASan](#hwasan日志规格)和[MemDebug](#memdebug日志规格)日志中，故障原因通过日志中的"Reason"字段提取，提取结果将作为后续聚类依据。详细字段说明可参考[AddrSanitizer日志type字段说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events)。    **标准化栈信息**   提取故障类型作为特征后，首先使用正则匹配筛选堆栈内容。然后，为了确保聚类准确性，需要对堆栈信息进行标准化和清洗。主要规则如下：  去除易变信息：行号、相同的BuildID和绝对地址。  过滤基础库栈帧：
```text
libc.so
libc++.so
libclang_rt.hwasan.so
libclang_rt.asan.so
ld-musl-aarch64-asan.so
ld-musl-aarch64.so
```

  保留业务相关栈帧：保留业务so路径作为关键特征。     对调用栈进行标准化后，最后得到的特征栈如下：
| 原始栈帧内容 | 标准化后栈帧内容 |
| --- | --- |
| #0 0x5b6d263a58 (/system/lib64/libclang_rt.hwasan.so+0x23a58) (BuildId: a1396c21a0290124b0e0ebd03a4cced52b1addcc) | 忽略（基础库） |
| #1 0x661be0e870 (/data/storage/el1/bundle/libs/arm64/libentry.so+0x4e870) (BuildId: 5bc0684c2c3fc90841c2498efe1af4fd4792e5a8) | /data/storage/el1/bundle/libs/arm64/libentry.so+0x4e870 |


## 提取聚类特征

在完成标准化后，根据不同故障类型提取关键栈作为特征： Use After Free
| 故障特征 | 来源 | 提取规则 |
| --- | --- | --- |
| 故障特征1 | 使用栈 | 过滤基础库后，取栈顶的前两帧（so名+相对偏移） |
| 故障特征2 | 释放栈 | 过滤基础库后，取栈顶的前两帧（so名+相对偏移） |

   Double Free
| 故障特征 | 来源 | 提取规则 |
| --- | --- | --- |
| 故障特征1 | 第一次释放栈 | 过滤基础库后，取栈顶的前两帧（so名+相对偏移） |
| 故障特征2 | 第二次释放栈 | 过滤基础库后，取栈顶的前两帧（so名+相对偏移） |

   其他故障类型
| 故障特征 | 来源 | 提取规则 |
| --- | --- | --- |
| 故障特征 | 使用栈 | 过滤基础库后，取栈顶的前两帧（so名+相对偏移） |


## 生成聚类特征

最终聚类特征为：故障类型+若干条标准化业务栈帧，以GWP-ASan日志为例：
```text
*** GWP-ASan detected a memory error ***
Use After Free at 0x5bab376000 (0 bytes into a 64-byte allocation at 0x5bab376000) by thread 52616 here:
 #0 0x5cad4c7ba4  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x7ba4) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
 #1 0x5cad4c849c  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x849c) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
 #2 0x5aef3bc03c  (/lib/ld-musl-aarch64.so.1+0x1dd03c) (BuildId: c89ea5bf4368de59af764818c03eb41b)
0x5bab376000 was deallocated by thread 52616 here:
 #0 0x5aef331010  (/lib/ld-musl-aarch64.so.1+0x152010) (BuildId: c89ea5bf4368de59af764818c03eb41b)
 #1 0x5aef329614  (/lib/ld-musl-aarch64.so.1+0x14a614) (BuildId: c89ea5bf4368de59af764818c03eb41b)
 #2 0x5cad4c7b9c  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x7b9c) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
 #3 0x5cad4c849c  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x849c) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
 #4 0x5cad4c8434  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x8434) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
0x5bab376000 was allocated by thread 52616 here:
 #0 0x5aef331010  (/lib/ld-musl-aarch64.so.1+0x152010) (BuildId: c89ea5bf4368de59af764818c03eb41b)
 #1 0x5aef3292e4  (/lib/ld-musl-aarch64.so.1+0x14a2e4) (BuildId: c89ea5bf4368de59af764818c03eb41b)
 #2 0x5aef34b5e0  (/lib/ld-musl-aarch64.so.1+0x16c5e0) (BuildId: c89ea5bf4368de59af764818c03eb41b)
 #3 0x5cad4c7b84  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x7b84) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
 #4 0x5cad4c849c  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x849c) (BuildId: 2a3f1826c75a903f89c46b8ffcd1846295fdebcf)
*** End GWP-ASan report ***
```

 根据聚类规则： 从“at”处提取故障类型：Use After Free。分别对使用栈与释放栈进行标准化。过滤基础库栈帧后，取栈顶前两帧作为关键特征。 最终生成的聚类特征如下：
| 故障特征 | 聚类特征 |
| --- | --- |
| 故障特征1-使用栈 | /data/storage/el1/bundle/libs/arm64/libsample.so+0x7ba4 /data/storage/el1/bundle/libs/arm64/libsample.so+0x849c |
| 故障特征2-释放栈 | /data/storage/el1/bundle/libs/arm64/libsample.so+0x7b9c /data/storage/el1/bundle/libs/arm64/libsample.so+0x849c |

  开发者可通过比对多份日志的聚类特征来归并AddrSanitizer故障，也可以对故障类型和故障特征内容计算哈希值，用于问题分类统计与自动化分析。
