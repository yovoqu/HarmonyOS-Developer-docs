# 模型（Model）配置

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model

CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。


#### 操作步骤
1. 点击界面右上方
![](assets/模型（Model）配置/file-20260514132759917-0.png)
按钮，或者点击界面右上方**Settings**
![](assets/模型（Model）配置/file-20260514132759917-1.png)
按钮，选择**Model**，进入配置页面。

  
![](assets/模型（Model）配置/file-20260514132759917-2.png)

2. 点击
![](assets/模型（Model）配置/file-20260514132759917-3.png)
按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加，推荐使用Service Provider方式。

  
 - 通过服务提供商添加。CodeGenie已预置主流模型服务商的配置信息，填写API Key即可快速接入。

  填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。          
**Name**：模型名称。

3. **Provider**：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。

4. **API Key**：模型的访问密钥，在提供商网站申请。

5. **Model**：模型的标识。

6. 通过URL添加。

  填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。          
**Name**：模型名称。

7. **Url**：模型的访问地址。

8. **Protocol**：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。

9. **API Key**：模型的访问密钥，在提供商网站申请。

10. **Model**：模型的标识。

11. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

  
![](assets/模型（Model）配置/file-20260525091725481-001.png)


  

  #### 附录

  

  #### 通过URL添加模型

  **约束与限制**

  
暂不支持开启深度思考（Deep Thinking）功能和多模态图片处理功能。


**配置说明**

 - 代理配置：为了避免代理问题造成的请求超时，将内网模型服务域名添加到[HTTP代理的No proxy for](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config#section10369436568)中。
 - URL：填写URL时，若URL中包含"/chat/completions"后缀，请删除该部分，CodeGenie在请求时会自动拼接。示例如下：       
原URL： https://api.deepseek.com/chat/completions
 - 填写为： https://api.deepseek.com

      - API Key：填写模型的访问密钥时不需要添加"Bearer"前缀。示例如下：       
原API Key：Bearer sk-f9e98c******8
 - 填写为：sk-f9e98c******8



**配置示例**

 - 添加本地Ollama部署的模型       
![](assets/模型（Model）配置/file-20260525091725482-002.png)



 - 添加DeepSeek模型（OpenAI协议）       
![](assets/模型（Model）配置/file-20260525091725482-003.png)

 - 添加DeepSeek模型（Anthropic协议）       
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/RgfZfegHRDePlwpQ0h0cJQ/zh-cn_image_0000002594634610.png?HW-CC-KV=V1&HW-CC-Date=20260624T020708Z&HW-CC-Expire=86400&HW-CC-Sign=EBD7FE10F5DF6597996642B175E5CA4DFEA958D5F6D167C51B98264654C882EA)
