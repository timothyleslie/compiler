# -----------------------Production Rule-----------------------
prodID = {('S\'', 'ID = S'): 0,
          ('S\'', 'int ID'): 1,
          ('S', 'S + A'): 2,
          ('S', 'S - A'): 3,
          ('S', 'A'): 4,
          ('A', 'B'): 5,
          ('A', 'A * B'): 6,
          ('B', '( S )'): 7,
          ('B', 'VAL'): 8,
          ('B', 'ID'): 9}

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
actions_map[('PLUS', 7)] = ('r', prodID[('S', 'A')])
actions_map[('PLUS', 8)] = ('r', prodID[('A', 'B')])
actions_map[('PLUS', 10)] = ('r', prodID[('B', 'ID')])
actions_map[('PLUS', 11)] = ('r', prodID[('B', 'ID')])
actions_map[('PLUS', 15)] = ('s', 24)
actions_map[('PLUS', 16)] = ('r', prodID[('S', 'A')])
actions_map[('PLUS', 17)] = ('r', prodID[('A', 'B')])
actions_map[('PLUS', 19)] = ('r', prodID[('B', 'ID')])
actions_map[('PLUS', 20)] = ('r', prodID[('B', 'VAL')])
actions_map[('PLUS', 21)] = ('r', prodID[('S', 'S + A')])
actions_map[('PLUS', 22)] = ('r', prodID[('S', 'S - A')])
actions_map[('PLUS', 23)] = ('r', prodID[('A', 'A * B')])
actions_map[('PLUS', 26)] = ('r', prodID[('B', '( S )')])
actions_map[('PLUS', 28)] = ('s', 24)
actions_map[('PLUS', 29)] = ('r', prodID[('S', 'S + A')])
actions_map[('PLUS', 30)] = ('r', prodID[('S', 'S - A')])
actions_map[('PLUS', 31)] = ('r', prodID[('A', 'A * B')])
actions_map[('PLUS', 32)] = ('r', prodID[('B', '( S )')])

actions_map[('SUB', 6)] = ('s', 13)
actions_map[('SUB', 7)] = ('r', prodID[('S', 'A')])
actions_map[('SUB', 8)] = ('r', prodID[('A', 'B')])
actions_map[('SUB', 10)] = ('r', prodID[('B', 'ID')])
actions_map[('SUB', 11)] = ('r', prodID[('B', 'VAL')])
actions_map[('SUB', 15)] = ('s', 25)
actions_map[('SUB', 16)] = ('r', prodID[('S', 'A')])
actions_map[('SUB', 17)] = ('r', prodID[('A', 'B')])
actions_map[('SUB', 19)] = ('r', prodID[('B', 'ID')])
actions_map[('SUB', 20)] = ('r', prodID[('B', 'VAL')])
actions_map[('SUB', 21)] = ('r', prodID[('S', 'S + A')])
actions_map[('SUB', 22)] = ('r', prodID[('S', 'S - A')])
actions_map[('SUB', 23)] = ('r', prodID[('A', 'A * B')])
actions_map[('SUB', 26)] = ('r', prodID[('B', '( S )')])
actions_map[('SUB', 28)] = ('s', 25)
actions_map[('SUB', 29)] = ('r', prodID[('S', 'S + A')])
actions_map[('SUB', 30)] = ('r', prodID[('S', 'S - A')])
actions_map[('SUB', 31)] = ('r', prodID[('A', 'A * B')])
actions_map[('SUB', 32)] = ('r', prodID[('B', '( S )')])

actions_map[('MUL', 7)] = ('s', 14)
actions_map[('MUL', 8)] = ('r', prodID[('A', 'B')])
actions_map[('MUL', 10)] = ('r', prodID[('B', 'ID')])
actions_map[('MUL', 11)] = ('r', prodID[('B', 'VAL')])
actions_map[('MUL', 16)] = ('s', 27)
actions_map[('MUL', 17)] = ('r', prodID[('A', 'B')])
actions_map[('MUL', 19)] = ('r', prodID[('B', 'ID')])
actions_map[('MUL', 20)] = ('r', prodID[('B', 'VAL')])
actions_map[('MUL', 21)] = ('s', 14)
actions_map[('MUL', 22)] = ('s', 14)
actions_map[('MUL', 23)] = ('r', prodID[('A', 'A * B')])
actions_map[('MUL', 26)] = ('r', prodID[('B', '( S )')])
actions_map[('MUL', 29)] = ('s', 27)
actions_map[('MUL', 30)] = ('s', 27)
actions_map[('MUL', 31)] = ('r', prodID[('A', 'A * B')])
actions_map[('MUL', 32)] = ('r', prodID[('B', '( S )')])

