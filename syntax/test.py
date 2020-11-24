# coding:UTF-8

class Stack(object):  # 栈的实现
    def __init__(self):
        self.items = []

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def show(self):
        print(str(self.items).ljust(50), end='')


class tmpNum():
    def __init__(self):
        self.tempNum = -1

    def newtmpNum(self):
        self.tempNum = self.tempNum + 1
        return 't' + str(self.tempNum)


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


def nextAction(char, state):
    actions_map = {}

    actions_map[('PLUS', 6)] = 's 12'
    actions_map[('PLUS', 7)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('PLUS', 8)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('PLUS', 10)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('PLUS', 11)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('PLUS', 15)] = 's 24'
    actions_map[('PLUS', 16)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('PLUS', 17)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('PLUS', 19)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('PLUS', 20)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('PLUS', 21)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('PLUS', 22)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('PLUS', 23)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('PLUS', 26)] = 'r ' + str(prodID[('B', '( S )')])
    actions_map[('PLUS', 28)] = 's 24'
    actions_map[('PLUS', 29)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('PLUS', 30)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('PLUS', 31)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('PLUS', 32)] = 'r ' + str(prodID[('B', '( S )')])

    actions_map[('SUB', 6)] = 's 13'
    actions_map[('SUB', 7)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('SUB', 8)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('SUB', 10)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('SUB', 11)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('SUB', 15)] = 's 25'
    actions_map[('SUB', 16)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('SUB', 17)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('SUB', 19)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('SUB', 20)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('SUB', 21)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('SUB', 22)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('SUB', 23)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('SUB', 26)] = 'r ' + str(prodID[('B', '( S )')])
    actions_map[('SUB', 28)] = 's 25'
    actions_map[('SUB', 29)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('SUB', 30)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('SUB', 31)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('SUB', 32)] = 'r ' + str(prodID[('B', '( S )')])

    actions_map[('MUL', 7)] = 's 14'
    actions_map[('MUL', 8)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('MUL', 10)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('MUL', 11)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('MUL', 16)] = 's 27'
    actions_map[('MUL', 17)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('MUL', 19)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('MUL', 20)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('MUL', 21)] = 's 14'
    actions_map[('MUL', 22)] = 's 14'
    actions_map[('MUL', 23)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('MUL', 26)] = 'r ' + str(prodID[('B', '( S )')])
    actions_map[('MUL', 29)] = 's 27'
    actions_map[('MUL', 30)] = 's 27'
    actions_map[('MUL', 31)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('MUL', 32)] = 'r ' + str(prodID[('B', '( S )')])

    actions_map[('LP', 5)] = 's 9'
    actions_map[('LP', 9)] = 's 18'
    actions_map[('LP', 12)] = 's 9'
    actions_map[('LP', 13)] = 's 9'
    actions_map[('LP', 14)] = 's 9'
    actions_map[('LP', 18)] = 's 18'
    actions_map[('LP', 24)] = 's 18'
    actions_map[('LP', 25)] = 's 18'
    actions_map[('LP', 27)] = 's 18'

    actions_map[('RP', 15)] = 's 26'
    actions_map[('RP', 16)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('RP', 17)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('RP', 19)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('RP', 20)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('RP', 28)] = 's 32'
    actions_map[('RP', 29)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('RP', 30)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('RP', 31)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('RP', 32)] = 'r ' + str(prodID[('B', '( S )')])

    actions_map[('EQ', 3)] = 's 5'

    actions_map[('ID', 0)] = 's 3'
    actions_map[('ID', 2)] = 's 4'
    actions_map[('ID', 5)] = 's 10'
    actions_map[('ID', 9)] = 's 19'
    actions_map[('ID', 12)] = 's 10'
    actions_map[('ID', 13)] = 's 10'
    actions_map[('ID', 14)] = 's 10'
    actions_map[('ID', 18)] = 's 19'
    actions_map[('ID', 24)] = 's 19'
    actions_map[('ID', 25)] = 's 19'
    actions_map[('ID', 27)] = 's 19'

    actions_map[('VAL', 5)] = 's 11'
    actions_map[('VAL', 9)] = 's 20'
    actions_map[('VAL', 12)] = 's 11'
    actions_map[('VAL', 13)] = 's 11'
    actions_map[('VAL', 14)] = 's 11'
    actions_map[('VAL', 18)] = 's 20'
    actions_map[('VAL', 24)] = 's 20'
    actions_map[('VAL', 25)] = 's 20'
    actions_map[('VAL', 27)] = 's 20'

    actions_map[('EOL', 1)] = 'a'
    actions_map[('EOL', 4)] = 'r ' + str(prodID[('S\'', 'int ID')])
    actions_map[('EOL', 6)] = 'r ' + str(prodID[('S\'', 'ID = S')])
    actions_map[('EOL', 7)] = 'r ' + str(prodID[('S', 'A')])
    actions_map[('EOL', 8)] = 'r ' + str(prodID[('A', 'B')])
    actions_map[('EOL', 10)] = 'r ' + str(prodID[('B', 'ID')])
    actions_map[('EOL', 11)] = 'r ' + str(prodID[('B', 'VAL')])
    actions_map[('EOL', 21)] = 'r ' + str(prodID[('S', 'S + A')])
    actions_map[('EOL', 22)] = 'r ' + str(prodID[('S', 'S - A')])
    actions_map[('EOL', 23)] = 'r ' + str(prodID[('A', 'A * B')])
    actions_map[('EOL', 26)] = 'r ' + str(prodID[('B', '( S )')])

    return actions_map[(char, state)]


