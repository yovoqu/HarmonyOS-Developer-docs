# 配置useNormalizedOHMUrl为true模式下常见错误

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-202

#### 问题现象

定义strictMode严格模式后，将useNormalizedOHMUrl设置为true，调用系统方法时会抛出异常。
 
```json
<span style="color: rgb(80,160,79);">"buildOption"</span><span style="color: rgb(181,106,1);">: </span>{
  <span style="color: rgb(80,160,79);">"strictMode"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(80,160,79);">"useNormalizedOHMUrl"</span><span style="color: rgb(181,106,1);">: true</span>
  }
}
```
 
报错信息如下：
 
```text
<span style="color: rgb(0,0,255);">startLivenessDetectCall init</span>
<span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">07 16</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">30.577 64714</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">64714 </span><span style="color: rgb(0,0,255);">C01201</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotm</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">EventHandler com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotma</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">iness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm I </span><span style="color: rgb(181,106,1);">~</span><span style="color: rgb(0,0,255);">EventHandler enter </span><span style="color: rgb(255,0,0);">35_74526985950083</span>
<span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">07 16</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">30.577 64714</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">64714 </span><span style="color: rgb(0,0,255);">C03900</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hot</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">siness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">Ace com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotma</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">iness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm I </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">page_router_manager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cpp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1201</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100000</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">100000</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">scope</span><span style="color: rgb(0,0,255);">)] </span><span style="color: rgb(0,0,255);">Page router manager is loading page</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(181,106,1);">bundle</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">huawei</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hmsapp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hiai</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hsp</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">interactivelivenessHsp</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">ets</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">pages</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">InteractivelivenessAbilityPage</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">07 16</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">30.577 64714</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">64714 </span><span style="color: rgb(0,0,255);">C03F00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hot</span><span style="color: rgb(181,106,1);">...</span>m<span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">ArkCompiler com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotma</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">iness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm I </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">ecmascript</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(0,0,255);">Get Pkg Name failed</span>
<span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">07 16</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">30.578 64714</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">64714 </span><span style="color: rgb(0,0,255);">C03F00</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hot</span><span style="color: rgb(181,106,1);">...</span>m<span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">ArkCompiler com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotma</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">iness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm E </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">ecmascript</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(0,0,255);">Cannot execute ark file </span><span style="color: rgb(255,0,170);">'@bundle:com.huawei.hmsapp.hiai.hsp/interactivelivenessHsp/ets/pages/InteractivelivenessAbilityPage.abc' </span>with <span style="color: rgb(0,0,255);">entry </span><span style="color: rgb(255,0,170);">'_GLOBAL::func_main_0'</span>
<span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">07 16</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">09</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">30.578 64714</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,0,0);">64714 </span><span style="color: rgb(0,0,255);">C03900</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hot</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">siness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">Ace com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hotma</span><span style="color: rgb(181,106,1);">...</span><span style="color: rgb(0,0,255);">iness</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hm W </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">jsi_declarative_engine</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cpp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1692</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100000</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">100000</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">scope</span><span style="color: rgb(0,0,255);">)] </span><span style="color: rgb(0,0,255);">page not found</span><span style="color: rgb(181,106,1);">! </span><span style="color: rgb(181,106,1);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">com</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">huawei</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hmsapp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hiai</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hsp</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">moduleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">interactivelivenessHsp</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">pages</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">InteractivelivenessAbilityPage</span>
```
 
 

#### 背景知识

- [strictMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312)用于定义严格模式。其useNormalizedOHMUrl字段表示是否使用标准化的OHMUrl格式，标准化的OHMUrl统一了原有OHMUrl的格式。使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式。
- 若工程引用了HAR/HSP，需确保工程的useNormalizedOHMUrl配置和HAR/HSP的useNormalizedOHMUrl配置保持一致，同时配置为true或false。
- 当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致。

 
 

#### 问题定位
1. 查看工程里所有的OHMUrl格式需统一。
2. 验证导入文件名大小写及路径配置是否正确。
3. 检查导入三方库名称是否一致。
 
 

#### 分析结论

在配置文件build-profile.json5中，设置strictMode字段，并将useNormalizedOHMUrl配置为true，主要目的是为了避免因URL处理方式不一致而导致的编译错误或运行时问题，确保应用的稳定性和安全性。
 
 

#### 修改建议
1. 启用[严格模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312)。
2. 确保导入文件的大小写与路径完全匹配。
3. 检查并调整导入文件的路径和大小写格式，以确保其符合严格模式的要求。
 
 

#### 常见FAQ

Q：配置useNormalizedOHMUrl为true后依赖报错：
 
```text
<span style="color: rgb(0,0,255);">This dependency alias does not match the package name</span><span style="color: rgb(181,106,1);">. </span><span style="color: rgb(0,0,255);">Change it to </span><span style="color: rgb(255,0,170);">'XXX'</span><span style="color: rgb(181,106,1);">.</span>
```
 
A：useNormalizedOHMUrl设置为true时，强制要求依赖引用的别名必须与模块的实际名称保持一致。
