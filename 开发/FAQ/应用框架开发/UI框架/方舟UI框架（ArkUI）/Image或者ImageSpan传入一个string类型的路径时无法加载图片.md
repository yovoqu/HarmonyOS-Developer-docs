# Image或者ImageSpan传入一个string类型的路径时无法加载图片

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-153

目前规格上只支持常量，需要把string提取出来用\$r( )包裹。例如：

```text
localImageName = $r( 'app.media.icon' )
```
