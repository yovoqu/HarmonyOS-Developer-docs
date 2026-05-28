# 应用UI生成插件解压缩APK文件时，提示“tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-1

**问题现象**
 
在Windows环境下使用应用UI生成插件时，选择完配置项信息（Install Package Path、SDK Path、Git Bash Path），点击Next按钮后，在应用UI生成插件的执行终端中提示“tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes”。
 

![](assets/应用UI生成插件解压缩APK文件时，提示“tar.exe／%20Tool-small%20extra%20data／%20Need%20at%20least%204%20bytes,%20but%20only%20found%201%20bytes”/file-20260515130349294-0.png)

 
**可能原因**
 
Windows内置的C:/Windows/System32/tar.exe不支持解压apk文件。
 
**解决措施**
 
1. 确保系统中安装了支持解压APK文件的工具（APK文件默认压缩格式为ZIP格式，即系统中安装了支持解压ZIP格式的工具即可）。
 
2. 打开“C:/Users/&lt;用户名&gt;/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/sim-sdk”目录。将路径中的&lt;用户名&gt;替换为电脑使用的用户名，<DevEco Studio缓存目录>替换为正在使用的DevEco Studio版本下的缓存目录，例如如果当前DevEco Studio版本命名格式是以DevEco Studio6.1.xx开头，则将<DevEco Studio缓存目录>替换为DevEcoStudio6.1。
 
3. 修改“C:/Users/&lt;用户名&gt;/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/sim-sdk/apk_unzip_all.sh”文件，将解压工具 /c/Windows/System32/tar替换为我们安装的解压工具。替换内容如下：
```text
if [ "${uu_names: 0: 5}" == "MINGW" ] || [ "${uu_names: 0: 6}" == "CYGWIN" ];then
    mkdir -p $unzipfile
    #/c/Windows/System32/tar -xf $dir_or_file -C $unzipfile
    # 使用安装的解压工具代替原本使用的 tar 命令
    unzip -q $dir_or_file -d $unzipfile
else
    unzip -q $dir_or_file -d $unzipfile
fi
```
 
 
4. 替换完成后清理历史转换缓存“C:/Users/&lt;用户名&gt;/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/build”，重新执行转换逻辑验证是否能够成功执行。
