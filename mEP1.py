x = float(input())
op = input()
y = float(input())
if y == 0 and op == "//" or y == 0 and op == "%":
    print("divisao por zero!")
elif op == "+":
    print(f"{x} + {y} = {x+y}")
elif op == "-":
    print(f"{x} - {y} = {x-y}")
elif op == "*":
    print(f"{x} * {y} = {x*y}")
elif op == "//":
    print(f"{x} // {y} = {x//y}")
elif op == "**":
    print(f"{x} ** {y} = {x**y}")
elif op == "%":
    print(f"{x} % {y} = {x%y}")
else:
    print("Operacao nao reconhecida!")