offset equ 0x0000
data equ 0x55aa

mov ax, 0x1000
mov ds, ax

mov al, 0x10
mov ah, 0x10
mov ax, data

mov ax, [offset] ;0x1000 * 0x10 + 0 = 0x10000
mov [offset], ax

mov byte [offset], 0x10
mov word [offset], 0x10
mov dword [offset], 0xaabbccdd

; bx bp si di

mov ax, [bx] ; [ds * 16 + bx]
mov ax, [bp] ; [ss * 16 + bp]
mov ax, [si] ; [ds * 16 + si]
mov ax, [di] ; [ds * 16 + di]

mov ax, [bx + si + 0x10] ; ds
mov ax, [bp + si + 0x10] ; ss
mov ax, [bp + di + 0x10] 