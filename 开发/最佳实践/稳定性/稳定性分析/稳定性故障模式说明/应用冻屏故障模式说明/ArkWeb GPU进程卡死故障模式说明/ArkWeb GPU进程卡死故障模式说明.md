# ArkWeb GPU进程卡死故障模式说明

更新时间：2026-07-14 02:11:31

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-gpu-freeze

#### 概述

本文旨在指导HarmonyOS应用开发者如何定位主线程阻塞在ArkWeb堆栈类型的应用冻屏（AppFreeze）问题。在这类问题中，在GPU相关业务的堆栈较为普遍，造成这类问题的原因一般为I/O阻塞和等锁，本文将就这两个原因提供一些分析指导。
 
关于应用冻屏（AppFreeze）问题的检测原理和日志说明可先阅读[AppFreeze（应用冻屏）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)。
 
 

#### I/O阻塞

 

#### 根因描述

主线程ArkWeb内核因被耗时I/O操作阻塞，导致应用卡死，从而触发抓取AppFreeze日志操作。
 
 

#### 问题分析思路

UI进程阻塞在WaitforGetOffsetInrange函数，该函数用于从UI进程向GPU进程发送mojo通信，I/O阻塞或GPU任务执行过慢，响应不及时，导致系统卡死。此类问题发生时，说明mojo通信对端有异常，可能存在耗时操作，需要查看I/O线程等堆栈进一步确认问题根因。
 1. 参考[栈顶在方舟运行时的应用冻屏问题定位实践](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-freeze-ark-runtime)，分析AppFreeze日志，3S和6S的堆栈一致，且栈帧如下：
```text
Tid:xxx, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+xx)
<span style="color: rgb(0,0,255);">#01</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_cond_timedwait+xx)
...
<span style="color: rgb(0,0,255);">#xx</span> pc xxx /data/.../libarkweb_engine.so
gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(...)
```

2. 搜索线程名Chrome_IOThread，分析该线程对应的堆栈。
 
 

#### 关键字

3S和6S的堆栈一致，且其栈帧中包含关键字WaitForGetOffsetInRange；此外，Chrome_IOThread线程作为I/O线程，也需要关注。
 
 

#### 案例分析

 
**问题现象**
 
应用Web页面卡死，6秒后应用闪退。
 
**问题分析**
 
