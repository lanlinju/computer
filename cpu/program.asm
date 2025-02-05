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