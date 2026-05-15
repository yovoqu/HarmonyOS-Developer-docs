# fileIo.write返回的长度和本身content长度不一致

更新时间：2026-04-27 09:10:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-39

fileIo.write返回的是实际写入的数据长度，单位字节。String.length返回的是字符串的长度，两者返回的单位不一样，所以在比较长度时也是不一致的。String.length返回UTF-16编码单元数，当字符串包含非ASCII字符时，其字节长度可能大于该值（如中文通常占3字节）。

参考文档：fileIo.write
