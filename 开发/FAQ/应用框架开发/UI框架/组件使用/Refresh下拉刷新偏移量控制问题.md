# Refresh下拉刷新偏移量控制问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1496

#### 问题现象

在实现下拉刷新功能时，Refresh如何根据下拉操作的实时偏移量来动态执行不同的逻辑？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/LczO3b1RSGe-1QeLsn2x9w/zh-cn_image_0000002628765712.png?HW-CC-KV=V1&HW-CC-Date=20260701T041245Z&HW-CC-Expire=86400&HW-CC-Sign=F86B9FF259BAE3D33E98D61FFFA2220DB938E251FC61C5582C9910D31974B591)

 
 

#### 背景知识

- [onStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onstatechange)：当前刷新状态变更时，触发回调。
- [onOffsetChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onoffsetchange12)：下拉距离发生变化时触发回调。
- [onRefreshing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onrefreshing)：进入刷新状态时触发回调。
- [cryptoFramework](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework)：对于安全要求比较高的场景，推荐使用加解密算法库框架[@ohos.security.cryptoFramework](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework)包生成安全随机数。

 
 

#### 解决方案

根据[onOffsetChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onoffsetchange12)方法判断下拉距离来实现不同的刷新效果。通过[onStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#onstatechange)方法中刷新的状态以及refreshOffset属性执行不同的刷新逻辑。
 
完整示例参考如下：
 
```text
import cryptoFramework from '@ohos.security.cryptoFramework';

@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
 <em> // 数据源</em>
  @State arr: String[] =
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'];
<em>  // Refresh刷新状态</em>
  @State refreshStatus: RefreshStatus = RefreshStatus.Inactive;
  <em>// 设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新。</em>
  @State refreshOffset: number = 60;
 <em> // 设置当下拉距离超过refreshOffset时是否能触发刷新。</em>
  @State isGettingData: boolean = false;

<em>  // 下拉大距离的动画刷新效果</em>
  getData() {
    setTimeout(() => {
      this.arr = Array(20)
        .fill(null)
        .map(() => Math.floor(Math.round(cryptoFramework.createRandom().generateRandomSync(1).data[0] * 40 / 255))
          .toString());
      this.isGettingData = false;
      this.isRefreshing = false;
    }, 1000);
  }

  build() {
    Column() {
      Refresh({
        refreshing: $$this.isRefreshing,
      }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF);
            };
          }, (item: string) => item);
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off);
      }
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .backgroundColor(0x89CFF0)
      .pullToRefresh(true)
      .refreshOffset(this.refreshOffset)
     <em> // 当前刷新状态变更时，触发回调。</em>
      .onStateChange((refreshStatus: RefreshStatus) => {
        this.refreshStatus = refreshStatus;
      <em>  // 通过判断刷新距离执行不同的方法</em>
        if (refreshStatus === 4 && this.refreshOffset === 60) {
          console.info('执行方法a');
        } else if (refreshStatus === 4 && this.refreshOffset === 150) {
          console.info('执行方法b');
        }
      })
    <em>  // 下拉距离发生变化时触发回调</em>
      .onOffsetChange((value: number) => {
     <em>   // 根据下拉距离不同，设置不同的触发刷新的下拉偏移量</em>
        if (value > 150) {
          this.refreshOffset = 150;
        } else if (value < 150 && value > 0) {
          this.refreshOffset = 60;
        }
      })
      .onRefreshing(() => {
        if (this.refreshOffset === 60) {
          setTimeout(() => {
            this.isRefreshing = false;
          }, 2000);
          return;
        }
        if (this.refreshOffset === 150 && this.isGettingData === false) {
          this.isGettingData = true;
          this.getData();
        }
      });
    };
  }
}
```
