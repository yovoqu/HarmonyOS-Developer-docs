# 编译报错“Invalid form name 'xxx'.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146

错误描述

卡片名称无效。

可能原因

在insight_intent.json中配置意图框架时，formName必须是form_config.json中已配置的forms之一。


![](assets/编译报错“Invalid%20form%20name%20'xxx'.”/file-20260515130159687-0.png)


解决措施

修改insight_intent.json中的 form 配置，确保formName已在form_config.json文件的 forms 中配置。