分析AppFreeze日志，3S和6S的堆栈一致，堆栈如下：
```text
Tid:<span style="color: rgb(80,160,79);">59546</span>, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b9438 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>bb58c /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">0000000004</span>f9b1cc /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::ConditionVariable::Wait() at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\condition_variable_posix.cc:<span style="color: rgb(80,160,79);">79</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">0000000004</span>fbed40 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::TimedWaitImpl(base::TimeDelta) at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\waitable_event_posix.cc:<span style="color: rgb(80,160,79);">193</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000004</span>f4f754 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::TimedWait(base::TimeDelta) at /devcloud/ws/suJWu/workspace/j_HLS1VBOR/src/out/musl_64\../../base/synchronization\waitable_event.cc:<span style="color: rgb(80,160,79);">39</span>
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000004</span>f4f6e4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::Wait() at /devcloud/ws/suJWu/workspace/j_HLS1VBOR/src/out/musl_64\../../base/synchronization\waitable_event.cc:<span style="color: rgb(80,160,79);">23</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">0000000005205390</span> /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::(anonymous <span style="color: rgb(0,0,255);">namespace</span>)::ThreadSafeInterfaceEndpointClientProxy::SendMessageWithResponder(mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) (<span style="color: rgb(80,160,79);">.64</span>c5c9a486ae75b6fffaf6ed09e7ff33) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../mojo/<span style="color: rgb(0,0,255);">public</span>/cpp/bindings/lib\interface_endpoint_client.cc:<span style="color: rgb(80,160,79);">431</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">000000000520</span>d680 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::<span style="color: rgb(0,0,255);">internal</span>::ThreadSafeForwarderBase::AcceptWithResponder(mojo::Message*, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) at /devcloud/ws/syGBE/workspace/j_PCKU3CLG/src/out/musl_64\../../mojo/<span style="color: rgb(0,0,255);">public</span>/cpp/bindings/lib\thread_safe_forwarder_base.cc:<span style="color: rgb(80,160,79);">32</span> (discriminator <span style="color: rgb(80,160,79);">4</span>)
<span style="color: rgb(0,0,255);">#08</span> pc <span style="color: rgb(80,160,79);">0000000005213040</span> /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::<span style="color: rgb(0,0,255);">internal</span>::SendMojoMessage(mojo::MessageReceiverWithResponder&, mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../mojo/<span style="color: rgb(0,0,255);">public</span>/cpp/bindings/lib\send_message_helper.cc:<span style="color: rgb(80,160,79);">42</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#09</span> pc <span style="color: rgb(80,160,79);">0000000002</span>f7ffe4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
gpu::mojom::GpuChannelProxy::WaitForGetOffsetInRange(<span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, gpu::CommandBuffer::State*) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\gen/gpu/ipc/common\gpu_channel.mojom.cc:<span style="color: rgb(80,160,79);">3251</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#10</span> pc <span style="color: rgb(80,160,79);">0000000003073</span>c10 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/ipc/client\command_buffer_proxy_impl.cc:<span style="color: rgb(80,160,79);">317</span> (discriminator <span style="color: rgb(80,160,79);">4</span>)
```
 
 
分析上述堆栈，发现卡在WaitForGetOffsetInRange函数，表明此时可能有I/O阻塞的情况，需要全局查找线程Chrome_IOThread。此时发现#19帧为Web提供的网络拦截接口，且最上层的#02栈是业务libxxx.so。分析可知，业务侧对Web进行网络拦截时，执行了超过6秒的逻辑，导致阻塞I/O线程超过6秒，此时UI线程转发mojo消息无法成功导致的卡死。
```text
Tid:<span style="color: rgb(80,160,79);">59729</span>, Name:Chrome_IOThread
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b9438 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>bf5b4 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">0000000000010</span>a58 /data/storage/el1/bundle/libs/arm64/libxxx.so
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">0000000000019848</span> /data/storage/el1/bundle/libs/arm64/libxxx.so
...
<span style="color: rgb(0,0,255);">#19</span> pc <span style="color: rgb(80,160,79);">0000000004e75</span>bd8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
OHOS::NWeb::NWebSchemeHandlerFactory::Create(scoped_refptr<CefBrowser>, scoped_refptr<CefFrame>, CefStringBase<CefStringTraitsUTF16> <span style="color: rgb(0,0,255);">const</span>&, scoped_refptr<CefRequest>) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../ohos_nweb/src/cef_delegate\nweb_scheme_handler_factory.cc:<span style="color: rgb(80,160,79);">150</span>
<span style="color: rgb(0,0,255);">#20</span> pc <span style="color: rgb(80,160,79);">00000000027</span>f8824 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
net_service::(anonymous <span style="color: rgb(0,0,255);">namespace</span>)::InterceptedRequestHandlerWrapper::GetOhosResourceHandlerResult(<span style="color: rgb(0,0,255);">int</span>, network::ResourceRequest*, scoped_refptr<CefResourceHandler>, base::OnceCallback<<span style="color: rgb(0,0,255);">void</span> (std::__h::unique_ptr<net_service::ResourceResponse, std::__h::default_delete<net_service::ResourceResponse> >)>) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../cef/libcef/browser/net_service\resource_request_handler_wrapper.cc:<span style="color: rgb(80,160,79);">974</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
 (inlined by) net_service::(anonymous <span style="color: rgb(0,0,255);">namespace</span>)::InterceptedRequestHandlerWrapper::GetOhosResourceHandlerResultInIO(<span style="color: rgb(0,0,255);">int</span>, network::ResourceRequest*, base::OnceCallback<<span style="color: rgb(0,0,255);">void</span> (std::__h::unique_ptr<net_service::ResourceResponse, std::__h::default_delete<net_service::ResourceResponse> >)>, scoped_refptr<CefResourceHandler>) (.df3920d6276824318412197eb3d7bb61) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../cef/libcef/browser/net_service\resource_request_handler_wrapper.cc:<span style="color: rgb(80,160,79);">1073</span> (discriminator <span style="color: rgb(80,160,79);">4</span>)
```
 
 
**问题总结**
 
遇到此类问题时，需要分析Chrome_IOThread线程，查看该线程的调用栈来进一步分析。
 
**修复建议**
 
针对网络拦截的接口实现，建议参考用法：start后直接返回，在异步线程完成操作后再调用DidReceiveResponse()/DidReceiveData()返回数据。接口使用参考[拦截Web组件发起的网络请求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-scheme-handler)。
 

