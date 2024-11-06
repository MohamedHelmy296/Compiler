import re

class Scanner:
    def __init__(self):
        # Regular expressions for various token types
        self.identifiers = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.numericConst = re.compile(r"-?\d+(\.\d+)?")  # Fixed regex for numeric constants
        self.charConst = re.compile(r"'[a-zA-Z]'")

        # Mapping of keywords and operators
        self.tokensClasses = {
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

    def extract_lexems(self, input_string):
        lexems = []
        current_lexem = ""
        in_comment = False
        
        # Iterate through the input string split by spaces
        for i, lexem in enumerate(input_string.split()):
            if in_comment:
                lexems.append("//")
                return lexems

            current_lexem = ""
            for j, c in enumerate(lexem):
                # Handle special cases for single-character and multi-character tokens
                if c in ";,(){}[]":
                    if current_lexem:
                        lexems.append((current_lexem, i))
                    lexems.append((c, i))
                    current_lexem = ""
                elif c in "+-*/=<>!&|":
                    if current_lexem:
                        lexems.append((current_lexem, i))
                    if j < len(lexem) - 1:
                        ch = lexem[j + 1]
                        s = c + ch
                        if s in self.tokensClasses:
                            lexems.append((s, i))
                            j += 1  # Skip next character for multi-char operator
                        else:
                            lexems.append((c, i))
                    else:
                        lexems.append((c, i))
                    current_lexem = ""
                elif c == "/":
                    if current_lexem:
                        lexems.append((current_lexem, i))
                    if j < len(lexem) - 1 and lexem[j + 1] == "/":
                        in_comment = True  # Handle comments
                        j += 1  # Skip next character
                    else:
                        lexems.append((c, i))
                    current_lexem = ""
                else:
                    current_lexem += c  # Continue building the current lexem

            if current_lexem:
                lexems.append((current_lexem, i))  # Add the last lexem if any

        return lexems
    
    def check_lexem_class(self, lexem, line):
        token = {}

        # Check if lexem matches predefined tokens (keywords, operators, etc.)
        if lexem in self.tokensClasses:
            token["first"] = self.tokensClasses[lexem][0]
            token["second"] = self.tokensClasses[lexem][1]
        # Check if the lexem matches the identifiers regex
        elif re.match(self.identifiers, lexem):
            token["first"] = "Identifier"
            token["second"] = "ID"
        # Check if the lexem matches the character constant regex
        elif re.match(self.charConst, lexem):
            token["first"] = "CharacterConst"
            token["second"] = "CHARCONST"
        # Check if the lexem matches the numeric constant regex
        elif re.match(self.numericConst, lexem):
            token["first"] = "NumericConst"
            token["second"] = "NUMCONST"
        else:
            token["first"] = f"there is an error in line {line}, {lexem} is not defined"

        return token


def main():
    s = Scanner()
    
    # Open input and output files
    with open('test.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        line = 1
        vec = []
        error = False
        
        for inputLine in infile:
            lexems = s.extract_lexems(inputLine.strip())
            
            for lexem in lexems:
                token = s.check_lexem_class(lexem[0], line)
                
                # Check if error condition is met (based on token start with 'th')
                if token['first'].startswith('there is an error'):
                    error = True
                
                if error:
                    print(token['first'], file=outfile)
                else:
                    vec.append(((lexem[0], (token['first'], token['second'])), line))
            
            line += 1
        
        if not error:
            for item in vec:
                lexem, token = item[0]
                print(f"{lexem:<18} {token[0]:<18} {token[1]:<18} {item[1]}", file=outfile)


if __name__ == "__main__":
    main()
