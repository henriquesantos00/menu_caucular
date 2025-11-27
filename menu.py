def calcular_idade():
    ano_nasc = int(input("Digite o ano que você nasceu: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = ano_atual - ano_nasc
    print(f"Sua idade é {idade} anos.\n")

def calcular_preco_compra():
    qtd = int(input("Quantidade de itens: "))
    preco = float(input("Preço por item: R$ "))
    total = qtd * preco
    print(f"Total da compra: R$ {total:.2f}\n")

while True:
    print("MENU")
    print("1 - Calcular idade")
    print("2 - Calcular preço da compra")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        calcular_idade()
    elif opcao == "2":
        calcular_preco_compra()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")