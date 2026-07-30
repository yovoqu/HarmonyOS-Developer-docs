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

<em>/**</em>
<em> * open(port?: number, host?: string, wait?: boolean): void</em>
<em> * port：用于监听检查器连接的端口。</em>
<em> * host：用于监听检查器连接的主机。</em>
<em> * wait：阻塞直到有客户端连接。</em>
<em> */</em>
open(9229, undefined, true);

<em>// 自定义插件</em>
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
  system: hapTasks,<em> /* Built-in plugin of Hvigor. It cannot be modified. */</em>
  plugins: [
    customPlugin()
  ]      <em> /* Custom plugin to extend the functionality of Hvigor. */</em>
}
```


2. 打开Chrome调试页面：chrome://inspect/#devices：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/YbdCc0FdQlOBlwJmnoDt3Q/zh-cn_image_0000002658928587.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=DFAB9A4E00969186D9C7EF183663C94352C0A5E18D1DB6CAED0EED558741F094)


3. 勾选“Discover network targets”，点击Configure按钮：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/N1jgr0UITEeqKidK_LeAjw/zh-cn_image_0000002658808637.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=C249EB9D85DC08C483FDB73F302AD88DA76081E186172DB01200AFB273C3693F)


4. 配置监听接口，勾选“Enable port forwarding”，点击Done：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/VdA7sXxeTNqD-xRuiVEC2w/zh-cn_image_0000002628569272.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=9325DAC5DE6E70197161C84DC24FC0C5A9154F77CB8761EFB31FC4B8B4D1DB9B)


5. 回到DevEco Studio界面，执行构建：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/rYfBcWX3TGKcY-EWhQfNxg/zh-cn_image_0000002628409366.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=70B19C4B7007A1625F1992B721CCEFCFE5ED2B75A72627049FD737F2ABC360FF)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/D3dmiQ4cQkenhUp07JQCgQ/zh-cn_image_0000002658928589.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=F194053C46238223BF5F9CD7989F0070772E65FA599D72DF968D24FC592079CA)


6. 切换至Chrome调试页面，点击“inspect”，即可开始调试：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ysts6cKdTFqyHMtx6hr6zA/zh-cn_image_0000002658808639.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=5364B774F3AA4DD73F9E993185EC095F8B8F5116A8388ABA19203E16F3AA9757)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/w1svjcfETAW0OLcaTUHxYg/zh-cn_image_0000002628569274.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=3179E8FFED87EEB8F368C6CF1C39644D417233C840480563C6A3095CD778DCA2)


7. 调试如果开启了[守护进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon)，二次构建时会因守护进程还在出现以下报错，[关闭当前工程的守护进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon#section298519112359)重新执行步骤5即可：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/D_zMFb2hQweuKgTCi9-MFQ/zh-cn_image_0000002628409368.png?HW-CC-KV=V1&HW-CC-Date=20260730T072717Z&HW-CC-Expire=86400&HW-CC-Sign=4EA9D6D4DDD94138B882E2423479C31A65B30FA9C2B035230FC8AAF4E143BB74)