def gotoMap(NonTerminal, state):
    gotomap = {}
    gotomap[('S\'', 0)] = 1

    gotomap[('S', 5)] = 6
    gotomap[('S', 9)] = 15
    gotomap[('S', 18)] = 28

    gotomap[('A', 5)] = 7
    gotomap[('A', 9)] = 16
    gotomap[('A', 12)] = 21
    gotomap[('A', 13)] = 22
    gotomap[('A', 18)] = 16
    gotomap[('A', 24)] = 29
    gotomap[('A', 25)] = 30

    gotomap[('B', 5)] = 8
    gotomap[('B', 9)] = 17
    gotomap[('B', 12)] = 8
    gotomap[('B', 13)] = 8
    gotomap[('B', 14)] = 23
    gotomap[('B', 18)] = 17
    gotomap[('B', 24)] = 17
    gotomap[('B', 25)] = 17
    gotomap[('B', 27)] = 31

    return gotomap[(NonTerminal, state)]


state_stack = Stack()  # 状态栈
symbol_stack = Stack()  # 符号栈
input_string = ""
input_tokens = []


def printState(stepcnt, action):  # 输出当前栈内信息
    print(str(stepcnt).ljust(10), end='')
    state_stack.show()
    symbol_stack.show()
    for i in input_tokens:
        print(i, end=' ')
    # print(' '.join(input_tokens).ljust(30), end='')
    print(action)


def emitAction(rid, poped):
    '''
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
          :return string
    '''
    if rid == 0:
        str = (poped[2][2] + '=' + poped[0][2])
        emitCode(str)
        ret = ('S\'', 'S\'', poped[0][2])
    elif rid == 1:
        pass
    elif rid == 2:
        newtmp = tgen.newtmpNum()
        str = (newtmp + '=' + poped[2][2] + '+' + poped[0][2])
        emitCode(str)
        ret = ('S', 'S', newtmp)
    elif rid == 3:
        newtmp = tgen.newtmpNum()
        str = (newtmp + '=' + poped[2][2] + '-' + poped[0][2])
        emitCode(str)
        ret = ('S', 'S', newtmp)
    elif rid == 4:
        ret = ('S', 'S', poped[0][2])
    elif rid == 5:
        ret = ('A', 'A', poped[0][2])
    elif rid == 6:
        newtmp = tgen.newtmpNum()
        str = (newtmp + '=' + poped[2][2] + '*' + poped[0][2])
        emitCode(str)
        ret = ('A', 'A', newtmp)
    elif rid == 7:
        ret = ('B', 'B', poped[1][2])
    elif rid == 8:
        ret = ('B', 'B', poped[0][2])
    elif rid == 9:
        ret = ('B', 'B', poped[0][2])
    else:
        print("Error!!")
        return
    return ret

def emitCode(code):
    Code.append(code)

if __name__ == "__main__":
    Code = []
    tgen = tmpNum()
    input_string = "<ID,a> <EQ,=> <ID,b> <PLUS,+> <ID,c> <SUB,-> <LP,(> <ID,c> <MUL,*> <ID,d> <SUB,-> <VAL,3> <RP,)> <EOL,#>"
    symTable = {'a': '', 'b': '', 'c': '', 'd': '', 'e': ''}
    for k, v in symTable.items():
        symTable[k] = tgen.newtmpNum()
    # ( type, symbol, value )
    print("输入串：", input_string)
    input_tok = input_string.split(' ')
    input_tokens = []
    for t in input_tok:
        tok = t[1:-1]
        tok = tok.split(',')
        val = None
        if tok[0] == 'ID':
            val = symTable[tok[1]]
        elif tok[0] == 'VAL':
            val = tok[1]
        else:
            val = "None"
        token = (tok[0], tok[1], val)
        input_tokens.append(token)
    print(input_tokens)

    state_stack.push(0)  # 开始状态入符号栈
    symbol_stack.push(('EOL', '#', 'None'))  # 终结符入状态栈

    print('步骤'.ljust(8), '状态栈'.ljust(47), '符号栈'.ljust(47), '剩余输入串'.ljust(45), '动作')
    step = 0
    printState(step, '-')
    while True:  # 开始分析过程
        currState = state_stack.top()  # 状态栈
        currInput = input_tokens[0][0]  # 输入符号栈
        try:
            nextActStr = nextAction(currInput, currState)  # 看下一步操作
        except KeyError:
            print("ERROR!")
            exit(-1)
        Action = ""
        if 's' in nextActStr:  # 移进
            state_stack.push(int(nextActStr.split(' ')[1]))  # 压入新的状态
            symbol_stack.push(input_tokens[0])  # 压入当前字符
            input_tokens = input_tokens[1:]
            Action = "Shift " + nextActStr.split(' ')[1]
        elif 'r' in nextActStr:  # 规约
            prod_num = int(nextActStr.split(' ')[1])
            left_side = prod[prod_num][0]  # 产生式左部
            right_side = prod[prod_num][1]  # 产生式右部

            popcnt = len(right_side.split(' '))
            poped = []
            for i in range(popcnt):  # 弹出产生式的右部
                poped.append(symbol_stack.pop())
                state_stack.pop()

            ls = emitAction(prod_num, poped)
            symbol_stack.push(ls)
            try:
                nextState = gotoMap(symbol_stack.top()[0], state_stack.top())
            except KeyError:
                print("ERROR!")
                exit(-1)
            state_stack.push(gotoMap(symbol_stack.top()[0], state_stack.top()))  # 压入新的状态

            Action = "Reduce " + prod[prod_num][0] + "->" + prod[prod_num][1]

        elif 'a' in nextActStr:
            print('ACCEPT')
            break
        else:
            print("ERROR")
            exit(-1)

        step += 1

        printState(step, Action)
    for code in Code:
        print(code)
