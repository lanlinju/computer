import os
import re
import pin
import assembly as ASM

dirname = os.path.dirname(__file__)

inputfile = os.path.join(dirname, 'program.asm')
outputfile = os.path.join(dirname, 'program.bin')

annotation = re.compile(r"(.*?);.*")

codes = []

OP2 = {
    'MOV': ASM.MOV, # 1000_0000, 0x80
}

OP1 = {
    
}

OP0 = {
    'NOP': ASM.NOP, # 0000_0000, 0x00
    'HLT': ASM.HLT, # 0011_1111, ox3f
}

OP2SET = set(OP2.values())
OP1SET = set(OP1.values())
OP0SET = set(OP0.values())

REGISTERS = {
    'A': pin.A,
    'B': pin.B,
    'C': pin.C,
    'D': pin.D,
}
        
class Code(object):
    
    def __init__(self, number, source):
        self.number = number
        self.source = source.upper()
        self.op = None
        self.dst = None 
        self.src = None
        self.prepare_source() # 解析op, dst, src
        
    def get_op(self): # 获取操作码二进制指令
        if self.op in OP2:
            return OP2[self.op]
        if self.op in OP1:
            return OP1[self.op]
        if self.op in OP0:
            return OP0[self.op]
        raise SyntaxError(self)
    
    def get_am(self, addr):
        if not addr:
            return 0, 0
        if addr in REGISTERS: # 寄存器寻址
            return pin.AM_REG, REGISTERS[addr]
        if re.match(r'^[0-9]+$', addr): # 立即数寻址
            return pin.AM_INS, int(addr) 
        if re.match(r'0X[0-9A-F]+$', addr): # 立即数寻址, 16进制
            return pin.AM_INS, int(addr, 16)
        match = re.match(r'^\[([0-9]+)\]$', addr) # 直接寻址
        if match:
            return pin.AM_DIR, int(match.group(1))
        match = re.match(r'^\[(0X[0-9A-F]+)\]$', addr) # 直接寻址, 16进制
        if match:   
            return pin.AM_DIR, int(match.group(1), 16)
        match = re.match(r'^\[(.+)\]$', addr)
        if match and match.group(1) in REGISTERS:
            return pin.AM_RAM, REGISTERS[match.group(1)]

        raise SyntaxError(self) 
            
    def prepare_source(self):
        tub = self.source.split(',')
        if len(tub) > 2:
            raise SyntaxError(self)
        if len(tub) == 2:
            self.src = tub[1].strip() # 源操作数
            
        tub = re.split(r" +", tub[0])
        if len(tub) > 2:
            raise SyntaxError(self)
        if len(tub) == 2:
            self.dst = tub[1].strip() # 目标操作数
            
        self.op = tub[0].strip() # 操作码
        
    def compile_code(self):
        op = self.get_op()
        
        amd, dst = self.get_am(self.dst)
        ams, src = self.get_am(self.src)
        
        if src and (amd, ams) not in ASM.INSTRUCTIONS[2][op]:
            raise SyntaxError(self)
        if not src and dst and amd not in ASM.INSTRUCTIONS[1][op]:
            raise SyntaxError(self)
        if not src and not dst and op not in ASM.INSTRUCTIONS[0]:
            raise SyntaxError(self)
        
        if op in OP2SET:
            ir = op | (amd << 2) | ams
        elif op in OP1SET:
            ir = op | amd
        elif op in OP0SET:
            ir = op
        
        return [ir, dst, src]
        
    def __repr__(self):
        return f"[{self.number}] - {self.source}"

class SyntaxError(Exception):
    
    def __init__(self, code: Code, *args):
        super().__init__(*args)
        self.code = code

def compile_program():
    with open(inputfile, encoding='utf-8') as file:
        lines = file.readlines()
        
        for index, line in enumerate(lines):
            source = line.strip()
            if ';' in source: # 去除注释信息
                source = annotation.match(source).group(1)
            if not source:
                continue
            code = Code(index + 1, source)
            codes.append(code)
            
        with open(outputfile, 'wb') as file:
            for code in codes:
                values = code.compile_code()
                for value in values:
                    result = value.to_bytes(1, byteorder='little')
                    file.write(result)
            

def main():
    try:
        compile_program()
    except SyntaxError as e:
        print(f"SyntaxError: {e.code}")
        return
    
    print('Program.asm has been compiled successfully!')
    
if __name__ == '__main__':
    main()