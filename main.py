import math

# Inteiros (int)
# 1)Escreva um programa que soma dois números inteiros inseridos pelo usuário
def exercicio01():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    resultado = num1 + num2

    print(f" O resultado da soma é: {resultado}.")


# 2)Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
def exercicio02():
    numero = int(input("Digite um número: "))
    resultado = numero % 5

    print(f"O resultado da divisão de {numero} por 5 é: {resultado}.")


# 3)Desenvolva um programa que multiplica dois números fornecidos pelo usuário e mostre o resultado.
def exercicio03():
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    resultado = num1 * num2

    print(f"O resultado da multiplicação é:{resultado} ")


# 4)Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
def exercicio04():
    num1 = int(input("Digite um valor inteiro: "))
    num2 = int(input("Digite outro valor inteiro: "))
    resultado = num1 // num2

    print(f"O resultado da divisão é {resultado}")


# 5)Escreva um programa que calcule o quadrado de um número fornecido pelo usuário
def exercicio05():
    numero = int(input("Digite um valor: "))
    quadrado = numero ** 2 # número digitado pelo usuário **(expoente) ao quadrado (2)

    print(f"{numero} ao quadrado é: {quadrado}") 


# Números de Ponto Flutuante(float)
# 6)Escreva um programa que receba dois números flutuantes e realize sua adição
def exercicio06():
    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))
    resultado = numero1 + numero2

    print(f"A adição entre os número é: {resultado}")



# 7)Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário
def exercicio07():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor: "))
    media = (num1 + num2) / 2

    print(f"A média entre {num1} e {num2} é: {media}")


# 8)Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário.
def exercicio08():
    numero1 = int(input("Digite o valor para calcular sua potência: "))
    numero2 = int(input("Digite o expoente desejado: "))
    resultado = numero1 ** numero2

    print(f"A potência de {numero1} com o expoente {numero2} é: {resultado}")


# 9)Faça um programa que converta a temperatura de Celsius para Fahrenheit
def exercicio09():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius}°C é igual a {fahrenheit:.1f}°F.")


# 10)Escreva um programa que calcula a área de um círculo, recebendo o raio como entrada.
def exercicio10():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * (raio ** 2) 

    print(f"A área de um circulo com o raio {raio} é aproximadamente {area:.2f}.")


# Strings (str)
# 11)Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def exercicio11():
    palavra = str(input("Digite um texto: ")).upper()

    print(palavra)


# 12)Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def exercicio12():
    nome_usuario = str(input("Digite seu nome completo: ")).lower()

    print(nome_usuario)


# 13)Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def exercicio13():
    frase = str(input("Digite uma frase: "))
    frase_espaco = frase.strip()

    print(f"Frase com .strip(): {frase_espaco}")


# 14)Faça um programa que peça ao usuário para digitar uma data no formato “dd/mm/aaa” e, em seguida, imprima o dia, o mês e o ano separadamente.
def exercicio14():
    data = input("Digite uma data em formato dd/mm/aaaa: ")
    dia, mes, ano = data.split("/")

    print("Dia:",dia)
    print("Mês:",mes)
    print("Ano:",ano)


# 15)Escreva um programa que concactene duas strings fornecidas pelo usuário.
def exercicio15():
    texto1 = input("Digite primeiro texto: ")
    texto2 = input("Digite o segundo texto: ")
    texto_conctenado = texto1 + " " + texto2

    print(texto_conctenado)


# Booleanos (bool)
# 16)Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def exercicio16():
    texto1 = input("Digite o primeiro texto true ou false: ").lower() .strip()
    valor_bool1 = texto1 == True
    texto2 = input("Digite o segundo texto true ou false: ")
    valor_bool2 = texto2 == True
    resultado = texto1 and texto2

    print(f"A operação {valor_bool1} and {valor_bool2} resulta em: {resultado}")
    

# 17)Crie um programa que receba dois valores booleanos de usuário e retorne o resultado da operação OR.
def exercicio17():
    texto1 = input("Digite o primeiro valor 'true ou false': ").lower() .strip()
    valor_bool1 = texto1 == True
    texto2 = input("Digite o segundo valor 'true ou false': ").lower() .strip()
    valor_bool2 = texto2 == True

    resultado = valor_bool1 or valor_bool2

    print(f"A operação {valor_bool1} or {valor_bool2} resulta em: {resultado}")


# 18)Desenvolva um programa que peça ao usuário para inserir um valor booleano, e em seguida, inverta esse valor.
def exercicio18():
    texto = input("Digite um valor true ou false:").lower() .strip()
    valor_bool = texto == True

    resultado_invertido = not valor_bool

    print(f"O valor digitado foi {valor_bool}. Sua inversão é {resultado_invertido}")


# 19)Faça um programa que compara se dois números fornecidos pelo usuário são iguais.
def exercicio19():
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite outro valor: ")
    resultado = valor1 == valor2

    print("O resultado de igualde é", resultado)


# 20)Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def exercicio20():
    valor1 = input("Digite um valor: ")
    valor2 = input("Digite outro valor: ")
    resultado = valor1 != valor2

    print("O resultado da diferença é", resultado)




if __name__ == "__main__":
    # exercicio01()
    # exercicio02()
    # exercicio03()
    # exercicio04()
    # exercicio05()
    # exercicio06()
    # exercicio07()
    # exercicio08()
    # exercicio09()
    # exercicio10()
    # exercicio11()
    # exercicio12()
    # exercicio13() 
    # exercicio14()
    # exercicio15()
    # exercicio16()
    # exercicio17()
    # exercicio18()
    # exercicio19()
    exercicio20()
