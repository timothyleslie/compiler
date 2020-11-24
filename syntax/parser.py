
prod = [('E\'', 'S\''),
        ('S\'', 'ID = S'),
        ('S\'', 'int ID'),
        ('S', 'S + A'),
        ('S', 'S - A'),
        ('S', 'A'),
        ('A', 'B'),
        ('A', 'A * B'),
        ('B', '( S )'),
        ('B', 'VAL'),
        ('B', 'ID')]

def nextAction(current_input, state):
    action_map = {}

    return action_map[(current_input, state)]


def gotoMap(no_terminal_char, state):
    goto_map = {}

    return goto_map[(no_terminal_char, state)]


if __name__ == '__main__':
    input_string = "<ID,a> <EQ,=> <ID,b> <PLUS,+> <ID,c> <SUB,-> <LP,(> <ID,c> <MUL,*> <ID,d> <SUB,-> <VAL,3> <RP,)> <EOL,#>"
    symTable = {'a': '', 'b': '', 'c': '', 'd': ''}
    input_tokens = input_string.split(' ')
    state_stack = []
    symbol_stack = []

    state_stack.append(0)
    symbol_stack.append(('EOL', '#'))
    step = 0
    Actions = ""

    while True:
        current_state = state_stack[-1]
        current_input = input_tokens[0][0]

        next_action = nextAction(current_input, current_state)

        if 's' in next_action:
            state_stack.append(int(next_action[1]))
            symbol_stack.append(input_tokens[0])
            input_tokens = input_tokens[1:]
            Actions += "Shift" + str(next_action[1]) + '\n'

        elif 'r' in next_action:
            prod_id = next_action[1]
            left_side = prod[prod_id][0]
            right_side = prod[prod_id][1]

            right_side_len = len(right_side.split(' '))
            for i in range(right_side_len):
                symbol_stack.pop()

            symbol_stack.append(left_side)
