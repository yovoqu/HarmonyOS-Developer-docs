# @hw-stylistic/max-len

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_max-len

强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/max-len": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
@Entry
@Component
struct Index {
  message: string = 'hello';

  build() {
    Text(this.message)
  }
}
```
 
 

#### 反例

```text
// This line has a length of 135. Maximum allowed is 120.
export const longLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongName = 10;
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
