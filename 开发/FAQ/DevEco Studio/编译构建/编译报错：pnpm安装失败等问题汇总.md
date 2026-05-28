# 编译报错：pnpm安装失败等问题汇总

更新时间：2026-04-27 09:10:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195

**问题现象**
 
执行sync或构建命令时，编译报错：“ERROR: 003080xx Operation Error”。
 
常见错误码为：00308019-00308024
 
**背景知识**
 
00308019-00308024错误码为开发者在hvigor-config.json5中新增js包依赖，执行sync或编译时在“Build Init”阶段编译的报错。报错原因为pnpm/npm工具安装包时失败。
 
**场景一：ERROR: 00308019 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308019</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
 ERR_PNPM_FETCH_404  <span style="color: rgb(0,0,255);">GET</span> https://xxx/npm-central-repo/testX:  - <span style="color: rgb(80,160,79);">404</span>
This error happened <span style="color: rgb(0,0,255);">while</span> installing a direct dependency of C:\Users\xxx\.hvigor\project_caches\<span style="color: rgb(80,160,79);">4</span>cfxxx4f5\workspace
testX is not <span style="color: rgb(0,0,255);">in</span> the <span style="color: rgb(0,0,255);">npm</span> registry, or you have no permission to fetch it.
No authorization header was <span style="color: rgb(0,0,255);">set</span> <span style="color: rgb(0,0,255);">for</span> the request.
* Try the following: 
  > Check whether the failed package exists <span style="color: rgb(0,0,255);">in</span> the <span style="color: rgb(0,0,255);">npm</span> repository.
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了形如 testX: '3.3.10'的包，hvigor初始化时调用pnpm工具安装tesXt@3.3.10包，但是在pnpm仓库中找不到匹配的包名testX。常见为包的名称写错，或者pnpm仓库地址配置错误，或者没有权限访问此包。
 
**解决措施：**
 
1、在电脑console控制台上，运行`pnpm view xxx versions`命令查看xxx包在仓库里是否存在。
 
2、请联系xxx包的提供方，明确xxx包的仓库地址，及访问权限，然后修改本地pnpm的配置。
 

 
**场景二：ERROR: 00308020 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308020</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
 ERR_PNPM_NO_MATCHING_VERSION  No matching version found <span style="color: rgb(0,0,255);">for</span> test@<span style="color: rgb(80,160,79);">3.3</span>.<span style="color: rgb(80,160,79);">10</span> <span style="color: rgb(0,0,255);">while</span> fetching it from https://xxx/npm-central-repo/
This error happened <span style="color: rgb(0,0,255);">while</span> installing a direct dependency of C:\Users\xxx\.hvigor\project_caches\<span style="color: rgb(80,160,79);">4</span>cf***<span style="color: rgb(80,160,79);">4</span>f5\workspace
The latest release of test is <span style="color: rgb(255,0,0);">"3.3.0"</span>. Published at <span style="color: rgb(80,160,79);">2023</span>/<span style="color: rgb(80,160,79);">12</span>/<span style="color: rgb(80,160,79);">8</span>
<span style="color: rgb(0,0,255);">If</span> you need the full list of all <span style="color: rgb(80,160,79);">3</span> published versions run <span style="color: rgb(255,0,0);">"$ pnpm view test versions"</span>.
* Try the following: 
  > Check whether the version of the failed package exists <span style="color: rgb(0,0,255);">in</span> the <span style="color: rgb(0,0,255);">npm</span> repository.
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了 test: '3.3.10'的包，hvigor初始化时调用pnpm工具安装test@3.3.10包，但是在pnpm仓库中找不到匹配的版本。常见为包的版本写错，或者pnpm仓库地址配置错误。
 
**解决措施：**
 
1、在电脑console控制台上，运行`pnpm view xxx versions`命令查看xxx包在仓库里的可用版本，使用可用的版本。
 
