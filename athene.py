class And:
    def __init__(self, *arguments):
        self.arguments = arguments

    def calculate(self):
        return all(a.calculate() for a in self.arguments)


class Or:
    def __init__(self, *arguments):
        self.arguments = arguments

    def calculate(self):
        return any(a.calculate() for a in self.arguments)


class Not:
    def __init__(self, argument):
        self.argument = argument

    def calculate(self):
        return not self.argument.calculate()


class Implication:
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2

    def calculate(self):
        return not self.argument1.calculate() or self.argument2.calculate()


class Value:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self.value


a = Value(True)
b = Value(True)
c = Value(True)

expr = Implication(
    And(
        Implication(a, b),
        Implication(b, c),
    ),
    Implication(a, c),
)

if __name__ == '__main__':
    print(expr.calculate())
