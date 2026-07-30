# AI字幕控件和AI识图的多语言配置以及依赖问题

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-9

#### 问题现象

若需在同一个应用中同时使用AI字幕控件（中英文）和AI识图（含其他语种），如何协调多语言配置？是否存在冲突或依赖问题？
 
 

#### 解决方案

[AI字幕控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speech-aicaption-guide)提供对应音频语种的字幕不涉及多语言配置。[AI识图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-imageanalyzer)支持划词手动选择语种翻译，仅[自定义的文字分析菜单项](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-image-analyzer#setcustomtextmenuitems)名称涉及多语言配置。因此无协调问题，且无冲突或依赖问题。
