digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
keywords = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch', 'case', 'enum',
            'register', 'typedef', 'char', 'extern', 'return', 'union', 'const', 'float', 'short', 'unsigned',
            'continue', 'for', 'signed', 'void', 'default', 'goto', 'sizeof', 'volatile', 'do', 'if',
            'while', 'static']

boadwords = [';', ',', '(', ')', '.', '{', '}', '[', ']']

current_state = 10
msg = ""
buf = ""
character_table = []


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
    global character_table
    print(ch)
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
            elif ch == '&':
                current_state = States[25]
            elif ch == '=':
                current_state = States[26]
                return
            elif ch == '<':
                current_state = States[27]
                return
            elif ch == '>':
                current_state = States[28]
                return
            else:
                current_state = States[0]
                return

        elif current_state == States[1]:
            if is_alpha(ch) or is_digit(ch):
                buf = buf + ch
                return
            else:
                current_state = States[2]

        elif current_state == States[2]:
            if buf in keywords:
                msg = msg + '(' + buf.upper() + ', ' + buf + ')\n'
                # print(msg)

            else:
                msg = msg + '(ID, ' + buf + ')\n'
                if buf not in character_table:
                    character_table.append(buf)
                # print(msg)

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
            msg = msg + '(Int, ' + buf + ')\n'
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
            msg = msg + '(Real, ' + buf + ')\n'
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
            msg = msg + '(Char ' + buf + ')\n'
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
            msg = msg + '(String ' + buf + ')\n'
            buf = ""
            current_state = States[0]
            return

        # ","
        elif current_state == States[11]:
            msg = msg + '(DOT, ,)\n'
            current_state = States[0]
            return

        # ";"
        elif current_state == States[12]:
            msg = msg + '(SEMIC, ;)\n'
            current_state = States[0]
            return

        # "("
        elif current_state == States[13]:
            msg = msg + '(OPEN_PAREN, ()\n'
            current_state = States[0]
            return

        # ")"
        elif current_state == States[14]:
            msg = msg + '(CLOSE_PAREN, ))\n'
            current_state = States[0]
            return

        # "{"
        elif current_state == States[15]:
            msg = msg + '(OPEN_CURLY, {)\n'
            current_state = States[0]
            return

        # "}"
        elif current_state == States[16]:
            msg = msg + '(CLOSE_CURLY, })\n'
            current_state = States[0]
            return

        # "["
        elif current_state == States[17]:
            msg = msg + '(OPEN_BRACKET, [)\n'
            current_state = States[0]
            return

        # "]"
        elif current_state == States[18]:
            msg = msg + '(CLOSE_BRACKET, ])\n'
            current_state = States[0]
            return

        # "+"
        elif current_state == States[19]:
            msg = msg + '(PLUS, +)\n'
            current_state = States[0]
            return

        # "-"
        elif current_state == States[20]:
            msg = msg + '(MINUS, -)\n'
            current_state = States[0]
            return

        # "*"
        elif current_state == States[21]:
            msg = msg + '(MULTI, *)\n'
            current_state = States[0]
            return

        # "/"
        elif current_state == States[22]:
            msg = msg + '(DIVIDE, /)\n'
            current_state = States[0]
            return

        # "!"
        elif current_state == States[23]:
            msg = msg + '(NOT, !)\n'
            current_state = States[0]
            return

        # "|"
        elif current_state == States[24]:
            msg = msg + '(OR, |)\n'
            current_state = States[0]
            return

        # "&"
        elif current_state == States[25]:
            msg = msg + '(AND, &)\n'
            current_state = States[0]
            return

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
            msg = msg + '(EQUAL, ==)\n'
            current_state = States[0]
            return

        elif current_state == States[30]:
            msg = msg + '(ASSIGN, =)\n'
            current_state = States[0]

        #  "<="
        elif current_state == States[31]:
            msg = msg + '(LEQ, <=)\n'
            current_state = States[0]
            return

        elif current_state == States[32]:
            msg = msg + '(LE, <)\n'
            current_state = States[0]

        #  ">="
        elif current_state == States[33]:
            msg = msg + '(GEQ, >=)\n'
            current_state = States[0]
            return

        elif current_state == States[34]:
            msg = msg + '(GE, >)\n'
            current_state = States[0]


def scanner(text):
    global msg
    global character_table
    text_length = len(text)
    for i in range(0, text_length):
        analysis(text[i])
    with open('token.txt', 'w') as token_file:
        token_file.write(msg)
    with open('charactertable.txt', 'w') as character_file:
        for character in character_table:
            character_file.write(character)
            character_file.write('\n')


def main():
    global States
    global current_state
    States = generate_states()
    current_state = States[0]
    fp = open('test.c', 'r')
    fp = fp.read()
    scanner(fp)


if __name__ == '__main__':
    main()
