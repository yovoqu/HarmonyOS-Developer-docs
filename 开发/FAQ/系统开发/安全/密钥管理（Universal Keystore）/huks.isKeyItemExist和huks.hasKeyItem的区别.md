# huks.isKeyItemExist和huks.hasKeyItem的区别

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-12

[huks.isKeyItemExist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksiskeyitemexist9)：若密钥存在，data为true，若密钥不存在，则error中会输出密钥不存在的error code。开发者需要通过错误码判断密钥不存在，不符合逻辑习惯。建议使用hasKeyItem接口。
 
[huks.hasKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#hukshaskeyitem11)：若密钥存在，返回值为true，若密钥不存在，返回值为false。
