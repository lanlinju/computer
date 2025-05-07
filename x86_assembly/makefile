build/%.bin: src/%.asm
	nasm -f bin -o $@ $<

build/master.img: build/boot.bin build/loader.bin
ifeq ("$(wildcard build/master.img)", "")
	bximage -q -hd=16M -func=create -sectsize=512 -imgmode=flat $@
endif
	dd if=build/boot.bin of=build/master.img bs=512 count=1 conv=notrunc
	dd if=build/loader.bin of=build/master.img bs=512 count=4 seek=2 conv=notrunc

.PHONY: bochs
bochs: build/master.img
	cd build && bochs-debugger -q -debugger -f bochsrc -unlock

.PHONY: clean
clean:
	rm -rf build/master.img
	rm -rf build/*.bin