#### 等锁

 

#### 根因描述

主线程ArkWeb内核由于受到其他业务持锁影响，mojo消息转发受阻塞，导致应用卡死，从而触发抓取AppFreeze日志操作。
 
 

#### 问题分析思路

这类问题的3S和6S栈都报在ArkWeb的栈中，但此时往往ArkWeb是受害者，需要找到对应的持锁等待的线程，堆栈一般如下：
 
```text
Tid:xxx, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+xx)
<span style="color: rgb(0,0,255);">#01</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(pthread_cond_timedwait+xx)
...
<span style="color: rgb(0,0,255);">#xx</span> pc xxx /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(viz::mojom::PAC_FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::PAC_FrameSinkId <span style="color: rgb(0,0,255);">const</span>&)+xx)
```
 
被阻塞线程堆栈一般如下：
 
```text
Tid:xxx, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+xx)
<span style="color: rgb(0,0,255);">#01</span> pc xxx /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(pthread_cond_timedwait+xx)
<span style="color: rgb(0,0,255);">#02</span> pc xxx /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::condition_variable::wait(std::__n1::unique_lock<std::__n1::mutex>&)+xx)
<span style="color: rgb(0,0,255);">#03</span> pc xxx /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::__shared_mutex_base::lock_shared()+xx)
...
```
 
需要找到Chrome_InProcGp、VizCompositorTh、CompositorGpuTh、Chrome_IOThread等线程分析持锁情况，查看系统或业务堆栈，分析持锁是否不当。
 
 

#### 关键字

被阻塞线程堆栈一般有mutex、lock等关键字；3S和6S的堆栈则无特殊关键字。
 
 

#### 案例分析

**案例一**
 
**问题现象**
 
应用Web页面卡死，6秒后闪退。
 
**问题分析**
 
3S和6S的堆栈一致，堆栈如下：
 
```text
Timestamp:<span style="color: rgb(80,160,79);">2025</span>-<span style="color: rgb(80,160,79);">06</span>-<span style="color: rgb(80,160,79);">24</span> <span style="color: rgb(80,160,79);">11</span>:<span style="color: rgb(80,160,79);">22</span>:<span style="color: rgb(80,160,79);">11</span>:<span style="color: rgb(80,160,79);">814</span>
Tid:<span style="color: rgb(80,160,79);">8360</span>, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b67f8 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">192</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b87fc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_cond_timedwait+<span style="color: rgb(80,160,79);">188</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">0000000004</span>f32180 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
base::ConditionVariable::Wait() at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\condition_variable_posix.cc:<span style="color: rgb(80,160,79);">79</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
...
<span style="color: rgb(0,0,255);">#13</span> pc <span style="color: rgb(80,160,79);">0000000003</span>bfed38 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
viz::mojom::FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::FrameSinkId <span style="color: rgb(0,0,255);">const</span>&) at /devcloud/ws/s1qK3/workspace/j_SNQMFI5M/HwHarmonyEngine/src/out/musl_64\gen/services/viz/privileged/mojom/compositing\frame_sink_manager.mojom.cc:<span style="color: rgb(80,160,79);">1387</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
```
 
根据栈顶分析，阻塞发生在mojo的接口中，分析调用栈发现是viz业务DestroyCompositorFrameSink触发的等待，因此优先检查Chrome_InProcGp线程堆栈是否存在阻塞。此时发现阻塞在EglWrapper调用中，#02帧显示正在等待recursive_mutex。
 
