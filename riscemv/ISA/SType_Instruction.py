import os, json
from riscemv.ISA.Instruction import Instruction


class SType_Instruction(Instruction):
    def __init__(self, opcode, imm, funct3, rs1, rs2):
        self.opcode = opcode
        self.imm = imm
        self.funct3 = funct3
        self.rs1 = rs1
        self.rs2 = rs2


    @staticmethod
    def parse(binary_code):
        imm11 = binary_code[:7]
        rs2 = int(binary_code[7:12], 2)
        rs1 = int(binary_code[12:17], 2)
        funct3 = binary_code[17:20]
        imm4 = binary_code[20:25]
        opcode = binary_code[25:32]
        imm = int(imm11 + imm4, 2)
        return SType_Instruction(opcode, imm, funct3, rs1, rs2)


    def execute(self, rs_value):
        code = self.execution_code
        code = code.replace('rs', str(rs_value))

        return eval(code)
