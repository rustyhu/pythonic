"""
A Calculator evaluator loop implementation.
Ref:
https://github.com/wizardforcel/sicp-py-zh/blob/master/3.5.md
http://composingprograms.com/examples/scalc/scalc.html

modified for Lisp-Syntax style expression
"""

from operator import mul, truediv, mod, pow
from typing import Collection, List, Union


##### Stage1: The execution of evaluation(low level implementation) #####
class Exp:
    """A valid expression, basic element of expression tree."""

    known_operators = ['add', 'sub', 'mul', 'div', 'mod', 'pow',
                       '+', '-', '*', '/', '%', '^']

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands: Collection = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '({0} {1})'.format(self.operator, operand_strs)


def calc_apply(operator, args: List):
    """Apply the named operator to a list of args."""

    def check_reduce(op, seq: List):
        if len(seq) < 2:
            raise TypeError(operator + ' requires at least 2 arguments')

        rst = seq[0]
        for n in seq[1:]:
            rst = op(rst, n)
        return rst

    if operator in ('add', '+'):
        return sum(args)

    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])

    if operator in ('mul', '*'):
        return check_reduce(mul, args)

    if operator in ('div', '/'):
        return check_reduce(truediv, args)

    if operator in ('mod', '%'):
        return check_reduce(mod, args)

    if operator in ('pow', '^'):
        return check_reduce(pow, args)

    raise TypeError(operator + ' this operator is not supported.')


def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


##### Stage2: token parse #####
def calc_parse(line: str) -> Union[int, float, Exp]:
    if len(line) == 0:
        raise EmptyTokensWarning("THIS IS EMPTY!")

    def tokenize(line: str) -> List[str]:
        """ lexical analyzer, to generate Exp tree Convert a string into a list of tokens."""
        spaced = line.replace(
            '(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
        return spaced.split()

    tokens = tokenize(line)
    expressions_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra tokens!')

    return expressions_tree


def analyze(tokens: List[str]) -> Union[int, float, Exp]:
    """ Create a nested EXPRESSION tree from a sequence of tokens.  """

    def ananlyze_token(token):
        "Convert string tokens into valid token values(such as interger)"
        try:
            return int(token)
        except (TypeError, ValueError):
            try:
                return float(token)
            except (TypeError, ValueError):
                return token

    token = ananlyze_token(tokens.pop(0))
    # valid LISP style expression always start with 2 patterns
    # 1. number
    if type(token) in (int, float):
        return token

    # 2. '( operator...'
    if token == '(':
        if len(tokens) > 0 and tokens[0] in Exp.known_operators:
            op = tokens.pop(0)
            return Exp(op, analyze_operands(tokens))
        elif len(tokens) >= 2 and tokens[1] == ')':
            t = ananlyze_token(tokens[0])
            if type(t) in (int, float):
                del tokens[:2]
                return t
            else:
                raise SyntaxError(f"unexpected '{t}'")

        else:
            raise SyntaxError(
                "expected valid operator or expression after '('")

    else:
        raise SyntaxError(f"unexpected '{token}'")


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


class EmptyTokensWarning(SyntaxWarning):
    pass


##### Stage3: The Outer loop(User inferface) #####
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    print("Notice: type in 'Ctrl-C' to exit!")
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except EmptyTokensWarning:
            pass  # ignore
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return


if __name__ == '__main__':
    "Example: operator(operand, o)"
    read_eval_print_loop()
