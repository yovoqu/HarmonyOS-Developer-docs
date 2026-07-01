# 如何快速关闭工程中所有字节码HAR配置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-169

**解决措施**
 
方案一：适用于HAR文件较少的场景，直接修改字段byteCodeHar为false，详细字段可在以下链接中查询：[模块级build-profile.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile)
 
方案二：适用于HAR文件数量较多的场景。单独为每个HAR包配置较为繁琐，可以通过自定义插件直接修改所有HAR包的byteCodeHar字段值。该方法在编译时生效，但不会修改build-profile.json5文件中的字段值。
 
```text
<em>// Engineering-level hvigorfile.ts file</em>
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHarContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
<em>// Implement custom plugins</em>
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(async () => {
        <em>// Register module-level tasks</em>
        harTask(currentNode);
      });
    }
  };
}
function harTask(currentNode: HvigorNode) {
  currentNode.subNodes((node: HvigorNode) => {
    const context = node.getContext(OhosPluginId.OHOS_HAR_PLUGIN)
    context?.targets((target: Target) => {
      const targetName = target.getTargetName();
      node.registerTask({
        <em>// Task name</em>
        name: `HarTask`,
        <em>// Main function of task execution logic</em>
        run() {
          if (context.getBuildProfileOpt) {
            const buildProfile = context.getBuildProfileOpt();
            console.log(buildProfile)
            <em>// Set the bytecode har config to false</em>
            buildProfile["buildOption"] = { arkOptions: { byteCodeHar: false } };
            console.log(buildProfile)
            context.setBuildProfileOpt(buildProfile);
          }
        },
        <em>// Configure the dependency of the pre-task</em>
        dependencies: [`${targetName}@PackageHar`],
        <em>// Post-task dependency for configuring tasks</em>
        postDependencies: ['assembleHar']
      });
    });
  });
}
export default {
  system: appTasks,  <em>/* Built-in plugin of Hvigor. It cannot be modified. */</em>
  plugins:[customPlugin()]  <em>/* Custom plugin to extend the functionality of Hvigor. */</em>
}
```
