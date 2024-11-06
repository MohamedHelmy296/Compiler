import re

class Scanner:
    def __init__(self):
        # Regex patterns for identifiers, numeric constants, and character constants
        self.identifiers = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.numeric_const = re.compile(r"-?\d+(\.\d*)?")
        self.char_const = re.compile(r"\'[a-zA-Z]\'")

        # Dictionary for keywords, operators, and special characters
        self.tokens_classes = {
            "int": ("keyword", "INT"),
            "float": ("keyword", "FLOAT"),
            "long long": ("keyword", "LONGLONG"),
            "double": ("keyword", "DOUBLE"),
            "char": ("keyword", "CHAR"),
            "string": ("keyword", "STRING"),
            "if": ("keyword", "IF"),
            "else": ("keyword", "ELSE"),
            "for": ("keyword", "FOR"),
            "const": ("keyword", "CONST"),
            "bool": ("keyword", "BOOL"),
            "return": ("keyword", "RETURN"),
            "auto": ("keyword", "AUTO"),
            "break": ("keyword", "BREAK"),
            "case": ("keyword", "CASE"),
            "continue": ("keyword", "CONTINUE"),
            "default": ("keyword", "DEFAULT"),
            "do": ("keyword", "DO"),
            "goto": ("keyword", "GOTO"),
            "short": ("keyword", "SHORT"),
            "signed": ("keyword", "SIGNED"),
            "sizeof": ("keyword", "SIZEOF"),
            "static": ("keyword", "STATIC"),
            "struct": ("keyword", "STRUCT"),
            "switch": ("keyword", "SWITCH"),
            "typedef": ("keyword", "TYPEDEF"),
            "unsigned": ("keyword", "UNSIGNED"),
            "void": ("keyword", "VOID"),
            "while": ("keyword", "WHILE"),
            "=": ("operator", "ASSIGN"),
            "+": ("operator", "PLUS"),
            "-": ("operator", "MINUS"),
            "*": ("operator", "MULT"),
            "/": ("operator", "DIV"),
            "++": ("operator", "PLUSPLUS"),
            "--": ("operator", "MINUSMINUS"),
            "==": ("operator", "EQ"),
            "<=": ("operator", "<="),
            ">=": ("operator", ">="),
            "!=": ("operator", "NEQ"),
            "<": ("operator", "LESSTHAN"),
            ">": ("operator", "GREATERTHAN"),
            "||": ("operator", "OR"),
            "!": ("operator", "NOT"),
            "&&": ("operator", "AND"),
            "(": ("specialChar", "LPAREN"),
            ")": ("specialChar", "RPAREN"),
            "{": ("specialChar", "LQURLY"),
            "}": ("specialChar", "RQURLY"),
            ";": ("specialChar", "SEMICOLON"),
            "//": ("comment", "COMMENT")
        }

    def extract_lexems(self, input_line):
        lexems = []
        current_lexem = ""
        in_comment = False

        for char in input_line:
            if in_comment:
                break
            elif char.isspace():
                if current_lexem:
                    lexems.append(current_lexem)
                    current_lexem = ""
            elif char == '/':
                if current_lexem == "/":
                    in_comment = True
                elif current_lexem:
                    lexems.append(current_lexem)
                    current_lexem = char
                else:
                    current_lexem = char
            else:
                current_lexem += char

        if current_lexem and not in_comment:
            lexems.append(current_lexem)

        return lexems

    def check_lexem_class(self, lexem, line_number):
        if lexem in self.tokens_classes:
            return self.tokens_classes[lexem]
        elif self.identifiers.fullmatch(lexem):
            return ("Identifier", "ID")
        elif self.numeric_const.fullmatch(lexem):
            return ("NumericConst", "NUMCONST")
        elif self.char_const.fullmatch(lexem):
            return ("CharacterConst", "CHARCONST")
        else:
            return f"Error on line {line_number}: '{lexem}' is not defined"
