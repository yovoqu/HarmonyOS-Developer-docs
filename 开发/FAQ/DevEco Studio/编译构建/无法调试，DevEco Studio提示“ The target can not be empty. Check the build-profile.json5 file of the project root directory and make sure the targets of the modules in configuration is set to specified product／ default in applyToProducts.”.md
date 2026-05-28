# 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-43

**问题现象**
 

![](assets/无法调试，DevEco%20Studio提示“%20The%20target%20can%20not%20be%20empty.%20Check%20the%20build-profile.json5%20file%20of%20the%20project%20root%20directory%20and%20make%20sure%20the%20targets%20of%20the%20modules%20in%20configuration%20is%20set%20to%20specified%20product／%20default%20in%20applyToProducts.”/file-20260515130112968-0.png)

 
**问题分析**
 
报该错误，可能是build-profile.json5文件中未添加“targets”配置，Module Target下为空，工程同步失败。
 

![](assets/无法调试，DevEco%20Studio提示“%20The%20target%20can%20not%20be%20empty.%20Check%20the%20build-profile.json5%20file%20of%20the%20project%20root%20directory%20and%20make%20sure%20the%20targets%20of%20the%20modules%20in%20configuration%20is%20set%20to%20specified%20product／%20default%20in%20applyToProducts.”/file-20260515130112968-1.png)

 
**解决措施**
 
需要在模块级build-profile.json5文件中添加“targets”配置，点击“Sync Now”，待完成同步后，即可解决该问题（确保工程同步成功）。具体配置如图所示：
 

![](assets/无法调试，DevEco%20Studio提示“%20The%20target%20can%20not%20be%20empty.%20Check%20the%20build-profile.json5%20file%20of%20the%20project%20root%20directory%20and%20make%20sure%20the%20targets%20of%20the%20modules%20in%20configuration%20is%20set%20to%20specified%20product／%20default%20in%20applyToProducts.”/file-20260515130112968-2.png)
