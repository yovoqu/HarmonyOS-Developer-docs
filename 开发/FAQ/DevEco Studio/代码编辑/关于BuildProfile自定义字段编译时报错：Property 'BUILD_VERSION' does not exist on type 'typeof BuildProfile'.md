# 关于BuildProfile自定义字段编译时报错：Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-10

问题描述

项目编译时，关于 BuildProfile 的自定义字段报错如下：

```text
Property 'BUILD_VERSION' does not exist on type 'typeof BuildProfile'
```

解决措施

获取构建参数并生成BuildProfile类文件后，在HSP中可以通过以下方式引入该文件：

```text
import BuildProfile from '${packageName}/BuildProfile';
```

可参考在代码中获取构建参数。
