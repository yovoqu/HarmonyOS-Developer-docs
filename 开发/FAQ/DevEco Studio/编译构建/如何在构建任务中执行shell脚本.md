# 如何在构建任务中执行shell脚本

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-104

#### 场景一

只在模块中调用shell脚本，在模块的hvigorfile.ts文件中执行如下示例：
 
> [!WARNING]
> 需要特别注意system字段的取值，不同的模块需要使用不同的值： 在har模块的hvigorfile.ts中，需要使用system: harTasks。 在hsp模块的hvigorfile.ts中，需要使用system: hspTasks。 在hap模块的hvigorfile.ts中，需要使用system: hapTasks。

 
```text
<em>// 模块级hvigorfile.ts文件</em>
import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child_process';
import util from 'node:util';
const scriptPath = 'xxxx.bat';
<em>// 实现自定义插件</em>
export function customPluginFunction2(str?: string) {
  return {
    pluginId: 'CustomPluginID2',
    apply(pluginContext) {
      pluginContext.registerTask({
       <em>// 在模块上注册任务</em>
        name: 'customTask2',
        run: (taskContext) => {
          console.log('run into: ');
          const execPromise = util.promisify(exec)
          execPromise(scriptPath).then(res => {
            console.log(res, 'res');
          }).catch(err => {
            console.log(err, 'err');
          })
        },
<em>        // 配置前置任务依赖</em>
        dependencies: ['default@BuildJS'],
	<em>// 配置任务的后置任务依赖</em>
        postDependencies: ['default@CompileArkTS']
      })
    }
  }
}
export default {
  <em>// Hvigor插件任务类型，具体请查看最后的说明内容</em>
  system: harTasks,
  <em>// 用于扩展Hvigor功能的自定义插件</em>
  plugins: [customPluginFunction2()]
}
```
 
 

#### 场景二

如果多个模块的shell脚本是共用的，可以在工程级的hvigorfile.ts中调用：
```text
<em>// 工程级hvigorfile.ts文件</em>
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child_process';
import util from 'node:util';
const scriptPath = 'xxxx.bat';
<em>// 实现自定义插件</em>
export function customPluginFunction1(): HvigorPlugin {
  return {
    pluginId: 'CustomPluginID1',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        <em>// 注册模块级任务</em>
        hapTask(currentNode);
      });
    }
  };
}
function hapTask(currentNode: HvigorNode) {
  <em>// 遍历所有子模块节点</em>
  currentNode.subNodes((node: HvigorNode) => {
    <em>// 在每个子模块上注册任务</em>
    node.registerTask({
      name: 'customTask1',
      run: (taskContext) => {
        console.log('run into: ', taskContext.moduleName);
        const execPromise = util.promisify(exec);
        execPromise(scriptPath).then(res => {
          console.log(res, 'res');
        }).catch(err => {
          console.log(err, 'err');
        })
      },
	  <em>// 配置前置任务依赖</em>
	  dependencies: ['default@BuildJS'],
	  <em>// 配置任务的后置任务依赖</em>
	  postDependencies: ['default@']
    });
  });
}
export default {
  <em>// 任务类型，不可修改</em>
  system: appTasks,
  <em>// 用于扩展Hvigor功能的自定义插件</em>
  plugins: [customPluginFunction1()]
};
```
