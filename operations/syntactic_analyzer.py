from ply.lex import lex
from ply.yacc import yacc


error_value = None, None

variables = {}
variables_err = []
conditional_result = []
conditional_err = []
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
            if not isinstance(value, bool):
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
        p[0] = int(p[1]) if p[1].isdigit() else bool(p[1])


# Grammar of conditional declaration
def p_GC(p):
    '''
    GC : CN PA CD PC MY C MN BLOCK_CODE
        | CN PA CD PC MY MN BLOCK_CODE
        | EMPTY
    '''
    if len(p) == 9:
        if p[3]:
            p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
        else:
            p[0] = p[8]
    elif len(p) == 8:
        if p[3]:
            p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        else:
            p[0] = p[7]
    else:
        pass


# If
def p_CN(p):
    '''
    CN : IF
    '''
    p[0] = p[1]


def validate_conditions(p1, p2, p3):
    error = ""
    p0 = ""
    if p2 == "<":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 < p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 < variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] < p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] < variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        else:
            error = f"La condicional '{p1} '{p2}' '{p3}' no es valida"
    elif p2 == ">":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 > p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 > variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] > p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] > variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        else:
            error = f"La condicional '{p1} '{p2}' '{p3}' no es valida"
    elif p2 == "<=":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 <= p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 <= variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] <= p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] <= variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        else:
            error = f"La condicional '{p1} '{p2}' '{p3}' no es valida"
    elif p2 == ">=":
        if isinstance(p1, (int, float)) and isinstance(p3, (int, float)):
            p0 = p1 >= p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 >= variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] >= p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] >= variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        else:
            error = f"La condicional '{p1} '{p2}' '{p3}' no es valida"
    elif p2 == "==":
        if (isinstance(p1, (int, float)) and isinstance(p3, (int, float))) or (isinstance(p1, str) and isinstance(p3, str)) or (isinstance(p1, bool) and isinstance(p3, bool)):
            p0 = p1 == p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 == variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] == p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] == variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif isinstance(p1, str) and (("Cdn", p3) in variables):
            p0 = p1 == variables[("Cdn", p3)]
        elif (("Cdn", p1) in variables) and isinstance(p3, str):
            p0 = variables[("Cdn", p1)] == p3
        elif (("Cdn", p1) in variables) and (("Cdn", p3) in variables):
            p0 = variables[("Cdn", p1)] == variables[("Cdn", p3)]
        elif isinstance(p1, bool) and (("Bool", p3) in variables):
            print(variables[("Bool", p3)], "ASDFASDF")
            p0 = p1 == variables[("Bool", p3)]
        elif (("Bool", p1) in variables) and isinstance(p3, bool):
            p0 = variables[("Bool", p1)] == p3
        elif (("Bool", p1) in variables) and (("Bool", p3) in variables):
            p0 = variables[("Bool", p1)] == variables[("Bool", p3)]
        else:
            error = f"La condicional '{p1} '{p2}' '{p3}' no es valida"
    elif p2 == "!=":
        if (isinstance(p1, (int, float)) and isinstance(p3, (int, float))) or (isinstance(p1, str) and isinstance(p3, str)) or (isinstance(p1, bool) and isinstance(p3, bool)):
            p0 = p1 != p3
        elif isinstance(p1, (int, float)) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = p1 != variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and isinstance(p3, (int, float)):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] != p3
        elif (("Ent", p1) in variables or ("Dcm", p1) in variables) and (("Ent", p3) in variables or ("Dcm", p3) in variables):
            p0 = variables[("Ent", p1)] if ("Ent", p1) in variables else variables[("Dcm", p1)] != variables[("Ent", p3)] if ("Ent", p3) in variables else variables[("Dcm", p3)]
        elif isinstance(p1, str) and (("Cdn", p3) in variables):
            p0 = p1 != variables[("Cdn", p3)]
        elif (("Cdn", p1) in variables) and isinstance(p3, str):
            p0 = variables[("Cdn", p1)] != p3
        elif (("Cdn", p1) in variables) and (("Cdn", p3) in variables):
            p0 = variables[("Cdn", p1)] != variables[("Cdn", p3)]
        elif isinstance(p1, bool) and (("Bool", p3) in variables):
            p0 = p1 == variables[("Bool", p3)]
        elif (("Bool", p1) in variables) and isinstance(p3, bool):
            p0 = variables[("Bool", p1)] != p3
        elif (("Bool", p1) in variables) and (("Bool", p3) in variables):
            p0 = variables[("Bool", p1)] != variables[("Bool", p3)]
        else:
            error = f"Valor '{p1}' o '{p3}' no es valido"
    else:
        error = f"Operador '{p2}' no es un operador valido"

    if error == "" and p0 != "":
        return ((p1, p2, p3), p0), True
    else:
        conditional_err.append(error)
        return (), False


# Condition
def p_CD(p):
    '''
    CD : V S V
        | V S VA
        | VA S V
        | VA S VA
    '''
    conditional = validate_conditions(p[1], p[2], p[3])
    if conditional[1]:
        p[0] = conditional[0][1]
        conditional_result.append(conditional[0])


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


def p_EMPTY(p):
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
    conditional_err.clear()
    errors.clear()
    input_entry = ""
    entry = []
    content = 0
    content_body = {}
    for index, (token, lexeme) in enumerate(tkn):
        if token == 'OPEN_BODY':
            content += 1
            entry.append((index, index))
        elif token == 'LESS_OR_EQUAL':
            content -= 1
            content_body[index] = (token, lexeme)

        if content == 0 and token != 'LESS_OR_EQUAL':
            entry.append((token, lexeme))
        else:
            content_body[index] = (token, lexeme)

    structure = []
    structures = []
    for index, (token, lexeme) in enumerate(entry):
        if token == lexeme:
            copy_token = token
            copy_body = content_body.copy()
            for key, value in copy_body.items():
                if key == copy_token:
                    content_body.pop(key)
                    structure.append(value[1])
                    copy_token += 1
        else:
            if token == 'INTEGER_TYPE' or token == 'BOOLEAN_TYPE' or token == 'DECIMAL_TYPE' or token == 'STRING_TYPE' or token == 'IF' or token == 'FOR' or (
                    entry[index - 1][0] == 'VARIABLE' and token == 'VARIABLE'):
                if index > 0:
                    structures.append(structure[:])
                    structure.clear()
            structure.append(lexeme)

        if (len(entry) - 1) == index:
            structures.append(structure[:])
            structure.clear()

    for s in reversed(structures):
        for entry_value in s:
            input_entry += f'{entry_value} '

    add_errors_semantics = []

    validated_entry = parser.parse(input_entry)
    if type(validated_entry) is tuple and len(errors) == 0:
        error_value = None, None
        print("Variables valor final -> ", variables)
        [print("Condicionales valor final -> ", c) for c in conditional_result]
        add_errors_semantics.extend(variables_err)
        add_errors_semantics.extend(conditional_err)
        return f'CADENA VALIDA \n', add_errors_semantics
    elif validated_entry is tuple and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n', []
    elif validated_entry is None and len(errors) > 0:
        return f'CADENA INVALIDA {errors[0][1]} \n', []
    else:
        value_error = f'CADENA INVALIDA {error_value[1]} \n'
        error_value = None, None
        return value_error, []
