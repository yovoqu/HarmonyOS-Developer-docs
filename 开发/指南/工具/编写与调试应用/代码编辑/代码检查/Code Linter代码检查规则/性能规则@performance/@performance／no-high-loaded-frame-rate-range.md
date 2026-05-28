# @performance/no-high-loaded-frame-rate-range

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-high-loaded-frame-rate-range

不允许锁定最高帧率运行。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/no-high-loaded-frame-rate-range"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 60,
  min: 45,
  max: 60,
});
```
 
 

#### 反例

```text
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 120,
  min: 120,
  max: 120,
});
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
