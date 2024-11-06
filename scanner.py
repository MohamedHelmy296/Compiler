import re

class Scanner:
    def __init__(self):

        self.identifiers = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.numericConst = re.compile(r"-?\d+(\.\d+)?")
        self.charConst = re.compile(r"'[a-zA-Z]'")

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
        temp = input_string
        current_lexem = ""
        in_comment = False
        
        for i, lexem in enumerate(input_string.split()):
            if in_comment:
                lexems.append("//")
                return lexems
            current_lexem = ""
            for j, c in enumerate(lexem):
                if c == ';':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))
                    lexems.append((c, temp.find(c)))
                    current_lexem = ""

                elif c == ',' or c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))
                    lexems.append((c, temp.find(c)))
                    current_lexem = ""

                elif c == '+':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(lexem) - 1:  #input_string -> lexem
                        ch = lexem[i + 1] #input_string -> lexem
                        s = c + ch
                        if ch == '+':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""

                elif c == '-':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '-':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""
                
                elif c == '<':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '=':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""

                elif c == '>':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '=':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""
                
                elif c == '=':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '=':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""

                elif c == '!':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '=':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))
                    current_lexem = ""
                
                elif c == '|':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(input_string) - 1:
                        ch = input_string[i + 1]
                        s = c + ch
                        if ch == '|':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(c)))
                    else:
                        lexems.append((c, temp.find(c)))

                    current_lexem = ""

                elif c == '&':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if i < len(lexem) - 1:
                        ch = lexem[i + 1]
                        s = c + ch
                        if ch == '&':
                            lexems.append((s, temp.find(s)))
                            i += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(s)))
                    else:
                        lexems.append((c, temp.find(s)))

                    current_lexem = ""

                elif c == '/':
                    if current_lexem:
                        lexems.append((current_lexem, temp.find(current_lexem)))

                    if j < len(lexem) - 1:
                        ch = lexem[j + 1]
                        s = c + ch
                        if ch == '/':
                            in_comment = True
                            j += 1  # Skip the next character
                        else:
                            lexems.append((c, temp.find(c)))
                    else:
                        lexems.append((c, temp.find(c)))
                    current_lexem = ""

                else:
                    current_lexem += c

            if current_lexem:
                lexems.append((current_lexem, temp.find(current_lexem)))

        return lexems
    
    def check_lexem_class(self,lexem, l):
        token = {}

        if lexem[0] in self.tokensClasses and self.tokensClasses[lexem[0]][0]:
            token["first"] = self.tokensClasses[lexem[0]][0]
            token["second"] = self.tokensClasses[lexem[0]][1]
        # Check if the lexem matches the identifiers regex
        elif re.match(self.identifiers, lexem[0]):
            token["first"] = "Identifier"
            token["second"] = "ID"
        # Check if the lexem matches the character constant regex
        elif re.match(self.charConst, lexem[0]):
            token["first"] = "CharacterConst"
            token["second"] = "CHARCONST"
        # Check if the lexem matches the numeric constant regex
        elif re.match(self.numericConst, lexem[0]):
            token["first"] = "NumericConst"
            token["second"] = "NUMCONST"
        else:
            token["first"] = f"there is an error in line {l}, {lexem[0]} is not defined"

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
                token = s.check_lexem_class(lexem, line)
                
                # Check if error condition is met (based on token start with 'th')
                if token['first'].startswith('th'):
                    error = True
                
                if error and token['first'].startswith('th'):
                    print(token['first'], file=outfile)
                else:
                    vec.append(((lexem, (token['first'], token['second'])), line))
            
            line += 1
        
        if not error:
            for item in vec:
                lexem, token = item[0]
                print(f"{lexem[0]:<18} {token[0]:<18} {token[1]:<18} {item[1]}", file=outfile)

if __name__ == "__main__":
    main()
    

