# @correctness/redundant-dependency-check

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-redundant-dependency-check

建议删除冗余的依赖配置。冗余依赖会增加依赖加载和解析时间，影响代码质量。
 

##### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@correctness/redundant-dependency-check": "suggestion"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

1. 在 entry 下的oh-package.json5文件中配置了a、b、c三个依赖，entry/src/main/ets中的文件中全部 import 导入。
 
2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，整个工程全部 import 导入。
 
 

##### 反例

1. 在 entry 下的oh-package.json5文件中配置了a、b、c三个依赖，但entry/src/main/ets中的文件中只 import 导入了a,b两个依赖。
 
2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，但整个工程只 import 导入了a,b两个依赖。
 
 

##### 规则集

```text
<span style="color: rgb(80,160,79);">plugin:@correctness/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
