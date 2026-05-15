# ArkTS编译工具链概述

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/compilation-tool-chain-overview

ArkTS SDK提供了一套完整的编译工具链，以支持ArkTS的应用编译，通过集成至[Hvigor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor)编译任务的编排工具上，实现将应用的ArkTS/TS/JS源码编译生成方舟字节码文件（*.abc）。

 编译工具链在编译过程中首先执行语法转换，包括语法检查和UI转换。为确保源码安全，编译工具链使用[ArkGuard源码混淆工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation)对源码进行混淆操作。在字节码落盘之前，编译工具链会判断是否需要进行[字节码自定义修改](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/customize-bytecode-during-compilation)，如果需要，则加载并执行自定义修改代码。在生成字节码文件后，开发者可以使用[Disassembler反汇编工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool-disassembler)查看字节码文件的内容。关于字节码的具体内容，可参考[方舟字节码文件格式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-file-format)章节。

 ArkTS编译工具链目前主要包含以下功能：


 ArkTS编译工具链在构建HAP流程如下图所示：

 ![](assets/ArkTS编译工具链概述/file-20260514130451294-0.png)