actions_map[('LP', 5)] = ('s', 9)
actions_map[('LP', 9)] = ('s', 18)
actions_map[('LP', 12)] = ('s', 9)
actions_map[('LP', 13)] = ('s', 9)
actions_map[('LP', 14)] = ('s', 9)
actions_map[('LP', 18)] = ('s', 18)
actions_map[('LP', 24)] = ('s', 18)
actions_map[('LP', 25)] = ('s', 18)
actions_map[('LP', 27)] = ('s', 18)

actions_map[('RP', 15)] = ('s', 26)
actions_map[('RP', 16)] = ('r', prodID[('S', 'A')])
actions_map[('RP', 17)] = ('r', prodID[('A', 'B')])
actions_map[('RP', 19)] = ('r', prodID[('B', 'ID')])
actions_map[('RP', 20)] = ('r', prodID[('B', 'VAL')])
actions_map[('RP', 28)] = ('s', 32)
actions_map[('RP', 29)] = ('r', prodID[('S', 'S + A')])
actions_map[('RP', 30)] = ('r', prodID[('S', 'S - A')])
actions_map[('RP', 31)] = ('r', prodID[('A', 'A * B')])
actions_map[('RP', 32)] = ('r', prodID[('B', '( S )')])

actions_map[('EQ', 3)] = ('s', 5)

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

actions_map[('VAL', 5)] = ('s', 11)
actions_map[('VAL', 9)] = ('s', 20)
actions_map[('VAL', 12)] = ('s', 11)
actions_map[('VAL', 13)] = ('s', 11)
actions_map[('VAL', 14)] = ('s', 11)
actions_map[('VAL', 18)] = ('s', 20)
actions_map[('VAL', 24)] = ('s', 20)
actions_map[('VAL', 25)] = ('s', 20)
actions_map[('VAL', 27)] = ('s', 20)

actions_map[('EOL', 1)] = ('a', 0)
actions_map[('EOL', 4)] = ('r', prodID[('S\'', 'int ID')])
actions_map[('EOL', 6)] = ('r', prodID[('S\'', 'ID = S')])
actions_map[('EOL', 7)] = ('r', prodID[('S', 'A')])
actions_map[('EOL', 8)] = ('r', prodID[('A', 'B')])
actions_map[('EOL', 10)] = ('r', prodID[('B', 'ID')])
actions_map[('EOL', 11)] = ('r', prodID[('B', 'VAL')])
actions_map[('EOL', 21)] = ('r', prodID[('S', 'S + A')])
actions_map[('EOL', 22)] = ('r', prodID[('S', 'S - A')])
actions_map[('EOL', 23)] = ('r', prodID[('A', 'A * B')])
actions_map[('EOL', 26)] = ('r', prodID[('B', '( S )')])

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


def parse_input(input_string):
    ret = []
    input_tokens = input_string.split(' ')
    for item in input_tokens:
        item = item[1:-1]
        item = item.split(',')
        ret.append(item)
    return ret


def find_action(current_input, state):
    return actions_map[(current_input, state)]


def find_goto(no_terminal_char, state):
    return goto_map[(no_terminal_char, state)]


def write_result(result):
    with open('parser_out.txt', 'w') as output_file:
        for item in result:
            output_file.write(item)
            output_file.write('\n')


if __name__ == '__main__':
    input_string = "<ID,a> <EQ,=> <ID,b> <PLUS,+> <ID,c> <SUB,-> <LP,(> <ID,c> <MUL,*> <ID,d> <SUB,-> <VAL,3> <RP,)> <EOL,#>"
    symTable = {'a': '', 'b': '', 'c': '', 'd': ''}
    input_tokens = parse_input(input_string)
    state_stack = []
    symbol_stack = []

    state_stack.append(0)
    symbol_stack.append(('EOL', '#'))
    step = 0
    Actions = ""
    result = []
    while True:
        current_state = state_stack[-1]
        current_input = input_tokens[0][0]
        try:
            next_action = find_action(current_input, current_state)
        except KeyError:
            print("Error0")
            exit(-1)

        if 's' in next_action:
            state_stack.append(int(next_action[1]))
            symbol_stack.append(input_tokens[0])
            input_tokens = input_tokens[1:]
            Actions += "Shift " + str(next_action[1]) + '\n'

        elif 'r' in next_action:
            prod_id = next_action[1]
            left_side = prod[prod_id][0]
            right_side = prod[prod_id][1]

            right_side_len = len(right_side.split(' '))
            for i in range(right_side_len):
                symbol_stack.pop()
                state_stack.pop()

            symbol_stack.append(left_side)

            try:
                next_state = find_goto(left_side, state_stack[-1])
            except KeyError:
                print("Error1")
                exit(-1)
            state_stack.append(next_state)
            result_str = left_side + "->" + right_side
            result.append(result_str)
            Actions += "Reduce" + result_str + '\n'

        elif 'a' in next_action:
            print("Accept!")
            write_result(result)
            break

        else:
            print("Error2")
            exit(-1)

    print(Actions)