2、如果要使用的版本在pnpm仓库里不存在，请联系xxx包的提供方，明确xxx包的仓库地址，然后修改本地pnpm的仓库地址。
 

 
**场景三：ERROR: 00308021 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308021</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
WARN  <span style="color: rgb(0,0,255);">GET</span> https://xxx/test error (ETIMEDOUT). Will retry <span style="color: rgb(0,0,255);">in</span> <span style="color: rgb(80,160,79);">10</span> seconds. <span style="color: rgb(80,160,79);">2</span> retries left.
WARN  <span style="color: rgb(0,0,255);">GET</span> https://xxx/test error (ETIMEDOUT). Will retry <span style="color: rgb(0,0,255);">in</span> <span style="color: rgb(80,160,79);">1</span> minute. <span style="color: rgb(80,160,79);">1</span> retries left.
ERR_PNPM_META_FETCH_FAIL  <span style="color: rgb(0,0,255);">GET</span> https://xxx/test: request to https://xxx/test failed, reason: connect ETIMEDOUT xxx.xxx.xxx.xxx:<span style="color: rgb(80,160,79);">443</span>.
This error happened <span style="color: rgb(0,0,255);">while</span> installing a direct dependency of xxx.
* Try the following: 
  > Ensure that the <span style="color: rgb(0,0,255);">npm</span> repository address is accessible.
  > Contact the repository provider or replace the <span style="color: rgb(0,0,255);">npm</span> repository address.
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了test包，hvigor初始化时调用pnpm工具安装test包，但是链接超时在远程仓库中找不到test包的元数据。常见为网络问题，或者pnpm仓库地址配置错误。
 
**解决措施：**
 
1、在电脑console控制台上，运行install命令查看是否可以正常安装。
 
2、请确保仓库地址可以访问，查看npm配置的仓库地址是否正确、是否有防火墙或代理限制等。
 
3、联系仓库提供方确认仓库地址是否可用，或更换新的npm仓库地址。
 

 
**场景四：ERROR: 00308022 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308022</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
ERR_PNPM_NO_OFFLINE_META Failed to resolve test@<span style="color: rgb(80,160,79);">1.2</span>.<span style="color: rgb(80,160,79);">3</span> <span style="color: rgb(0,0,255);">in</span> package mirror xxx.
This error happened <span style="color: rgb(0,0,255);">while</span> installing a direct dependency of xxx.
* Try the following: 
  > Check whether the offline package has been completely downloaded before the migration.
  > Refer to <span style="color: rgb(255,0,0);">'Setting Up the Development Environment Offline'</span>: https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-no-network
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了test包，且使用离线安装模式，pnpm在离线模式下，无法从本地缓存中找到某个依赖包的元数据。常见为包的相关依赖没有打包完整，导致离线环境下无法找到。
 
**解决措施：**
 
1、请检查离线包在迁移前是否已下载完整。
 
2、参考[离线环境配置指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-network)。
 

 
**场景五：ERROR: 00308023 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308023</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
<span style="color: rgb(0,0,255);">npm</span> ERR! code CERT_HAS_EXPIRED
<span style="color: rgb(0,0,255);">npm</span> ERR! errno CERT_HAS_EXPIRED
<span style="color: rgb(0,0,255);">npm</span> ERR! request to https://xxx failed, reason: certificate has expired
<span style="color: rgb(0,0,255);">npm</span> ERR! A complete log of this run can be found <span style="color: rgb(0,0,255);">in</span>: xxx
* Try the following: 
  > Contact the <span style="color: rgb(0,0,255);">npm</span> repository provider to ensure that the certificate of the repository server is valid, or replace the repository address with a new one.
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了test包，但是hvigor初始化构建时，安装依赖时链接npm远程仓库失败。常见为npm仓库服务器证书过期。
 
**解决措施：**
 
请联系仓库提供方确保仓库服务器的证书有效，或更换新的npm仓库地址。
 

 
**场景六：ERROR: 00308024 Operation Error**
 
**报错现象：**
 
```text
> hvigor ERROR: <span style="color: rgb(80,160,79);">00308024</span> Operation Error
Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
<span style="color: rgb(0,0,255);">npm</span> ERR! code ETIMEDOUT
<span style="color: rgb(0,0,255);">npm</span> ERR! errno ETIMEDOUT
<span style="color: rgb(0,0,255);">npm</span> ERR! request to https://xxx failed, reason: connect ETIMEDOUT xxx.xxx.xxx.xxx:<span style="color: rgb(80,160,79);">443</span>
This error happened <span style="color: rgb(0,0,255);">while</span> installing a direct dependency of xxx.
* Try the following: 
  > Ensure that the <span style="color: rgb(0,0,255);">npm</span> repository address is accessible.
  > Contact the repository provider or replace the <span style="color: rgb(0,0,255);">npm</span> repository address.
  > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```
 
**常见原因：**
 
hvigor-config.json5中dependencies字段中配置了test包，但是hvigor初始化构建时，链接npm仓库超时。常见为代理、防火墙限制或npm仓库地址失效等导致无法访问。
 
**解决措施：**
 
1、请确保仓库地址可以访问，查看npm配置的仓库地址是否正确、是否有防火墙或代理限制等。
 
2、联系仓库提供方确认仓库地址是否可用，或更换新的npm仓库地址。
