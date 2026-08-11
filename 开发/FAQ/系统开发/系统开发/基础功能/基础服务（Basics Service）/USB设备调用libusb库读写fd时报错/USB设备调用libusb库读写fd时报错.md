# USB设备调用libusb库读写fd时报错

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-48

#### 问题现象

USB设备调用libusb库的ioctl函数进行设备读写时失败，返回错误码16，提示“文件已存在”或“资源已被占用”。
 
```text
<span style="color: rgb(0,0,255);">ioctl</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hpriv </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">IOCTL_USBFS_SUBMITURB</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">urb</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">失败</span><span style="color: rgb(128,128,128);">，errno=16</span></em>
```
 
涉及到接口占用部分的问题代码示例参考如下：
 
- TS侧USB初始化。
```text
<span style="color: rgb(0,0,255);">initUUBar</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">USBDevice</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">{</span>
  if<span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">{</span>
    return
  <span style="color: rgb(181,106,1);">}</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">initEndpoints</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(255,0,170);">)</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">connectDevice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">claimInterface</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">configs</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">interfaces</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span>
  <span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setConfiguration</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">configs</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span>
  <span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setInterface</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">device</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">configs</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">interfaces</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipeFd </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">usbManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFileDescriptor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">usbPipe</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>
```

- C++侧调用libusb库的ioctl函数进行设备读写。
```text
<span style="color: rgb(255,255,255);">r </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ioctl</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hpriv</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">IOCTL_USBFS_SUBMITURB</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">urb</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">这里返回错误码</span><span style="color: rgb(128,128,128);">16</span></em>
if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">r </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">free</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">urb</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">tpriv</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,255,255);">urbs </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">NULL</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">errno </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,255,255);">ENODEV</span><span style="color: rgb(255,0,170);">)</span>
    return <span style="color: rgb(255,255,255);">LIBUSB_ERROR_NO_DEVICE</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">usbi_err</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">TRANSFER_CTX</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">transfer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">"submiturb failed, errno=%d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errno</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">这里返回错误码</span><span style="color: rgb(128,128,128);">16</span></em>
  return <span style="color: rgb(255,255,255);">LIBUSB_ERROR_IO</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 

#### 解决方案

使用usbManager的claimInterface方法时，系统会独占该接口。其他进程（包括使用libusb的进程）将无法再访问该接口。所以使用libusb场景，不要调用usbManager提供的claimInterface等接口，否则会造成USB服务进程占用接口，其他进程使用时会报错。
 
 

#### 总结

使用libusb场景，不要调用usbManager提供的claimInterface等接口，否则会造成USB服务进程占用接口，其他进程使用时会报错。
