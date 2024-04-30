def A(s):
    n = []
    k = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            n.append(num)
        elif s[i] == '(':
            k.append(s[i])
            i += 1
        elif s[i] == ')':
            while k[-1] != '(':
                num2 = n.pop()
                num1 = n.pop()
                op = k.pop()
                if op == '+':
                    n.append(num1 + num2)
                elif op == '-':
                    n.append(num1 - num2)
                elif op == '*':
                    n.append(num1 * num2)
                elif op == '/':
                    n.append(num1 // num2)
            k.pop()
            i += 1
        elif s[i] in ['+', '-', '*', '/']:
            while k and k[-1] in ['*', '/'] and s[i] in ['+', '-']:
                num2 = n.pop()
                num1 = n.pop()
                op = k.pop()
                if op == '*':
                    n.append(num1 * num2)
                elif op == '/':
                    n.append(num1 // num2)
            k.append(s[i])
            i += 1
    while k:
        num2 = n.pop()
        num1 = n.pop()
        op = k.pop()
        if op == '+':
            n.append(num1 + num2)
        elif op == '-':
            n.append(num1 - num2)
        elif op == '*':
            n.append(num1 * num2)
        elif op == '/':
            n.append(num1 // num2)
    return n[0]
s = input("Введите выражение: ")
result = A(s)
print("Ответ:", result)
