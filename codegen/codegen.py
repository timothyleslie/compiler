regs = [-1 for i in range(32)]
sym_table = {}
middle_code = []
target_code = []


def reg_alloc(symbol):
    if symbol is None:
        return "$0"
    for i in range(1, 32):
        if regs[i] == symbol:
            return "$" + str(i)

    for i in range(1, 32):
        if regs[i] == -1:
            regs[i] = symbol
            return "$" + str(i)


def op_change(op):
    if op == 'assign':
        return 'addi'
    else:
        return op


def get_symbol_table():
    with open('./data/symbol_table.txt', 'r') as st:
        for line in st:
            line = line[:-1]
            symbol, type, addr = line.split(',')
            sym_table[symbol] = [addr, type]


def get_middle_code():
    with open('./data/semantic_out.txt', 'r') as mc:
        for line in mc:
            line = line[:-1]
            middle_code.append(line)


def move_symbol(symbol):
    op = "lw"
    dst = reg_alloc(symbol)
    src1 = str(sym_table[symbol][0]) + "($0)"
    target_code.append([op, dst, src1, None])


def code_gen():
    for line in middle_code:
        try:
            op, dst, src1, src2 = line.split(',')
        except ValueError:
            op, dst, src1 = line.split(',')
            src2 = None
        # print(src2)
        dst_reg = reg_alloc(dst)
        s1_reg = reg_alloc(src1)
        s2_reg = reg_alloc(src2)
        op = op_change(op)
        target_code.append([op, dst_reg, s1_reg, s2_reg])


def write_back_symbol():
    for symbol in sym_table.keys():
        symbol_reg = reg_alloc(symbol)
        op = 'sw'
        dst = str(sym_table[symbol][0]) + "($0)"
        target_code.append([op, symbol_reg, dst, None])


def write_result():
    with open('./data/target_code.txt', 'w') as result:
        for line in target_code:
            result.write(line[0] + ' ')
            result.write(line[1] + ', ')
            result.write(line[2])
            if line[3] is not None:
                result.write(' ,' + line[3])
            result.write('\n')


def main():
    get_symbol_table()
    get_middle_code()
    for symbol in sym_table.keys():
        reg_alloc(symbol)
        move_symbol(symbol)
    code_gen()
    write_back_symbol()
    write_result()


if __name__ == '__main__':
    main()
