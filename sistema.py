from time import sleep
cardapio = list()
menu = ['Adicionar pizza no cardápio', 'Consultar pizza', 'Alterar pizza do cardápio', 'Excluir pizza do cardápio',
        'Exibir cardápio completo', 'Exportar cardápio para arquivo texto', 'Sair']


def exibe_menu(lista):
    print('-' * 30)
    print('MENU INICIAL'.center(30))
    print('-' * 30)
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c += 1
    
    
def cardapio_cadastrar(id, nome, ingredientes, preço):
    item = dict()
    item['id'] = id
    item['nome'] = nome
    item['ingredientes'] = ingredientes
    item['preço'] = preço
    cardapio.append(item)

    
def cardapio_consulta(id):
    pizza_encontrada = ''
    indice_encontrado = ''
    for indice, valor in enumerate(cardapio):
        if valor['id'] == id:
            indice_encontrado = indice
            pizza_encontrada = cardapio[indice_encontrado]
            return pizza_encontrada
    return None
        
    
def cardapio_alterar(id, pizza_atualizada):
    pizza_encontrada = ''
    indice_encontrado = ''
    for indice, valor in enumerate(cardapio):
        if valor['id'] == id:
            indice_encontrado = indice
            pizza_encontrada = cardapio[indice_encontrado]
    if pizza_encontrada:
        cardapio[indice_encontrado] = pizza_atualizada
        print('Pizza atualizada com sucesso!')
    else:
        print('Não foi possível concluir as atualizações, ID não encontrado.')
    
    
def cardapio_remover(id):
    pizza_encontrada = ''
    indice_encontrado = ''
    for indice, valor in enumerate(cardapio):
        if valor['id'] == id:
            indice_encontrado = indice
            pizza_encontrada = cardapio[indice_encontrado]
    if pizza_encontrada:
        del cardapio[indice_encontrado]
        print('Pizza removida com sucesso!')
    else:
        print('ID não encontrado, não foi possível concluir a remoção.')
    
    
def cardapio_exibir():
    if cardapio:
        for pizza in cardapio:
            print(f"Código: {pizza['id']} - Pizza: {pizza['nome']} - Ingredientes: {pizza['ingredientes']} - Preço: R${pizza['preço']:.2f}")
    else:
        print('Não há nenhuma pizza cadastrada.')
    
    
def cardapio_salvar(lista):
    arquivo = open('cardapio.txt', 'w')
    for pizza in lista:
        arquivo.write(f'Pizza: {pizza};\n')
    arquivo.close()
    # Crie uma função chamada cardapio_salvar que irá gravar todos os itens da lista cardápio em um arquivo texto, onde cada campo da pizza esteja separado por ";" e cada pizza do cardápio fique em uma linha do arquivo texto.
    
def valida_id(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('O código da pizza(ID) deve ser um número inteiro, tente novamente.')
            continue
        else:
            return num


def valida_preço(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um preço válido.')
            continue
        else:
            return num

while True:
    exibe_menu(menu)
    opção = int(input('Selecione uma opção: '))
    print('-' * 30)
    if opção == 1:
        print('-' * 30)
        print('CADASTRAR PIZZA'.center(30))
        print('-' * 30)
        id_pizza = valida_id('ID: ')
        nome_pizza = str(input('Nome: '))
        ingredientes_pizza = list()
        while True:
            ingredientes_pizza.append(str(input('Digite um ingrediente para adicionar: ')))
            print('Ingrediente adicionado com sucesso!')
            opção = str(input('Quer adicionar mais ingredientes? [S/N] ')).strip()[0]
            if opção in 'Nn':
                print('Lista de ingredientes finalizada.')
                break
        preço_pizza = valida_preço('Preço: R$')
        cardapio_cadastrar(id_pizza, nome_pizza, ingredientes_pizza, preço_pizza)
        print('Pizza adicionada com sucesso!')
    elif opção == 2:
        print('-' * 30)
        print('CONSULTAR PIZZA'.center(30))
        print('-' * 30)
        id_pizza = valida_id('ID: ')
        resultado = cardapio_consulta(id_pizza)
        print(f'O índice da pizza cadastrada é {resultado}.')
    elif opção == 3:
        print('-' * 30)
        print('ALTERAR PIZZA'.center(30))
        print('-' * 30)
        id_pizza = valida_id('Digite o ID da pizza que deseja alterar: ')
        nova_pizza = dict()
        nova_pizza['id'] = valida_id('ID: ')
        nova_pizza['nome'] = str(input('Nome: '))
        lista_ingredientes = list()
        while True:
            lista_ingredientes.append(str(input('Digite um ingrediente para adicionar: ')))
            print('Ingrediente adicionado com sucesso!')
            opção = str(input('Quer adicionar mais ingredientes? [S/N] ')).strip()[0]
            if opção in 'Nn':
                print('Lista de ingredientes finalizada.')
                break
        nova_pizza['ingredientes'] = lista_ingredientes
        nova_pizza['preço'] = valida_preço('Preço: R$')
        cardapio_alterar(id_pizza, nova_pizza)
    elif opção == 4:
        print('-' * 30)
        print('REMOVER PIZZA'.center(30))
        print('-' * 30)
        id_pizza = valida_id('Digite o ID da pizza que deseja remover: ')
        cardapio_remover(id_pizza)
    elif opção == 5:
        print('-' * 30)
        print('CARDAPIO PIZZARIA'.center(30))
        print('-' * 30)
        cardapio_exibir()
    elif opção == 6:
        cardapio_salvar(cardapio)
    elif opção == 7:
        print('Finalizando o sistema... Até logo!')
        break
    else:
        print('Por favor, digite uma opção válida.')
    sleep(0.5)
