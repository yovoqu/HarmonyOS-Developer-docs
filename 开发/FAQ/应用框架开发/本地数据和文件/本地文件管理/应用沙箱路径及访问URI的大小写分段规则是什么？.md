# 应用沙箱路径及访问URI的大小写分段规则是什么？

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-49

## 应用沙箱路径及访问URI的大小写分段规则是什么？ 
 

**问题描述**
 
应用沙箱路径及访问URI的大小写分段规则是什么？
 
**解决措施**
 
在应用沙箱路径和URI中，常用目录名和文件名的大小写敏感规则如下表：
 
一、大小写不敏感目录
  
| path | URI | 当前目录及子目录是否不敏感 |
| --- | --- | --- |
| /storage/Users/currentUser/Download | file://docs/storage/Users/currentUser/Download | 是 |
| /storage/Users/currentUser/Documents | file://docs/storage/Users/currentUser/Documents | 是 |
| /storage/Users/currentUser/Desktop | file://docs/storage/Users/currentUser/Desktop | 是 |
| /data/storage/el2/distributedfiles/&lt;bundleName&gt; | file://&lt;bundleName&gt;/data/storage/el2/distributedfiles/&lt;bundleName&gt; | 是 |
| /data/storage/el2/cloud/&lt;bundleName&gt; | file://&lt;bundleName&gt;/data/storage/el2/distributedfiles/&lt;bundleName&gt; | 是 |
 
 
二、大小写敏感目录
  
| path | URI | 当前目录及子目录是否敏感 |
| --- | --- | --- |
| /storage/Users/currentUser | file://docs//storage/Users/currentUser | 是 |
| /data/storage/el1/base | file://&lt;bundleName&gt;/data/storage/el1/base | 是 |
| /data/storage/el1/database | file://&lt;bundleName&gt;/data/storage/el1/database | 是 |
| /data/storage/el2/base | file://&lt;bundleName&gt;/data/storage/el2/base | 是 |
| /data/storage/el2/cloud | file://&lt;bundleName&gt;/data/storage/el2/cloud | 否 |
| /data/storage/el2/database | file://&lt;bundleName&gt;/data/storage/el2/database | 是 |
 
 
**例1**：/storage/Users/currentUser/Download/AAA/BBB目录大小写分段规则如下。
  
| 目录层级 | 是否大小写敏感 |
| --- | --- |
| storage | 敏感 |
| Users | 敏感 |
| currentUser | 敏感 |
| Download | 不敏感 |
| AAA | 不敏感 |
| BBB | 不敏感 |
