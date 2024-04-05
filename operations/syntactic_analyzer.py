from ply.lex import lex
from ply.yacc import yacc


error_value = None, None

variables = {}
variables_err = []
conditional_result = []
loop_result = []

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
            | PRINT
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
        | PRINT
        | EMPTY
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        pass


# Grammar of variable declaration
def check_variable_type(variable, value):
    # print(f"variable: {variable}, value: {value}, type: {type(value)}")
    variable_type, variable_name = variable
    error = ""

    if (variable_type, variable_name) in variables:
        if variable_type == 'Ent':
            if not isinstance(value, int):
                error = f"Variable '{variable_name}' debe ser de tipo entero - valor {value}"
        elif variable_type == 'Bool':
            if not (value == 'True' or value == 'False'):
                error = f"Variable '{variable_name}' debe ser de tipo booleano"
        elif variable_type == 'Dcm':
            if not isinstance(value, float):
                error = f"Variable '{variable_name}' debe ser de tipo decimal"
        elif variable_type == 'Cdn':
            if not isinstance(value, str):
                error = f"Variable '{variable_name}' debe ser de tipo cadena"
        else:
            error = f"Tipo de dato desconocido para variable '{variable_name}'"
    else:
        # Nueva variable
        variables[(variable_type, variable_name)] = value
        check_variable_type((variable_type, variable_name), value)

    if error == "":
        return True
    else:
        variables_err.append(error)
        return False


def p_GV(p):
    '''
    GV : TD V I VA BLOCK_CODE
        | TD V BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
        print((p[1], p[2], p[3]))
        variables[(p[1], p[2])] = None
    elif len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
        print((p[1], p[2], p[3], p[4], p[5]))
        if check_variable_type((p[1], p[2]), p[4]):
            variables[(p[1], p[2])] = p[4]
            print("Variables -> ", variables)
    else:
        pass


def p_PRINT(p):
    '''
    PRINT : SUBTRACTION MA VAP ME SUBTRACTION BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
    else:
        pass


def p_VAP(p):
    '''
    VAP : V
        | VA
        | CD
        | FR
    '''
    p[0] = p[1]


def p_FR(p):
    '''
    FR : TD V ME PR MA
        | TD V ME MA
    '''
    if len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = (p[1], p[2], p[3], p[4])



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
    if len(p) == 4:  # Decimal or String
        p[0] = float(str(p[1]) + str(p[2]) + str(p[3])) if '.' in p[2] else str(p[1] + p[2] + p[3])
    else:  # Int or Boolean
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
        print((p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
    elif len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        print((p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
    else:
        pass


# If
def p_CN(p):
    '''
    CN : IF
    '''
    p[0] = p[1]


def validate_conditions(p1, p2, p3):
    return None


# Condition
def p_CD(p):
    '''
    CD : V S V
        | V S VA
        | VA S V
        | VA S VA
    '''
    validate_conditions(p[1], p[2], p[3])
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
        print((p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))
    elif len(p) == 8:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], [7])
        print((p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
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


def analyze_syntax(tkn):
    global error_value
    variables_err.clear()
    errors.clear()
    input_entry = ""
    # input_entry_list = []
    # count = 1
    for token, lexeme in tkn:
        # if token == "INTEGER_TYPE" or token == "DECIMAL_TYPE" or token == "STRING_TYPE" or token == "BOOLEAN_TYPE" or token == 'IF' or token == 'FOR':
        #     input_entry_list.append(input_entry)
        #     input_entry = ""
        input_entry += f'{lexeme} '
        # if count == len(tkn):
        #     input_entry_list.append(input_entry)
        #     input_entry = ""
        # count += 1

    print(input_entry)

    # [print(c) for c in input_entry_list]

    # lexer.input(input_entry)
    # for t in lexer:

    # input_entry = ""
    # for index, structure in enumerate(input_entry_list):
    #     print(structure, index)
    #     print("asdf")
    #     if structure.strip().endswith("<=") or not structure.strip().endswith("=>"):
    #         va = input_entry_list[index - 1]
    #         input_entry_list[index - 1] = structure
    #         input_entry_list[index] = va
    #     input_entry += f'{structure}'
    #
    # print("cvb")
    # [print(c) for c in input_entry_list]
    #
    # for s in reversed(input_entry_list):
    #     print("------------------------")
    #     print(s)
    # print("--------asdfsdfasdf------")

    validated_entry = parser.parse(input_entry)
    print(validated_entry, len(errors))
    if type(validated_entry) is tuple and len(errors) == 0:
        error_value = None, None
        print("Variables valor final -> ", variables)
        return f'CADENA VALIDA \n', variables_err
    elif validated_entry is tuple and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n', []
    elif validated_entry is None and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n', []
    else:
        value_error = f'CADENA INVALIDA {error_value[1]} \n'
        error_value = None, None
        return value_error, []
