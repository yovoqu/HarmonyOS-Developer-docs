# 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8

**问题现象**
 
Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。
 

![](assets/编译报错“Could%20not%20load%20${file1}%20imported%20by%20${file2}／%20Maximum%20call%20stack%20size%20exceeded”/file-20260515130044629-0.png)

 
**解决措施**
 
问题源于file1位于当前工程外，步骤如下：
 1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。
 

![](assets/编译报错“Could%20not%20load%20${file1}%20imported%20by%20${file2}／%20Maximum%20call%20stack%20size%20exceeded”/file-20260515130044629-1.png)
