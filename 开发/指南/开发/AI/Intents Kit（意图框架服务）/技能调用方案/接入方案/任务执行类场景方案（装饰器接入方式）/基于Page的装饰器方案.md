# 基于Page的装饰器方案

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-page

#### 概述

开发者使用@InsightIntentPage装饰器进行基于Page的意图声明，可快速将已有的Navigation页面接入意图框架，实现功能页面的拉起。
 
  

#### 约束说明

- 仅支持Navigation页面架构跳转。
- 该跳转不能有自定义上下文依赖，比如必须打开前置页面才能跳转，开发者需要进行验证，确认兜底策略。
- 跳转页面时，默认使用Navigation页面栈进行push，如果开发者需要实现其他跳转逻辑，则需要自行适配。

 
  

#### 开发示例

以购买电影票的意图为例，详细说明如下：
 1. 装饰器添加位置：基于Page的装饰器需要添加在Entry页面组件上，建议在目标页面中进行声明。

  
```text
import { InsightIntentPage } from '@kit.AbilityKit';

@Builder
export function purchaseMovieTicketsIntentPageBuilder(pageName: string, param: object) {
  PurchaseMovieTicketsIntentPage({ param: param });
}

@InsightIntentPage({
  intentName: 'PurchaseMovieTickets',
  domain: 'PurchaseTickets',
  intentVersion: '1.0.1',
  displayName: '购买电影票',
  llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
  uiAbility: 'EntryAbility',
  pagePath: './ets/pages/MainPage',
  navDestinationName: 'PurchaseMovieTicketsIntentPage',
  parameters: {
    'type': 'object',
    'properties': {
      'cinema': {
        'type': 'string',
        'description': '目标影院名称，仅支持平台合作的影院'
      },
      'film': {
        'type': 'string',
        'description': '目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影'
      },
      'time': {
        'type': 'string',
        'description': '放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为\'YYYY-MM-DD HH:MM\'（例如\'2025-07-01 19:30\'）'
      }
    },
    'required': ['cinema', 'film', 'time']
  }
})
@Entry
@Component
struct PurchaseMovieTicketsIntentPage {
  param: object = new Object();
  cinema: string = '';
  film: string = '';
  time: string = '';
  aboutToAppear(): void {
    this.cinema = this.param?.['cinema'];
    this.film = this.param?.['film'];
    this.time = this.param?.['time'];
  }
  build() {
    NavDestination(){
      Text(`${this.cinema} ${this.film} ${this.time}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bolder)
    }
    .title('IntentPage')
    .width('100%')
  }
}
```

2. 装饰器的字段说明以及示例：@InsightIntentPage字段以及具体说明如下。

| 字段名称 | 类型 | 必选 | 说明 |

| --- | --- | --- | --- |

| intentName | string | 是 | 意图名称，最大长度：64。 |

| domain | string | 是 | 意图所属的功能垂域。 |

| intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |

| displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |

| llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用。 |

| parameters | Record<string, object> | 否 | 意图参数定义，描述参数类型以及含义。 |

| uiAbility | string | 否 | 页面依赖的UiAbility名，如果不传递默认使用EntryAbility。 |

| pagePath | string | 是 | Navigation组件所在页面的路径，路径基于Module的根目录的相对路径。 |

| navDestinationName | string | 否 | Navigation子页面名称，如果不填写，则跳转到pagePath指定的页面。 |

  为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-specification)。
3. 装饰器的添加方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下。

  
- 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie#section18337533718)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/COt4ugH7TXmR2y8oafbc-g/zh-cn_image_0000002581275506.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=C50D1796D5C3EEE96795BA803053B4AE85632B324611045879C2EC6BDBF8A7FC)


4. 框选想要接入意图框架功能的代码。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/kVXb2HJWRN-mF852aj--Lg/zh-cn_image_0000002611755363.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=8A4AD1F22A861DFA4E3BD270F0BB8943F3C135EC5C9EF81EBDC6FA1A109F54EC)


5. 在选中的代码块上右键CodeGenie > Insight Intent，选择适合的装饰器。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/H-ycdOTVSuKNZJq_1qdc_w/zh-cn_image_0000002581435426.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=8B1E84F5CCAEB77C4F5CBFA99437EC54A3D79D04974A54A9BAA3DDDF84DD85AB)


6. 在DevEco CodeGenie对话框中对意图定义，功能，参数等进行描述。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/ZKn9KubURaCukly18n8jtg/zh-cn_image_0000002611835255.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=F6564F8EAC29245AE33FAA5FD67BDCEE9983F0C7060775F808293D422E355464)


7. 回车或者点击发送按钮，即可生成对应的装饰器内容。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/PP2kaKo9SwuWTzRwFzcCsg/zh-cn_image_0000002581275508.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=FA0D6661EB366F94442DDF4E3D5E55447D588471C9DDF0673D8512C1F0845BE4)


8. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

  插入前：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/OVyoKnZuQ_ir3Xw0qZ12Sw/zh-cn_image_0000002611755365.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=60E44E0B6FE4E4A2E39488A5D151BF183FB56598A25436D8FB9482C312C6E56C)


  插入后：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/qfWksP0URb-MQWfuFRwPzA/zh-cn_image_0000002581435428.png?HW-CC-KV=V1&HW-CC-Date=20260528T025924Z&HW-CC-Expire=86400&HW-CC-Sign=0E480E23B0DF412D3FE7D54CA79C03EA74E3205DED9CE46672CEB87CEFBF7782)
