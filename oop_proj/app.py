import os
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.mesa import Mesa


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_nome_do_programa():
    print("""
░██████╗███████╗███╗░░██╗░█████╗░░█████╗░
██╔════╝██╔════╝████╗░██║██╔══██╗██╔══██╗
╚█████╗░█████╗░░██╔██╗██║███████║██║░░╚═╝
░╚═══██╗██╔══╝░░██║╚████║██╔══██║██║░░██╗
██████╔╝███████╗██║░╚███║██║░░██║╚█████╔╝
╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░
""")


def exibir_opcoes():
    print('1.  Cadastrar restaurante')
    print('2.  Listar restaurantes')
    print('3.  Alternar estado do restaurante')
    print('4.  Adicionar mesa')
    print('5.  Listar mesas')
    print('6.  Ocupar/Liberar mesa')
    print('7.  Adicionar item ao cardápio')
    print('8.  Exibir cardápio')
    print('9.  Adicionar avaliação (com crítica)')
    print('10. Exibir avaliações')
    print('11. Sair')


def buscar_restaurante_por_input():
    nome = input("Nome do restaurante: ")
    restaurante = Restaurante.buscar_por_nome(nome)
    if not restaurante:
        print("Restaurante não encontrado.")
    return restaurante


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
    print('Lista de Restaurantes\n')

    Restaurante.listar_restaurantes()

    input('\nPressione Enter para voltar ao menu...')


def alternar_estado_restaurante():
    limpar_tela()
    print("Alternar estado do restaurante\n")

    restaurante = buscar_restaurante_por_input()
    if restaurante:
        restaurante.ativo = not restaurante.ativo
        estado = "ativado" if restaurante.ativo else "desativado"
        print(f"{restaurante.nome} {estado} com sucesso!")

    input('\nPressione Enter para voltar ao menu...')


def adicionar_mesa():
    limpar_tela()
    print("Adicionar mesa\n")

    restaurante = buscar_restaurante_por_input()
    if restaurante:
        try:
            numero = int(input("Número da mesa: "))
            capacidade = int(input("Capacidade (nº de pessoas): "))
        except ValueError:
            print("Valor inválido.")
            input('\nPressione Enter para voltar ao menu...')
            return

        if restaurante.buscar_mesa(numero):
            print(f"Já existe uma mesa com o número {numero}.")
        else:
            restaurante.adicionar_mesa(Mesa(numero, capacidade))
            print(f"Mesa {numero} cadastrada com sucesso!")

    input('\nPressione Enter para voltar ao menu...')


def listar_mesas():
    limpar_tela()
    print("Listar mesas\n")

    restaurante = buscar_restaurante_por_input()
    if restaurante:
        restaurante.listar_mesas()

    input('\nPressione Enter para voltar ao menu...')


def ocupar_ou_liberar_mesa():
    limpar_tela()
    print("Ocupar/Liberar mesa\n")

    restaurante = buscar_restaurante_por_input()
    if not restaurante:
        input('\nPressione Enter para voltar ao menu...')
        return

    try:
        numero = int(input("Número da mesa: "))
    except ValueError:
        print("Valor inválido.")
        input('\nPressione Enter para voltar ao menu...')
        return

    mesa = restaurante.buscar_mesa(numero)
    if not mesa:
        print("Mesa não encontrada.")
        input('\nPressione Enter para voltar ao menu...')
        return

    if mesa.ocupada:
        mesa.liberar()
    else:
        cliente = input("Nome do cliente: ")
        mesa.ocupar(cliente)

    input('\nPressione Enter para voltar ao menu...')


def adicionar_item_no_cardapio():
    limpar_tela()
    print("Adicionar item ao cardápio\n")

    restaurante = buscar_restaurante_por_input()
    if not restaurante:
        input('\nPressione Enter para voltar ao menu...')
        return

    tipo = input("1 - Prato\n2 - Bebida\nEscolha: ")

    if tipo == "1":
        Prato.listar_predefinidos()
        print("0. Cadastrar um prato personalizado")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            nome_item = input("Nome: ")
            preco = float(input("Preço: "))
            descricao = input("Descrição: ")
            item = Prato(nome_item, preco, descricao)
        else:
            try:
                item = Prato.criar_a_partir_do_indice(int(escolha))
            except (ValueError, IndexError):
                print("Opção inválida.")
                input('\nPressione Enter para voltar ao menu...')
                return

        restaurante.adicionar_no_cardapio(item)
        print(f"\n{item.nome} adicionado ao cardápio com sucesso!")

    elif tipo == "2":
        Bebida.listar_predefinidas()
        print("0. Cadastrar uma bebida personalizada")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            nome_item = input("Nome: ")
            preco = float(input("Preço: "))
            tamanho = input("Tamanho: ")
            item = Bebida(nome_item, preco, tamanho)
        else:
            try:
                item = Bebida.criar_a_partir_do_indice(int(escolha))
            except (ValueError, IndexError):
                print("Opção inválida.")
                input('\nPressione Enter para voltar ao menu...')
                return

        restaurante.adicionar_no_cardapio(item)
        print(f"\n{item.nome} adicionado ao cardápio com sucesso!")

    else:
        print("Opção inválida.")

    input('\nPressione Enter para voltar ao menu...')


def exibir_cardapio():
    limpar_tela()
    print("Exibir cardápio\n")

    restaurante = buscar_restaurante_por_input()
    if restaurante:
        restaurante.exibir_cardapio()

    input('\nPressione Enter para voltar ao menu...')


def adicionar_avaliacao():
    limpar_tela()
    print("Adicionar avaliação\n")

    restaurante = buscar_restaurante_por_input()
    if not restaurante:
        input('\nPressione Enter para voltar ao menu...')
        return

    cliente = input("Nome do cliente: ")

    try:
        nota = int(input("Nota (0 a 5): "))
    except ValueError:
        print("Nota inválida.")
        input('\nPressione Enter para voltar ao menu...')
        return

    if nota < 0 or nota > 5:
        print("A nota deve estar entre 0 e 5.")
        input('\nPressione Enter para voltar ao menu...')
        return

    critica = input("Deixe sua crítica/comentário (opcional): ")

    restaurante.receber_avaliacao(cliente, nota, critica)
    print("\nAvaliação cadastrada com sucesso!")

    input('\nPressione Enter para voltar ao menu...')


def exibir_avaliacoes():
    limpar_tela()
    print("Exibir avaliações\n")

    restaurante = buscar_restaurante_por_input()
    if restaurante:
        restaurante.exibir_avaliacoes()

    input('\nPressione Enter para voltar ao menu...')


def finalizar_app():
    limpar_tela()
    print('Programa encerrado!')


def escolher_opcao():
    opcao = input("\nEscolha uma opção: ")

    acoes = {
        "1": cadastrar_restaurante,
        "2": listar_restaurantes,
        "3": alternar_estado_restaurante,
        "4": adicionar_mesa,
        "5": listar_mesas,
        "6": ocupar_ou_liberar_mesa,
        "7": adicionar_item_no_cardapio,
        "8": exibir_cardapio,
        "9": adicionar_avaliacao,
        "10": exibir_avaliacoes,
    }

    if opcao == "11":
        finalizar_app()
        exit()
    elif opcao in acoes:
        acoes[opcao]()
    else:
        print("Opção inválida.")
        input('\nPressione Enter para voltar ao menu...')


def main():
    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()


if __name__ == "__main__":
    main()
