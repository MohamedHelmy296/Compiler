class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.pos = 0

    def parse(self, start_symbol, tokens):
        self.tokens = tokens
        self.pos = 0
        return self._parse_non_terminal(start_symbol)

    def _parse_non_terminal(self, non_terminal):
        if self.pos >= len(self.tokens):
            return False
        rules = self.grammar.get(non_terminal, [])
        for rule in rules:
            start_pos = self.pos
            if self._match(rule):
                return True
            self.pos = start_pos
        return False

    def _match(self, rule):
        for symbol in rule:
            if symbol in self.grammar:  # Non-terminal
                if not self._parse_non_terminal(symbol):
                    return False
            else:  # Terminal
                if self.pos >= len(self.tokens) or self.tokens[self.pos] != symbol:
                    return False
                self.pos += 1
        return True

def is_simple_grammar(grammar):
    return all(len(rules) <= 2 for rules in grammar.values())

def main():
    print("Welcome to the Dynamic Top-Down Parser!")

    while True:
        print("\nEnter grammar rules (Enter 'done' when finished):")
        grammar = {}
        while True:
            rule = input()
            if rule == 'done':
                break
            non_terminal, rule_rhs = rule.split(' -> ')
            grammar.setdefault(non_terminal, []).append(rule_rhs.split())

        if not is_simple_grammar(grammar):
            print("The grammar is not simple. Please enter a simple grammar.")
            continue

        parser = Parser(grammar)
        while True:
            print("\nEnter a sequence to parse (or 'new' to enter a new grammar, 'exit' to quit):")
            sequence = input().strip()
            if sequence == 'exit':
                return
            if sequence == 'new':
                break
            tokens = sequence.split()
            if parser.parse(list(grammar.keys())[0], tokens):
                print("Accepted")
            else:
                print("Rejected")

if __name__ == "__main__":
    main()
