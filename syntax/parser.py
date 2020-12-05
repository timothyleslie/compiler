# -----------------------Production Rule-----------------------
prod = [('S\'', 'ID = S'),
        ('S\'', 'int ID'),
        ('S', 'S + A'),
        ('S', 'S - A'),
        ('S', 'A'),
        ('A', 'B'),
        ('A', 'A * B'),
        ('B', '( S )'),
        ('B', 'VAL'),
        ('B', 'ID')]

# -----------------------Action-----------------------
actions_map = {}
actions_map[('PLUS', 6)] = ('s', 12)
actions_map[('PLUS', 7)] = ('r', 4)
actions_map[('PLUS', 8)] = ('r', 5)
actions_map[('PLUS', 10)] = ('r', 9)
actions_map[('PLUS', 11)] = ('r', 9)
actions_map[('PLUS', 15)] = ('s', 24)
actions_map[('PLUS', 16)] = ('r', 4)
actions_map[('PLUS', 17)] = ('r', 5)
actions_map[('PLUS', 19)] = ('r', 9)
actions_map[('PLUS', 20)] = ('r', 8)
actions_map[('PLUS', 21)] = ('r', 2)
actions_map[('PLUS', 22)] = ('r', 3)
actions_map[('PLUS', 23)] = ('r', 6)
actions_map[('PLUS', 26)] = ('r', 7)
actions_map[('PLUS', 28)] = ('s', 24)
actions_map[('PLUS', 29)] = ('r', 2)
actions_map[('PLUS', 30)] = ('r', 3)
actions_map[('PLUS', 31)] = ('r', 6)
actions_map[('PLUS', 32)] = ('r', 7)
actions_map[('MINUS', 6)] = ('s', 13)
actions_map[('MINUS', 7)] = ('r', 4)
actions_map[('MINUS', 8)] = ('r', 5)
actions_map[('MINUS', 10)] = ('r', 9)
actions_map[('MINUS', 11)] = ('r', 8)
actions_map[('MINUS', 15)] = ('s', 25)
actions_map[('MINUS', 16)] = ('r', 4)
actions_map[('MINUS', 17)] = ('r', 5)
actions_map[('MINUS', 19)] = ('r', 9)
actions_map[('MINUS', 20)] = ('r', 8)
actions_map[('MINUS', 21)] = ('r', 2)
actions_map[('MINUS', 22)] = ('r', 3)
actions_map[('MINUS', 23)] = ('r', 6)
actions_map[('MINUS', 26)] = ('r', 7)
actions_map[('MINUS', 28)] = ('s', 25)
actions_map[('MINUS', 29)] = ('r', 2)
actions_map[('MINUS', 30)] = ('r', 3)
actions_map[('MINUS', 31)] = ('r', 6)
actions_map[('MINUS', 32)] = ('r', 7)
actions_map[('MULTI', 7)] = ('s', 14)
actions_map[('MULTI', 8)] = ('r', 5)
actions_map[('MULTI', 10)] = ('r', 9)
actions_map[('MULTI', 11)] = ('r', 8)
actions_map[('MULTI', 16)] = ('s', 27)
actions_map[('MULTI', 17)] = ('r', 5)
actions_map[('MULTI', 19)] = ('r', 9)
actions_map[('MULTI', 20)] = ('r', 8)
actions_map[('MULTI', 21)] = ('s', 14)
actions_map[('MULTI', 22)] = ('s', 14)
actions_map[('MULTI', 23)] = ('r', 6)
actions_map[('MULTI', 26)] = ('r', 7)
actions_map[('MULTI', 29)] = ('s', 27)
actions_map[('MULTI', 30)] = ('s', 27)
actions_map[('MULTI', 31)] = ('r', 6)
actions_map[('MULTI', 32)] = ('r', 7)
actions_map[('OPEN_PAREN', 5)] = ('s', 9)
actions_map[('OPEN_PAREN', 9)] = ('s', 18)
actions_map[('OPEN_PAREN', 12)] = ('s', 9)
actions_map[('OPEN_PAREN', 13)] = ('s', 9)
actions_map[('OPEN_PAREN', 14)] = ('s', 9)
actions_map[('OPEN_PAREN', 18)] = ('s', 18)
actions_map[('OPEN_PAREN', 24)] = ('s', 18)
actions_map[('OPEN_PAREN', 25)] = ('s', 18)
actions_map[('OPEN_PAREN', 27)] = ('s', 18)
actions_map[('CLOSE_PAREN', 15)] = ('s', 26)
actions_map[('CLOSE_PAREN', 16)] = ('r', 4)
actions_map[('CLOSE_PAREN', 17)] = ('r', 5)
actions_map[('CLOSE_PAREN', 19)] = ('r', 9)
actions_map[('CLOSE_PAREN', 20)] = ('r', 8)
actions_map[('CLOSE_PAREN', 28)] = ('s', 32)
actions_map[('CLOSE_PAREN', 29)] = ('r', 2)
actions_map[('CLOSE_PAREN', 30)] = ('r', 3)
actions_map[('CLOSE_PAREN', 31)] = ('r', 6)
actions_map[('CLOSE_PAREN', 32)] = ('r', 7)
actions_map[('ASSIGN', 3)] = ('s', 5)
actions_map[('ID', 0)] = ('s', 3)
actions_map[('ID', 2)] = ('s', 4)
actions_map[('ID', 5)] = ('s', 10)
actions_map[('ID', 9)] = ('s', 19)
actions_map[('ID', 12)] = ('s', 10)
actions_map[('ID', 13)] = ('s', 10)
actions_map[('ID', 14)] = ('s', 10)
actions_map[('ID', 18)] = ('s', 19)
actions_map[('ID', 24)] = ('s', 19)
actions_map[('ID', 25)] = ('s', 19)
actions_map[('ID', 27)] = ('s', 19)
actions_map[('INT_NUM', 5)] = ('s', 11)
actions_map[('INT_NUM', 9)] = ('s', 20)
actions_map[('INT_NUM', 12)] = ('s', 11)
actions_map[('INT_NUM', 13)] = ('s', 11)
actions_map[('INT_NUM', 14)] = ('s', 11)
actions_map[('INT_NUM', 18)] = ('s', 20)
actions_map[('INT_NUM', 24)] = ('s', 20)
actions_map[('INT_NUM', 25)] = ('s', 20)
actions_map[('INT_NUM', 27)] = ('s', 20)
actions_map[('EOL', 1)] = ('a', 0)
actions_map[('EOL', 4)] = ('r', 1)
actions_map[('EOL', 6)] = ('r', 0)
actions_map[('EOL', 7)] = ('r', 4)
actions_map[('EOL', 8)] = ('r', 5)
actions_map[('EOL', 10)] = ('r', 9)
actions_map[('EOL', 11)] = ('r', 8)
actions_map[('EOL', 21)] = ('r', 2)
actions_map[('EOL', 22)] = ('r', 3)
actions_map[('EOL', 23)] = ('r', 6)
actions_map[('EOL', 26)] = ('r', 7)
actions_map[('INT', 0)] = ('s', 2)

