# DECLARE_ERRORNO

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-declare-errorno

错误码及描述注册宏，该宏对外提供如下四个错误码供开发者使用：


 声明如下所示：


```text
DECLARE_ERRORNO(0, 0, SUCCESS, 0);
DECLARE_ERRORNO(0xFF, 0xFF, FAILED, 0xFFFFFFFF);
DECLARE_ERRORNO_COMMON(PARAM_INVALID, 1); // 50331649
DECLARE_ERRORNO(SYSID_FWK, 1, SCOPE_NOT_CHANGED, 201);
```

 开发者可以在“compiler安装目录/latest/compiler/include/register/register_error_codes.h”下查看错误码定义。
