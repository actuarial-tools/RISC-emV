from riscemv.Tomasulo import Tomasulo
from riscemv.Program import Program


def test_tomasulo():
    xlen = 32
    n_adders = n_mult = n_div = n_ld = 1
    code_text = "addi x10, x9, 12"
    thread_id = 0

    tomasulo = Tomasulo(xlen, thread_id, n_adders, n_mult, n_div, n_ld, n_adders, n_mult, n_div, n_ld)
    P = Program(tomasulo.DM)
    P.load_text(code_text)

    for l in P:
        tomasulo.IFQ.put(l)
    tomasulo.Regs.PC.set_value(P.get_entry_point())

    reg_addr = 9
    tomasulo.Regs.writeInt(reg_addr, 0)

    tomasulo.step()

    tomasulo.step()

    tomasulo.step()

    assert tomasulo.Regs.readInt(10) == 12
