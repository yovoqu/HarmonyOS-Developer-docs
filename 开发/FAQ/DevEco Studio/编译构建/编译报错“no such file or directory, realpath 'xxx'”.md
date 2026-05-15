# 编译报错“no such file or directory, realpath 'xxx'”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-105

问题现象

DevEco Studio编译时出现错误，提示“no such file or directory, realpath 'xxx'”错误信息。
![](assets/编译报错“no%20such%20file%20or%20directory,%20realpath%20'xxx'”/file-20260515130134809-0.png)


解决措施

“no such file or directory”是一种常见的错误提示，表示当前工程无法找到指定文件或目录。该错误可能由以下原因引起：

1. 检查报错路径是否真实存在。
2. 检查文件或目录路径的正确性，包括文件名、目录名和字母大小写。
3. 检查权限：如果文件或目录存在，确保工程有足够权限访问。
