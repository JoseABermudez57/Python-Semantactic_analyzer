import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0

        self.reserved_words = {
            'INTEGER_TYPE': 'Ent',
            'BOOLEAN_TYPE': 'Bool',
            'DECIMAL_TYPE': 'Dcm',
            'STRING_TYPE': 'Cdn',
            'TRUE_VALUE': 'True',
            'FALSE_VALUE': 'False',
            'IF': 'if',
            'FOR': 'for',
            'PIPE': '|',
            'EQUAL': '==',
            'ASSIGNMENT': '=',
            'GREATER_THAN': '>',
            'LESS_THAN': '<',
            'GREATER_OR_EQUAL': '>=',
            'OPEN_BODY': '=>',
            'LESS_OR_EQUAL': '<=',
            'NOT_EQUAL': '!=',
            'PARENTHESIS_CLOSE': ')',
            'PARENTHESIS_OPEN': '(',
            'QUOTATION_MARKS': '"',
            'DOT': ".",
            'ADDITION': '+',
            'SUBTRACTION': '-',
            'RETURN': 'rtn',
            'KUNAI': 'kunai',
        }

        self.reserved_words = dict(sorted(self.reserved_words.items(), key=lambda x: len(x[1]), reverse=True))
        self.variable_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*$')

    def next_token(self):
        self.skip_whitespace()
        if self.pos >= len(self.input_text):
            return None, None

        char = self.input_text[self.pos]
        number = ''

        while self.pos < len(self.input_text) and char.isdigit():
            number += char
            self.pos += 1
            char = self.input_text[self.pos] if self.pos < len(self.input_text) else ''

        if number:
            return "NUMBER", number

        for token, lexeme in self.reserved_words.items():
            if self.input_text[self.pos:].startswith(lexeme):
                self.pos += len(lexeme)
                return token, lexeme

        word = ''

        while self.pos < len(self.input_text) and char.isalnum():
            word += char
            self.pos += 1
            char = self.input_text[self.pos] if self.pos < len(self.input_text) else ''

        if word:
            if self.is_valid_variable(word):
                return "VARIABLE", word
            else:
                return "ERROR", word

        self.pos += 1

        return "ERROR", char

    def skip_whitespace(self):
        self.pos += len(self.input_text[self.pos:]) - len(self.input_text[self.pos:].lstrip())

    def is_valid_variable(self, variable):
        return bool(self.variable_regex.match(variable))