```text
Tid:<span style="color: rgb(80,160,79);">8599</span>, Name:Chrome_InProcGp
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b67f8 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">192</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>bc810 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_mutex_timedlock_inner+<span style="color: rgb(80,160,79);">592</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">00000000000</span>c4014 /system/lib64/libc++.so(std::__h::recursive_mutex::lock()+<span style="color: rgb(80,160,79);">8</span>)(a2d45389edece3475c17a1d7fc9a76ec2b697825)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">000000000003</span>a788 /system/lib64/libEGL.so(OHOS::EglWrapperDisplay::MakeCurrent(<span style="color: rgb(0,0,255);">void</span>*, <span style="color: rgb(0,0,255);">void</span>*, <span style="color: rgb(0,0,255);">void</span>*)+<span style="color: rgb(80,160,79);">44</span>)(<span style="color: rgb(80,160,79);">12088e3</span>ba5a7595b85687e148a8d8bd2)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">000000000002e</span>e60 /system/lib64/libEGL.so(eglMakeCurrent+<span style="color: rgb(80,160,79);">288</span>)(<span style="color: rgb(80,160,79);">12088e3</span>ba5a7595b85687e148a8d8bd2)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000005</span>c87530 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gl::GLContextEGL::MakeCurrentImpl(gl::GLSurface*) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../ui/gl\gl_context_egl.cc:<span style="color: rgb(80,160,79);">486</span> (discriminator <span style="color: rgb(80,160,79);">6</span>)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">00000000062500</span>dc /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gpu::SharedContextState::MakeCurrent(gl::GLSurface*, <span style="color: rgb(0,0,255);">bool</span>) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/command_buffer/service\shared_context_state.cc:<span style="color: rgb(80,160,79);">596</span> (discriminator <span style="color: rgb(80,160,79);">2</span>)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">000000000622</span>d278 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gpu::raster::GrCacheController::PurgeGrCache(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">long</span>) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/command_buffer/service\gr_cache_controller.cc:<span style="color: rgb(80,160,79);">62</span>
<span style="color: rgb(0,0,255);">#08</span> pc <span style="color: rgb(80,160,79);">00000000030</span>cd728 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
base::RepeatingCallback<<span style="color: rgb(0,0,255);">void</span> ()>::Run() && at /devcloud/ws/sP0jU/workspace/j_HLCVDUC4/HwHarmonyEngine/src/out/musl_64\../../base/functional\callback.h:<span style="color: rgb(80,160,79);">152</span> (discriminator <span style="color: rgb(80,160,79);">4</span>)
```
 
因单进程中仅允许一个线程持有EGL锁，故搜索EglWrapperDisplay，查看其他线程调用。
 
