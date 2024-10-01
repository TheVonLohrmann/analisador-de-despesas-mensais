import pandas as pd


# Classe para o usuário se registrar com nome e salário
class Usuario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.despesas = []


# Função para adicionar uma nova despesa
def adicionar_despesa(usuario):
    categoria = input("Digite a categoria da despesa (ex: Alimentação, Transporte, etc.): ")
    valor = float(input("Digite o valor da despesa: "))
    importancia = input("Qual a importância? (Alta, Média, Baixa): ")
    usuario.despesas.append({'Categoria': categoria, 'Valor': valor, 'Importância': importancia})


# Função para imprimir as despesas em forma de tabela
def imprimir_despesas(usuario):
    if len(usuario.despesas) > 0:
        df = pd.DataFrame(usuario.despesas)
        print(df)
    else:
        print("Nenhuma despesa cadastrada.")


# Função para alterar uma despesa
def alterar_despesa(usuario):
    imprimir_despesas(usuario)
    if len(usuario.despesas) > 0:
        indice = int(input("Digite o número da despesa que deseja alterar (começa de 0): "))
        if 0 <= indice < len(usuario.despesas):
            usuario.despesas[indice]['Categoria'] = input("Digite a nova categoria da despesa: ")
            usuario.despesas[indice]['Valor'] = float(input("Digite o novo valor da despesa: "))
            usuario.despesas[indice]['Importância'] = input("Digite a nova importância: ")
        else:
            print("Índice inválido.")
    else:
        print("Nenhuma despesa para alterar.")


# Função para excluir uma despesa
def excluir_despesa(usuario):
    imprimir_despesas(usuario)
    if len(usuario.despesas) > 0:
        indice = int(input("Digite o número da despesa que deseja excluir (começa de 0): "))
        if 0 <= indice < len(usuario.despesas):
            del usuario.despesas[indice]
        else:
            print("Índice inválido.")
    else:
        print("Nenhuma despesa para excluir.")


# Função para gerar relatório de gastos
def relatorio_gastos(usuario):
    total_despesas = sum(d['Valor'] for d in usuario.despesas)
    saldo = usuario.salario - total_despesas
    print(f"Salário: R$ {usuario.salario:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo final: R$ {saldo:.2f}")

    imprimir_despesas(usuario)

    if saldo < 0:
        print("\nVocê está no vermelho!")
        print("Sugestões de economia:")
        sugestoes_economia(usuario)
    else:
        print("\nTudo certo! Sobrou dinheiro.")


# Função para sugerir métodos de economia
def sugestoes_economia(usuario):
    despesas_altas = [d for d in usuario.despesas if d['Importância'].lower() == 'alta']
    despesas_medias = [d for d in usuario.despesas if d['Importância'].lower() == 'média']
    despesas_baixas = [d for d in usuario.despesas if d['Importância'].lower() == 'baixa']

    if despesas_baixas:
        print("Você pode tentar cortar as seguintes despesas de baixa importância:")
        for despesa in despesas_baixas:
            print(f"- {despesa['Categoria']}: R$ {despesa['Valor']:.2f}")

    if despesas_medias:
        print("\nConsidere reduzir as seguintes despesas de importância média:")
        for despesa in despesas_medias:
            print(f"- {despesa['Categoria']}: R$ {despesa['Valor']:.2f}")

    if despesas_altas:
        print(
            "\nEstas são as suas despesas de alta importância. Elas são mais essenciais, então reduzir pode ser "
            "difícil:")
        for despesa in despesas_altas:
            print(f"- {despesa['Categoria']}: R$ {despesa['Valor']:.2f}")


# Função principal para o menu
def menu():
    usuario = None

    while True:
        if usuario is None:
            print("\n--- Cadastro de Usuário ---")
            nome = input("Digite seu nome: ")
            salario = float(input("Digite seu salário: "))
            usuario = Usuario(nome, salario)
        else:
            print("\n--- Menu ---")
            print("1. Adicionar despesa")
            print("2. Alterar despesa")
            print("3. Excluir despesa")
            print("4. Ver relatório de gastos")
            print("5. Sair")
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                adicionar_despesa(usuario)
            elif escolha == 2:
                alterar_despesa(usuario)
            elif escolha == 3:
                excluir_despesa(usuario)
            elif escolha == 4:
                relatorio_gastos(usuario)
            elif escolha == 5:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida!")


# Iniciar o programa
menu()
