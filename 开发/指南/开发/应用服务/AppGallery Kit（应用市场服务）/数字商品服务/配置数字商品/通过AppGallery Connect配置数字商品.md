# 通过AppGallery Connect配置数字商品

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-product-agc

您可以通过华为数字商品管理系统将您的数字商品信息托管在华为侧，方便您的商品价格国际化管理，助力您的应用进行全球化推广。开发者需要在AppGallery Connect中提前录入商品信息（包括商品ID、商品类型、不同国家的商品价格、商品名称等），在客户端调用购买接口时，只需传入此处配置的商品ID和商品类型，系统会根据用户当前的账号服务地展示对应国家/地区的商品信息（包括商品价格、商品名称等），而无需开发者自行管理商品价格。


在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)完成商品配置后，AppGallery Connect不会跟随汇率实时刷新商品价格，开发者需要定期[手动刷新价格](https://developer.huawei.com/consumer/cn/doc/app/single-0000001931995708)，在商品的价格编辑页面点击刷新并保存，即可根据当时的汇率刷新商品价格。
