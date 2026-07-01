# 编译构建library模块时报错："Property 'xxxxx' of exported class expression may not be private or protected"

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-168

## 编译构建library模块时报错："Property 'xxxxx' of exported class expression may not be private or protected"
 


##### 问题现象

编译构建library模块时（Build->Make Module 'library'），报错信息如下：
 
```text
Property 'xxx' of exported class expression may not be private or protected.
```
 
 

##### 背景知识

ArkTS提供了private、protected和public访问修饰符。默认情况下，属性的可访问修饰符为public。选取适当的可访问修饰符可以提升代码的安全性和可读性。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/pY-EyDpYRXCJ9FZCZhgpZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025520Z&HW-CC-Expire=86400&HW-CC-Sign=733B6829149F2DD3D6FC514127D2B78D5C89070B5D7E337F36F5C3809453D1E1)
 

如果类中包含private属性，无法通过对象字面量初始化该类，在有需要通过字面量创建、或者直接访问属性时设置为public，具体参考[给类属性添加访问修饰符](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-high-performance#section743155016482)。
 

 
 

##### 问题定位

根据报错信息提示，导出的类表达式中使用了私有（private）或保护（protected）访问修饰符定义属性，而这些属性可能在类的外部被访问到。
 
 

##### 分析结论

导出的模块中可能存在private或protected修饰的属性，在类的外部，只有公共（public）属性是可以直接访问的，私有和保护属性不应在类的外部使用。
 
 

##### 修改建议

有以下两种修改方式：
 
- 将private或protected修饰符改为public。
- 使用单例模式，通过公共方法暴露私有属性，参考以下示例代码：
src/main/ets/pages/Index.ets代码：
```text
import { singletonInstance } from './SingletonManager';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Get Data')
        .onClick(() => {
          // 通过单例访问数据
          console.log(singletonInstance.getModifiedData());
        })

      Button('Update Data')
        .onClick(() => {
          // 通过单例修改数据
          singletonInstance.updateData('New Private Data');
          console.log(singletonInstance.getModifiedData());
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

- src/main/ets/pages/SingletonManager.ets代码：
```text
// 单例类定义
class SingletonManager {
  // 私有静态实例
  private static instance: SingletonManager;
  // 私有属性（避免直接暴露）
  private _privateData: string = 'Initial Data';

  // 私有构造函数（防止外部实例化）
  private constructor() {
  }

  // 静态方法获取唯一实例
  public static getInstance(): SingletonManager {
    if (!SingletonManager.instance) {
      SingletonManager.instance = new SingletonManager();
    }
    return SingletonManager.instance;
  }

  // 公共方法访问私有属性
  public getModifiedData(): string {
    return this._privateData + '(Processed)';
  }

  // 公共方法修改私有属性
  public updateData(newValue: string): void {
    this._privateData = newValue;
  }
}

// 导出单例实例（非类本身）
export const singletonInstance = SingletonManager.getInstance();
```
