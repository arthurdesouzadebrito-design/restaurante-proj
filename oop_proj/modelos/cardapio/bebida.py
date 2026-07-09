from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """Representa uma bebida do cardápio."""

    # Lista de bebidas pré-definidas para facilitar o cadastro rápido.
    # Formato: (nome, preco, tamanho)
    BEBIDAS_PADRAO = [
        ("Refrigerante Cola", 6.50, "350ml"),
        ("Suco de Laranja", 8.00, "300ml"),
        ("Água Mineral", 4.00, "500ml"),
        ("Cerveja Pilsen", 9.90, "600ml"),
        ("Caipirinha", 15.00, "300ml"),
        ("Suco de Maracujá", 8.50, "300ml"),
    ]

    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def exibir(self):
        print(f"- [Bebida] {self._nome} | R$ {self._preco:.2f} | {self._tamanho}")

    @classmethod
    def listar_predefinidas(cls):
        print("\nBebidas pré-definidas:")
        for i, (nome, preco, tamanho) in enumerate(cls.BEBIDAS_PADRAO, start=1):
            print(f"{i}. {nome} - R$ {preco:.2f} - {tamanho}")

    @classmethod
    def criar_a_partir_do_indice(cls, indice: int):
        nome, preco, tamanho = cls.BEBIDAS_PADRAO[indice - 1]
        return cls(nome, preco, tamanho)
