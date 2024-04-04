from ply.lex import lex
from ply.yacc import yacc


error_value = None, None

variables = {}

# --- Tokenizer

# Tokens of reserved words
reserved_words = {
    'Ent': 'INTEGER_TYPE',
    'Bool': 'BOOLEAN_TYPE',
    'Dcm': 'DECIMAL_TYPE',
    'Cdn': 'STRING_TYPE',
    'True': 'TRUE_VALUE',
    'False': 'FALSE_VALUE',
    'if': 'IF',
    'for': 'FOR',
    'rtn': 'RETURN',
}

# All list Tokens
tokens = ['ASSIGNMENT',
          'ADDITION',
          'SUBTRACTION',
          'NUMBER',
          'DOT',
          'QUOTATION_MARKS',
          'PARENTHESIS_CLOSE',
          'PARENTHESIS_OPEN',
          'GREATER_THAN',
          'LESS_THAN',
          'GREATER_OR_EQUAL',
          'LESS_OR_EQUAL',
          'NOT_EQUAL',
          'EQUAL',
          'OPEN_BODY',
          'PIPE',
          'VARIABLE'] + list(reserved_words.values())

# Ignored characters
t_ignore = ' \t'

# Tokens of symbols with their regexs
t_ASSIGNMENT = r'='
t_ADDITION = r'\+'
t_SUBTRACTION = '-'
t_DOT = r'\.'
t_PARENTHESIS_CLOSE = r'\)'
t_PARENTHESIS_OPEN = r'\('
t_QUOTATION_MARKS = r'\"'
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_OR_EQUAL = r'>='
t_LESS_OR_EQUAL = r'<='
t_NOT_EQUAL = r'!='
t_EQUAL = r'=='
t_OPEN_BODY = r'=>'
t_PIPE = r'\|'


# Rule to declare variables
def t_VARIABLE(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    # Verify if the word is a reserved word
    t.type = reserved_words.get(t.value, 'VARIABLE')
    return t


# Rule to declare numbers
def t_NUMBER(t):
    # r'\d+(\.\d+)?'
    r'\d+'
    return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# Error handler for illegal characters
def t_error(t):
    t.type = 'ERROR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t


lexer = lex()


# Content
def p_C(p):
    '''
    C : GV
        | GC
        | GCF
        | GF
    '''
    p[0] = p[1]


# Grammar of variable declaration
def p_GV(p):
    '''
    GV : TD V I VA
        | TD V
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
        variables[p[2]] = None
    else:
        p[0] = (p[1], p[2], p[3], p[4])
        variables[p[2]] = p[4]


# Type data
def p_TD(p):
    '''
    TD : INTEGER_TYPE
        | BOOLEAN_TYPE
        | DECIMAL_TYPE
        | STRING_TYPE
    '''
    p[0] = p[1]


# Variable
def p_V(p):
    '''
    V : VARIABLE
    '''
    p[0] = p[1]


# Assignment
def p_I(p):
    '''
    I : ASSIGNMENT
    '''
    p[0] = p[1]


# Value
def p_VA(p):
    '''
    VA : NUMBER
        | NUMBER DOT NUMBER
        | TRUE_VALUE
        | FALSE_VALUE
        | QUOTATION_MARKS V QUOTATION_MARKS
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]


# Grammar of conditional declaration
def p_GC(p):
    '''
    GC : CN PA CD PC MY C MN
        | CN PA CD PC MY MN
    '''
    if len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])


# If
def p_CN(p):
    '''
    CN : IF
    '''
    p[0] = p[1]


# Condition
def p_CD(p):
    '''
    CD : V S V
        | V S VA
        | VA S V
        | VA S VA
    '''
    p[0] = (p[1], p[2], p[3])


# Symbols
def p_S(p):
    '''
    S : EQUAL
        | GREATER_THAN
        | LESS_THAN
        | GREATER_OR_EQUAL
        | LESS_OR_EQUAL
        | NOT_EQUAL
    '''
    p[0] = p[1]


# Grammar of function declaration
def p_GF(p):
    '''
    GF : TD V ME PR MA MY C RT MN
        | V ME PR MA MY C MN
        | TD V ME PR MA MY RT MN
        | V ME PR MA MY MN
        | TD V ME MA MY C RT MN
        | V ME MA MY C MN
        | TD V ME MA MY RT MN
        | V ME MA MY MN
    '''
    if len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    elif len(p) == 10:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
    elif len(p) == 7:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 9:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5])


# Variable parameter
def p_PR(p):
    '''
    PR : V
    '''
    p[0] = p[1]


# <
def p_ME(p):
    '''
    ME : LESS_THAN
    '''
    p[0] = p[1]


# >
def p_MA(p):
    '''
    MA : GREATER_THAN
    '''
    p[0] = p[1]


# Return variable
def p_RT(p):
    '''
    RT : RETURN V
    '''
    p[0] = (p[1], p[2])


# Grammar of cycle declaration
def p_GCF(p):
    '''
    GCF : F PA CDF PC MY C MN
        | F PA CDF PC MY MN
    '''
    if len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])


# for
def p_F(p):
    '''
    F :  FOR
    '''
    p[0] = p[1]


# Conditional for
def p_CDF(p):
    '''
    CDF : NUMBER SE NUMBER SE O
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])


# Separate or
def p_PIPE(p):
    '''
    SE : PIPE
    '''
    p[0] = p[1]


# Operations
def p_O(p):
    '''
    O : SUBTRACTION
        | ADDITION
    '''
    p[0] = p[1]


# Rules globals to all grammars


# (
def p_PA(p):
    '''
    PA : PARENTHESIS_OPEN
    '''
    p[0] = p[1]


# )
def p_PC(p):
    '''
    PC : PARENTHESIS_CLOSE
    '''
    p[0] = p[1]


# =>
def p_MY(p):
    '''
    MY : OPEN_BODY
    '''
    p[0] = p[1]


# <=
def p_MN(p):
    '''
    MN : LESS_OR_EQUAL
    '''
    p[0] = p[1]


# Error handler for syntax errors
def p_error(p):
    global error_value
    if p:
        error_value = "Syntax error", p.value
    else:
        error_value = "Syntax error", "AL FINAL DE LA ENTRADA"


parser = yacc()


def analyze_syntax(tokens):
    global error_value
    input_entry = ""
    for token, lexeme in tokens:
        input_entry += f'{lexeme} '

    # lexer.input(input_entry)
    # for t in lexer:
    #     print(t)

    validated_entry = parser.parse(input_entry)
    if type(validated_entry) is tuple:
        error_value = None, None
        print(variables)
        return f'CADENA VALIDA \n'
    else:
        return f'CADENA INVALIDA {error_value[1]} \n'
