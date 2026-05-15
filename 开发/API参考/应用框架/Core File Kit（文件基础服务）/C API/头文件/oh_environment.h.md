# oh_environment.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-environment-h
**支持设备：** PC/2in1


## 概述
**支持设备：** PC/2in1

environment模块接口定义，使用environment提供的native接口，获取公共文件根目录的沙箱路径。

**引用文件：** <filemanagement/environment/oh_environment.h>

**库：** libohenvironment.so

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**起始版本：** 12

**相关模块：** [Environment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-environment)


## 汇总
**支持设备：** PC/2in1


### 函数
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| [FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)](#oh_environment_getuserdownloaddir) | 获取Download根目录沙箱路径。 |
| [FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)](#oh_environment_getuserdesktopdir) | 获取Desktop根目录沙箱路径。 |
| [FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)](#oh_environment_getuserdocumentdir) | 获取Document根目录沙箱路径。 |


## 函数说明
**支持设备：** PC/2in1


### OH_Environment_GetUserDownloadDir()
**支持设备：** PC/2in1


```text
FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)
```

**描述**

获取Download根目录沙箱路径。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| char **result | Download根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |


### OH_Environment_GetUserDesktopDir()
**支持设备：** PC/2in1


```text
FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)
```

**描述**

获取Desktop根目录沙箱路径。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| char **result | Desktop根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |


### OH_Environment_GetUserDocumentDir()
**支持设备：** PC/2in1


```text
FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)
```

**描述**

获取Document根目录沙箱路径。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| char **result | Document根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |
