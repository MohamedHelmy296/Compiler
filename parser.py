class RecursiveDescentParser:
    def __init__(self):
        self.rules = {}
        self.start = None

    def load_grammar(self):
        print("Input grammar rules in the form: NonTerminal -> productions.")
        print("Separate multiple productions with a comma ',' and type 'done' when finished.")
        self.rules = {}
        while True:
            entry = input("Enter rule (or 'done' to stop): ")
            if entry.lower() == 'done':
                break
            try:
                lhs, rhs = entry.split("->")
                lhs = lhs.strip()
                rhs = [prod.strip() for prod in rhs.split(",")]
                self.rules.setdefault(lhs, []).extend(rhs)
            except ValueError:
                print("Incorrect format. Example: A -> aB, bC")

        self.start = input("Specify the start symbol: ").strip()

    def validate_simple_grammar(self):
         #Simple Grammar rules.
        if not self.rules:
            print("No grammar provided.")
            return False

        for lhs, rhs_list in self.rules.items():
            for rhs in rhs_list:
                # Ensure each production has at most one non-terminal
                if sum(1 for char in rhs if char.isupper()) > 1:
                    print(f"Rule '{lhs} -> {rhs}' is invalid (more than one non-terminal).")
                    return False

        print("The grammar qualifies as Simple Grammar.")
        return True

    def analyze_sequence(self, input_string):
        #grammar via top-down parsing.
        def helper(expansion, seq, index):
            if index == len(seq):
                return expansion == ""
            if not expansion:
                return False

            current = expansion[0]
            remainder = expansion[1:]

            if current.isupper():  # Non-terminal
                if current not in self.rules:
                    return False
                for alt in self.rules[current]:
                    if helper(alt + remainder, seq, index):
                        return True
            else:  # Terminal
                if index < len(seq) and seq[index] == current:
                    return helper(remainder, seq, index + 1)

            return False

        return helper(self.start, input_string, 0)

    def interface(self):
        while True:
            print("\n--- Menu ---")
            print("1. Input Grammar")
            print("2. Check Grammar Simplicity")
            print("3. Test Sequence")
            print("4. Exit")
            selection = input("Choose an option: ").strip()

            if selection == "1":
                self.load_grammar()
            elif selection == "2":
                if self.validate_simple_grammar():
                    print("The grammar is Simple.")
                else:
                    print("The grammar is not Simple.")
            elif selection == "3":
                if not self.rules:
                    print("Please input grammar first.")
                    continue
                test_seq = input("Enter sequence to test: ").strip()
                if self.analyze_sequence(test_seq):
                    print(f"The sequence '{test_seq}' is Accepted.")
                else:
                    print(f"The sequence '{test_seq}' is Rejected.")
            elif selection == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    RecursiveDescentParser().interface()
