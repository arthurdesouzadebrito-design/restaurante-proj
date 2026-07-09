class ItemCardapio:
    """Classe base para qualquer item do cardápio (Prato, Bebida etc)."""

    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def exibir(self):
        print(f"- {self._nome} | R$ {self._preco:.2f}")

    def __str__(self):
        return f"{self._nome} (R$ {self._preco:.2f})"
