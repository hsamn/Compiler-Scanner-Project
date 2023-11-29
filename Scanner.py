import sys
import re

def getCharsStream(filePath):
    with open(filePath, "rt") as codeFile:
        return codeFile.read()

def tokenize(code):
    rules = [
        ('Identifier_MAIN', r'main'),          # main
        ('Keyword_INT', r'int'),            # int
        ('Keyword_FLOAT', r'float'),        # float
        ('Keyword_IF', r'if'),              # if
        ('Keyword_ELSE', r'else'),          # else
        ('Keyword_WHILE', r'while'),        # while
        ('Identifier_READ', r'read'),          # read
        ('Identifier_PRINT', r'print'),        # print
        ('Special_Symbol_LBRACKET', r'\('),        # (
        ('Special_Symbol_RBRACKET', r'\)'),        # )
        ('Special_Symbol_LBRACE', r'\{'),          # {
        ('Special_Symbol_RBRACE', r'\}'),          # }
        ('Special_Symbol_COMMA', r','),            # ,
        ('Special_Symbol_PCOMMA', r';'),           # ;
        ('Special_Symbol_STR', r'"'),           # ;
        ('Special_Symbol_PER', r'\.'),           # ;
        ('Operator_EQ', r'=='),              # ==
        ('Operator_NE', r'!='),              # !=
        ('Operator_LE', r'<='),              # <=
        ('Operator_GE', r'>='),              # >=
        ('Operator_OR', r'\|\|'),            # ||
        ('Operator_AND', r'&&'),             # &&
        ('Operator_ATTR', r'\='),            # =
        ('Operator_LT', r'<'),               # <
        ('Operator_GT', r'>'),               # >
        ('Operator_PLUS', r'\+'),            # +
        ('Operator_MINUS', r'-'),            # -
        ('Operator_MULT', r'\*'),            # *
        ('Operator_DIV', r'\/'),             # /
        ('Operator_MOD', r'%'),             # /
        ('Identifier', r'[a-zA-Z]\w*'),     # IDENTIFIERS
        ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
        ('INTEGER_CONST', r'\d(\d)*'),          # INT
        ('NEWLINE', r'\n'),         # NEW LINE
        ('SKIP', r'[ \t]+'),        # SPACE and TABS
        ('MISMATCH', r'.'),         # ANOTHER CHARACTER
    ]

    tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)

    # It analyzes the code to find the lexemes and their respective Tokens
    for m in re.finditer(tokens_join, code):
        token_type = m.lastgroup
        token_lexeme = m.group(token_type)

        if token_type == 'NEWLINE':
            lin_start = m.end()
        elif token_type == 'SKIP':
            continue
        elif token_type == 'MISMATCH':
            raise RuntimeError('%r unexpected on line' % (token_lexeme))
        else:
            print("Token:", token_lexeme)
            print("Type:", token_type)
            print()

def main():
    tokenize(getCharsStream(sys.argv[1]))


if __name__ == "__main__":
    main()
