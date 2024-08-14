# Desafio 1 Condicional
# Criar um sistema de E-commerce, onde o usuario possa 
# cadastrar-se 
# comprar um produto 
# descobrir o valor total
# Pagar

produtos = {
    "Camiseta": 94.99,
    "Calça": 170.99,
    "Tênis": 379.99
}

carrinho = []

def cadastrar():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    print(f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}.")

def adicionar_ao_carrinho(produto):
    carrinho.append(produto)
    print(f"Produto {produto} adicionado ao carrinho.")

def calcular_total():
    total = 0
    for produto in carrinho:
        total += produtos[produto]
    print(f"O valor total da sua compra é R$ {total:.2f}")

def realizar_pagamento():
    print("Simulando pagamento...")
    print("Pagamento realizado com sucesso!")
    carrinho.clear()  

def menu():
    while True:
        print("\n--- Bem-vindo à Nike Store ---")
        print("1. Cadastrar-se")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver valor total")
        print("4. Realizar pagamento")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            produto = input("Digite o nome do produto: ")
            if produto in produtos:
                adicionar_ao_carrinho(produto)
            else:
                print("Produto não encontrado.")
        elif opcao == '3':
            calcular_total()
        elif opcao == '4':
            realizar_pagamento()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

