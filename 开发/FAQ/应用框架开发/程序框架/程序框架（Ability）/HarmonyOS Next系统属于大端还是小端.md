# HarmonyOS Next系统属于大端还是小端

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-117

属于小端序，可以通过以下代码验证：
 
```text
@Entry
@Component
struct IndexTest {
  @State message: string = 'Hello World';

  isLittleEndian(): boolean {
    const buffer = new ArrayBuffer(2);
    const uint8Array = new Uint8Array(buffer);
    const uint16Array = new Uint16Array(buffer);
    <em>// Write 0xAA and 0xBB into the buffer</em>
    uint8Array[0] = 0xAA;
    uint8Array[1] = 0xBB;
    <em>// If read in small order, 0xBBAA will be interpreted as 48042</em>
    <em>// If read in big endian order, 0xAABB will be interpreted as 43707</em>
    return uint16Array[0] === 0xBBAA;
  }


  aboutToAppear() {
    if (this.isLittleEndian()) {
      console.log('Small end');
    } else {
      console.log('Big end');
    }
  }


  build() {
    RelativeContainer() {
      Text(this.message)
        .id('IndexTest')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
