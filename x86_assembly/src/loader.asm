[org 0x1000]

xchg bx, bx

check_memory:
    mov ax, 0
    mov es, ax
    xor ebx, ebx
    mov edx, 0x534d4150
    mov di, ards_buffer

.next:
    mov eax, 0xE820
    mov ecx, 20
    int 0x15

    jc .error

    add di, cx
    inc word [ards_cout]
    cmp ebx, 0
    jnz .next

    jmp prepare_protext_mode

.error:
    mov ax, 0xb800
    mov es, ax
    mov byte [es:0], 'E'
    jmp $

prepare_protext_mode:
    cli; 关闭中断

    ; 打开 A20 线
    in al, 0x92
    or al, 0b10
    out 0x92, al

    lgdt [gdt_ptr]; 加载gdt

    mov eax, cr0
    or eax, 1
    mov cr0, eax 

    jmp dword code_selector:protect_enable

    ud2; 出错

jmp $

[bits 32]
protect_enable:
    mov ax, data_selector
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov fs, ax
    mov gs, ax; 初始化数据段

    mov esp, 0x10000

    xchg bx, bx    

    call setup_page
    xchg bx, bx    
    mov byte [0xC00b8000], 'P'
    xchg bx, bx    

    jmp $

PDE equ 0x2000
PTE equ 0x3000
ATTR equ 0b11

setup_page:
    mov eax, PDE
    call .clear_page
    mov eax, PTE
    call .clear_page

    ; 前面的 1M 内映射到 前面的 1M
    ; 前面的 1M 内映射到 0xC0000000 ~ 0xC0100000
    mov eax, PTE
    or eax, ATTR
    mov [PDE], eax              ; 0b_00000_00000_00000_00000_00000_00000_00
    mov [PDE + 0x300 * 4], eax  ; 0b_11000_00000_00000_00000_00000_00000_00

    mov eax, PDE
    or eax, ATTR
    mov [PDE +0x3ff * 4], eax   ;把最后一个页表指向页目录

    mov ebx, PTE
    mov ecx, (0x100000 / 0x1000) ;256
    mov esi, 0
    ; xchg bx, bx
.next_page:
    mov eax, esi
    shl eax, 12
    or eax, ATTR
    mov [ebx + esi * 4], eax
    inc esi
    loop .next_page

    ; xchg bx, bx
    mov eax, PDE
    mov cr3, eax

    mov eax, cr0
    or eax, 0b1000_0000_0000_0000_0000_0000_0000_0000
    mov cr0, eax

    ret    

.clear_page:
    ; 清空一个内存页，地址参数在 eax 中
    mov ecx, 0x1000
    mov esi, 0
.set:
    mov byte [eax + esi], 0
    inc esi
    loop .set
    ret

code_selector equ (1 << 3)
data_selector equ (2 << 3)
test_selector equ (3 << 3)

gdt_ptr:
    dw (gdt_end - gdt_base - 1)
    dd gdt_base

gdt_base:
    dd 0, 0
gdt_code:
    dw 0xffff
    dw 0
    db 0
    db 0b1001_1110
    db 0b1100_1111 
    db 0
gdt_data:
    dw 0xffff
    dw 0
    db 0
    db 0b1001_0010
    db 0b1100_1111
    db 0
gdt_test:
    dw 0xfff
    dw 0x0000
    db 0x1
    db 0b1001_0010 ; 0x92
    db 0b0100_0000 ; 0x40
    db 0x0
gdt_end:

ards_cout:
    dw 0
ards_buffer:
