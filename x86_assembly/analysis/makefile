CFLAGS:= -m32 \
		 -O0 \
		 -fno-asynchronous-unwind-tables \
		 -fno-pic \
		 -mpreferred-stack-boundary=2 \
		#  -fno-stack-protector \
		#  -fno-builtin \
		#  -fomit-frame-pointer \
		#  -static \
		#  -fverbose-asm \

CC:=gcc

.PHONY: hello.s
hello.s: hello.c
	gcc $(CFLAGS) -S $< -o $@