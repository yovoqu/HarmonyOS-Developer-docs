# 获取Hap包的打包构建时间

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-217

#### 问题现象

如何通过Hvigor构建获取Hap包的构建时间？
 
 

#### 背景知识

Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享。
 
Hvigor主要提供了两种方式来实现插件：[基于hvigorfile脚本开发插件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-plugin#section552855418188)、[基于typescript项目开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-plugin#section1825121193616)。
 
 

#### 解决方案

afterNodeEvaluate回调函数中将构建时间手动插入到自定义的Json文件中，并保存到rawfile目录下，后续读取该文件，Hap模块下的hvigorfile.ts参考如下：
 
```json
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import * as fs from 'fs';
import path from 'path';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(node: HvigorNode): Promise<void> {
    <em>  // node评估后的回调函数</em>
      hvigor.afterNodeEvaluate((hvigorNode) => {
        <em>// 确保目录存在</em>
        const resourcesDir = path.join(__dirname, 'src/main/resources/rawfile');
        if (!fs.existsSync(resourcesDir)) {
          fs.mkdirSync(resourcesDir, { recursive: true });
        }
        <em>// </em><em>写入构建时间到json文件</em>
        const now = new Date();
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const date = String(now.getDate()).padStart(2, '0');
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const buildTime = `${year}-${month}-${date} ${hours}:${minutes}:${seconds}`;
        const buildInfo = { 'buildTime': buildTime };
        fs.writeFileSync(
          path.join(resourcesDir, 'build_hap_info.json'),
          JSON.stringify(buildInfo, null, 2)
        );
      })
    }
  };
};

export default {
  system: hapTasks,
  plugins: [customPlugin()]
}
```
