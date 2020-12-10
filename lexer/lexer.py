digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
EncodeTable = {'auto': (1, "AUTO"), 'double': (2, "DOUBLE"), 'int': (3, "INT"), 'struct': (4, "STRUCT"),
               'break': (5, "BREAK"), 'else': (6, "ELSE"), 'long': (7, "LONG"), 'switch': (8, "SWITCH"),
               'case': (9, "CASE"), 'enum': (10, "ENUM"),
               'register': (11, "REGISTER"), 'typedef': (12, "TYPEDEF"), 'char': (13, "CHAR"), 'extern': (14, "EXTERN"),
               'return': (15, "RETURN"), 'union': (16, "UNION"), 'const': (17, "CONST"),
               'float': (18, "FLOAT"), 'short': (19, "SHORT"), 'unsigned': (20, "UNSIGNED"),
               'continue': (21, "CONTINUE"), 'for': (22, "FOR"), 'signed': (23, "SIGNED"), 'void': (24, "VOID"),
               'default': (25, "DEFAULT"), 'goto': (26, "GOTO"), 'sizeof': (27, "SIZEOF"),
               'volatile': (28, "VOLATILE"), 'do': (29, "DO"), 'if': (30, "IF"),
               'while': (31, "WHILE"), 'static': (32, "STATIC"), ';': (33, "SEMIC"), ',': (34, "COMMA"),
               '(': (35, "OPEN_PAREN"), ')': (36, "CLOSE_PAREN"), '.': (37, "DOT"), '{': (38, "OPEN_CURLY"),
               '}': (39, "CLOSE_CURLY"),
               '[': (40, "OPEN_BRACKET"), ']': (41, "CLOSE_BRACKET"),
               '+': (42, "PLUS"), '-': (43, "MINUS"), '*': (44, "MULTI"), '/': (45, "DIVIDE"), '!': (46, "NOT"),
               '|': (47, "BIT_OR"), '&': (48, "BIT_AND"), '=': (49, "ASSIGN"), '==': (50, "EQUAL"), '<': (51, "LE"),
               '>': (52, "GE"), '<=': (53, "LEQ"), '>=': (54, "GEQ"), '&&': (59, "AND"), '||': (60, "OR")}
ID = (0, "ID")
INT = (55, "INT_NUM")
REAL = (56, "REAL_NUM")
CHAR = (57, "CHAR_CONST")
STRING = (58, "STRING_CONST")
current_state = 10
msg = ""
buf = ""
symbol_table = {}
INT_LEN = 4
REAL_LEN = 8

def generate_states():
    states = []
    for i in range(0, 50):
        states.append(i)
    return states


def is_digit(ch):
    if ch in digits:
        return True
    else:
        return False


def is_alpha(ch):
    if ch in alphas:
        return True
    else:
        return False


