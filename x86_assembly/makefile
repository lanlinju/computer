%.bin: %.asm
	nasm -f bin -o $@ $<

master.img: boot.bin
ifeq ("$(wildcard master.img)", "")
	bximage -q -hd=16M -func=create -sectsize=512 -imgmode=flat $@
endif
	dd if=$< of=$@ bs=512 count=1 conv=notrunc

.PHONY: bochs
bochs: master.img
	bochs-debugger -q -debugger -f bochsrc -unlock

.PHONY: clean
clean:
	rm -rf master.img
	rm -rf *.bin