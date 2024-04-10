import math

# Função para verificar se um número é um quadrado perfeito
def is_perfect_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt*sqrt == n

# Função para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

# Função para gerar os primeiros n números na sequência de Fibonacci
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Obtenha a entrada do usuário
user_input = input("Digite um número ou 'sequence n': ")

# Verifique se a entrada do usuário é um número ou uma sequência
if user_input.startswith('sequence'):
    n = int(user_input.split(' ')[1])
    print(f"A sequência de Fibonacci com {n} números é: {generate_fibonacci(n)}")
else:
    num = int(user_input)
    if is_fibonacci(num):
        print(f"{num} é um número de Fibonacci.")
    else:
        print(f"{num} não é um número de Fibonacci.")
