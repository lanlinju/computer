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

## 条件转移指令

```
# 6大条件跳转，根据PSW来判定
# 溢出跳转
JO = (4 << pin.ADDR1_SHIFT) | pin.ADDR1
# 非溢出跳转
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1
# 零跳转
JZ = (6 << pin.ADDR1_SHIFT) | pin.ADDR1
# 非零跳转
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1
# 奇数跳转
JP = (8 << pin.ADDR1_SHIFT) | pin.ADDR1
# 非奇数跳转
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1
```

### ASM例子

```assembly
    MOV D, 0;

increase:
    INC D;
    CMP D, 5;
    JO increase

decrease:
    DEC D;
    CMP D, 0;
    JZ increase
    JMP decrease

    HLT
```

## 堆栈操作指令

### PUSH指令

```python
        PUSH: {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_OUT | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_R | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
```

### POP指令

```python
        POP: {
            pin.AM_REG: [
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_W | pin.RAM_OUT,
                pin.SP_OUT | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.SP_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
```

### ASM例子

```python
    MOV SS, 1
    MOV SP, 0x10; [0, 0xF]
    MOV D, 10;

    PUSH D
    PUSH 1

    POP C
    POP B
    MOV A, C;
    ADD A, B;
    MOV D, A;
    HLT
```

## 函数调用指令

### CALL命令

```python
        CALL: {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_R | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
```

### RET指令

```python
        RET: [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.ALU_OUT | pin.SP_IN,
            pin.CS_OUT | pin.MSR_IN,
        ],
```

### ASM例子

```python
    MOV SS, 1
    MOV SP, 0x10; [0, 0xF]
    JMP start

show:
    MOV D, 255;
    ret;

start:
    MOV C, 0;

increase:
    INC C;
    MOV D, C;
    call show;
    JMP increase

    HLT
```

## 内中断指令

### 中断指令

- INT - 中断调用
- IRET - 中断返回
- STI - 开中断
- CLI - 关中断
  
### INT命令

```python
        INT: {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_R | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_CLI,
            ],
        },
```

### IRET指令

```python
        IRET: [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.ALU_OUT | pin.SP_IN,
            pin.CS_OUT | pin.MSR_IN | pin.ALU_PSW | pin.ALU_STI,
        ],
```

### STI指令

```python
        STI: [
            pin.ALU_PSW | pin.ALU_STI,
        ],
```

### CLI指令

```python
        CLI: [
            pin.ALU_PSW | pin.ALU_CLI,
        ],
```

### ASM例子

```python
    MOV SS, 1
    MOV SP, 0x10; [0, 0xF]
    JMP start

show:
    MOV D, 255;
    ret;

start:
    MOV C, 0;

increase:
    INC C;
    MOV D, C;
    JP disable;

enable:
    sti;
    jmp interrupt;

disable:
    cli;

interrupt:
    int show;
    JMP increase

    HLT
```