# 如何解析华为CDN场景下manifestUrl对应的xml文件

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5

推荐使用[@ifbear/fast-xml-parser](https://ohpm.openharmony.cn/#/cn/detail/@ifbear%2Ffast-xml-parser)。
 
执行如下命令行，安装依赖。
 
```xml
To use as package dependency $ ohpm install @ifbear/fast-xml-parser
```
 
示例代码：
 
```xml
const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");

const parser = new XMLParser();
let jObj = parser.parse(XMLdata);
```
