# 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6

**问题现象**
 
通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：
 
- app日志提示“"state":65”

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/vuY3qud_Q8ulOGLJ1I2iIQ/zh-cn_image_0000002581434976.png?HW-CC-KV=V1&HW-CC-Date=20260528T030049Z&HW-CC-Expire=86400&HW-CC-Sign=3A46F777EA8CA5EB262CFA43A266759BE278CF4CA0959FEE382C11CE763D979C)

- upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/9745RJqJRpy6MbMJCj0apg/zh-cn_image_0000002611834807.png?HW-CC-KV=V1&HW-CC-Date=20260528T030049Z&HW-CC-Expire=86400&HW-CC-Sign=362740172A20DF9170AA039B583F0A54E81362866EBD1CB43F3D7CB8CD0413C3)


 
**解决措施**
 
出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。
 
请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
