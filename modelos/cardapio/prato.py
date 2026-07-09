from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):

    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'{super().__str__()} | Descrição: {self._descricao}'
