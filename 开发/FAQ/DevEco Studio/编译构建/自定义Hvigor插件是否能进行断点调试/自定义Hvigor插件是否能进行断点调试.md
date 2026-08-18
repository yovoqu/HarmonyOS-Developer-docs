# 自定义Hvigor插件是否能进行断点调试

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-228

#### 问题现象

自定义Hvigor插件如何调试？
 
 

#### 背景知识

- Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享，参考[开发Hvigor插件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-plugin)。
- Node.js的Inspector模块是用于启用和管理V8 Inspector的内置模块，它允许开发者通过Chrome DevTools远程调试和检查运行中的Node.js应用程序。

 
 

#### 解决方案

- hvigorfile.ts文件暂时不支持在DevEco Studio调试。
- 可借助Node.js的Inspector模块通过Chrome DevTools进行断点调试，具体步骤如下：1. 在hvigorfile.ts通过open启动调试器并等待连接：
```text
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';
import { open } from 'inspector';

/**
 * open(port?: number, host?: string, wait?: boolean): void
 * port：用于监听检查器连接的端口。
 * host：用于监听检查器连接的主机。
 * wait：阻塞直到有客户端连接。
 */
open(9229, undefined, true);

// 自定义插件
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode): void {
      debugger
      console.info("hello customPlugin");
    }
  }
}

export default {
  system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [
    customPlugin()
  ]       /* Custom plugin to extend the functionality of Hvigor. */
}
```


2. 打开Chrome调试页面：chrome://inspect/#devices：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/YbdCc0FdQlOBlwJmnoDt3Q/zh-cn_image_0000002658928587.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=C2B0ED841C33F1D8BBFCDD574C4C48570EFE6F3A1BFCDB67219DE8EB930669C6)


3. 勾选“Discover network targets”，点击Configure按钮：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/N1jgr0UITEeqKidK_LeAjw/zh-cn_image_0000002658808637.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=2A0598E3AED1776A265C94847583B1ACD23D3B17CD0CC9F78874B3F6DA6EED3C)


4. 配置监听接口，勾选“Enable port forwarding”，点击Done：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/VdA7sXxeTNqD-xRuiVEC2w/zh-cn_image_0000002628569272.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=0D437D32C482AA7D240891C19B04686771B05148F4FEB07D05A19DFBF64D365A)


5. 回到DevEco Studio界面，执行构建：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/rYfBcWX3TGKcY-EWhQfNxg/zh-cn_image_0000002628409366.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=E404EA926FAB9CC8D3F973F759A8BBDC662C90FE5CF07B1EC81D36F93C9D454F)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/D3dmiQ4cQkenhUp07JQCgQ/zh-cn_image_0000002658928589.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=DA6F639A369CD783DEDA7875497176E629E571195EC5785BE0EF59B8A697E192)


6. 切换至Chrome调试页面，点击“inspect”，即可开始调试：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ysts6cKdTFqyHMtx6hr6zA/zh-cn_image_0000002658808639.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=783F44C25DCCE4305D66DB339BD3E9B38E59353C820D3BA31F8C742FFC9CF32D)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/w1svjcfETAW0OLcaTUHxYg/zh-cn_image_0000002628569274.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=DF81A32421D33C10DE187FC4CC9617EC0266D108EF0367CE1ADF67865F736DAA)


7. 调试如果开启了[守护进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon)，二次构建时会因守护进程还在出现以下报错，[关闭当前工程的守护进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon#section298519112359)重新执行步骤5即可：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/D_zMFb2hQweuKgTCi9-MFQ/zh-cn_image_0000002628409368.png?HW-CC-KV=V1&HW-CC-Date=20260811T005528Z&HW-CC-Expire=86400&HW-CC-Sign=632D7A25A2DB7A66CFE1F0465C8DB4EBCFA2BB9D2B8F2426038084800A87F636)
