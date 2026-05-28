# @typescript-eslint/prefer-enum-initializers

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-enum-initializers

推荐显式初始化每个枚举成员值。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-enum-initializers": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
export enum Status {
  open = 'Open',
  close = 'Close'
}

export enum Direction {
  up = '1',
  down = '2'
}

export enum Color {
  red = 'Red',
  green = 'Green',
  blue = 'Blue'
}
```
 
 

#### 反例

```text
export enum Status {
  open,
  close
}

export enum Direction {
  up,
  down
}

export enum Color {
  red,
  green,
  blue
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
