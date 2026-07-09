import os
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_nome_do_progama():
    print("""
░░░░░██╗███████╗░██████╗░██╗░░░██╗███████╗░██████╗
░░░░░██║██╔════╝██╔════╝░██║░░░██║██╔════╝██╔════╝
░░░░░██║█████╗░░██║░░██╗░██║░░░██║█████╗░░╚█████╗░
██╗░░██║██╔══╝░░██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗
╚█████╔╝███████╗╚██████╔╝╚██████╔╝███████╗██████╔╝
░╚════╝░╚══════╝░╚═════╝░░╚═════╝░╚══════╝╚═════╝░
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Adicionar avaliação')
    print('5. Adicionar item ao cardápio')
    print('6. Exibir cardápio')
    print('7. Sair')


def cadastrar_restaurante():
    limpar_tela()

    print('Cadastro de Restaurante\n')
    nome = input('Nome: ')
    categoria = input('Categoria: ')

    Restaurante(nome, categoria)

    print(f'\n{nome} cadastrado com sucesso!')
    input('\nPressione Enter para voltar ao menu...')


def listar_restaurantes():
    limpar_tela()

    print('Lista de Restaurante\n')

    if not Restaurante.restaurantes:
        print('Nenhum restaurante cadastrado ainda.')
    else:
        Restaurante.listar_restaurantes()

    input('\nPressione Enter para voltar ao menu...')


def buscar_restaurante(nome):
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            return restaurante
    return None


def alternar_estado_restaurante():
    limpar_tela()
    nome = input("Digite o nome do restaurante: ")
    restaurante = buscar_restaurante(nome)

    if restaurante:
        restaurante.ativo = not restaurante.ativo
        if restaurante.ativo:
            print(f"{restaurante._nome} ativado com sucesso!")
        else:
            print(f"{restaurante._nome} desativado com sucesso!")
    else:
        print("Restaurante não encontrado.")

    input('\nPressione Enter para voltar ao menu...')


def adicionar_avaliacao():
    limpar_tela()
    nome = input("Nome do restaurante: ")
    restaurante = buscar_restaurante(nome)

    if restaurante:
        cliente = input("Nome do cliente: ")
        try:
            nota = int(input("Nota (0 a 5): "))
            restaurante.receber_avaliacao(cliente, nota)
            print("Avaliação cadastrada!")
        except ValueError:
            print("Nota inválida.")
    else:
        print("Restaurante não encontrado.")

    input('\nPressione Enter para voltar ao menu...')


def adicionar_item_no_cardapio():
    limpar_tela()
    nome = input("Nome do restaurante: ")
    restaurante = buscar_restaurante(nome)

    if restaurante:
        tipo = input("1 - Prato\n2 - Bebida\nEscolha: ")
        nome_item = input("Nome: ")

        try:
            preco = float(input("Preço: "))
        except ValueError:
            print("Preço inválido.")
            input('\nPressione Enter para voltar ao menu...')
            return

        if tipo == "1":
            descricao = input("Descrição: ")
            item = Prato(nome_item, preco, descricao)
            restaurante.adicionar_no_cardapio(item)
            print("Item adicionado com sucesso!")
        elif tipo == "2":
            tamanho = input("Tamanho: ")
            item = Bebida(nome_item, preco, tamanho)
            restaurante.adicionar_no_cardapio(item)
            print("Item adicionado com sucesso!")
        else:
            print("Tipo inválido.")
    else:
        print("Restaurante não encontrado.")

    input('\nPressione Enter para voltar ao menu...')


def exibir_cardapio():
    limpar_tela()
    nome = input("Nome do restaurante: ")
    restaurante = buscar_restaurante(nome)

    if restaurante:
        restaurante.exibir_cardapio()
    else:
        print("Restaurante não encontrado.")


def finalizar_app():
    limpar_tela()
    print('Programa encerrado!')


def escolher_opcao():
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_restaurante()
    elif opcao == "2":
        listar_restaurantes()
    elif opcao == "3":
        alternar_estado_restaurante()
    elif opcao == "4":
        adicionar_avaliacao()
    elif opcao == "5":
        adicionar_item_no_cardapio()
    elif opcao == "6":
        exibir_cardapio()
        input('\nPressione Enter para voltar ao menu...')
    elif opcao == "7":
        finalizar_app()
        exit()
    else:
        print("Opção inválida.")
        input('\nPressione Enter para voltar ao menu...')


def main():
    while True:
        limpar_tela()
        exibir_nome_do_progama()
        exibir_opcoes()
        escolher_opcao()


if __name__ == "__main__":
    main()
