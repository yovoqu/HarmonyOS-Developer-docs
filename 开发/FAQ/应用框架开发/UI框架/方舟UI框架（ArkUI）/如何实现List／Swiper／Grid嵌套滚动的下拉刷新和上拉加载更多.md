# 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-278

开发者可通过Refresh组件嵌套List实现下拉刷新。刷新逻辑在onRefreshing回调方法中执行。上拉加载更多给List添加onReachEnd事件回调，列表滑动到底部时触发。示例代码如下：
 
```text
build() {
  Column() {
   <em> // Search box at the top</em>
    this.searchBarBuilder()
   <em> // Pull down refresh component</em>
    Refresh({ refreshing: $$this.isRefreshing }) {
     <em> // List component as long list layout</em>
      List({ space: 10 }) {
       <em> // ListItem Customize the Swiper carousel module</em>
        ListItem() {
          this.bannerBuilder()
        }
       <em> // ListItem Custom Grid Quick Access Module</em>
        ListItem() {
          this.quickBuilder()
        }
      <em>  // ListItem Custom Column Flash Sale Module</em>
        ListItem() {
          this.flashBuilder()
        }
      <em>  // ListItemGroup Product Classification List</em>
        this.productsBuilder()
      <em>  // 最后ListItem Customize bottom loading for more</em>
        ListItem() {
          this.footerLoadingBuilder()
        }.height(50).width('100%').backgroundColor(0xeeeeee)
      }
      .sticky(StickyStyle.Header)
      .height('100%')
  <em>    // List component hits bottom to simulate network requests</em>
      .onReachEnd(() => {
       <em> // Load more data logic</em>
      })
    }
    <em>// Pull down refresh simulation network request</em>
    .onRefreshing(() => {
    <em>  // Data refresh logic</em>
    })
    .layoutWeight(1)
    .width('100%')
  }
}
```
