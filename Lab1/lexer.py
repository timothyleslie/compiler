digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

global current_state
global States


def generate_states():
    states = []
    for i in range(0, 20):
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
    global current_state
    global States
    if current_state == States[0]:
        if is_alpha(ch):
            current_state = States[14]
        elif is_digit(ch):
            current_state = States[16]



def scanner(text):
    text_length = len(text)
    for i in range(0, text_length):
        analysis(text[i])


def main():
    global States
    global current_state
    States = generate_states()
    current_state = States[0]
    fp = open('test.c', 'r')
    scanner(fp.open)


if __name__ == '__main__':
    main()
