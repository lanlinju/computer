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