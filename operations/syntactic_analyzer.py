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


def p_PROGRAM(p):
    '''
	PROGRAM : BLOCK_CODE
	'''
    p[0] = p[1]


def p_BLOCK_CODE(p):
    '''
    BLOCK_CODE : GV
            | GC
            | GF
            | GCF
            | EMPTY
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        pass


# Content
def p_C(p):
    '''
    C : GV
        | GC
        | GCF
        | EMPTY
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        pass


# Grammar of variable declaration
def check_variable_type(variable, value):
    print(f"variable: {variable}, value: {value}, type: {type(value)}")
    if variable[0] == 'Ent':
        if not isinstance(value, int):
            print(f"Variable {variable[1]} debe ser de tipo entero")
        else:
            print("Tipo de dato valido")
    elif variable[0] == 'Bool':
        if not (value == 'True' or value == 'False'):
            print(f"Variable {variable[1]} debe ser de tipo booleano")
        else:
            print("Tipo de dato valido")
    elif variable[0] == 'Dcm':
        if not isinstance(value, float):
            print(f"Variable {variable[1]} debe ser de tipo decimal")
        else:
            print("Tipo de dato valido")
    elif variable[0] == 'Cdn':
        if not isinstance(value, str):
            print(f"Variable {variable[1]} debe ser de tipo cadena")
        elif not (value.startswith('"') and value.endswith('"')):
            print(f"Variable {variable[1]} debe ser una cadena entre comillas")
        else:
            print("Tipo de dato valido")
    else:
        print(f"Tipo de dato desconocido para variable {variable[1]}")


def p_GV(p):
    '''
    GV : TD V I VA BLOCK_CODE
        | TD V BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
        variables[p[2]] = None
    elif len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
        if p[4] is not None:
            check_variable_type((p[1], p[2]), p[4])
        variables[p[2]] = p[4]
    else:
        pass


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
        p[0] = float(str(p[1]) + str(p[2]) + str(p[3])) if '.' in p[2] else str(p[1] + p[2] + p[3])
    else:  # Caso de número entero o booleano
        p[0] = int(p[1]) if p[1].isdigit() else p[1]



# Grammar of conditional declaration
def p_GC(p):
    '''
    GC : CN PA CD PC MY C MN BLOCK_CODE
        | CN PA CD PC MY MN BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 9:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    elif len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        pass


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
    GF : TD V ME PR MA MY C RT MN BLOCK_CODE
        | V ME PR MA MY C MN BLOCK_CODE
        | TD V ME PR MA MY RT MN BLOCK_CODE
        | V ME PR MA MY MN BLOCK_CODE
        | TD V ME MA MY C RT MN BLOCK_CODE
        | V ME MA MY C MN BLOCK_CODE
        | TD V ME MA MY RT MN BLOCK_CODE
        | V ME MA MY MN BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 10:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
    elif len(p) == 12:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])
    elif len(p) == 9:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    elif len(p) == 11:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10])
    elif len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        pass


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
    GCF : F PA CDF PC MY C MN BLOCK_CODE
        | F PA CDF PC MY MN BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 9:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    elif len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], [7])
    else:
        pass


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


def p_empty(p):
    '''
	EMPTY :
	'''
    pass


errors = []


# Error handler for syntax errors
def p_error(p):
    global error_value
    if p:
        error_value = "Syntax error", p.value
        errors.append(error_value)
    else:
        error_value = "Syntax error", "AL FINAL DE LA ENTRADA"
        errors.append(error_value)


parser = yacc()


def analyze_syntax(tokens):
    global error_value
    errors.clear()
    input_entry = ""
    for token, lexeme in tokens:
        input_entry += f'{lexeme} '

    # lexer.input(input_entry)
    # for t in lexer:

    validated_entry = parser.parse(input_entry)
    if type(validated_entry) is tuple and len(errors) == 0:
        error_value = None, None
        return f'CADENA VALIDA \n'
    elif validated_entry is tuple and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n'
    elif validated_entry is None and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n'
    else:
        value_error = f'CADENA INVALIDA {error_value[1]} \n'
        error_value = None, None
        return value_error
