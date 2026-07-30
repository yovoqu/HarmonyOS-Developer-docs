# 如何解决mock中继承Base64Helper不生效的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-20

#### 问题现象

mock中继承Base64Helper不生效。
 
问题代码示例参考如下：
 
```ArkTS
<em>// Base64HelperMock.mock.ets</em>
import { util } from '@kit.ArkTS'

export class Base64HelperMock extends util.Base64Helper {
  decodeSync(src: string | Uint8Array, options?: util.Type | undefined): Uint8Array {
    return new Uint8Array([99,97,10]);
  }
  encodeSync(src: Uint8Array, options?: util.Type | undefined) {
    return new Uint8Array([99,97,10]);
  }
  encodeToStringSync(src: Uint8Array, options?: util.Type | undefined): string {
    return '';
  }
}
```
 
```ArkTS
<em>// mock-config.json5</em>
{
  "@ohos.util": {
    "source": "src/mock/Base64HelperMock.mock.ets"
  }
}
```
 
```text
<em>// </em><em>测试文件</em>
import { util } from '@kit.ArkTS'
import { describe, it } from '@ohos/hypium';

export default function localUnitTest() {
  describe('localUnitTest', () => {
    it('assertContain', 0, () => {
      const array = new util.Base64Helper().decodeSync('')
    });
  });
}
```
 
运行报错如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/wtkWrTbfTKyLeVlLxbjdAg/zh-cn_image_0000002658808815.png?HW-CC-KV=V1&HW-CC-Date=20260701T041012Z&HW-CC-Expire=86400&HW-CC-Sign=A5238829833170872BC5E7A4089708952A2A09DEAA43F0788B151977D80BA3FF)

 
 

#### 背景知识

[Mock能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-test-mock)：在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用mock能力，对这些接口或对象进行模拟。
 
 

#### 问题定位

请按以下方案进行排查：
 1. 确认mock文件的导出方式和被mock接口的导出方式一致。查看被mock接口的导出方式，可以用Ctrl+鼠标左键点击被mock的接口。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/i5etq4F7S8uAXh7qXE9NHA/zh-cn_image_0000002628409548.png?HW-CC-KV=V1&HW-CC-Date=20260701T041012Z&HW-CC-Expire=86400&HW-CC-Sign=40A1405C3C7617314CDC6E8ECD0D57D2163D465255C29AEB5D4CB8B5202177B8)


  查看mock文件的导出方式。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/VExXDQuJSCSYZVctRgxvmw/zh-cn_image_0000002628569446.png?HW-CC-KV=V1&HW-CC-Date=20260701T041012Z&HW-CC-Expire=86400&HW-CC-Sign=CCA8A18FF357BD099B027A1B2C19631F76687DDF0D4BB49C8AB67D35252241FC)

 
 

#### 分析结论

mock文件的导出方式和被mock接口的导出方式不一致。
 
 

#### 修改建议

mock文件的导出方式要与mock的接口（util接口）的导出方式一致，[util](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util)接口的导出方式为export default util，所以这边mock文件的导出方式要为export default mockUtil。
 1. 在“src/mock”目录下新建一个ArkTS文件，例如Base64HelperMock.mock.ets，在这个文件内定义目标模块的mock实现。
```text
import { util } from '@kit.ArkTS'
type MockUtil = Record<string, Object>;

export class Base64HelperMock {
  decodeSync(src: string | Uint8Array, options?: util.Type | undefined): Uint8Array {
    console.info('run mock')
    return new Uint8Array([99,97,10]);
  }
  encodeSync(src: Uint8Array, options?: util.Type | undefined) {
    return new Uint8Array([99,97,10]);
  }
  encodeToStringSync(src: Uint8Array, options?: util.Type | undefined): string {
    return '';
  }
}

const mockUtil: MockUtil = {
  'Base64Helper': Base64HelperMock,
}

export default mockUtil
```

2. 在mock配置文件“src/mock/mock-config.json5”中定义目标模块与mock实现的映射关系。
```ArkTS
{
  "@ohos.util": {
    "source": "src/mock/Base64HelperMock.mock.ets"
  }
}
```

3. 在测试文件中编写如下代码。
```text
import { util } from '@kit.ArkTS'
import { describe, it } from '@ohos/hypium';

export default function localUnitTest() {
  describe('localUnitTest', () => {
    it('assertContain', 0, () => {
      const array = new util.Base64Helper().decodeSync('')
    });
  });
}
```
