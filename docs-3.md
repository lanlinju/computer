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

