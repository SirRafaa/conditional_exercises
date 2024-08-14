import random

# Condicionais 

# Exercicios 1

numero = random.randint(-100,100)
if numero > 0:
    print(f'Seu número é Positivo e Seu número é: {numero}')
elif numero == 0:
    print(f'Seu numero é nulo ou seja igual a zero, Seu número: {numero}')
else:
    print(f'Seu número é Negativo e Seu número é: {numero}')

# Exercícios 2 
    
idade = int(input('Digite sua Idade: '))
idade_minima = 16

if idade >= idade_minima:
    print('Pessoa Apta para votação')
else:
    print('Você ainda não pode votar')

# Exercícios 3

num = random.randint(0,10000)
if num % 2 == 0:
    print (f'O número: {num} é Par. ')
elif num % 2 == 1:
    print(f'O número : {num} é Ímpar. ')

# Exercícios 4

def verifica_triangulo(lado1, lado2, lado3):

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "Não forma um triângulo"

for i in range(3):
    lado1 = random.randint(1, 10)  
    lado2 = random.randint(1, 10)
    lado3 = random.randint(1, 10)

    resultado = verifica_triangulo(lado1, lado2, lado3)
    print(f"Triângulo {i+1}: Lados {lado1}, {lado2}, {lado3} - {resultado}")

# Exercicio 5
def multiplo_5_e_7(num1):

    if num1 % 5 == 0 and num1 % 7 == 0:
        return f"O número {num1} é múltiplo de 5 e 7."
    elif num1 % 5 == 0:
        return f"O número {num1} é múltiplo de 5."
    elif num1 % 7 == 0:
        return f"O número {num1} é múltiplo de 7."
    else:
        return f"O número {num1} não é múltiplo de 5 nem de 7."

num1 = random.randint(0, 10000)
resultado = multiplo_5_e_7(num1)
print(resultado)

#  Exercício 6

numero_positivo = random.randint(0,20)
if numero_positivo >= 10:
    print(f'O número {numero_positivo} é maior que 10. ')
else:
    print(f'O número {numero_positivo} é menor que 10. ')

# Exercício 7 
def divisivel_por_3_e_5(num2):

    if num2 % 3 == 0 and num2 % 5 == 0:
        return f"O número {num2} é divisivel por 3 e 5."
    elif num2 % 3 == 0:
        return f"O número {num2} é divisivel por 3."
    elif num2 % 5 == 0:
        return f"O número {num2} é divisivel por 5."
    else: 
        return f"O número {num2} não é divisivel por 3 e nem por 5."
    
num2 = random.randint(0,10000)
resultado2 = divisivel_por_3_e_5(num2)
print(resultado2)