# -----------------------Goto-----------------------
goto_map = {}
goto_map[('S\'', 0)] = 1

goto_map[('S', 5)] = 6
goto_map[('S', 9)] = 15
goto_map[('S', 18)] = 28

goto_map[('A', 5)] = 7
goto_map[('A', 9)] = 16
goto_map[('A', 12)] = 21
goto_map[('A', 13)] = 22
goto_map[('A', 18)] = 16
goto_map[('A', 24)] = 29
goto_map[('A', 25)] = 30

goto_map[('B', 5)] = 8
goto_map[('B', 9)] = 17
goto_map[('B', 12)] = 8
goto_map[('B', 13)] = 8
goto_map[('B', 14)] = 23
goto_map[('B', 18)] = 17
goto_map[('B', 24)] = 17
goto_map[('B', 25)] = 17
goto_map[('B', 27)] = 31

symbols_table = {}


def read_symbol_table():
    with open("../lab1/symbol_table.txt") as st:
        for line in st:
            address, symbol, type = line.split(',')
            symbols_table[symbol] = [type, address]


class tmpNums():
    def __init__(self):
        self.tmpNum = -1

    def newtmpNum(self):
        self.tmpNum += 1
        return 't' + str(self.tmpNum)


def parse_input(input_string):
    ret = []
    input_tokens = input_string.split('\n')
    for item in input_tokens:
        item = item[1:-1]
        item = item.replace(' ', '')
        item = item.split(',')
        ret.append(item)
    return ret


