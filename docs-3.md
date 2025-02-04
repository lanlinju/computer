# 指令系统

## 指令存储方式

指令的长度为：16位

| 指令 IR 8位 | 程序状态字PSW 4位 | 微程序周期CYC 4位 |

- 2地址指令
  - 1xxx[aa][bb]

- 1地址指令
  - 01xxxx[aa]
  
- 0地址指令
  - 00xxxxxx

## 指令寻址方式

指令寻址方式有很多种，此处只实现如下4种寻址方式

```
MOV A, 5; 立即寻址
MOV A, B; 寄存器寻址
MOV A, [5]; 直接寻址
MOV A, [B]; 寄存器间接寻址
```

## 取指周期指令

- 占用6个微操作

```python
FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]
```

> [!NOTE]
> 指令周期CYC是4位，则一个指令周期内最多执行2^4=16个微操作。取指周期固定需要6个微操作，因此还剩下10个微操作去实现汇编指令。


## 数据传输指令

### MOV指令

```python
MOV: {
            (pin.AM_REG, pin.AM_INS): [  # MOV A, 5
                pin.DST_W | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_REG): [  # MOV A, B
                pin.DST_W | pin.SRC_R,
            ],
            (pin.AM_REG, pin.AM_DIR): [  # MOV A, [5]
                pin.MAR_IN | pin.SRC_OUT,
                pin.DST_W | pin.RAM_OUT,
            ],
            (pin.AM_REG, pin.AM_RAM): [  # MOV A, [B]
                pin.SRC_R | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT,
            ],
            (pin.AM_DIR, pin.AM_INS): [  # MOV [0x9], 5
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_DIR, pin.AM_REG): [  # MOV [0x9], C
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_DIR, pin.AM_DIR): [  # MOV [0x3f], [0x2e]
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_DIR, pin.AM_RAM): [  # MOV [0x3f], [C]
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_INS): [  # MOV [A], 5
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_RAM, pin.AM_REG): [  # MOV [A], C
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_RAM, pin.AM_DIR): [  # MOV [A], [0x2e]
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_RAM): [  # MOV [A], [C]
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
        },
```

## 算术运算指令

### 加法ADD指令

```python
        ADD: {
            (pin.AM_REG, pin.AM_INS): [  # ADD D, 5
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [  # ADD D, C
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### 减法SUB指令

```python
        SUB: {
            (pin.AM_REG, pin.AM_INS): [  # SUB D, 5
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [  # SUB D, C
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### 加一INC指令

```python
        INC: {
            pin.AM_REG: [  # INC D
                pin.DST_R | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### 减一DEC指令

```python
        DEC: {
            pin.AM_REG: [  # DEC D
                pin.DST_R | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

## 逻辑运算指令

### AND指令

```python
        AND: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### OR指令

```python
        OR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### XOR指令

```python
        XOR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```

### NOT指令

```python
        NOT: {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_NOT | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
```