def analysis(ch):
    global States
    global current_state
    global msg
    global buf
    global symbol_table
    # print(ch)
    while True:
        # print(ch)
        # print(current_state)
        if current_state == States[0]:
            if is_alpha(ch):
                buf = buf + ch
                current_state = States[1]
                return
            elif is_digit(ch):
                buf = buf + ch
                current_state = States[3]
                return
            elif ch == '\'':
                current_state = States[7]
                return
            elif ch == '\"':
                current_state = States[9]
                return
            elif ch == ',':
                current_state = States[11]
            elif ch == ';':
                current_state = States[12]
            elif ch == '(':
                current_state = States[13]
            elif ch == ')':
                current_state = States[14]
            elif ch == '{':
                current_state = States[15]
            elif ch == '}':
                current_state = States[16]
            elif ch == '[':
                current_state = States[17]
            elif ch == ']':
                current_state = States[18]
            elif ch == '+':
                current_state = States[19]
            elif ch == '-':
                current_state = States[20]
            elif ch == '*':
                current_state = States[21]
            elif ch == '/':
                current_state = States[22]
            elif ch == '!':
                current_state = States[23]
            elif ch == '|':
                current_state = States[24]
                return
            elif ch == '&':
                current_state = States[25]
                return
            elif ch == '=':
                current_state = States[26]
                return
            elif ch == '<':
                current_state = States[27]
                return
            elif ch == '>':
                current_state = States[28]
                return
            elif ch == '.':
                current_state = States[39]
            else:
                current_state = States[0]
                return

        elif current_state == States[1]:
            if is_alpha(ch) or is_digit(ch) or ch == '_':
                buf = buf + ch
                return
            else:
                current_state = States[2]

        elif current_state == States[2]:
            if buf in EncodeTable.keys():
                msg = msg + '(' + str(EncodeTable[buf][1]) + ', ' + buf + ')\n'

            else:
                if buf not in symbol_table.keys():
                    symbol_table[buf] = len(symbol_table)*INT_LEN
                msg = msg + '(' + ID[1] + ', ' + buf + ')\n'

            buf = ""
            current_state = States[0]

        elif current_state == States[3]:
            if is_digit(ch):
                buf = buf + ch
                current_state = States[3]
                return
            elif ch == '.':
                buf = buf + ch
                current_state = States[5]
                return
            else:
                current_state = States[4]

        elif current_state == States[4]:
            msg = msg + '(' + INT[1] + ', ' + buf + ')\n'
            buf = ""
            current_state = States[0]

        elif current_state == States[5]:
            if is_digit(ch):
                buf = buf + ch
                current_state = States[5]
                return
            else:
                current_state = States[6]

        elif current_state == States[6]:
            msg = msg + '(' + REAL[1] + ', ' + buf + ')\n'
            buf = ""
            current_state = States[0]

        elif current_state == States[7]:
            if ch == '\'':
                current_state = States[8]
            else:
                buf = buf + ch
                current_state = States[7]
                return

        elif current_state == States[8]:
            msg = msg + '(' + CHAR[1] + ', ' + buf + ')\n'
            buf = ""
            current_state = States[0]
            return

        elif current_state == States[9]:
            if ch == '\"':
                current_state = States[10]
            else:
                buf = buf + ch
                current_state = States[9]
                return

        elif current_state == States[10]:
            msg = msg + '(' + STRING[1] + ', ' + buf + ')\n'
            buf = ""
            current_state = States[0]
            return

        # ","
        elif current_state == States[11]:
            msg = msg + '(' + str(EncodeTable[','][1]) + ', ' + ',' + ')\n'
            current_state = States[0]
            return

        # ";"
        elif current_state == States[12]:
            msg = msg + '(' + str(EncodeTable[';'][1]) + ', ' + ';' + ')\n'
            current_state = States[0]
            return

        # "("
        elif current_state == States[13]:
            msg = msg + '(' + str(EncodeTable['('][1]) + ', ' + '(' + ')\n'
            current_state = States[0]
            return

        # ")"
        elif current_state == States[14]:
            msg = msg + '(' + str(EncodeTable[')'][1]) + ', ' + ')' + ')\n'
            current_state = States[0]
            return

        # "{"
        elif current_state == States[15]:
            msg = msg + '(' + str(EncodeTable['{'][1]) + ', ' + '{' + ')\n'
            current_state = States[0]
            return

        # "}"
        elif current_state == States[16]:
            msg = msg + '(' + str(EncodeTable['}'][1]) + ', ' + '}' + ')\n'
            current_state = States[0]
            return

        # "["
        elif current_state == States[17]:
            msg = msg + '(' + str(EncodeTable['['][1]) + ', ' + '[' + ')\n'
            current_state = States[0]
            return

        # "]"
        elif current_state == States[18]:
            msg = msg + '(' + str(EncodeTable[']'][1]) + ', ' + ']' + ')\n'
            current_state = States[0]
            return

        # "+"
        elif current_state == States[19]:
            msg = msg + '(' + str(EncodeTable['+'][1]) + ', ' + '+' + ')\n'
            current_state = States[0]
            return

        # "-"
        elif current_state == States[20]:
            msg = msg + '(' + str(EncodeTable['-'][1]) + ', ' + '-' + ')\n'
            current_state = States[0]
            return

        # "*"
        elif current_state == States[21]:
            msg = msg + '(' + str(EncodeTable['*'][1]) + ', ' + '*' + ')\n'
            current_state = States[0]
            return

        # "/"
        elif current_state == States[22]:
            msg = msg + '(' + str(EncodeTable['/'][1]) + ', ' + '/' + ')\n'
            current_state = States[0]
            return

        # "!"
        elif current_state == States[23]:
            msg = msg + '(' + str(EncodeTable['!'][1]) + ', ' + '!' + ')\n'
            current_state = States[0]
            return

        # "|"
        elif current_state == States[24]:
            if ch == '|':
                current_state = States[35]
            else:
                current_state = States[36]

        # "&"
        elif current_state == States[25]:
            if ch == '&':
                current_state = States[37]
            else:
                current_state = States[38]

        # "="
        elif current_state == States[26]:
            if ch == '=':
                current_state = States[29]
            else:
                current_state = States[30]

        # "<"
        elif current_state == States[27]:
            if ch == '=':
                current_state = States[31]
            else:
                current_state = States[32]

        # ">"
        elif current_state == States[28]:
            if ch == '=':
                current_state = States[33]
            else:
                current_state = States[34]

        #  "=="
        elif current_state == States[29]:
            msg = msg + '(' + str(EncodeTable['=='][1]) + ', ' + '==' + ')\n'
            current_state = States[0]
            return

        elif current_state == States[30]:
            msg = msg + '(' + str(EncodeTable['='][1]) + ', ' + '=' + ')\n'
            current_state = States[0]

        #  "<="
        elif current_state == States[31]:
            msg = msg + '(' + str(EncodeTable['<='][1]) + ', ' + '<=' + ')\n'
            current_state = States[0]
            return

        elif current_state == States[32]:
            msg = msg + '(' + str(EncodeTable['<'][1]) + ', ' + '<' + ')\n'
            current_state = States[0]

        #  ">="
        elif current_state == States[33]:
            msg = msg + '(' + str(EncodeTable['>='][1]) + ', ' + '>=' + ')\n'
            current_state = States[0]
            return

        elif current_state == States[34]:
            msg = msg + '(' + str(EncodeTable['>'][1]) + ', ' + '>' + ')\n'
            current_state = States[0]

        # ||
        elif current_state == States[35]:
            msg = msg + '(' + str(EncodeTable['||'][1]) + ', ' + '||' + ')\n'
            current_state = States[0]
            return

        elif current_state == States[36]:
            msg = msg + '(' + str(EncodeTable['|'][1]) + ', ' + '|' + ')\n'
            current_state = States[0]

        # &&
        elif current_state == States[37]:
            msg = msg + '(' + str(EncodeTable['&&'][1]) + ', ' + '&&' + ')\n'
            current_state = States[0]
            return

        elif current_state == States[38]:
            msg = msg + '(' + str(EncodeTable['&'][1]) + ', ' + '&' + ')\n'
            current_state = States[0]

        # .
        elif current_state == States[39]:
            msg = msg + '(' + str(EncodeTable['.'][1]) + ', ' + '.' + ')\n'
            current_state = States[0]
            return


def scanner(text):
    global msg
    global symbol_table
    text_length = len(text)
    for i in range(0, text_length):
        analysis(text[i])

    with open('./data/token.txt', 'w') as token_file:
        token_file.write(msg)
        token_file.write("(EOL, #)")
    with open('./data/symbol_table.txt', 'w') as character_file:
        for character in symbol_table.items():
            character_file.write(str(character[1]))
            character_file.write(',')
            character_file.write(str(character[0]))
            character_file.write(',')
            character_file.write('None')
            character_file.write('\n')


def main():
    global States
    global current_state
    States = generate_states()
    current_state = States[0]

    fp = open('./data/src_code', 'r')
    fp = fp.read()
    scanner(fp)


if __name__ == '__main__':
    main()