def find_action(current_input, state):
    return actions_map[(current_input, state)]


def find_goto(no_terminal_char, state):
    return goto_map[(no_terminal_char, state)]


def write_result(result, semantic_actions):
    with open('parser_out.txt', 'w') as output_file:
        for item in result:
            output_file.write(item)
            output_file.write('\n')
    # print(semantic_actions)
    with open('semantic_out.txt', 'w') as f:
        for item in semantic_actions:
            f.write(item)
            f.write('\n')


def semantic_aciton(prod, symbols):
    global semantic_acitons
    # print('symbols', symbols)
    # print(symbols_table)
    if prod == 0:
        str = ("assign," + symbols[2][1] + ',' + symbols[0][1])
        ret = ['S\'', symbols[2][1]]
        semantic_acitons.append(str)

    elif prod == 1:
        symbols_table[symbols[0][1]][0] = 'int'
        ret = ['S\'', 'INT']
    elif prod == 2:
        newtmp = tmpNums().newtmpNum()
        str = ("add," + newtmp + "," + symbols[2][1] + ',' + symbols[0][1])
        semantic_acitons.append(str)
        ret = ['S', newtmp]
    elif prod == 3:
        newtmp = tmpNums().newtmpNum()
        str = ("sub," + newtmp + "," + symbols[2][1] + ',' + symbols[0][1])
        semantic_acitons.append(str)
        ret = ['S', newtmp]
    elif prod == 4:
        ret = ['S', symbols[0][1]]
    elif prod == 5:
        ret = ['A', symbols[0][1]]
    elif prod == 6:
        newtmp = tmpNums().newtmpNum()
        str = ("mul," + newtmp + "," + symbols[2][1] + ',' + symbols[0][1])
        semantic_acitons.append(str)
        ret = ['A', newtmp]
    elif prod == 7:
        ret = ['B', symbols[1][1]]
    elif prod == 8:
        newtmp = tmpNums().newtmpNum()
        str = ("assign_const," + newtmp + "," + symbols[0][1] + "," + ' ')
        semantic_acitons.append(str)
        ret = ['B', newtmp]
    elif prod == 9:
        ret = ['B', symbols[0][1]]
    else:
        print("Error!!")
        return
    # print(semantic_acitons)
    return ret


if __name__ == '__main__':
    fp = open("../lab1/token.txt", 'r')
    read_symbol_table()
    fp = fp.read()
    input_tokens = parse_input(fp)
    # print(input_tokens)
    state_stack = []
    symbol_stack = []

    state_stack.append(0)
    symbol_stack.append(('EOL', '#', 'None'))
    semantic_acitons = []
    result = []
    while True:
        current_state = state_stack[-1]
        current_input = input_tokens[0][0]
        poped_symbols = []
        # print(current_state)
        # print(current_input)
        try:
            next_action = find_action(current_input, current_state)
        except KeyError:
            print("Error0")
            exit(-1)

        if 's' in next_action:
            state_stack.append(int(next_action[1]))
            symbol_stack.append(input_tokens[0])
            input_tokens = input_tokens[1:]

        elif 'r' in next_action:
            prod_id = next_action[1]
            left_side = prod[prod_id][0]
            right_side = prod[prod_id][1]
            right_side_len = len(right_side.split(' '))
            for i in range(right_side_len):
                poped_symbols.append(symbol_stack.pop())
                state_stack.pop()

            # print('popsymbol: ', poped_symbols)
            left_string = semantic_aciton(prod_id, poped_symbols)
            symbol_stack.append(left_string)

            try:
                next_state = find_goto(left_side, state_stack[-1])
            except KeyError:
                print("Error1")
                exit(-1)
            state_stack.append(next_state)
            result_str = left_side + "->" + right_side
            result.append(result_str)

        elif 'a' in next_action:
            print("Accept!")
            write_result(result, semantic_acitons)
            break

        else:
            print("Error2")
            exit(-1)

