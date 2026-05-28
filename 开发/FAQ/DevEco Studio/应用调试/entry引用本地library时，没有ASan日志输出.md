# entry引用本地library时，没有ASan日志输出

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-18

**问题现象**
 
entry引用本地library时，已经勾选ASan选择项，没有ASan日志输出。
 
**解决措施**
 
引用本地C++ library时，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS_ENABLE_ASAN=ON”，表示以ASan模式编译so文件。
 
```json
{
  // ...
      "arguments": "-DOHOS_ENABLE_ASAN=ON",
      // ...
    }
  },
  // ...
}
```
 

![](assets/entry引用本地library时，没有ASan日志输出/file-20260515130309922-0.png)
