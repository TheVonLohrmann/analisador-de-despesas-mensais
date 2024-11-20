# Classe para o Usuário
class Usuario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.cartao_credito = False
        self.limite_cartao = 0
        self.fatura_cartao = 0

    def adicionar_cartao(self, limite_cartao):
        self.cartao_credito = True
        self.limite_cartao = limite_cartao


# Classe para Despesas
class Despesa:
    def __init__(self, categoria, valor, importancia, descricao, pagamento_credito=False):
        self.categoria = categoria
        self.valor = valor
        self.importancia = importancia
        self.descricao = descricao
        self.pagamento_credito = pagamento_credito


# Função para registro do usuário
def registrar_usuario():
    nome = input("Digite seu nome: ")
    salario = float(input("Digite o valor do seu salário: "))
    usuario = Usuario(nome, salario)

    # Verificar se o usuário possui cartão de crédito
    possui_cartao = input("Você possui cartão de crédito? (s/n): ").lower()
    if possui_cartao == 's':
        limite_cartao = float(input("Digite o limite do seu cartão de crédito: "))
        usuario.adicionar_cartao(limite_cartao)

    return usuario


# Função para adicionar despesa
def adicionar_despesa(usuario, despesas):
    categoria = input("Digite a categoria da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    importancia = input("A despesa é essencial, média ou baixa? ").lower()
    descricao = input("Digite uma descrição para a despesa: ")

    # Verificar se a despesa será paga no crédito
    if usuario.cartao_credito:
        pagamento_credito = input("Essa despesa será paga no crédito? (s/n): ").lower() == 's'
        if pagamento_credito:
            if usuario.fatura_cartao + valor > usuario.limite_cartao:
                print("Cartão estourou! Despesa não pode ser adicionada no crédito.")
                return
            else:
                usuario.fatura_cartao += valor
    else:
        pagamento_credito = False

    despesa = Despesa(categoria, valor, importancia, descricao, pagamento_credito)
    despesas.append(despesa)
    print("Despesa adicionada com sucesso!")


# Função para alterar despesa
def alterar_despesa(despesas):
    listar_despesas(despesas)
    indice = int(input("Digite o número da despesa que deseja alterar: ")) - 1
    if 0 <= indice < len(despesas):
        despesas[indice].categoria = input("Digite a nova categoria: ")
        despesas[indice].valor = float(input("Digite o novo valor: "))
        despesas[indice].importancia = input("Digite a nova importância (essencial, média, baixa): ").lower()
        despesas[indice].descricao = input("Digite a nova descrição: ")
        print("Despesa alterada com sucesso!")
    else:
        print("Índice inválido!")


# Função para excluir despesa
def excluir_despesa(despesas):
    listar_despesas(despesas)
    indice = int(input("Digite o número da despesa que deseja excluir: ")) - 1
    if 0 <= indice < len(despesas):
        despesas.pop(indice)
        print("Despesa excluída com sucesso!")
    else:
        print("Índice inválido!")


# Função para listar todas as despesas
def listar_despesas(despesas):
    if despesas:
        print("\n--- Lista de Despesas ---")
        for i, despesa in enumerate(despesas, 1):
            print(
                f"{i}. {despesa.categoria} - R${despesa.valor:.2f} - {despesa.importancia.capitalize()} - {despesa.descricao}")
            if despesa.pagamento_credito:
                print("   (Pago no crédito)")
    else:
        print("Nenhuma despesa cadastrada.")


# Função para relatório de gastos
def relatorio_gastos(usuario, despesas):
    total_despesas = sum(d.valor for d in despesas if not d.pagamento_credito)
    total_despesas += usuario.fatura_cartao
    saldo_restante = usuario.salario - total_despesas

    print("\n--- Relatório de Gastos ---")
    listar_despesas(despesas)
    print(f"Fatura do cartão: R${usuario.fatura_cartao:.2f}")
    print(f"Total de despesas: R${total_despesas:.2f}")
    print(f"Salário restante: R${saldo_restante:.2f}")

    if saldo_restante < 0:
        print("\nAtenção! Você está no vermelho.")
        sugerir_economia(despesas)


# Função para sugerir métodos de economia
def sugerir_economia(despesas):
    print("\n--- Métodos de Economia ---")
    despesas_nao_essenciais = [d for d in despesas if d.importancia != 'essencial']
    if despesas_nao_essenciais:
        print("Considere reduzir ou eliminar as seguintes despesas:")
        for despesa in despesas_nao_essenciais:
            print(f"- {despesa.descricao}: R${despesa.valor:.2f} ({despesa.categoria})")
    else:
        print("Todas as despesas são essenciais. Tente aumentar sua renda.")


# Função principal com menu
def menu():
    usuario = registrar_usuario()
    despesas = []

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar despesa")
        print("2. Alterar despesa")
        print("3. Excluir despesa")
        print("4. Relatório de gastos")
        print("5. Sugerir economia")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_despesa(usuario, despesas)
        elif opcao == "2":
            alterar_despesa(despesas)
        elif opcao == "3":
            excluir_despesa(despesas)
        elif opcao == "4":
            relatorio_gastos(usuario, despesas)
        elif opcao == "5":
            sugerir_economia(despesas)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
menu()
