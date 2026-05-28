# @performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-reuseid-if-else-component

建议使用reuseId标记不同结构的组件构成。
 
滑动丢帧场景下，建议优先修改。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { ChartInfoEntry } from './data/DataEntry';
import { PublicChatItem } from './component/PublicChatItem';
import { ChatItem } from './component/ChatItem';

@Entry
@Component
struct MyComponent{
  private scroller: Scroller = new Scroller()
  private lazyChatList: MyDataSource = new MyDataSource();

  build() {
    Column() {
      List({ scroller: this.scroller }) {
        LazyForEach(this.lazyChatList, (item: ChartInfoEntry, index: number) => {
          ListItem() {
            // 使用reuseId进行组件复用的控制
            InnerRecentChat({ chatInfo: item }).reuseId(this.lazyChatList.getReuseIdByIndex(index))
          }
          .height(72)
        }, (item: ChartInfoEntry) => item.id)
      }
      .cachedCount(3)
      .width('100%')
      .height('100%')
    }
  }
}

@Reusable
@Component
struct InnerRecentChat {
  @State chatInfo: ChartInfoEntry = new ChartInfoEntry()

  aboutToReuse(params: Record<string, ESObject>): void {
    this.chatInfo = params.chatInfo as ChartInfoEntry
  }

  build() {
    Button({ type: ButtonType.Normal }) {
      Row() {
        if (this.chatInfo['isPublicChat']) {
          // 源码文件，请以工程实际为准
          PublicChatItem({ chatInfo: chatInfo as ChartInfoEntry })
        } else {
          // 源码文件，请以工程实际为准
          ChatItem({ chatInfo: this.chatInfo as ChatItem })
        }
      }.padding({ left: 16, right: 16 })
    }
    .type(ButtonType.Normal)
    .width('100%')
    .height('100%')
    .borderRadius(0)
  }
}
```
 
 

##### 反例

```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { ChartInfoEntry } from './data/DataEntry';
import { PublicChatItem } from './component/PublicChatItem';
import { ChatItem } from './component/ChatItem';

@Entry
@Component
struct MyComponent{
  private scroller: Scroller = new Scroller()
  private lazyChatList: MyDataSource = new MyDataSource();

  build() {
    Column() {
      List({ scroller: this.scroller }) {
        LazyForEach(this.lazyChatList, (item: ChartInfoEntry, index: number) => {
          ListItem() {
            // ListItem里有if-else并且直接在分支里使用了自定义复用组件
            Button({ type: ButtonType.Normal }) {
              Row() {
                if (item['isPublicChat']) {
                  // 源码文件，请以工程实际为准
                  PublicChatItem({ chatInfo: item as PublicChatItem })
                } else {
                  // 源码文件，请以工程实际为准
                  ChatItem({ chatInfo: item as ChatItem })
                }
              }.padding({ left: 16, right: 16 })
            }
            .type(ButtonType.Normal)
            .width('100%')
            .height('100%')
            .borderRadius(0)
          }
          .height(72)
        }, (item: ChartInfoEntry) => item.id)
      }
      .cachedCount(3)
      .width('100%')
      .height('100%')
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
