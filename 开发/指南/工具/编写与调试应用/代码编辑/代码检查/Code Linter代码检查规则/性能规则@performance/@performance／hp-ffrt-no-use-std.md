# @performance/hp-ffrt-no-use-std

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-ffrt-no-use-std

禁止在FFRT worker中使用std::xxx等同步接口。该规则仅对C/C++文件进行检查。
 
并行化场景下，建议优先修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-ffrt-no-use-std"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition_variable>
#include <unistd.h>
// ffrt头文件
#include "ffrt/ffrt.h"
using namespace std;
int N = 100;
int M = 100;

<em>// ffrt::submit中使用了std::mutex</em>
    void PositiveCase1(int temp) {
    ffrt::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            [&]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
<em>// ffrt::submit中使用了std::condition_variable</em>
    void PositiveCase2(int temp) {
    ffrt::condition_variable cond;
    int a = 0;
    ffrt::mutex lock_;
    ffrt::submit(
        [&]() {
            std::unique_lock<ffrt::mutex> lck(lock_);
            cond.wait(lck, [&] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        [&]() {
            std::unique_lock<ffrt::mutex> lck(lock_);
            a = 1;
            cond.notify_one();
        },
        {}, {});
    ffrt::wait();
}
<em>// ffrt::submit中使用了std::usleep</em>
    void PositiveCase3(int temp) {
    ffrt::submit(
        [&]() {
        ffrt_usleep(100);
        printf("test");
        ffrt_yield();      
    }, {}, {});
}
<em>// ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock</em>
    void PositiveCase4(int temp) {
    int a = 0;
    ffrt_rwlock_t mtx;
    ffrt::submit(
        [&]() {
        int ret = ffrt_rwlock_wrlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
        a++;
        ret = ffrt_rwlock_unlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
    }, {}, {});
    ffrt::submit(
        [&]() {
        int ret = ffrt_rwlock_rdlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
        printf("sum is %d\n", a);
        ret = ffrt_rwlock_unlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
    }, {}, {});
}
```
 

 
 

#### 反例

```text
#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition_variable>
#include <unistd.h>
// ffrt头文件 
#include "ffrt/ffrt.h" 
using namespace std;
int N = 100;
int M = 100;
<em>// ffrt::submit中使用了std::mutex</em>
    void NegativeCase1(int temp) {
    std::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            [&]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
<em>// ffrt::submit中使用了std::condition_variable</em>
    void NegativeCase2(int temp) {
    std::condition_variable cond;
    int a = 0;
    std::mutex lock_;
    ffrt::submit(
        [&]() {
            std::unique_lock<std::mutex> lck(lock_);
            cond.wait(lck, [&] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        [&]() {
            std::unique_lock<std::mutex> lck(lock_);
            a = 1;
            cond.notify_one();
        },
        {}, {});
    ffrt::wait();
}
<em>// ffrt::submit中使用了std::usleep</em>
    void NegativeCase3(int temp) {
    ffrt::submit(
        [&]() {
        usleep(100);
        printf("test");
        ffrt_yield();
    }, {}, {});
}
<em>// ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock</em>
    void NegativeCase4(int temp) {
    int a = 0;
    pthread_rwlock_t mtx;
    ffrt::submit(
        [&]() {
        int ret = pthread_rwlock_wrlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
        a++;
        ret = pthread_rwlock_unlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
    }, {}, {});
    ffrt::submit(
        [&]() {
        int ret = pthread_rwlock_rdlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
        printf("sum is %d\n", a);
        ret = pthread_rwlock_unlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
    }, {}, {});
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
