import math  # Importa o módulo math para usar funções matemáticas, como a raiz quadrada

# Função para somar dois números
def soma(a, b):  # a: primeiro número, b: segundo número
    return a + b

# Função para subtrair dois números
def subtrai(a, b):  # a: primeiro número, b: segundo número
    return a - b

# Função para multiplicar dois números
def multiplica(a, b):  # a: primeiro número, b: segundo número
    return a * b

# Função para dividir dois números
def divide(a, b):  # a: numerador, b: denominador
    if b == 0:
        return 'Erro: divisão por zero!'
    return a / b

# Função para calcular a potência de um número
def potencia(a, b):  # a: base, b: expoente
    return a ** b

# Função para calcular o módulo (resto da divisão) de dois números
def modulo(a, b):  # a: dividendo, b: divisor
    return a % b

# Função para calcular a raiz quadrada de um número
def raiz_quadrada(a):  # a: número para calcular a raiz quadrada
    if a < 0:
        return 'Erro: raiz de número negativo!'
    return math.sqrt(a)

# Função para exibir o menu de operações
def menu():
    print('Calculadora Python')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Potência')
    print('6. Módulo')
    print('7. Raiz Quadrada')
    print('0. Sair')

# Loop principal do programa
while True:
    menu()  # Exibe o menu de opções
    escolha = input('Escolha a operação: ')  # Recebe a escolha do usuário
    if escolha == '0':  # Se o usuário escolher 0, o programa encerra
        print('Saindo...')
        break
    elif escolha in ['1', '2', '3', '4', '5', '6']:
        a = float(input('Digite o primeiro número: '))  # Recebe o primeiro número
        b = float(input('Digite o segundo número: '))  # Recebe o segundo número
        if escolha == '1':
            print('Resultado:', soma(a, b))  # Chama a função soma
        elif escolha == '2':
            print('Resultado:', subtrai(a, b))  # Chama a função subtrai
        elif escolha == '3':
            print('Resultado:', multiplica(a, b))  # Chama a função multiplica
        elif escolha == '4':
            print('Resultado:', divide(a, b))  # Chama a função divide
        elif escolha == '5':
            print('Resultado:', potencia(a, b))  # Chama a função potencia
        elif escolha == '6':
            print('Resultado:', modulo(a, b))  # Chama a função modulo
    elif escolha == '7':
        a = float(input('Digite o número: '))  # Recebe o número para a raiz quadrada
        print('Resultado:', raiz_quadrada(a))  # Chama a função raiz_quadrada
    else:
        print('Opção inválida!')  # Caso o usuário digite uma opção inválida