```text
Tid:<span style="color: rgb(80,160,79);">10052</span>, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b67f8 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">192</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b87fc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_cond_timedwait+<span style="color: rgb(80,160,79);">188</span>)(<span style="color: rgb(80,160,79);">35064</span>c759de623f1ea3ec0b012a28c3c)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">00000000000</span>c11c0 /system/lib64/libc++.so(std::__h::condition_variable::__do_timed_wait(std::__h::unique_lock<std::__h::mutex>&, std::__h::chrono::time_point<std::__h::chrono::system_clock, std::__h::chrono::duration<<span style="color: rgb(0,0,255);">long</span> <span style="color: rgb(0,0,255);">long</span>, std::__h::ratio<<span style="color: rgb(80,160,79);">1l</span>, <span style="color: rgb(80,160,79);">1000000000l</span>>>>)+<span style="color: rgb(80,160,79);">108</span>)(a2d45389edece3475c17a1d7fc9a76ec2b697825)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">0000000000056</span>d10 /system/lib64/chipset-pub-sdk/libsurface.z.so(<span style="color: rgb(80,160,79);">38e</span>cd06f7a8774e8edf4b5cc278015ea)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000000048</span>b98 /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::BufferQueue::RequestBufferLocked(OHOS::BufferRequestConfig <span style="color: rgb(0,0,255);">const</span>&, OHOS::sptr<OHOS::BufferExtraData>&, OHOS::IBufferProducer::RequestBufferReturnValue&, std::__h::unique_lock<std::__h::mutex>&)+<span style="color: rgb(80,160,79);">840</span>)(<span style="color: rgb(80,160,79);">38e</span>cd06f7a8774e8edf4b5cc278015ea)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000000049</span>b1c /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::BufferQueue::RequestBuffer(OHOS::BufferRequestConfig <span style="color: rgb(0,0,255);">const</span>&, OHOS::sptr<OHOS::BufferExtraData>&, OHOS::IBufferProducer::RequestBufferReturnValue&)+<span style="color: rgb(80,160,79);">272</span>)(<span style="color: rgb(80,160,79);">38e</span>cd06f7a8774e8edf4b5cc278015ea)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">0000000000073</span>a1c /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::ProducerSurface::RequestBuffer(OHOS::sptr<OHOS::SurfaceBuffer>&, OHOS::sptr<OHOS::SyncFence>&, OHOS::BufferRequestConfig&)+<span style="color: rgb(80,160,79);">204</span>)(<span style="color: rgb(80,160,79);">38e</span>cd06f7a8774e8edf4b5cc278015ea)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">000000000006</span>d170 /system/lib64/chipset-pub-sdk/libsurface.z.so(OH_NativeWindow_NativeWindowRequestBuffer+<span style="color: rgb(80,160,79);">404</span>)(<span style="color: rgb(80,160,79);">38e</span>cd06f7a8774e8edf4b5cc278015ea)
<span style="color: rgb(0,0,255);">#08</span> pc <span style="color: rgb(80,160,79);">0000000000416</span>cf8 /vendor/lib64/chipsetsdk/libhvgr_v200.so
<span style="color: rgb(0,0,255);">#09</span> pc <span style="color: rgb(80,160,79);">000000000037</span>c314 /vendor/lib64/chipsetsdk/libhvgr_v200.so
<span style="color: rgb(0,0,255);">#10</span> pc <span style="color: rgb(80,160,79);">000000000037</span>d138 /vendor/lib64/chipsetsdk/libhvgr_v200.so
<span style="color: rgb(0,0,255);">#11</span> pc <span style="color: rgb(80,160,79);">000000000037</span>ce80 /vendor/lib64/chipsetsdk/libhvgr_v200.so(eglSwapBuffers+<span style="color: rgb(80,160,79);">44</span>)
<span style="color: rgb(0,0,255);">#12</span> pc <span style="color: rgb(80,160,79);">000000000003</span>bcd8 /system/lib64/libEGL.so(OHOS::EglWrapperDisplay::SwapBuffers(<span style="color: rgb(0,0,255);">void</span>*)+<span style="color: rgb(80,160,79);">100</span>)(<span style="color: rgb(80,160,79);">12088e3</span>ba5a7595b85687e148a8d8bd2)
<span style="color: rgb(0,0,255);">#13</span> pc <span style="color: rgb(80,160,79);">000000000002</span>f2d0 /system/lib64/libEGL.so(eglSwapBuffers+<span style="color: rgb(80,160,79);">264</span>)(<span style="color: rgb(80,160,79);">12088e3</span>ba5a7595b85687e148a8d8bd2)
<span style="color: rgb(0,0,255);">#14</span> pc <span style="color: rgb(80,160,79);">00000000001</span>f6370 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#15</span> pc <span style="color: rgb(80,160,79);">00000000001</span>f50bc /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#16</span> pc <span style="color: rgb(80,160,79);">000000000022</span>c1d8 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#17</span> pc <span style="color: rgb(80,160,79);">0000000000229e</span>d4 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
```
 
此时发现10052线程调用EGL函数卡住，对应业务需进一步分析，可通过调用栈排查具体业务so的持锁情况。
 
**排查建议**
 
业务优先解堆栈，根据业务的堆栈代码，排查是否有持EGL锁的业务，查看EGL锁使用是否规范。
 
**案例二**
 
**问题现象**
 
应用Web页面卡死，6秒后闪退。
 
**问题分析**
 
3S和6S的堆栈如下：
 
```text
Tid:<span style="color: rgb(80,160,79);">50027</span>, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b64c8 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">148</span>)(<span style="color: rgb(80,160,79);">16e71</span>a67bfa83c977534a6b3e5f80cee)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b8518 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_cond_timedwait+<span style="color: rgb(80,160,79);">168</span>)(<span style="color: rgb(80,160,79);">16e71</span>a67bfa83c977534a6b3e5f80cee)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">0000000005003</span>aa0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::ConditionVariable::Wait()+<span style="color: rgb(80,160,79);">104</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">0000000005027368</span> /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::TimedWaitImpl(base::TimeDelta)+<span style="color: rgb(80,160,79);">784</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000004</span>fb8960 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::TimedWait(base::TimeDelta)+<span style="color: rgb(80,160,79);">96</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000004</span>fb88f0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::Wait()+<span style="color: rgb(80,160,79);">16</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">000000000526e3</span>d4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::(anonymous <span style="color: rgb(0,0,255);">namespace</span>)::ThreadSafeInterfaceEndpointClientProxy::SendMessageWithResponder(mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+<span style="color: rgb(80,160,79);">1336</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">00000000052766</span>c4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::<span style="color: rgb(0,0,255);">internal</span>::ThreadSafeForwarderBase::AcceptWithResponder(mojo::Message*, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+<span style="color: rgb(80,160,79);">44</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#08</span> pc <span style="color: rgb(80,160,79);">000000000527</span>c084 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::<span style="color: rgb(0,0,255);">internal</span>::SendMojoMessage(mojo::MessageReceiverWithResponder&, mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+<span style="color: rgb(80,160,79);">144</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#09</span> pc <span style="color: rgb(80,160,79);">0000000002</span>fb59a0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(gpu::mojom::GpuChannelProxy::WaitForGetOffsetInRange(<span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, gpu::CommandBuffer::State*)+<span style="color: rgb(80,160,79);">360</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
<span style="color: rgb(0,0,255);">#10</span> pc <span style="color: rgb(80,160,79);">00000000030</span>b9ad4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">int</span>)+<span style="color: rgb(80,160,79);">612</span>)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
```
 
