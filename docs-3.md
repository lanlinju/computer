## 指令系统

### 取指周期指令

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