[org 0x1000]

xchg bx, bx
mov ax, 0xb800
mov es, ax
mov byte [es:0], 'L'

xchg bx, bx

jmp $
