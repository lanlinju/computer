## 基本门电路

### 与门

#### 继电器实现

![与门](img/basic_gate_circuit/Relay_Gate_AND.png)

符号表示形式如下：
![与门](img/basic_gate_circuit/Gate_AND.png)

#### 真值表

| AND | 0 | 1 |
| - | - | - |
| 0 | 0 | 0 |
| 1 | 0 | 1 |


### 或门

#### 继电器实现

![或门](img/basic_gate_circuit/Relay_Gate_OR.png)

符号表示形式如下：
![或门](img/basic_gate_circuit/Gate_OR.png)

#### 真值表

| OR | 0 | 1 |
| - | - | - |
| 0 | 0 | 1 |
| 1 | 1 | 1 |

### 反相器

#### 继电器实现

![反相器](img/basic_gate_circuit/relay_inverter.png)

符号表示形式如下：
![反相器](img/basic_gate_circuit/inverter.png)

### 或非门

#### 继电器实现

![或非门](img/basic_gate_circuit/relay_gate_NOR.png)

符号表示形式如下：
![或非门](img/basic_gate_circuit/gate_NOR.png)

#### 真值表

| NOR | 0 | 1 |
| - | - | - |
| 0 | 1 | 0 |
| 1 | 0 | 0 |

### 与非门

#### 继电器实现

![与非门](img/basic_gate_circuit/relay_gate_NOR.png)

符号表示形式如下：
![与非门](img/basic_gate_circuit/gate_NOR.png)

#### 真值表

| NAND | 0 | 1 |
| - | - | - |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

### 四种不同逻辑门关系如下
![Truth Tables](img/basic_gate_circuit/Logic_Gates_Truth_Tables.png)

### 摩根定律可以简单地表示为如下形式：

$$
\begin{align*}
    \overline{A} \times \overline{B} &= \overline{A+B} \\
    \overline{A} +      \overline{B} &= \overline{A \times B} 
\end{align*}
$$

## 二进制加法器

一对二进制数相加的结果中具有两个数码，其中一位叫做加法位（sum bit），另一位则叫做进位位（carry bit，例如，1加1等于0，进位为1）

- 表示加法的表格：

    |+加法|0|1|
    |-|-|-|
    |0|0|1|
    |1|1|0|

- 表示进位的表格：

    |+进位|0|1|
    |-|-|-|
    |0|0|0|
    |1|0|1| 

### 异或门

符号表示形式如下：
![异或门](img/ALU/NOR.png)
电路图如下：
![异或门](img/ALU/circuit_nor.png)

#### 电路实现
![异或门](img/ALU/nor_impl.png)

### 半加器

符号表示形式如下：
![半加器](img/ALU/half_adder.png)
电路图如下：
![半加器](img/ALU/circuit_half_adder.png)

#### 电路实现
![半加器](img/ALU/half_adder_impl.png)

### 全加器

符号表示形式如下：
![全加器](img/ALU/full_adder.png)
电路图如下：
![全加器](img/ALU/circuit_full_adder.png)

#### 电路实现
![全加器](img/ALU/full_adder_impl.png)

以下表格总结了全加法器所有可能的输入组合以及对应的输出结果。

|输入A|输入B|进位输出|加和输出|进位输出|
|-|-|-|-|-|
|0|0|0|0|0|
|0|1|0|1|0|
|1|0|0|1|0|
|1|1|0|0|1|
|0|0|1|1|0|
|0|1|1|0|1|
|1|0|1|0|1|
|1|1|1|1|1|

### 8位行波进位（ripple carry）全加器

电路图如下：
![8位全加器](img/ALU/circuit_8bit_full_adder.png)

#### 电路实现
![8位全加器](img/ALU/8bit_full_adder_impl.png)

## 如何实现减法

### 求补器

符号表示形式如下：
![求补器](img/ALU/one's_complement.png)
电路图如下：
![求补器](img/ALU/circuit_one's_complement.png)

#### 电路实现
![求补器](img/ALU/one's_complement_impl.png)

### 减法电路实现
![减法](img/ALU/8bit_full_adder_with_subtraction_impl.png)

## 触发器

### R-S触发器
电路图如下：
![R-S触发器](img/Flip-Flop/R-S.png)

#### 电路实现
![R-S触发器](img/Flip-Flop/R-S_impl.png)

#### R-S触发器真值表

| 输入 | 输入 | 输出 | 输出 |
|------|------|------|------|
| **S** | **R** | **Q** | **Q̅** |
| 1    | 0    | 1    | 0    |
| 0    | 1    | 0    | 1    |
| 0    | 0    | Q    | Q̅   |
| 1    | 1    | 禁止 | 禁止 |


### 具有保持位的R-S触发器
电路图如下：
![R-S触发器](img/Flip-Flop/R-S_hold_that_bit.png)

#### 电路实现
![R-S触发器](img/Flip-Flop/R-S_hold_that_bit_impl.png)

#### 具有保持位R-S触发器真值表

| **数据** | **保持位** | **Q** |
|------|------|------|
| 0    | 1    | 0    | 
| 1    | 1    | 1    | 
| X    | 0    | Q    |

### 电平触发的D型触发器
电路图如下：
![D型触发器](img/Flip-Flop/D_level.png)

#### 电路实现
![D型触发器](img/Flip-Flop/D_level_impl.png)

#### 电平触发的D型触发器真值表

| 输入 | 输入 | 输出 | 输出 |
|------|------|------|------|
| **D** | **Clk** | **Q** | **Q̅** |
| 0    | 1    | 0    | 1    |
| 1    | 1    | 1    | 0    |
| X    | 0    | Q    | Q̅   |

### 边沿触发的D型触发器
电路图如下：
![D型触发器](img/Flip-Flop/D_edge.png)

#### 电路实现
![D型触发器](img/Flip-Flop/D_edge_impl.png)

#### 边沿触发的D型触发器真值表

| 输入 | 输入 | 输出 | 输出 |
|------|------|------|------|
| **D** | **Clk** | **Q** | **Q̅** |
| 0    | ↑    | 0    | 1    |
| 1    | ↑    | 1    | 0    |
| X    | 0    | Q    | Q̅    |

#### 边沿触发的D型触发器（带有清除和预设）

#### 电路实现
![D型触发器](img/Flip-Flop/D_edge_with_preset_and_clear.png)

#### 边沿触发的D型触发器真值表

| 输入 | 输入 | 输入 | 输入 | 输出 | 输出 |
|------|------|------|------|------|------|
| **Pre** | **Clr** | **D** | **Clk** | **Q** | **Q̅** |
| 1   | 0   | X    | X    | 1    | 0    |
| 0   | 1   | X    | X    | 0    | 1    |
| 0   | 0   | 0    | ↑    | 0    | 1    |
| 0   | 0   | 1    | ↑    | 1    | 0    |
| 0   | 0   | X    | 0    | Q    | Q̅    |

## 计数器

### 分频器
电路图如下：
![分频器](img/counter/frequency_divider.png)

#### 电路实现
![分频器](img/counter/frequency_divider_impl.png)

### 8位行波计数器
电路图如下：
![计数器](img/counter/8bit_counter.png)

#### 电路实现
![计数器](img/counter/8bit_counter_impl.png)

## 寄存器 (edge-triggered）

### 三态门（Three-State Gate）

#### 电路实现
![三态门](img/basic/gate.png)

### 8位锁存器
电路图如下：
![8位锁存器](img/register/latch.png)

#### 电路实现
![8位锁存器](img/register/latch_impl.png)

### 8位寄存器

#### 电路实现
![8位寄存器](img/register/register.png)