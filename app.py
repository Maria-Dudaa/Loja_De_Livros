import random 

livros = {
    "É Assim que Acaba": {"autor(a)": "Colleen Hoover", "preço": 21.99, "estoque": 25},
    "A Culpa é das Estrelas": {"autor(a)": "John Green", "preço": 19.99, "estoque": 50},
    "Um Milhão de Finais Felizes": {"autor(a)": "Vitor Martins", "preço": 16.99, "estoque": 36}
}

total_vendas= 0.0

def cadastrar_livros():
    nome = input ("Digite aqui o nome do livro: ")
    autor = input (f"Digite o nome do autor(a): ")
    preco = float (input(f"Digite o preço de {nome}: "))
    estoque = int (input(f"Digite a quantidade em estoque de {nome}: "))
    livros[nome] = {"autor": autor, "preço": preco, "estoque": estoque}
    print(f"Livro '{nome}' cadastrado com sucesso!\n")

def exibir_livros():
    print("\nLivros disponiveis:")
    for livro, info in livros.items():
       print(f"{livro} - autor(a): {info['autor(a)']}, preço: R${info['preço']:.2f}, Estoque: {info['estoque']} unidades")
    print()

def realizar_venda():
    global total_vendas
    livro_vendido = input("Digite o título do livro que deseja comprar: ")
    if livro_vendido in livros:
        quantidade = int(input(f"Digite a quantidade de {livro_vendido} que deseja comprar: "))
        if livros[livro_vendido]["estoque"] >= quantidade:
            valor_venda = quantidade * livros[livro_vendido]["preço"]
            livros[livro_vendido]["estoque"] -= quantidade
            total_vendas += valor_venda
            print(f"Venda realizada: {quantidade}x {livro_vendido} - Total: R${valor_venda:.2f}\n")
        else:
            print("Quantidade em estoque insuficiente.\n")
    else:
        print("Livro não encontrado.\n")

def exibir_vendas():
    print(f"\nTotal de vendas realizadas: R${total_vendas:.2f}\n")

import random

def sortear_promocao():
    livro_sorteado = random.choice(list(livros.keys()))  
    descontado = random.randint(10, 50) 
    preco_antigo = livros[livro_sorteado]["preço"]
    livros[livro_sorteado]["preço"] *= (1 - descontado / 100)
    print(f"\nPromoção: O livro '{livro_sorteado}' está com {descontado}% de desconto!")
    print(f"Preço original: R${preco_antigo:.2f} | Novo preço: R${livros[livro_sorteado]['preço']:.2f}\n")

def menu():
    while True:
        print("=== Sistema de Gerenciamento de Livros ===")
        print("1. Cadastrar livro")
        print("2. Exibir livros")
        print("3. Realizar venda")
        print("4. Exibir total de vendas")
        print("5. Sortear promoção")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livros()
        elif opcao == "2":
            exibir_livros()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            exibir_vendas()
        elif opcao == "5":
            sortear_promocao()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

menu()