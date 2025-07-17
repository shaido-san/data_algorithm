def tokenize(expression):
    tokens = []
    num = ''
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(int(num))
                num = ''
            if ch in '+-*/()':
                tokens.append(ch)
    if num:
        tokens.append(int(num))
    return tokens

def precedence(op):
    return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b  # 整数除算
    raise ValueError("未知の演算子")

def evaluate(expression):
    tokens = tokenize(expression)
    values = []
    ops = []

    def compute():
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, int):
            values.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                compute()
            ops.pop()  # '(' を捨てる
        elif token in '+-*/':
            while ops and precedence(ops[-1]) >= precedence(token):
                compute()
            ops.append(token)
        i += 1

    while ops:
        compute()

    return values[0]

print(evaluate("3 + 4 * (2 - 1)"))  # → 7
print(evaluate("10 + 2 * 6"))       # → 22
print(evaluate("(100 * (2 + 12)) / 14"))  # → 100（整数除算）