cardapio = []
def exibe_menu():
    while True:
        print("********** MENU **********")
        print("1. Adicionar pizza no cardápio")
        print("2. Consultar pizza")
        print("3. Alterar pizza do cardápio")
        print("4. Excluir pizza do cardápio")
        print("5. Exibir cardápio completo")
        print("6. Exportar cardápio para arquivo texto")
        print("7. SAIR")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista_ingredientes = list()
            id = int(input('Digite o código da pizza: '))
            nome = str(input('Digite o nome da pizza: '))
            while True:
                lista_ingredientes.append(str(input('Ingredientes: ')))
                print('Ingrediente adicionado com sucesso!')
                resp = str(input('Deseja adicionar mais ingredientes? [S/N] ')).strip()[0]
                if resp in 'Nn':
                    print('Lista de ingredientes finalizada.')
                    break
            preço = float(input('Digite o preço da pizza: R$'))
            cardapio_cadastrar(id, nome, lista_ingredientes, preço)

        elif opcao == "2":
            id_pizza = int(input('ID: '))
            resultado = cardapio_consulta(id_pizza)
            print(f'O índice da pizza cadastrada é {resultado}')
    
        elif opcao == "3":
            nome = input("Digite o nome da pizza que deseja alterar: ")
            for pizza in cardapio:
                if pizza["nome"] == nome:
                    print(f"Nome atual: {pizza['nome']}")
                    novo_nome = input("Digite o novo nome da pizza: ")
                    pizza["nome"] = novo_nome

                    print(f"Ingredientes atuais: {pizza['ingredientes']}")
                    novos_ingredientes = input("Digite os novos ingredientes da pizza: ")
                    pizza["ingredientes"] = novos_ingredientes

                    print(f"Valor atual: {pizza['valor']}")
                    novo_valor = float(input("Digite o novo valor da pizza: "))
                    pizza["valor"] = novo_valor

                    print("Pizza alterada com sucesso no cardápio!")
                    break
            else:
                print("Pizza não encontrada no cardápio!")

        elif opcao == "4":
            nome = input("Digite o nome da pizza que deseja excluir: ")
            for pizza in cardapio:
                if pizza["nome"] == nome:
                    cardapio.remove(pizza)
                    print("Pizza removida com sucesso do cardápio!")
                    break
            else:
                print("Pizza não encontrada no cardápio!")

        elif opcao == "5":
            if cardapio:
                print("********** CARDÁPIO **********")
                for pizza in cardapio:
                    print(f"Nome: {pizza['nome']}")
                    print(f"Ingredientes: {pizza['ingredientes']}")
                    print(f"Valor: {pizza['valor']}")
                    print("------------------------------")
            else:
                print("O cardápio está vazio!")

        elif opcao == "6":
            if cardapio:
                nome_arquivo = input("Digite o nome do arquivo para exportar o cardápio: ")
                with open(nome_arquivo, "w") as arquivo:
                    for pizza in cardapio:
                        arquivo.write(f"Nome: {pizza['nome']}\n")
                        arquivo
        elif opcao == "7":
            print('Finalizando o sistema... Até logo!')
            break

def cardapio_cadastrar(id, nome, ingrediente, preço):
    item = dict()
    item['id'] = id
    item['nome'] = nome
    item['ingredientes'] = ingrediente
    item['preço'] = preço
    cardapio.append(item)
    print("Pizza adicionada com sucesso no cardápio!")

def cardapio_consulta(id):
    for indice, valor in enumerate(cardapio):
        if valor['id'] == id:
            return indice
    return None

exibe_menu()
print(cardapio)