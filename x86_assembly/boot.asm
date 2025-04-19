mov ax, 3
int 0x10    ; 设置显示模式为80x25文本模式

xchg bx, bx

mov ax, 0x1111
mov bx, 0x2222
mov cx, 0x3333
mov dx, 0x4444
mov di, 0x5555
mov si, 0x6666
mov sp, 0x7777
mov bp, 0x8888

; mov ax, 0xb800
; mov ds, ax; 将代码段设置为 0xb800

; mov byte [0], 'T'
; mov byte [2], 'e'
; mov byte [4], 'l'
; mov byte [6], 'l'
; mov byte [8], 'o'
; mov byte [10], ' '
; mov byte [12], 'W'
; mov byte [14], 'o'
; mov byte [16], 'r'
; mov byte [18], 'l'
; mov byte [20], 'd'
; mov byte [22], '!'

; 下面阻塞停下来
halt:
    jmp halt

times 510 - ($ - $$) db 0 ; 用 0 填充满 510 个字节
db 0x55, 0xaa; 主引导扇区最后两个字节必须是 0x55aa