观察到有关键字WaitForGetOffsetInRange，在堆栈日志中全局搜索Chrome_IOThread，找到该线程的堆栈。
 
```text
Tid:<span style="color: rgb(80,160,79);">50276</span>, Name:Chrome_IOThread
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b64c8 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">148</span>)(<span style="color: rgb(80,160,79);">16e71</span>a67bfa83c977534a6b3e5f80cee)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>b8518 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__pthread_cond_timedwait+<span style="color: rgb(80,160,79);">168</span>)(<span style="color: rgb(80,160,79);">16e71</span>a67bfa83c977534a6b3e5f80cee)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">00000000000</span>c439c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::condition_variable::wait(std::__n1::unique_lock<std::__n1::mutex>&)+<span style="color: rgb(80,160,79);">20</span>)(<span style="color: rgb(80,160,79);">1204</span>f957e9c8ca1e5b2539b1755de7e26e4f8e8d)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">00000000000</span>ca004 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::__shared_mutex_base::lock_shared()+<span style="color: rgb(80,160,79);">84</span>)(<span style="color: rgb(80,160,79);">1204</span>f957e9c8ca1e5b2539b1755de7e26e4f8e8d)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">00000000000840</span>cc /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000000089444</span> /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">0000000000088908</span> /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">000000000008</span>d00c /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
```
 
这类问题的根本原因在于Chromium原生逻辑：需要在UI线程上抛出同步任务到GPU相关线程，等待任务执行完成后返回，才能析构Web组件，保证生命周期。在这里mojo同步接口需通过Chrome_IOThread线程转发消息，通过调用栈可以看到，由于业务so持锁未释放，阻塞了Chrome_IOThread线程消息转发，导致UI线程阻塞。
 
**排查建议**
 
业务优先根据so解堆栈，根据堆栈代码排查业务持锁的问题，是否未释放锁。
 
**案例三**
 
**问题现象**
 
应用Web页面卡死，6秒后闪退。
 
**问题分析**
 
3S和6S的堆栈一致，堆栈如下：
 
