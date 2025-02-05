# 计算机体系结构

## 一个8位二进制CPU的设计和实现

![CPU](img/cpu/cpu.png)

## 实现指令列表如下

- 二地址指令
  - MOV - 数据传递指令，支持4种寻址方式组合
  - ADD - 加法运算指令
  - SUB - 减法运算指令
  - CMP - 比较指令
  - AND - 逻辑与运行指令
  - OR - 逻辑或运算指令
  - XOR - 逻辑异或运行指令
- 一地址指令
  - INC - 加1指令
  - DEC - 减一指令
  - NOT - 逻辑取反指令
  - JMP - 跳转指令
  - JO - 溢出跳转指令
  - JNO - 非溢出跳转指令
  - JZ - 零跳转指令
  - JNZ - 非零跳转指令
  - JP - 奇数跳转指令
  - JNP - 非奇数跳转指令
  - PUSH - 入栈指令
  - POP - 出栈指令
  - CALL - 函数调用指令
  - INT - 中断调用指令
- 零地址指令
  - NOP - 空指令
  - RET - 函数返回指令
  - IRET - 中断返回指令
  - STI - 开启中断位指令
  - CLI - 关闭中断位指令
  - HLT - 停止指令


## 参考

- [computer](https://github.com/StevenBaby/computer)
- 《编码：隐匿在计算机软硬件背后的语言》
