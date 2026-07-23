# 模拟器工具（Emulator）

更新时间：2026-07-15 09:00:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-emulator

从6.1.0 Release版本开始，Command Line Tools集成Emulator工具，支持Windows和macOS平台，可独立进行模拟器创建、启动、关闭、镜像下载等操作。

从26.0.0 Beta1版本开始，支持在Linux平台上使用Emulator，具体使用方式请参考[使用Linux版本Emulator工具](#section15887175165919)。

> [!NOTE]
> 在macOS上使用命令行工具时，如果弹框提示Emulator无法验证开发者，可以在系统的 设置 > 隐私与安全性 中选择 仍要打开Emulator， 或者使用 DevEco Studio目录下的Emulator工具 。



#### 环境准备

Emulator工具在command-line-tools安装目录的emulator目录下，有两种执行命令的方式。

 - 方式一：在命令行终端中进入emulator目录下，执行命令。
 - 方式二：配置环境变量后，在任意目录下执行命令。       
Windows环境变量设置方法：         在系统或者用户的PATH变量中，添加路径{command-line-tools安装目录}/emulator，配置完成后重新打开命令行窗口使环境变量生效。
 - macOS/Linux环境变量设置方法：         打开命令行终端，执行以下命令。

  
```bash
export PATH={command-line-tools安装目录}/emulator:$PATH
```






#### 模拟器命令

Emulator命令请参考[通过命令行使用模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line)。



#### 在模拟器上推包调试

可通过hdc工具在模拟器上进行推包调试。
1. 使用时需要先确认模拟器和hdc的连接状态，模拟器的IP和端口号是127.0.0.1:5555，如果端口号已经被占用，则从5555起递增2，例如5555、5557、5559，端口号范围在5555-15555之间。       
```bash
hdc list targets
```

2. 如果未连接，执行命令`hdc tconn {IP:端口号}`连接模拟器，例如：       
```bash
hdc tconn 127.0.0.1:5555
```

3. 连接成功后，通过hdc在模拟器上安装、卸载应用等，更多使用方式请参考[SDK命令行工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/command-line-tools-overview)。



#### 使用Linux版本Emulator工具

从26.0.0 Beta1版本开始，支持在Linux平台使用模拟器工具。



#### 环境准备

当前仅支持Ubuntu 18.04及以上的Linux系统，使用前需要安装相关的依赖，以Ubuntu 18.04操作系统为例，执行命令：

```bash
apt install -y libatomic1 libpulse0 libegl1 libgbm1 libgl1 libpng16-16 libfontconfig1 libfreetype6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libsm6 libice6 libxkbcommon-x11-0 libxkbcommon0 libglib2.0-0
```



#### 使用约束

 - Linux模拟器依赖系统kvm能力，需要手动将Emulator程序当前用户加入/dev/kvm所在的组中。
 - Linux模拟器图形渲染依赖/dev/dri下的设备渲染节点，如card0、renderD128等，需要手动将Emulator程序当前用户加入相关节点的用户组中。
 - 如需使用第三方远程桌面工具操作Linux，请确保工具可使用的图形驱动支持OpenGL4.1或以上版本。




#### 模拟器命令差异

针对无图形界面的Linux环境，[启动模拟器命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line#section1986131715236)必须添加-noWindow参数。除此之外，其他命令和Windows/macOS相同，详细命令请参考[通过命令行使用模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line)。



#### 使用远程服务

Linux模拟器提供了对外的gRPC服务，开发者可通过调用模拟器服务接口，远程获取模拟器内的视频流数据、音频流数据，以及远程使用场景化命令和鼠标点击功能。

在使用本文提供的能力之前，开发者需要具备gRPC开发的基础知识。

工作流程如下：


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/lA3bKJEGTo67hkT_YEHwew/zh-cn_image_0000002625074205.png?HW-CC-KV=V1&HW-CC-Date=20260723T012203Z&HW-CC-Expire=86400&HW-CC-Sign=8928C615EB57DCA806445C6D756DBFC106877AD5AC650F9B13D51F7D93D6643D)

1. 开发者需要自行开发本地gRPC客户端。
2. 开发者需要通过本文档提供的模拟器gRPC服务，定义服务接口和消息结构，使用protoc生成规范的接口头文件。
3. 在Linux服务器上以服务器模式启动模拟器，记录token，IP，端口号和认证信息。
4. 通过本地客户端构建包含认证信息的gRPC请求消息，并将所需调用的接口添加进消息中，发送给服务端。
5. 服务端接收消息并响应，返回请求结果。

**启动RPC服务器模式命令**

在Linux服务器上，以gRPC服务器模式启动模拟器，包括无认证模式和认证模式。

如果使用认证模式，启动后在命令执行路径下会生成token文件server_token.txt，其中包含认证所需要的token字段。

```bash
# 无认证模式
Emulator -start {模拟器名称} -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -grpcServer -grpcPort {端口} -noAuth
# 认证模式
Emulator -start {模拟器名称} -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -grpcServer -grpcPort {端口} -pem_root_certs {根证书路径} -pem_private_key {私钥路径} -pem_cert_chain {证书链路径}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -start | 必选参数，指定模拟器名称。 |
| -instancePath | 可选参数，指定模拟器实例路径。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -imageRoot | 可选参数，指定模拟器镜像路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -grpcServer | 必选参数，指定模拟器启动模式为gRPC服务器模式。 |
| -grpcPort | 可选参数，指定服务器的端口号。如果指定，需确保端口号存在且可用，不限范围。如果不指定，默认范围6555-6755，端口冲突情况下，默认端口号累加2，如6555、6557。 |
| -noAuth | 可选参数，使用无认证模式启动。 |
| -pem_root_certs | 可选参数，使用认证模式后必选，指定根证书路径。要求服务端和客户端证书均支持双向认证。 |
| -pem_private_key | 可选参数，使用认证模式后必选，指定私钥路径。 |
| -pem_cert_chain | 可选参数，使用认证模式后必选，指定证书链路径。 |


模拟器提供的gRPC服务如下。



#### VideoStreamService

```text
service VideoStreamService {
    rpc StreamVideo(VideoStreamRequest) returns (stream VideoFrame);
}
```

**描述**：服务端接收客户端视频流请求，请求消息为[VideoStreamRequest](#section19408143512553)。



#### VideoStreamRequest

```text
message VideoStreamRequest {
    int32 screen_index = 0;
}
```

**描述：**客户端请求视频流的请求消息。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screen_index | int32 | 是 | 屏幕索引，用于指定要获取的视频流来源，主屏幕默认为索引0，模拟器多屏模式下0 ~ 3分别对应模拟器的主屏幕和3个副屏幕。 |


**返回值**

| 类型 | 说明 |
| --- | --- |
| VideoFrame | 模拟器视频帧数据 |




#### VideoFrame

模拟器视频帧数据。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| width | int32 | 视频帧宽度（像素） |
| height | int32 | 视频帧高度（像素） |
| timestamp | int64 | 时间戳（微秒） |
| image_data | bytes | 视频帧数据（RAW RGB/NV21格式） |
| display_width | int32 | 显示设备宽度（用于缩放计算） |
| display_height | int32 | 显示设备高度（用于缩放计算） |




#### AudioStreamService

```text
service AudioStreamService {
    rpc StreamAudio(AudioStreamRequest) returns (stream AudioFrame);
}
```

**描述：**服务端接收客户端音频流请求，请求消息为[AudioStreamRequest](#section67501129195615)。



#### AudioStreamRequest

```text
message AudioStreamRequest {
}
```

**描述：**客户端请求音频流的请求消息。

**返回值**

| 类型 | 说明 |
| --- | --- |
| AudioFrame | 模拟器音频帧数据 |




#### AudioFrame

模拟器音频帧数据。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| sample_rate | int32 | 采样率（Hz），如44100、48000 |
| channels | int32 | 声道数，支持以下取值： 1：单声道 2：立体声 |
| format | int32 | 采样格式，支持以下取值： 0：格式为8-bit unsigned，标识符PCM_U8 1：格式为16-bit unsigned，标识符PCM_S16LE 2：格式为32-bit unsigned，标识符PCM_S32LE |
| timestamp | int64 | 时间戳（微秒） |
| audio_data | bytes | 音频数据（PCM 格式） |




#### ScenarioCommandService

```text
service ScenarioCommandService {
    rpc ExecuteCommand(CommandRequest) returns (CommandResponse);
}
```

**描述：**服务端接收执行模拟器命令的请求，请求消息为[CommandRequest](#section298891155819)。



#### CommandRequest

```text
message CommandRequest {
    string command = "";
}
```

**描述：**客户端发送命令的请求消息。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 模拟器场景化命令字符串，支持的命令请参考场景化模拟，如"-volume up"。 |


**返回值**

| 类型 | 说明 |
| --- | --- |
| CommandResponse | 模拟器命令执行结果 |




#### CommandResponse

模拟器命令执行结果。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| success | bool | 命令是否成功执行 |
| message | string | 结果消息或错误信息 |




#### MouseInputService

```text
service MouseInputService {
    rpc SendMouseEvent(MouseInputRequest) returns (MouseInputResponse);
}
```

**描述：**客户端发送鼠标事件到模拟器，请求消息为[MouseInputRequest](#section161605235598)。



#### MouseInputRequest

```text
message MouseInputRequest {
    int32 x = 1;
    int32 y = 2;
    int32 button = 3;
    int32 event_type = 4;
    int32 wheel_delta = 5;
    int32 screen_index = 0;
}
```

**描述：**客户端发送鼠标事件的请求消息。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | int32 | 是 | 鼠标X坐标，表示模拟器屏幕横坐标，以模拟器屏幕左上角为原点(0,0)。 多屏状态下每个屏幕坐标独立，以每个屏幕左上角为原点(0,0)。 通过屏幕索引screen_index区分屏幕。 横坐标以模拟器宽度(px)为范围，如果坐标点超出屏幕范围，无法执行。 |
| y | int32 | 是 | 鼠标Y坐标，表示模拟器屏幕纵坐标，以模拟器屏幕左上角为原点(0,0)。 多屏状态下每个屏幕坐标独立，以每个屏幕左上角为原点(0,0)。 通过屏幕索引screen_index区分屏幕。 纵坐标以模拟器高度(px)为范围，如果坐标点超出屏幕范围，无法执行。 |
| button | int32 | 是 | 按钮类型，支持以下类型： 0：表示无按钮 1：表示鼠标左键 2：表示鼠标右键 3：表示鼠标中键 |
| event_type | int32 | 是 | 事件类型，支持以下取值： 0：表示鼠标移动 1：表示按下鼠标 2：表示释放鼠标 3：表示鼠标滚轮 |
| wheel_delta | int32 | 是 | 滚轮滚动量 |
| screen_index | int32 | 是 | 屏幕索引，主屏幕为索引0，模拟器多屏模式下0 ~ 3分别对应模拟器的主屏幕和3个副屏幕。 |


**返回值**

| 类型 | 说明 |
| --- | --- |
| MouseInputResponse | 鼠标事件执行结果 |




#### MouseInputResponse

鼠标事件执行结果。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| success | bool | 事件是否成功执行 |
| message | string | 结果消息或错误信息 |




#### 示例代码

> [!NOTE]
> 以下示例无法直接运行，仅供参考。


开发者需要自行开发本地客户端。通过模拟器提供的gRPC服务，对指定模拟器进行远程操控。示例如下。
1. 在远端Linux服务器上执行命令，启动模拟器作为服务器。       
```bash
Emulator -start "myEmulator" -instancePath /path/to/instance -imageRoot /path/to/image -grpcServer -grpcPort 6555 -pem_root_certs /path/to/root.pem -pem_private_key /path/to/client.key -pem_cert_chain /path/to/client.pem
```

2. 开发本地客户端，通过服务器的IP和端口号以及认证方式，对模拟器服务器进行请求。       生成protobuf消息定义代码：

  
```text
# emulator_server.proto文件，用于生成protobuf消息定义
message VideoStreamRequest {
    int32 screen_index = 1;
}

message VideoFrame {
    int32 width = 1;
    int32 height = 2;
    int64 timestamp = 3;
    bytes image_data = 4;
    int32 display_width = 5;
    int32 display_height = 6;
}

message AudioStreamRequest {
}

message AudioFrame {
    int32 sample_rate = 1;
    int32 channels = 2;
    int32 format = 3;
    int64 timestamp = 4;
    bytes audio_data = 5;
}

message CommandRequest {
    string command = 1;
}

message CommandResponse {
    bool success = 1;
    string message = 2;
}

message MouseInputRequest {
    int32 x = 1;
    int32 y = 2;
    int32 button = 3;
    int32 event_type = 4;
    int32 wheel_delta = 5;
    int32 screen_index = 0;
}

message MouseInputResponse {
    bool success = 1;
    string message = 2;
}

service ScenarioCommandService {
    rpc ExecuteCommand(CommandRequest) returns (CommandResponse);
}

service MouseInputService {
    rpc SendMouseEvent(MouseInputRequest) returns (MouseInputResponse);
}

service VideoStreamService {
    rpc StreamVideo(VideoStreamRequest) returns (stream VideoFrame);
}

service AudioStreamService {
    rpc StreamAudio(AudioStreamRequest) returns (stream AudioFrame);
}
```


  开发本地客户端，发送gRPC请求给服务端。        
```text
# Token + TLS 双向认证模式
#!/usr/bin/env python3
# 导入必要的gRPC库和生成的protobuf代码
import grpc
import emulator_server_pb2
import emulator_server_pb2_grpc

# 服务器地址和认证token
SERVER_ADDR = "10.100.10.10:65555"
AUTH_TOKEN = "your_token_here"

# 读取证书私钥等信息，创建认证凭证
def create_channel():
    with open("./certs/ca.crt", 'rb') as f:
        ca_cert = f.read()
    with open("./certs/client.crt", 'rb') as f:
        client_cert = f.read()
    with open("./certs/client.key", 'rb') as f:
        client_key = f.read()

    # 创建凭证
    creds = grpc.ssl_channel_credentials(
        root_certificates=ca_cert,
        private_key=client_key,
        certificate_chain=client_cert
    )

    return grpc.secure_channel(
        SERVER_ADDR,
        creds,
        options=[
            ('grpc.max_receive_message_length', 16 * 1024 * 1024),
            ('grpc.max_send_message_length', 16 * 1024 * 1024),
        ]
    )

def main():
    channel = create_channel()
    metadata = [('authorization', f'Bearer {AUTH_TOKEN}')]

    # VideoStreamService示例
    # 创建命令服务
    video_stub = emulator_server_pb2_grpc.VideoStreamServiceStub(channel)
    for frame in video_stub.StreamVideo(
            # 请求视频流的请求消息
            emulator_server_pb2.VideoStreamRequest(screen_index=0),
            # 设置请求超时时间
            timeout=30,
            # 包含认证token的数据
            metadata=metadata):
        print(f"Video: {frame.width}x{frame.height}")
        break

    # ScenarioCommandService示例
    # 创建命令服务
    cmd_stub = emulator_server_pb2_grpc.ScenarioCommandServiceStub(channel)
    response = cmd_stub.ExecuteCommand(
        # 请求命令的请求消息
        emulator_server_pb2.CommandRequest(command="-volume up"),
        # 设置请求超时时间
        timeout=30,
        # 包含认证token的数据
        metadata=metadata)
    print(f"Command: {response.success}")
    channel.close()

if __name__ == "__main__":
    main()
```
