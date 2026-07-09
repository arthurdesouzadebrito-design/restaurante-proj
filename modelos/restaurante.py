from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cardapio = []
        self._avaliacoes = []
        self.ativo = True
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(19)} | {'Categoria'.ljust(19)} | Avaliações | Status")
        for restaurante in cls.restaurantes:
            status = 'Ativo' if restaurante.ativo else 'Inativo'
            print(f'{restaurante._nome.ljust(19)} | {restaurante._categoria.ljust(19)} | '
                  f'{str(restaurante.media_avaliacao).ljust(10)} | {status}')

    def receber_avaliacao(self, nome, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(nome, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print("Nota deve estar entre 0 e 5.")

    @property
    def media_avaliacao(self):
        if not self._avaliacoes:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = soma / len(self._avaliacoes)
        return round(media, 1)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'\nCardápio do restaurante: {self._nome}\n')
        if not self._cardapio:
            print('Nenhum item cadastrado no cardápio.')
        else:
            for item in self._cardapio:
                print(item)
