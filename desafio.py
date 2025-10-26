# Cria variável padrão
nome_padrao = ""
salario_num = None
valor_bonus = None

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ").strip()

if not nome:
    print("Erro: O nome não pode ser vazio.")
elif not nome.replace(' ', '').isalpha():
    print("Erro: O nome deve conter apenas letras e espaços.")
else:
    nome_padrao = nome.title()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_input = input("Digite o valor do seu salário: ")

    salario_limpo = salario_input.strip().replace(".",",").replace(",",".")

    if not salario_limpo:
        print("Erro: O valor do salário não pode ser vazio.")
    else:
        salario = float(salario_limpo)

        if salario < 0:
            print("Erro: O valor do salário não pode ser negativo.")
        else:
            salario_num = salario

except:
    print(f"Erro: A entrada '{salario_input}' não é um número válido.")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_input = input("Digite o valor do seu bônus:R$ ")
    bonus_limpo = bonus_input.strip().replace(".",",").replace(",",".")

    if not bonus_limpo:
        print("Erro: O valor do seu bônus não pode ser vazio")
    else:
        bonus = float(bonus_limpo)
        if bonus < 0:
            print("Erro: O valor do bônus não pode ser negativo")
        else:
            valor_bonus = bonus
except:
    print(f"Erro: A entrada '{bonus_input}' não é número válido.")

# 4) Calcule o valor do bônus final
if nome_padrao and salario_num is not None and bonus is not None:
    valor_total = salario_num + bonus


# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bônus
    print("\n" +"=" * 40)
    print("----------RECIBO DE PAGAMENTO----------")
    print("\n" +"=" * 40)
    print(f"Colaborador: {nome_padrao}")

    print(f"Salário Base: R${salario_num:.2f}")
    print(f"Bônus a Receber: R$ {bonus:.2f}")
    print("\n" +"=" * 40)
    print(f"TOTAL A RECEBER: R$ {valor_total:.2f}")
    print("\n" +"=" * 40)

else:
    print("\n" +"=" * 40)
    print("AVISO: O processamento falhou devido a erros de entradada de dados.")
    print("Por favor, execute o programa novamente e insira valores válidos.")
    print("\n" +"=" * 40)

    