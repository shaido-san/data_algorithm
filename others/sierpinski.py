def sierpinski(n):
    if n == 0:
        return ['▲']
    else:
        prev = sierpinski(n-1)
        space = ' ' * (2 ** (n-1))
        top = [space + p + space for p in prev]
        bottom = [p + ' ' + p for p in prev]
        return top + bottom

# 呼び出し
for line in sierpinski(4):
    print(line)