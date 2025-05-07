mov dx, 0x1f2
mov al, 1
out dx, al; 设置扇区数量

mov al, 2

inc dx; 0x1f3
out dx, al

mov al, 0

inc dx; 0x1f4
out dx, al

inc dx; 0x1f5
out dx, al

inc dx; 0x1f6
mov al, 0b1110_0000
out dx, al

inc dx; 0x1f7
mov al, 0x30; 写硬盘
out dx, al

mov ax, 0x100
mov es, ax
mov di, 0
mov dx, 0x1f0

write_loop:
    nop
    nop
    nop

    mov ax, [es:di]
    out dx, ax

    add di, 2
    cmp di, 512
    jnz write_loop

mov dx, 0x1f7
.check_write_state:
    nop
    nop
    nop ; 一点延迟

    in al, dx
    and al, 0b1000_0000
    cmp al, 0b1000_0000
    je .check_write_state