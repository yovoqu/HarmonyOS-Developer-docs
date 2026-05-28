# @typescript-eslint/typedef

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_typedef

在某些位置需要类型注释。
 
支持检查的范围从选项中查看。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/typedef": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/typedef选项](https://typescript-eslint.nodejs.cn/rules/typedef#options)。
 
 

#### 正例

```text
export const text = 'text';
```
 
 

#### 反例

```text
// 默认配置下，规则不会告警
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
