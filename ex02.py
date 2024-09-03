def isFibonacci(n):
    a, b = 0, 1

    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

x = int(input("Digite um número: "))

if isFibonacci(x):
    print(f"O número {x} pertence a sequência de Fibonacci.")
else:
    print(f"O número {x} não pertence a sequência de Fibonacci.")
