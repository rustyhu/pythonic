"""
A Calculator evaluator loop implementation.
Ref: https://github.com/wizardforcel/sicp-py-zh/blob/master/3.5.md
http://composingprograms.com/examples/scalc/scalc.html
"""

from operator import mul
from functools import reduce
from typing import Collection, List, Union


##### Stage1: The execution of evaluation(low level implementation) #####
class Exp(object):
    """A valid expression, basic element of expression tree."""

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands: Collection = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_apply(operator, args: List):
    """Apply the named operator to a list of args."""
    if operator in ('add', '+'):
        return sum(args)

    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])

    if operator in ('mul', '*'):
        return reduce(mul, args, 1)

    if operator in ('div', '/'):
        if len(args) < 2:
            raise TypeError(operator + ' requires at least 2 arguments')
        numer = args[0]
        for d in args[1:]:
            numer /= d
        return numer

    raise TypeError(operator + ' this operator is not supported.')


def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


##### Stage2: token parse #####
def calc_parse(line: str) -> List[Exp]:
    "how to get code token tree"
    tokens = tokenize(line)
    expressions_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra tokens!')

    return expressions_tree


def tokenize(line: str) -> List[str]:
    """
    lexical analyzer, to generate Exp tree
    Convert a string into a list of tokens.
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.split()


known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']


def analyze(tokens: List[str]) -> Union[int, float, Exp]:
    """
    Create a nested EXPRESSION tree from a sequence of tokens.
    """
    token = ananlyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token

    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError("expected '(' after " + token)

        return Exp(token, analyze_operands(tokens))

    else:
        raise SyntaxError("unexpected " + token)


def ananlyze_token(token):
    "Convert string tokens into valid token values(such as interger)"
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def analyze_operands(tokens: List):
    " Read a list of comma-separated operands. "
    operands = []
    while len(tokens) > 0 and tokens[0] != ')':
        # recognize ',' then jump over it
        if operands and tokens[0] == ',':
            tokens.pop(0)
        operands.append(analyze(tokens))

    # recognize ')' then jump over it
    if len(tokens) > 0 and tokens[0] == ')':
        tokens.pop(0)
    else:
        raise SyntaxError('no paired parenthesis!')

    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


##### Stage3: The Outer loop(User inferface) #####
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return


# token and analyze
# Vocabulary:
#   词法分析器 语法分析器； syntax（语法） semantics（语义）

if __name__ == '__main__':
    "Example: operator(operand, o)"
    read_eval_print_loop()
