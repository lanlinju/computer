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

#### 电路实现

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
    \overline{A} + \overline{B} &= \overline{A \times B} 
\end{align*}
$$