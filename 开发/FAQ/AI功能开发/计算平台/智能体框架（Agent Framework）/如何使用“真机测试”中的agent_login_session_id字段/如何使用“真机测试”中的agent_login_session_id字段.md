# 如何使用“真机测试”中的agent_login_session_id字段

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-4

#### 问题现象

小艺开放平台创建智能体后，使用“真机测试”，工作流插件运行时，没有看到系统变量字段agent_login_session_id，如何解决？
 
 

#### 解决方案

agent_login_session_id是智能体登录后才能使用，不会在开发阶段显示。当智能体正式发布或者真机调试时，且用户在真机上使用时默认生成。
