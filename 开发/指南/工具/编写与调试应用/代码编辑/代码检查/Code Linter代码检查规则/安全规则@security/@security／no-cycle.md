# @security/no-cycle

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle

该规则禁止使用循环依赖。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@security/no-cycle"</span>: <span style="color: rgb(6,125,23);">"error"</span>
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```ArkTS
// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';
```
 
 

#### 反例

```ArkTS
// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';
```
 
> [!NOTE]
> 反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@security/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
