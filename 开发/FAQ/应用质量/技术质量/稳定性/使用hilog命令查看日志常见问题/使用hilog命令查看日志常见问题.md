# 使用hilog命令查看日志常见问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-80

#### 问题现象

场景一：使用hilog命令查看日志时，发现某些日志没有输出，或者日志时有时无。
 
场景二：在代码中使用了hilog.debug()但控制台看不到DEBUG日志。
 
场景三：命令行中显示的中文日志出现乱码。
 
场景四：只想查看某个应用的日志，但日志中混杂了其他应用的信息。
 
 

#### 解决方案

 

#### 场景一
1. 当前全局日志级别设置过高，低于该级别的日志不会被打印。

  使用hilog -b D命令开启DEBUG级别日志显示。
```bash
hdc shell hilog -b D
```


  或者按需设置其他级别。
```bash
hdc shell hilog -b I   <em># 只显示INFO及以上级别</em>
hdc shell hilog -b W   <em># 只显示WARN及以上级别</em>
```

2. 日志打印量过大，触发了系统的流控机制。查看流控警告：在日志中搜索关键字LOGLIMIT、Slow reader missed、write socket failed。

  临时关闭流控（重启后失效）。

  
```bash
<em># 关闭进程级流控</em>
hdc shell hilog -Q pidoff

<em># 关闭domain级流控</em>
hdc shell hilog -Q domainoff
```


  增大缓冲区：默认hilog buffer大小为256K，可增大到最大16M。
```bash
hdc shell hilog -G 16M
```


  减少日志量：关闭不必要的DEBUG日志，或只开启特定domain的日志。
```bash
<em># 只显示指定domain的INFO级别日志</em>
hdc shell hilog -b I -D d003200
```

 
 

#### 场景二
1. 开启DEBUG开关。
```bash
hdc shell hilog -b D
```

2. 检查代码中的日志级别：确保调用hilog.isLoggable()检查日志是否可打印。
3. 确认应用版本：DEBUG级别日志在release版本中默认不打印，需要在调试版本或开启调试开关。
 
 

#### 场景三

- 临时解决（当前窗口生效）。
```bash
chcp 65001
hdc shell hilog
```

- 永久解决：创建批处理脚本，设置UTF-8编码。
```bash
@echo off
cmd /k chcp 65001
```


 
保存为.bat文件，每次通过该脚本启动命令行。
 
 

#### 场景四

- 按进程名过滤。
```bash
<em># 查看指定进程名的日志</em>
hdc shell hilog | grep "com.example.myapp"
```

- 按domain过滤：如果知道应用的domain ID。
```bash
hdc shell hilog -D 03200
```

- 按tag过滤。
```bash
hdc shell hilog -T "MyTag"
```

- 组合过滤。
```bash
<em># 查看指定domain的ERROR级别日志</em>
hdc shell hilog -L E -D 03200
```
