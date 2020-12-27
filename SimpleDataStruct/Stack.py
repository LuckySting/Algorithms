def check(parts):
    stack = list()
    bis = list()
    i = 0
    for p in parts:
        i += 1
        if p in ('}', ')', ']'):
            idx = i
            pb = '{'
            if p == ')':
                pb = '('
            elif p == ']':
                pb = '['
            if len(stack) != 0 and stack[-1] == pb:
                stack.pop()
                bis.pop()
            else:
                return idx
        elif p in ('{', '(', '['):
            bis.append(i)
            stack.append(p)
    if len(stack) != 0:
        return bis[-1]
    return 'Success'


if __name__ == '__main__':
    print(check(input()))
# assert check("{{{[][][]") == 3
# assert check("{*{{}") == 3
# assert check("[[*") == 2
# assert check("{*}") == 'Success'
# assert check("{{") == 2
# assert check("{}") == 'Success'
# assert check("") == 'Success'
# assert check("}") == 1
# assert check("*{}") == 'Success'
# assert check("{{{**[][][]") == 3
