# Mock能力

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-test-mock

在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用Mock能力，对这些接口或对象进行模拟。当前Instrument Test和Local Test均支持对模块进行Mock，对于调用系统模块API或外部依赖模块，使用import mock，对于本地模块，使用hamock/hypium插件包的mock接口或者import mock。
 
> [!NOTE]
> 仅API 11及以上版本的Stage模型工程支持。

 

#### 系统模块/依赖模块Mock

通过import mock对系统模块API或依赖模块的方法进行Mock，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以系统API bluetoothManager为例，具体实现如下。
 1. 在src/mock目录下新建一个ArkTS文件，例如bluetooth_manager.mock.ets，在这个文件内定义目标模块的Mock实现。
```ArkTS
// src/mock/bluetooth_manager.mock.ets
enum BluetoothState {
  /** Indicates the local Bluetooth is off */
  STATE_OFF = 0,
  /** Indicates the local Bluetooth is turning on */
  STATE_TURNING_ON = 1,
  /** Indicates the local Bluetooth is on, and ready for use */
  STATE_ON = 2,
  /** Indicates the local Bluetooth is turning off */
  STATE_TURNING_OFF = 3,
  /** Indicates the local Bluetooth is turning LE mode on */
  STATE_BLE_TURNING_ON = 4,
  /** Indicates the local Bluetooth is in LE only mode */
  STATE_BLE_ON = 5,
  /** Indicates the local Bluetooth is turning off LE only mode */
  STATE_BLE_TURNING_OFF = 6
}
interface BluetoothInfo {
  state: number
}
const MockBluetoothManager: Record<string, Object> = {
  'getBluetoothInfo': () => {
    return { state : BluetoothState.STATE_BLE_TURNING_ON } as BluetoothInfo;
  },
};
export default MockBluetoothManager;
```

2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。
```ArkTS
"@ohos.enterprise.bluetoothManager": {  // 待替换的模块名
  "source": "src/mock/bluetooth_manager.mock.ets"  // Mock代码的路径，相对于模块根目录
}
```

3. 在测试文件中编写如下代码。
```ArkTS
// bluetoothManager.test.ets
import { describe, it, expect } from '@ohos/hypium';
import { bluetoothManager } from '@kit.MDMKit';

export default function mock_system_api() {   
  describe('mock_system_api', () => {
    /* mock系统API */
    it('mock_system_api', 0, () => {
      let bluetoothInfo = bluetoothManager.getBluetoothInfo({
        bundleName: "com.example.myapplication"
      })
      expect(bluetoothInfo.state).assertEqual(4)
    });
  });
}
```

4. 如果测试文件是手动创建的，需要将用例类mock_system_api添加到List.test.ets文件中。
```text
import mock_system_api from <span style="color: rgb(255,0,170);">'./bluetoothManager.test'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">testsuite</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  mock_system_api<span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

5. 执行测试，用例通过。
 
 

#### 本地模块Mock

有两种方式可以对本地模块进行Mock，一是使用hamock/hypium插件包的mock接口，二是使用import mock。
 
 

#### 使用hamock/hypium插件包的mock接口

以下例子通过mock接口模拟本地模块的某个方法，关于Mock的更多说明可以参考[mock能力](https://gitcode.com/openharmony/testfwk_arkxtest#mock能力)。
 1. 在src/main/ets目录下新建一个ArkTS文件，例如ClassForMock.ets，并在其中导出一个类。
```text
export class ClassForMock {
  constructor() {
  }
  method_1(arg: string) {
    return '888888';
  }
  method_2(arg: string) {
    return '999999';
  }
}
```

2. 在测试文件中编写如下代码。
```ArkTS
// afterReturnTest.test.ets
import { describe, expect, it, MockKit, when } from '@ohos/hypium';
import { ClassForMock } from '../../../main/ets/ClassForMock';

export default function afterReturnTest() {
  describe('afterReturnTest', () => {
    it('afterReturnTest', 0, () => {
      console.info("it begin");
      // 1.创建一个mock能力的对象MockKit
      let mocker: MockKit = new MockKit();
      // 2.定义类ClassForMock，里面两个函数，然后创建一个对象classForMock
      let classForMock: ClassForMock = new ClassForMock();
      // 3.进行mock操作,比如需要对ClassForMock类的method_1函数进行mock
      let mockFunc: Function = mocker.mockFunc(classForMock, classForMock.method_1);
      // 4.期望classForMock.method_1函数被mock后, 以'test'为入参时调用函数返回结果'1'
      when(mockFunc)('test').afterReturn('1');
      // 5.对mock后的函数进行断言，看是否符合预期
      // 执行成功案例，参数为'test'
      expect(classForMock.method_1('test')).assertEqual('1'); // 执行通过
    })
  })
}
```

3. 如果测试文件是手动创建的，需要将用例类afterReturnTest添加到List.test.ets文件中。
```text
import afterReturnTest from <span style="color: rgb(255,0,170);">'./afterReturnTest.test'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">testsuite</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  afterReturnTest<span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 执行测试，用例通过。
 
 

#### 使用import mock

使用import mock对本地模块进行Mock，操作步骤和系统模块/依赖模块的Mock类似，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以下例子对本地模块entry/src/main/ets/common/calc.ets中的sum函数进行Mock。
 1. 在src/mock目录下新建一个common目录并创建一个ArkTS文件，例如calc.mock.ets，在这个文件内定义目标模块的Mock实现。
```ArkTS
// src/mock/common/calc.mock.ets
export function <span style="color: rgb(0,0,255);">sum</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  return <span style="color: rgb(132,63,161);">"this is mock sum"</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 calc.ets的原始实现如下：

  
```ArkTS
// src/main/ets/common/calc.ets
export function <span style="color: rgb(0,0,255);">sum</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  return <span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。
```ArkTS
{
<span style="color: rgb(132,63,161);">  "common/calc.ets"</span><span style="color: rgb(181,106,1);">: </span>{ // 本地模块只支持ets/xxx的相对路径，并需明确文件后缀
    <span style="color: rgb(132,63,161);">"source"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"src/mock/common/calc.mock.ets"</span>  // Mock代码的路径，相对于模块根目录
  }<span style="color: rgb(181,106,1);">,</span>
}
```

3. 在测试文件中编写如下代码。
```ArkTS
// <span style="color: rgb(0,0,255);">test_mock_local_method</span>.test.ets
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">it</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">expect </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos/hypium'</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">sum </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'../../../main/ets/common/calc'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">test_mock_local_method</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'test_mock_local_method'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">it</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"test_mock_local_method"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">expect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">sum</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">assertEqual</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"this is mock sum"</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 如果测试文件是手动创建的，需要将用例类test_mock_local_method添加到List.test.ets文件中。
```text
import <span style="color: rgb(0,0,255);">test_mock_local_method</span> from <span style="color: rgb(255,0,170);">'./test_mock_local_method.test'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">testsuite</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">test_mock_local_method</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

5. 执行测试，用例通过。
