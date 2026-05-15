# 历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’/ 'C:xxx\yyy\zzz\C:at Object.mkdirSync (node:fs:1391:3)”

更新时间：2026-03-25 01:58:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-190

问题现象

构建报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’”


![](assets/历史问题报错：“hvigor%20ERROR／%20Error／%20EINVAL／%20invalid%20argument,%20mkdir%20‘D／xxx／yyy／zzz／D／’／%20'C／xxx／yyy／zzz／C／at%20Object.mkdirSync%20node／fs／1391／3”/file-20260515130224452-0.png)


常见错误场景

工程A通过引用外部模块的方式使用了工程B中的har模块，在工程B中执行ohpm后，在工程A中没有重新执行ohpm install直接编译（或者调试），导致编译报错。

问题原因

ohpm远程第三方包安装后，软连接指向的路径为非本工程路径（是由于被其他工程篡改），编译时会出现预期之外的错误。注：能以非本工程路径存在的依赖仅为本地模块，参考官网工程外模块的使用方式）

解决措施

1.在问题工程中重新执行ohpm install，或者sync。


![](assets/历史问题报错：“hvigor%20ERROR／%20Error／%20EINVAL／%20invalid%20argument,%20mkdir%20‘D／xxx／yyy／zzz／D／’／%20'C／xxx／yyy／zzz／C／at%20Object.mkdirSync%20node／fs／1391／3”/file-20260515130224452-1.png)


2.使用build菜单先进行构建，再调试运行。


![](assets/历史问题报错：“hvigor%20ERROR／%20Error／%20EINVAL／%20invalid%20argument,%20mkdir%20‘D／xxx／yyy／zzz／D／’／%20'C／xxx／yyy／zzz／C／at%20Object.mkdirSync%20node／fs／1391／3”/file-20260515130224452-2.png)