```text
Tid:<span style="color: rgb(80,160,79);">1558</span>, Name:xxx
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>cc2fc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">156</span>)(<span style="color: rgb(80,160,79);">4</span>dcf1315ac91d1611e703e23ab16e8c7)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>ce3cc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(pthread_cond_timedwait+<span style="color: rgb(80,160,79);">172</span>)(<span style="color: rgb(80,160,79);">4</span>dcf1315ac91d1611e703e23ab16e8c7)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">00000000047</span>dce28 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_ConditionVariable::Wait()+<span style="color: rgb(80,160,79);">148</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">0000000004818</span>d08 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::TimedWaitImpl(base::PAC_TimeDelta)+<span style="color: rgb(80,160,79);">544</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000004782970</span> /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::TimedWait(base::PAC_TimeDelta)+<span style="color: rgb(80,160,79);">160</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">00000000047828</span>c0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::Wait()+<span style="color: rgb(80,160,79);">16</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">0000000004</span>bfceec /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::Wait(mojo::PAC_Handle, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, PAC_MojoHandleSignalsState*)+<span style="color: rgb(80,160,79);">268</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#07</span> pc <span style="color: rgb(80,160,79);">00000000038</span>c43c4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::Wait(mojo::PAC_Handle, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, PAC_MojoHandleSignalsState*)+<span style="color: rgb(80,160,79);">36</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#08</span> pc <span style="color: rgb(80,160,79);">0000000004</span>be1274 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_Connector::WaitForIncomingMessage()+<span style="color: rgb(80,160,79);">60</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#09</span> pc <span style="color: rgb(80,160,79);">0000000004</span>beb3e0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::<span style="color: rgb(0,0,255);">internal</span>::PAC_MultiplexRouter::PAC_InterfaceEndpoint::SyncWatchExclusive(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">long</span>)+<span style="color: rgb(80,160,79);">112</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#10</span> pc <span style="color: rgb(80,160,79);">0000000004</span>be4f18 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_InterfaceEndpointClient::SendMessageWithResponder(mojo::PAC_Message*, <span style="color: rgb(0,0,255);">bool</span>, mojo::PAC_InterfaceEndpointClient::SyncSendMode, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+<span style="color: rgb(80,160,79);">628</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#11</span> pc <span style="color: rgb(80,160,79);">0000000004</span>be5134 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_InterfaceEndpointClient::AcceptWithResponder(mojo::PAC_Message*, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+<span style="color: rgb(80,160,79);">32</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#12</span> pc <span style="color: rgb(80,160,79);">0000000004</span>bf84b8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::<span style="color: rgb(0,0,255);">internal</span>::SendMojoMessage(mojo::PAC_MessageReceiverWithResponder&, mojo::PAC_Message&, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+<span style="color: rgb(80,160,79);">108</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
<span style="color: rgb(0,0,255);">#13</span> pc <span style="color: rgb(80,160,79);">0000000001e</span>d1b7c /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(viz::mojom::PAC_FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::PAC_FrameSinkId <span style="color: rgb(0,0,255);">const</span>&)+<span style="color: rgb(80,160,79);">340</span>)(<span style="color: rgb(80,160,79);">36</span>d1a5650b9ab413653e7fb36581fd2f0610b9aa)
```
 
根据堆栈分析，找到VizCompositorTh线程，进一步看到阻塞在了IPC通信中，需要找到对端的线程号，因此全局搜索2178；
 
```text
Tid:<span style="color: rgb(80,160,79);">2178</span>, Name:VizCompositorTh
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">000000000018</span>a648 /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(ioctl+<span style="color: rgb(80,160,79);">164</span>)(<span style="color: rgb(80,160,79);">4</span>dcf1315ac91d1611e703e23ab16e8c7)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">000000000000e</span>cd0 /system/lib64/chipset-sdk-sp/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">long</span>, <span style="color: rgb(0,0,255);">void</span>*)+<span style="color: rgb(80,160,79);">124</span>)(<span style="color: rgb(80,160,79);">1</span>c998eec085cdb89fa5895a5080a0839)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">0000000000072e</span>e4 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(<span style="color: rgb(0,0,255);">bool</span>)+<span style="color: rgb(80,160,79);">284</span>)(<span style="color: rgb(80,160,79);">64</span>a17fcbe779a6da9fa26574ccce2f1e)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">000000000007187</span>c /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+<span style="color: rgb(80,160,79);">124</span>)(<span style="color: rgb(80,160,79);">64</span>a17fcbe779a6da9fa26574ccce2f1e)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000000070</span>cf0 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(<span style="color: rgb(0,0,255);">int</span>, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+<span style="color: rgb(80,160,79);">620</span>)(<span style="color: rgb(80,160,79);">64</span>a17fcbe779a6da9fa26574ccce2f1e)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000000049</span>b3c /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(<span style="color: rgb(0,0,255);">bool</span>, <span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+<span style="color: rgb(80,160,79);">272</span>)(<span style="color: rgb(80,160,79);">64</span>a17fcbe779a6da9fa26574ccce2f1e)
<span style="color: rgb(0,0,255);">#06</span> pc <span style="color: rgb(80,160,79);">000000000004</span>a588 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(<span style="color: rgb(0,0,255);">unsigned</span> <span style="color: rgb(0,0,255);">int</span>, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+<span style="color: rgb(80,160,79);">216</span>)(<span style="color: rgb(80,160,79);">64</span>a17fcbe779a6da9fa26574ccce2f1e)
```
 
找到线程2178的对端线程为2150，因此全局搜索2150；
 
