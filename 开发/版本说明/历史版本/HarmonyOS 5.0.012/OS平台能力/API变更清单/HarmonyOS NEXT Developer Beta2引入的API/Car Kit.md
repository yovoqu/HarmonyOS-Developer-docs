# Car Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：SystemNavigationListener； API声明：onQueryNavigationInfo(query: QueryType, args: {  [key: string]: object;  }): Promise<ResultData>; 差异内容：args: {  [key: string]: object;  } | 类名：SystemNavigationListener； API声明：onQueryNavigationInfo(query: QueryType, args: Record<string, Object>): Promise<ResultData>; 差异内容：args: Record<string, Object> | api/@hms.carService.navigationInfoMgr.d.ts |
| 函数变更 | 类名：SystemNavigationListener； API声明：onReceiveNavigationCmd(command: CommandType, args: {  [key: string]: object;  }): Promise<ResultData>; 差异内容：args: {  [key: string]: object;  } | 类名：SystemNavigationListener； API声明：onReceiveNavigationCmd(command: CommandType, args: Record<string, Object>): Promise<ResultData>; 差异内容：args: Record<string, Object> | api/@hms.carService.navigationInfoMgr.d.ts |
