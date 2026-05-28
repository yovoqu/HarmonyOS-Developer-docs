# @previewer/mandatory-default-value-for-local-initialization

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_value-for-local-initialization

如果组件的属性支持本地初始化，需要设置一个合法的不依赖运行时的默认值。
 

#### 规则配置

```json
// code-linter.json5
<span style="color: rgb(65,97,0);">{</span>
<span style="color: rgb(65,97,0);">  "rules": {</span>
<span style="color: rgb(65,97,0);">    "@previewer/mandatory-default-value-for-local-initialization": "warn"</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
@Builder
function MyBuilderFunction(): void {
}

@Entry
@Component
struct Index {
  messageA?: string;
  message: string = 'Hello World';
  @Provide messageB: string = 'messageB';
  @StorageLink('varA') varA: number = 2;
  @StorageProp('languageCode') lang: string = 'en';
  @LocalStorageLink('PropA') storageLink1: number = 1;
  @LocalStorageProp('PropB') storageLink2: number = 2;
  @BuilderParam myBuilder: () => void = MyBuilderFunction;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}
```
 
 

#### 反例

```text
@Entry
@Component
struct Index {
  @BuilderParam myBuilder: () => void;

  build() {
    Row() {
      Column() {
        Text('Hello World')
        this.myBuilder()
      }
    }
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@previewer/recommended</span>
<span style="color: rgb(106,135,89);">plugin:@previewer/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
