# @performance/web-on-active-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-web-on-active-check

使用了Web预渲染技术的应用，建议在预渲染完成后（onFirstMeaningfulPaint），调用停止渲染接口（onInactive）。
 

##### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/web-on-active-check": "warn",
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
import { webview } from '@kit.ArkWeb';

interface Config {
  url: string,
  localPath: string,
  options: webview.CacheOptions
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.None;
  configs: Array<Config> = [
    {
      url: 'https://www.example.com/example.js',
      localPath: 'example.js',
      options: {
        responseHeaders: [
          { headerKey: 'E-Tag', headerValue: 'xxx' },
          { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
        ]
      }
    }
  ]

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin(() => {
          this.controller.onActive();
        })
        // 预渲染完成后（onFirstMeaningfulPaint）
        .onFirstMeaningfulPaint(() => {
          // 调用停止渲染接口（onInactive）
          this.controller.onInactive();
        })
        .cacheMode(this.mode)
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
            let content = resourceMgr?.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!');
                }).catch((errCode: number) => {
                console.error('precompile failed.' + errCode);
              })
            } catch (err) {
              console.error('precompile failed!.' + err.code + err.message);
            }
          }
        })
    }
  }
}
```
 
 

##### 反例

```text
import { webview } from '@kit.ArkWeb';

interface Config {
  url: string,
  localPath: string,
  options: webview.CacheOptions
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.Default;
  configs: Array<Config> = [
    {
      url: 'https://www.example.com/example.js',
      localPath: 'example.js',
      options: {
        responseHeaders: [
          { headerKey: 'E-Tag', headerValue: 'xxx' },
          { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
        ]
      }
    }
  ]

  build() {
    Column() {
      // web中没有onFirstMeaningfulPaint属性，告警
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
        .onPageBegin(() => {
          this.controller.onActive();
        })
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
            let content = resourceMgr?.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!');
                }).catch((errCode: number) => {
                console.error('precompile failed.' + errCode);
              })
            } catch (err) {
              console.error('precompile failed!.' + err.code + err.message);
            }
          }
        })
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/</span><span style="color: rgb(4,81,165);">recommended</span>
<span style="color: rgb(80,160,79);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