```text
BinderCatcher --
    <span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">2178</span> to <span style="color: rgb(80,160,79);">1790</span>:<span style="color: rgb(80,160,79);">2150</span> code <span style="color: rgb(80,160,79);">5004</span> wait:<span style="color: rgb(80,160,79);">15.672447500</span> s frz_state:<span style="color: rgb(80,160,79);">3</span>,  ns:-<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span> to -<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span>, debug:<span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">2178</span> to <span style="color: rgb(80,160,79);">1790</span>:<span style="color: rgb(80,160,79);">2150</span>, active_code:<span style="color: rgb(80,160,79);">0</span>, active_thread=<span style="color: rgb(80,160,79);">0</span>, pending_async_proc=<span style="color: rgb(80,160,79);">0</span>
async   <span style="color: rgb(80,160,79);">5921</span>:<span style="color: rgb(80,160,79);">6512</span> to <span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">0</span> code <span style="color: rgb(80,160,79);">13</span> wait:<span style="color: rgb(80,160,79);">3.205905625</span> s frz_state:<span style="color: rgb(80,160,79);">3</span>,  ns:-<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span> to -<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span>, debug:<span style="color: rgb(80,160,79);">5921</span>:<span style="color: rgb(80,160,79);">6512</span> to <span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">0</span>, active_code:<span style="color: rgb(80,160,79);">2</span>, active_thread=<span style="color: rgb(80,160,79);">2037</span>, pending_async_proc=<span style="color: rgb(80,160,79);">5921</span>
async   <span style="color: rgb(80,160,79);">5921</span>:<span style="color: rgb(80,160,79);">6512</span> to <span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">0</span> code <span style="color: rgb(80,160,79);">2</span>f wait:<span style="color: rgb(80,160,79);">3.30637187</span> s frz_state:<span style="color: rgb(80,160,79);">3</span>,  ns:-<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span> to -<span style="color: rgb(80,160,79);">1</span>:-<span style="color: rgb(80,160,79);">1</span>, debug:<span style="color: rgb(80,160,79);">5921</span>:<span style="color: rgb(80,160,79);">6512</span> to <span style="color: rgb(80,160,79);">1558</span>:<span style="color: rgb(80,160,79);">0</span>, active_code:<span style="color: rgb(80,160,79);">2</span>, active_thread=<span style="color: rgb(80,160,79);">2037</span>, pending_async_proc=<span style="color: rgb(80,160,79);">5921</span>
```
 
根据2150线程的堆栈，需要排查下面的业务so的持锁情况。
 
```text
Tid:<span style="color: rgb(80,160,79);">2150</span>, Name:OS_IPC_0_2150
<span style="color: rgb(0,0,255);">#00</span> pc <span style="color: rgb(80,160,79);">00000000001</span>cc2fc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(__timedwait_cp+<span style="color: rgb(80,160,79);">156</span>)(<span style="color: rgb(80,160,79);">4</span>dcf1315ac91d1611e703e23ab16e8c7)
<span style="color: rgb(0,0,255);">#01</span> pc <span style="color: rgb(80,160,79);">00000000001</span>ce3cc /system/lib/ld-musl-aarch64.so<span style="color: rgb(80,160,79);">.1</span>(pthread_cond_timedwait+<span style="color: rgb(80,160,79);">172</span>)(<span style="color: rgb(80,160,79);">4</span>dcf1315ac91d1611e703e23ab16e8c7)
<span style="color: rgb(0,0,255);">#02</span> pc <span style="color: rgb(80,160,79);">00000000000</span>c4984 /system/lib64/chipset-sdk-sp/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+<span style="color: rgb(80,160,79);">32</span>)(<span style="color: rgb(80,160,79);">4</span>c257fafd66f57a4f1f873163a520100e191a256)
<span style="color: rgb(0,0,255);">#03</span> pc <span style="color: rgb(80,160,79);">00000000000</span>c55b0 /system/lib64/chipset-sdk-sp/libc++.so(std::__h::__assoc_sub_state::wait()+<span style="color: rgb(80,160,79);">72</span>)(<span style="color: rgb(80,160,79);">4</span>c257fafd66f57a4f1f873163a520100e191a256)
<span style="color: rgb(0,0,255);">#04</span> pc <span style="color: rgb(80,160,79);">0000000000214</span>a2c /system/lib64/libxxx.so(...)
<span style="color: rgb(0,0,255);">#05</span> pc <span style="color: rgb(80,160,79);">0000000000496770</span> /system/lib64/libxxx.so(...)
```
 
**排查建议**
 
结合binder对端进程堆栈信息，排查对端阻塞原因。
