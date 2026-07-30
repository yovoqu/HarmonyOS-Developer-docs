# 使用zlib解压buffer，如何动态设置目标缓冲区的数据长度

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-28

#### 问题现象

使用zlib进行解压，在数据解压完成前无法确定目标缓冲区需要的空间大小，所以目标缓冲区需要提前预设值，而目标缓冲区完成设置后，如果初始化长度不够，将会导致代码抛出异常。目标缓冲区的空间是否可以动态增加，边解压边增加目标缓冲区的空间呢？
 
 

#### 背景知识

- zlib内部流解压API文档：[inflate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib#inflate12)。
- zlib压缩ArrayBuffer的API文档：[compress2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib#compress212)。
- zlib解压ArrayBuffer的API文档：[uncompress2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib#uncompress212)。

 
 

#### 解决方案
1. 压缩的ArrayBuffer转成内部流的方式进行解压。
2. 将解压的流，循环每次只转换为一个固定大小的ArrayBuffer，并将此ArrayBuffer作为元素添加到一个输出的数组对象，下次循环以前一次结束位置作为新起点的平移量重新执行下一次转换。
3. ArrayBuffer数组对象元素按顺序循环合并为一个最终输出的Uint8Array对象。
4. 参考示意图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/hSFCxI4yQg-BuMevMxqXmA/zh-cn_image_0000002628613904.png?HW-CC-KV=V1&HW-CC-Date=20260701T041417Z&HW-CC-Expire=86400&HW-CC-Sign=707EA2A276EA2868DB0F648DE50EF62492A95A662D2D6820AC86867272E60C8D)

 
- **核心解压逻辑：**
inBuf：ArrayBuffer转strm：zlib.ZStream，每次的大小为readLen。
- 循环->BUFLEN计算stream的偏移量，作为起点继续下一个截取的stream转换[循环->(用BUFLEN大小的outBuf：ArrayBuffer缓冲目标区去接收分割后的stream)]。
- 判断当前的stream是否为最后的一个，如果是结束循环。

 
 
完整示例参考如下：
 
```json
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError, zlib } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

<em>/**</em>
<em> * 解压逻辑</em>
<em> * (1) inBuf：ArrayBuffer转 strm：zlib.ZStream 每次的大小为 let readLen = Math.min(BUFLEN, inBuf.byteLength - offset)</em>
<em> * 循环-> BUFLEN计算stream的偏移量，作为起点继续下一个截取的stream转换  [循环->(用BUFLEN大小的outBuf：ArrayBuffer缓冲目标区去接收分割后的stream]</em>
<em> * (3) 计算stream的偏移量，作为起点继续下一个截取的stream转换</em>
<em> * (4) 判断当前的stream是否为最后的一个，如果是结束循环</em>
<em> */</em>
async function unzip(inBuf: ArrayBuffer) {

  let zip = zlib.createZipSync();
<em>  // 将压缩后的arrayBuffer解压的正确姿势</em>
  let strm: zlib.ZStream = {};
  let BUFLEN = 4096;
  let count = inBuf.byteLength / BUFLEN;
  if (count > 1) {
    BUFLEN *= count;
  }

  let outBuf = new ArrayBuffer(BUFLEN);
  let output: ArrayBuffer[] = []; <em>// </em><em>用于存储解压后的数据</em>

  await zip.inflateInit(strm);
  let offset = 0; <em>// 用于跟踪读取的字节数</em>
  do {
    let readLen = Math.min(BUFLEN, inBuf.byteLength - offset);
    if (readLen <= 0) {
      break;
    }

    strm.availableIn = readLen;
    strm.nextIn = inBuf.slice(offset, offset + readLen);
    offset += readLen; <em>// 更新偏移量</em>

    do {
      strm.availableOut = BUFLEN;
      strm.nextOut = outBuf;<em> </em><em>// 压缩后的输出字节</em>

      try {
        await zip.inflate(strm, zlib.CompressFlushMode.SYNC_FLUSH);
        let innerStrm = zip.getZStream();
        strm.availableIn = (await innerStrm).availableIn;
        strm.nextIn = (await innerStrm).nextIn;
        strm.availableOut = (await innerStrm).availableOut;
        strm.nextOut = (await innerStrm).nextOut;
        strm.totalIn = (await innerStrm).totalIn;
        strm.totalOut = (await innerStrm).totalOut;

        if (strm.availableOut != undefined) {
          let have = BUFLEN - strm.availableOut;
          if (have > 0) {
        <em>    // 将解压后的数据存储到output数组中</em>
            output.push(outBuf.slice(0, have));
          }
        }
      } catch (err) {
        hilog.error(DOMAIN, 'testZip', JSON.stringify(err, null, 2));
      }
    } while (strm.availableOut == 0);
  } while (strm.availableIn! > 0 || strm.availableOut! > 0);

  zip.inflateEnd(strm);

<em>  // 将output数组中的Uint8Array合并为一个单一的Uint8Array</em>
  let totalLength = output.reduce((acc, val) => acc + val.byteLength, 0);
<em>  // 解压后的buff</em>
  let result = new Uint8Array(totalLength);
  let pos = 0;
  for (let arr of output) {
  <em>  // 将ArrayBuffer转换为Uint8Array</em>
    let u = new Uint8Array(arr);
  <em>  // 将解压后的数据写入result</em>
    result.set(u, pos);
  <em>  // 更新位置</em>
    pos += u.byteLength;
  }

<em>  // 转回string检测结果正确</em>
  hilog.info(DOMAIN, 'testZip', `解压后的数据：${uint8ArrayToString(result)}`);
}

<em>/**</em>
<em> * Uint8Array转string</em>
<em> */</em>
function uint8ArrayToString(arr: Uint8Array): string {
  let str = '';
  if (arr && arr.length > 0) {
    try {
      let textDecode = util.TextDecoder.create('utf-8');
      str = textDecode.decodeToString(arr);
    } catch (err) {
      hilog.error(DOMAIN, 'testZip', JSON.stringify(err, null, 2));
    }
  }
  return str;
}
<em>/**</em>
<em> * 压缩逻辑</em>
<em> */</em>
function zip(str: string): ArrayBuffer {
  const enc = util.TextEncoder.create('utf-8');
  const u8 = enc.encodeInto(str); // Uint8Array
  const arrayBufferIn = u8.buffer.slice(u8.byteOffset, u8.byteOffset + u8.byteLength);
 <em> // arrayBufferOut长度必须足够，否则会抛出异常</em>
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();

  zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then(() => {
    hilog.info(DOMAIN, 'testZip', 'compress2 success');
  }).catch((errData: BusinessError) => {
    hilog.error(DOMAIN, 'testZip', `errData is errCode:${errData.code}  message:${errData.message}`);
  });
  return arrayBufferOut;
}

@Entry
@Component
struct ZlibTest {
  aboutToAppear(): void {
   <em> // 仅作功能展示，用户可根据实际填写</em>
    let zipStr = '英文ABCdef中文123456字符，。、,./;';
    hilog.info(DOMAIN, 'testZip', `待压缩数据：${zipStr}`);
    hilog.info(DOMAIN, 'testZip', '开始压缩');
    let zipArrayBuffer: ArrayBuffer = zip(zipStr);
    hilog.info(DOMAIN, 'testZip', '开始解压缩');
    unzip(zipArrayBuffer);
  }

  build() {
    Column() {
      Text('Hello World')
        .position({ x: '50%', y: '50%' })
        .translate({ x: '-50%', y: '-50%' });
    };
  }
}
```
