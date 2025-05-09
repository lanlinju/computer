	.file	"hello.c"
	.text
	.section	.rodata
.LC0:
	.string	"hello world!!!"
	.text
	.globl	main
	.type	main, @function
main:
	pushl	%ebp
	movl	%esp, %ebp
	pushl	$.LC0
	call	puts
	addl	$4, %esp
	movl	$0, %eax
	leave
	ret
	.size	main, .-main
	.ident	"GCC: (GNU) 15.1.1 20250425 (Red Hat 15.1.1-1)"
	.section	.note.GNU-stack,"",@progbits
