# cd到SDK下toolchains目录，执行hdc list targets，错误提示command not found: hdc

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-71

**问题现象**
 
在Linux/MacOS平台安装DevEco Studio工具，在安装目录下的toolchains子目录执行hdc命令提示command not found:hdc。
 
**可能原因**
 1. toolchains目录下hdc可执行文件被手动替换，替换后的文件缺少可执行权限。
2. 在执行shell（如bash、zsh）时默认不会在当前目录（./）中搜索可执行文件。
 
**解决措施**
 1. hdc文件必须拥有可执行权限才能被系统执行。
检查方法：使用ls -l命令查看文件详情。
2. 解决方法：使用chmod命令为hdc文件添加可执行权限。
3. PATH环境变量默认不会将当前目录（./）添加到列表中，需手动添加
显式指定当前目录，执行hdc命令前添加“./”。
4. 添加HDC文件所在目录的绝对路径到PATH环境变量，具体可参考hdc[环境准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#环境准备)章节操作。
