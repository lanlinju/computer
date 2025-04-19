boot.bin: boot.asm
	nasm -f bin -o boot.bin boot.asm

master.img: boot.bin
	dd if=boot.bin of=master.img bs=512 count=1 conv=notrunc

.PHONY: bochs
bochs: master.img
	bochs-debugger -q -unlock

.PHONY: clean
clean:
	rm -rf *.bin