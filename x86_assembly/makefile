build/%.bin: src/%.asm
	nasm -f bin -o $@ $<

build/master.img: build/boot.bin
ifeq ("$(wildcard build/master.img)", "")
	bximage -q -hd=16M -func=create -sectsize=512 -imgmode=flat $@
endif
	dd if=$< of=$@ bs=512 count=1 conv=notrunc

.PHONY: bochs
bochs: build/master.img
	cd build && bochs-debugger -q -debugger -f build/bochsrc -unlock

.PHONY: clean
clean:
	rm -rf build/master.img
	rm -rf build/*.bin