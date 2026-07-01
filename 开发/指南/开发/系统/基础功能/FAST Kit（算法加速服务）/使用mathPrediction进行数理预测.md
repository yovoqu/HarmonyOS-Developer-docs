# 使用mathPrediction进行数理预测

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-math-prediction

从API版本26.0.0版本开始，FAST Kit提供mathPrediction数理预测模块，基于历史采样数据对序列数据进行建模和预测，适用于手势跟踪、动画曲线预测、运动轨迹预估等实时预测场景。

mathPrediction数理预测模块提供智能序列预测（predictIndex）能力：接收一组包含索引和时间戳的采样点数组，基于FAST Kit内置算法预测下一个时刻的索引值。


#### 场景介绍

mathPrediction数理预测模块适用于以下场景：

 - **手势跟踪**：根据历史触摸点的位置和时间，预测下一帧触摸点的索引位置，减少触摸跟随延迟。
 - **动画曲线预测**：基于动画曲线已有的关键帧索引-时间采样，预测后续帧的索引变化趋势，实现更平滑的动画过渡。
 - **运动轨迹预估**：在游戏或交互应用中，根据物体的历史运动轨迹采样，预测其后续位置，提升响应速度。
 - **滚动惯性预测**：在列表滚动场景中，根据历史滚动偏移量采样，预测减速阶段的最终停止位置。




#### 开发步骤
1. 导入[mathPrediction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction)模块。
2. 构造[IndexSample](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction#indexsample)接口数组，添加至少2个采样点。
3. 调用[predictIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction#predictindex)函数进行预测。
4. 获取返回的预测结果。

```text
import { hilog } from '@kit.PerformanceAnalysisKit';
import { mathPrediction } from '@kit.FASTKit';

const DOMAIN = 0x0000;

function mathPredictionTest(): void {
  let samples: mathPrediction.IndexSample[] = [
    { index: 0, timestamp: 0 },
    { index: 10, timestamp: 100 },
    { index: 20, timestamp: 200 }
  ];
  try {
    const predicted = mathPrediction.predictIndex(samples);
    hilog.info(DOMAIN, 'testTag', 'PredictionFunction predicted=%{public}d', predicted);
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(DOMAIN, 'testTag', 'PredictionFunction failed, code: %{public}d, message: %{public}s', code, message);
  }
}
```
