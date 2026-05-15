# 加载3DGS模型

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-load

## 适用场景

支持的3DGS模块格式包括：MP4、PLY、GLB三种格式。 效果如下图所示：
![](assets/加载3DGS模型/file-20260514131717832-0.png)

## 接口说明

以下仅列出本指南示例代码中调用的部分主要接口：
| 接口名 | 描述 |
| --- | --- |
| static loadGSNode(scene: [Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene), params: [GSImportSettings](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialrender#gsimportsettings), parent?: [Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)): Promise | 加载3DGS模型。 |


## 开发步骤

从entry目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。
```text
import { spatialRender } from '@kit.SpatialReconKit';
import { Scene, RenderContext } from '@kit.ArkGraphics3D'
```

加载当前场景的上下文。
```text
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
```

调用加载3DGS模型接口。
```text
if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb"; // 3DGS模型的uri，根据实际情况修改
    let offset = 0;
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}
```
