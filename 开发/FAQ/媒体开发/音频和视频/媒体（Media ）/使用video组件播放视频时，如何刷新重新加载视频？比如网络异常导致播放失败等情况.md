# 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-5

先将URL设置为空，再改回原来的值，示例代码如下：
 
```ArkTS
@Component
export struct VideoErrorReload {
  @State url: string = 'https://******';

  build() {
    Column({ space: 20 }) {
      Video({ src: this.url })
        .height(300)

      Button('重新url')
        .onClick(() => {
          let temp = this.url;
          this.url = '';
          setTimeout(() => {
            this.url = temp;
          }, 100);
        })
    }
  }
}
```
