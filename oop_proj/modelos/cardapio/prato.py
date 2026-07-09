from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    """Representa um prato do cardápio."""

    # Lista de pratos pré-definidos para facilitar o cadastro rápido.
    # Formato: (nome, preco, descricao)
    PRATOS_PADRAO = [
        ("Feijoada Completa", 42.90, "Feijoada com arroz, couve, farofa e laranja"),
        ("Filé à Parmegiana", 38.50, "Filé empanado com molho e queijo, acompanha arroz e fritas"),
        ("Frango Grelhado", 29.90, "Peito de frango grelhado com legumes salteados"),
        ("Macarrão à Bolonhesa", 27.00, "Massa com molho de carne moída e queijo ralado"),
        ("Salada Caesar", 22.50, "Alface, croutons, parmesão e molho caesar"),
        ("Picanha na Chapa", 55.00, "Picanha grelhada com arroz, farofa e vinagrete"),
    ]

    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao

    @property
    def descricao(self):
        return self._descricao

    def exibir(self):
        print(f"- [Prato] {self._nome} | R$ {self._preco:.2f} | {self._descricao}")

    @classmethod
    def listar_predefinidos(cls):
        print("\nPratos pré-definidos:")
        for i, (nome, preco, descricao) in enumerate(cls.PRATOS_PADRAO, start=1):
            print(f"{i}. {nome} - R$ {preco:.2f} - {descricao}")

    @classmethod
    def criar_a_partir_do_indice(cls, indice: int):
        nome, preco, descricao = cls.PRATOS_PADRAO[indice - 1]
        return cls(nome, preco, descricao)
