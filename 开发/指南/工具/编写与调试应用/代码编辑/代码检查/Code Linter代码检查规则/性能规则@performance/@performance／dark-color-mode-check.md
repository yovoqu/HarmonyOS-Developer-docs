# @performance/dark-color-mode-check

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-dark-color-mode-check

通过启用深色模式，可以进一步实现能耗的降低。应用需要根据当前设备状态来适配深色模式。
 
> [!NOTE]
> 在检查整个工程时，该规则才生效。 code-linter.json5配置文件中的 overrides 和 ignore 字段对该规则不生效。 若想关闭该规则检查，可将code-linter.json5配置文件中 rules 字段设置为off。

 

##### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```json
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│               └── color.json     
│           
├── mock
│   └── mock-config.json5
```
 
 

##### 反例

```json
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│           
├── mock
│   └── mock-config.json5
```
 
 

##### 规则集

```text
<span style="color: rgb(80,160,79);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
