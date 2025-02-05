# coding=utf-8

import pin

FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]

MOV = (0 << pin.ADDR2_SHIFT) | pin.ADDR2  # 1000_0000, 1000_ssdd
ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2  # 1001_0000, 1001_ssdd
SUB = (2 << pin.ADDR2_SHIFT) | pin.ADDR2  # 1010_0000, 1010_ssdd
CMP = (3 << pin.ADDR2_SHIFT) | pin.ADDR2
AND = (4 << pin.ADDR2_SHIFT) | pin.ADDR2
OR = (5 << pin.ADDR2_SHIFT) | pin.ADDR2
XOR = (6 << pin.ADDR2_SHIFT) | pin.ADDR2

INC = (0 << pin.ADDR1_SHIFT) | pin.ADDR1  # 0100_0000, 0100_00dd
DEC = (1 << pin.ADDR1_SHIFT) | pin.ADDR1  # 0100_0100, 0100_01dd
NOT = (2 << pin.ADDR1_SHIFT) | pin.ADDR1
JMP = (3 << pin.ADDR1_SHIFT) | pin.ADDR1

JO = (4 << pin.ADDR1_SHIFT) | pin.ADDR1  # 01010000, (0x50)
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1
JZ = (6 << pin.ADDR1_SHIFT) | pin.ADDR1
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1
JP = (8 << pin.ADDR1_SHIFT) | pin.ADDR1
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1

PUSH = (10 << pin.ADDR1_SHIFT) | pin.ADDR1
POP = (11 << pin.ADDR1_SHIFT) | pin.ADDR1

CALL = (12 << pin.ADDR1_SHIFT) | pin.ADDR1


NOP = 0     # 0000_0000
RET = 1
HLT = 0x3f  # 0011_1111

INSTRUCTIONS = {
    2: {
        MOV: {
            (pin.AM_REG, pin.AM_INS): [  # MOV A, 5
                pin.DST_W | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_REG): [  # MOV A, B
                pin.DST_W | pin.SRC_R,
            ],
            (pin.AM_REG, pin.AM_DIR): [  # MOV A, [5]
                pin.MAR_IN | pin.SRC_OUT,
                pin.DST_W | pin.RAM_OUT,
            ],
            (pin.AM_REG, pin.AM_RAM): [  # MOV A, [B]
                pin.SRC_R | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT,
            ],
            (pin.AM_DIR, pin.AM_INS): [  # MOV [0x9], 5
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_DIR, pin.AM_REG): [  # MOV [0x9], C
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_DIR, pin.AM_DIR): [  # MOV [0x3f], [0x2e]
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_DIR, pin.AM_RAM): [  # MOV [0x3f], [C]
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_INS): [  # MOV [A], 5
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_RAM, pin.AM_REG): [  # MOV [A], C
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_RAM, pin.AM_DIR): [  # MOV [A], [0x2e]
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_RAM): [  # MOV [A], [C]
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
        },
        ADD: {
            (pin.AM_REG, pin.AM_INS): [  # ADD D, 5
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [  # ADD D, C
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        SUB: {
            (pin.AM_REG, pin.AM_INS): [  # SUB D, 5
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [  # SUB D, C
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        CMP: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
        },
        AND: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        OR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        XOR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
    },
    1: {
        INC: {
            pin.AM_REG: [  # INC D
                pin.DST_R | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        DEC: {
            pin.AM_REG: [  # DEC D
                pin.DST_R | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        NOT: {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_NOT | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        JMP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JO: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNO: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JZ: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNZ: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        PUSH: {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_OUT | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_R | pin.RAM_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
        POP: {
            pin.AM_REG: [
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.DST_W | pin.RAM_OUT,
                pin.SP_OUT | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.SP_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
        CALL: {
            pin.AM_INS: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_OUT | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
            pin.AM_REG: [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.SP_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.PC_OUT | pin.RAM_IN,
                pin.DST_R | pin.PC_IN,
                pin.CS_OUT | pin.MSR_IN,
            ],
        },
    },
    0: {
        NOP: [
            pin.CYC,
        ],
        RET: [
            pin.SP_OUT | pin.MAR_IN,
            pin.SS_OUT | pin.MSR_IN,
            pin.PC_IN | pin.RAM_OUT,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.ALU_OUT | pin.SP_IN,
            pin.CS_OUT | pin.MSR_IN,
        ],
        HLT: [
            pin.HLT,
        ]
    }
}
