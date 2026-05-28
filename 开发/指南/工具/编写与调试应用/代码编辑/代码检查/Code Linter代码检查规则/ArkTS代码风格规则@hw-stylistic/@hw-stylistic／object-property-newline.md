# @hw-stylistic/object-property-newline

更新时间：2026-03-09 07:00:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_object-property-newline

强制对象属性换行。该规则仅检查.ets文件类型。
 
对象属性不超过4个时，允许在同一行，也可以每个属性都换行。对象属性超过4个时，每个属性必须都换行。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/object-property-newline": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
export {a, b};

interface II {
  p1: string;
  p2: string;
  p3: string;
  p4: string;
  p5?: string;
}

const a: II = {
  p1: 'p1',
  p2: 'p2',
  p3: 'p3',
  p4: 'p4',
  p5: 'p5'
};

const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4' };
```
 
 

##### 反例

```text
export {a, b};

interface II {
  p1: string;
  p2: string;
  p3: string;
  p4: string;
  p5?: string;
}

// Object properties must go on a new line.
const a: II = { p1: 'p1', p2: 'p2',
  p3: 'p3', p4: 'p4' };

// Object properties must go on a new line.
const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4', p5: 'p5' };
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
