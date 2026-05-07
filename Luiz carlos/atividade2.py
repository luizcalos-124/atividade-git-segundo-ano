print("////// Menu de jogo //////\n")

Estoque = [
    ["Nome", "Preço", "Quantidade em estoque"]
]

a = 0

while a != 4:
    print("/ 1- Cadastrar produto /")
    print("/ 2- Quantidade /")
    print("/ 3- Preço /")
    print("/ 4- Sair /")

    a = int(input("Escolha um: "))

    if (a > 4) or (a < 1):
        print("Número inválido! Tente novamente!")

    elif a == 1:
        nome = input("Digite o nome do item: ")
        quant = int(input("Digite a quantidade do item: "))
        pre = float(input("Digite o valor do produto: "))

        if quant > 50:
            estoque = "Estoque Alto"

        elif quant >= 20 and quant <= 50:
            estoque = "Estoque Médio"

        else:
            estoque = "Estoque Baixo"

        produto = [nome, pre, quant, estoque]
        Estoque.append(produto)

        print("Produto cadastrado com sucesso!\n")

    elif a == 2:
        print("\nQuantidade em estoque:")
        for i in Estoque:
            print(i)

    elif a == 3:
        print("\nLista de preços:")
        for i in Estoque:
            print(i)

print("Programa encerrado.")
