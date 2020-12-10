import codegen.codegen as codegen
import lexer.lexer as lexer
import syntax.parser as parser


def main():
    src_code = input("input your C code: ")
    if src_code[-1] == ';':
        src_code = src_code[:-1]
    with open('./data/src_code', 'w') as f_src:
        f_src.write(src_code)
        f_src.write('\n')
    lexer.main()
    parser.main()
    codegen.main()
    print("Success, see the target_code in data/target_code.txt")


if __name__ == '__main__':
    main()
