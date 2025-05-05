[org 0x7c00]

mov ax, 3
int 0x10    ; 设置显示模式为80x25文本模式

xchg bx, bx


; mov ax, 5
; mov bx, 6
; add ax, bx; ax = ax + bx

; add word [number], 0x1000 

mov ax, 5
mov bx, 7
mul bx; dx:ax = ax * bx

halt:
    jmp halt

number:
    dw 0x3456

times 510 - ($ - $$) db 0 
db 0x55, 0xaa; 主引导扇区最后两个字节必须是 0x55aa
