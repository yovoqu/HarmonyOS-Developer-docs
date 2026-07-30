# 应用包无法上传到AGC怎么办，是否网络限制

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-72

#### 问题现象

打包好的软件包上传到AGC速度非常慢，是否做了上传限制带宽，公司网络基本无法上传，使用个人家庭网络上传才可以。
 
 

#### 解决方案

在应用市场上传过程中，华为应用市场本身未明确对网络或带宽进行限制。上传失败常见原因有：
 1. 公司网络进行了网速限制。咨询公司IT人员进行网络环境排查，是否设有防火墙、流量管控或上传带宽限制策略等，如果有会导致大文件上传受阻。
2. 网络是否进行了代理等VPN环境设置。如果有，建议断开VPN代理后再尝试上传，尝试切换网络（如手机热点）验证是否为网络VPN问题。
3. 软件包上传完成后系统也会进行软件包解析，应用包的检测耗时会随着检测项目数量的增加而相应延长。通常情况下，检测时间在10分钟内完成属于正常范围。可以继续等待解析结果，或者切换其他页面后在“软件包管理”菜单查看解析报告。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ZC94ZuQ7Siy1lGGBxjCUJg/zh-cn_image_0000002628394630.png?HW-CC-KV=V1&HW-CC-Date=20260730T072702Z&HW-CC-Expire=86400&HW-CC-Sign=B3EDDB33505685BB2EA7A5BC6277A0AF4300C34023F8F065CE0CC8D0EAF4AA5F)
