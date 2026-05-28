# @performance/lazyforeach-args-check（已下线）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lazyforeach-args-check

建议在LazyForEach参数中设置keyGenerator。该规则已于5.0.3.500版本下线。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/lazyforeach-args-check"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(0,0,255);">class</span> <span style="color: rgb(0,128,128);">BasicDataSource</span> <span style="color: rgb(0,0,255);">implements</span> <span style="color: rgb(0,128,128);">IDataSource</span> {
  <span style="color: rgb(0,0,255);">private</span> listeners: <span style="color: rgb(0,128,128);">DataChangeListener</span>[] = [];
  <span style="color: rgb(0,0,255);">private</span> originDataArray: <span style="color: rgb(0,0,255);">string</span>[] = [];
  <span style="color: rgb(0,0,255);">public</span> totalCount(): <span style="color: rgb(0,0,255);">number</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(9,134,88);">0</span>;
  }
  <span style="color: rgb(0,0,255);">public</span> getData(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">string</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.originDataArray[index];
  }
  registerDataChangeListener(listener: <span style="color: rgb(0,128,128);">DataChangeListener</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">if</span> (<span style="color: rgb(0,0,255);">this</span>.listeners.indexOf(listener) < <span style="color: rgb(9,134,88);">0</span>) {
      console.info(<span style="color: rgb(163,21,21);">'add listener'</span>);
      <span style="color: rgb(0,0,255);">this</span>.listeners.push(listener);
    }
  }
  unregisterDataChangeListener(listener: <span style="color: rgb(0,128,128);">DataChangeListener</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">const</span> pos = <span style="color: rgb(0,0,255);">this</span>.listeners.indexOf(listener);
    <span style="color: rgb(0,0,255);">if</span> (pos >= <span style="color: rgb(9,134,88);">0</span>) {
      console.info(<span style="color: rgb(163,21,21);">'remove listener'</span>);
      <span style="color: rgb(0,0,255);">this</span>.listeners.splice(pos, <span style="color: rgb(9,134,88);">1</span>);
    }
  }
  notifyDataReload(): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }
  notifyDataAdd(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }
  notifyDataChange(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }
  notifyDataDelete(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }
}
<span style="color: rgb(0,0,255);">class</span> <span style="color: rgb(0,128,128);">MyDataSource</span> <span style="color: rgb(0,0,255);">extends</span> <span style="color: rgb(0,128,128);">BasicDataSource</span> {
  <span style="color: rgb(0,0,255);">private</span> dataArray: <span style="color: rgb(0,0,255);">string</span>[] = [];
  <span style="color: rgb(0,0,255);">public</span> totalCount(): <span style="color: rgb(0,0,255);">number</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.dataArray.length;
  }
  <span style="color: rgb(0,0,255);">public</span> getData(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">string</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.dataArray[index];
  }
  <span style="color: rgb(0,0,255);">public</span> addData(index: <span style="color: rgb(0,0,255);">number</span>, data: <span style="color: rgb(0,0,255);">string</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.dataArray.splice(index, <span style="color: rgb(9,134,88);">0</span>, data);
    <span style="color: rgb(0,0,255);">this</span>.notifyDataAdd(index);
  }
  <span style="color: rgb(0,0,255);">public</span> pushData(data: <span style="color: rgb(0,0,255);">string</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.dataArray.push(data);
    <span style="color: rgb(0,0,255);">this</span>.notifyDataAdd(<span style="color: rgb(0,0,255);">this</span>.dataArray.length - <span style="color: rgb(9,134,88);">1</span>);
  }
}
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(0,0,255);">private</span> data: <span style="color: rgb(0,128,128);">MyDataSource</span> = <span style="color: rgb(0,0,255);">new</span> <span style="color: rgb(0,128,128);">MyDataSource</span>();
  aboutToAppear() {
    <span style="color: rgb(0,0,255);">for</span> (<span style="color: rgb(0,0,255);">let</span> i = <span style="color: rgb(9,134,88);">0</span>; i <= <span style="color: rgb(9,134,88);">20</span>; i++) {
      <span style="color: rgb(0,0,255);">this</span>.data.pushData(<span style="color: rgb(163,21,21);">`Hello </span>${i}<span style="color: rgb(163,21,21);">`</span>)
    }
  }
  build() {
    <span style="color: rgb(0,128,128);">Column</span>({ space: <span style="color: rgb(9,134,88);">5</span> }) {
      <span style="color: rgb(0,128,128);">Grid</span>() {
        <span style="color: rgb(0,128,128);">LazyForEach</span>(<span style="color: rgb(0,0,255);">this</span>.data, (item: <span style="color: rgb(0,0,255);">string</span>) => {
          <span style="color: rgb(0,128,128);">GridItem</span>() {
            <span style="color: rgb(0,128,0);">// 使用可复用自定义组件</span>
            <span style="color: rgb(0,128,0);">// 业务逻辑</span>
          }
        }, (item: <span style="color: rgb(0,0,255);">string</span>) => item)
      }
      .cachedCount(<span style="color: rgb(9,134,88);">2</span>) <span style="color: rgb(0,128,0);">// 设置GridItem的缓存数量</span>
      .columnsTemplate(<span style="color: rgb(163,21,21);">'1fr 1fr 1fr'</span>)
      .columnsGap(<span style="color: rgb(9,134,88);">10</span>)
      .rowsGap(<span style="color: rgb(9,134,88);">10</span>)
      .margin(<span style="color: rgb(9,134,88);">10</span>)
      .height(<span style="color: rgb(9,134,88);">500</span>)
      .backgroundColor(<span style="color: rgb(48,48,192);">0xFAEEE0</span>)
    }
  }
}
```
 
 

##### 反例

```text
<span style="color: rgb(0,0,255);">class</span> <span style="color: rgb(0,128,128);">BasicDataSource</span> <span style="color: rgb(0,0,255);">implements</span> <span style="color: rgb(0,128,128);">IDataSource</span> {
  <span style="color: rgb(0,0,255);">private</span> listeners: <span style="color: rgb(0,128,128);">DataChangeListener</span>[] = [];
  <span style="color: rgb(0,0,255);">private</span> originDataArray: <span style="color: rgb(0,0,255);">string</span>[] = [];
  <span style="color: rgb(0,0,255);">public</span> totalCount(): <span style="color: rgb(0,0,255);">number</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(9,134,88);">0</span>;
  }
  <span style="color: rgb(0,0,255);">public</span> getData(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">string</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.originDataArray[index];
  }
  registerDataChangeListener(listener: <span style="color: rgb(0,128,128);">DataChangeListener</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">if</span> (<span style="color: rgb(0,0,255);">this</span>.listeners.indexOf(listener) < <span style="color: rgb(9,134,88);">0</span>) {
      console.info(<span style="color: rgb(163,21,21);">'add listener'</span>);
      <span style="color: rgb(0,0,255);">this</span>.listeners.push(listener);
    }
  }
  unregisterDataChangeListener(listener: <span style="color: rgb(0,128,128);">DataChangeListener</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">const</span> pos = <span style="color: rgb(0,0,255);">this</span>.listeners.indexOf(listener);
    <span style="color: rgb(0,0,255);">if</span> (pos >= <span style="color: rgb(9,134,88);">0</span>) {
      console.info(<span style="color: rgb(163,21,21);">'remove listener'</span>);
      <span style="color: rgb(0,0,255);">this</span>.listeners.splice(pos, <span style="color: rgb(9,134,88);">1</span>);
    }
  }
  notifyDataReload(): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }
  notifyDataAdd(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }
  notifyDataChange(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }
  notifyDataDelete(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }
}
<span style="color: rgb(0,0,255);">class</span> <span style="color: rgb(0,128,128);">MyDataSource</span> <span style="color: rgb(0,0,255);">extends</span> <span style="color: rgb(0,128,128);">BasicDataSource</span> {
  <span style="color: rgb(0,0,255);">private</span> dataArray: <span style="color: rgb(0,0,255);">string</span>[] = [];
  <span style="color: rgb(0,0,255);">public</span> totalCount(): <span style="color: rgb(0,0,255);">number</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.dataArray.length;
  }
  <span style="color: rgb(0,0,255);">public</span> getData(index: <span style="color: rgb(0,0,255);">number</span>): <span style="color: rgb(0,0,255);">string</span> {
    <span style="color: rgb(0,0,255);">return</span> <span style="color: rgb(0,0,255);">this</span>.dataArray[index];
  }
  <span style="color: rgb(0,0,255);">public</span> addData(index: <span style="color: rgb(0,0,255);">number</span>, data: <span style="color: rgb(0,0,255);">string</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.dataArray.splice(index, <span style="color: rgb(9,134,88);">0</span>, data);
    <span style="color: rgb(0,0,255);">this</span>.notifyDataAdd(index);
  }
  <span style="color: rgb(0,0,255);">public</span> pushData(data: <span style="color: rgb(0,0,255);">string</span>): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(0,0,255);">this</span>.dataArray.push(data);
    <span style="color: rgb(0,0,255);">this</span>.notifyDataAdd(<span style="color: rgb(0,0,255);">this</span>.dataArray.length - <span style="color: rgb(9,134,88);">1</span>);
  }
}
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(0,0,255);">private</span> data: <span style="color: rgb(0,128,128);">MyDataSource</span> = <span style="color: rgb(0,0,255);">new</span> <span style="color: rgb(0,128,128);">MyDataSource</span>();
  aboutToAppear() {
    <span style="color: rgb(0,0,255);">for</span> (<span style="color: rgb(0,0,255);">let</span> i = <span style="color: rgb(9,134,88);">0</span>; i <= <span style="color: rgb(9,134,88);">20</span>; i++) {
      <span style="color: rgb(0,0,255);">this</span>.data.pushData(<span style="color: rgb(163,21,21);">`Hello </span>${i}<span style="color: rgb(163,21,21);">`</span>)
    }
  }
  build() {
    <span style="color: rgb(0,128,128);">Column</span>({ space: <span style="color: rgb(9,134,88);">5</span> }) {
      <span style="color: rgb(0,128,128);">Grid</span>() {
        <span style="color: rgb(0,128,128);">LazyForEach</span>(<span style="color: rgb(0,0,255);">this</span>.data, (item: <span style="color: rgb(0,0,255);">string</span>) => {
          <span style="color: rgb(0,128,128);">GridItem</span>() {
            <span style="color: rgb(0,128,0);">// 使用可复用自定义组件</span>
            <span style="color: rgb(0,128,0);">// 业务逻辑</span>
          }
        })
      }
      .cachedCount(<span style="color: rgb(9,134,88);">2</span>) <span style="color: rgb(0,128,0);">// 设置GridItem的缓存数量</span>
      .columnsTemplate(<span style="color: rgb(163,21,21);">'1fr 1fr 1fr'</span>)
      .columnsGap(<span style="color: rgb(9,134,88);">10</span>)
      .rowsGap(<span style="color: rgb(9,134,88);">10</span>)
      .margin(<span style="color: rgb(9,134,88);">10</span>)
      .height(<span style="color: rgb(9,134,88);">500</span>)
      .backgroundColor(<span style="color: rgb(48,48,192);">0xFAEEE0</span>)
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
