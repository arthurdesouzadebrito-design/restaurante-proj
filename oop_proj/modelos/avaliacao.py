class Avaliacao:
    """Representa uma avaliação (nota + crítica) feita por um cliente."""

    def __init__(self, cliente: str, nota: int, critica: str = ""):
        self._cliente = cliente
        self._nota = nota
        self._critica = critica

    @property
    def cliente(self):
        return self._cliente

    @property
    def nota(self):
        return self._nota

    @property
    def critica(self):
        return self._critica

    def exibir(self):
        estrelas = "⭐" * self._nota
        print(f"- {self._cliente} | Nota: {self._nota} {estrelas}")
        if self._critica:
            print(f"  Crítica: \"{self._critica}\"")
