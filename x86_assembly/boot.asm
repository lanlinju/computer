[org 0x7c00]

mov ax, 3
int 0x10    ; 设置显示模式为80x25文本模式

xchg bx, bx

mov ax, 0xb800
mov es, ax

mov ax, 0
mov ds, ax

mov si, message
mov di, 0
mov cx, message_end - message

loop1:
    mov al, [ds:si]
    mov [es:di], al

    inc si
    add di, 2

    loop loop1

halt:
    jmp halt

message:
    db "hello world!!!", 0
message_end:
    

times 510 - ($ - $$) db 0 
db 0x55, 0xaa; 主引导扇区最后两个字节必须是 0x55aa
