from modelos.avaliacao import Avaliacao


class Restaurante:
    """Representa um restaurante com cardápio, mesas e avaliações."""

    restaurantes = []  # lista de todos os restaurantes cadastrados (nível de classe)

    def __init__(self, nome: str, categoria: str):
        self._nome = nome
        self._categoria = categoria
        self._ativo = True
        self._cardapio = []
        self._mesas = []
        self._avaliacoes = []

        Restaurante.restaurantes.append(self)

    # ---------- Propriedades ----------
    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor: bool):
        self._ativo = valor

    # ---------- Cardápio ----------
    def adicionar_no_cardapio(self, item):
        self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f"\nCardápio de {self._nome}:")
        if not self._cardapio:
            print("Nenhum item cadastrado ainda.")
            return
        for item in self._cardapio:
            item.exibir()

    # ---------- Mesas ----------
    def adicionar_mesa(self, mesa):
        self._mesas.append(mesa)

    def buscar_mesa(self, numero: int):
        for mesa in self._mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def listar_mesas(self):
        print(f"\nMesas de {self._nome}:")
        if not self._mesas:
            print("Nenhuma mesa cadastrada ainda.")
            return
        for mesa in self._mesas:
            mesa.exibir()

    # ---------- Avaliações ----------
    def receber_avaliacao(self, cliente: str, nota: int, critica: str = ""):
        avaliacao = Avaliacao(cliente, nota, critica)
        self._avaliacoes.append(avaliacao)

    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        return sum(a.nota for a in self._avaliacoes) / len(self._avaliacoes)

    def exibir_avaliacoes(self):
        print(f"\nAvaliações de {self._nome}:")
        if not self._avaliacoes:
            print("Nenhuma avaliação ainda.")
            return
        for avaliacao in self._avaliacoes:
            avaliacao.exibir()
        print(f"\nMédia geral: {self.media_avaliacoes():.1f} / 5")

    # ---------- Exibição geral ----------
    def exibir(self):
        status = "Ativo" if self._ativo else "Inativo"
        print(f"- {self._nome} | Categoria: {self._categoria} | Status: {status} "
              f"| Mesas: {len(self._mesas)} | Itens no cardápio: {len(self._cardapio)}")

    @classmethod
    def listar_restaurantes(cls):
        if not cls.restaurantes:
            print("Nenhum restaurante cadastrado ainda.")
            return
        for restaurante in cls.restaurantes:
            restaurante.exibir()

    @classmethod
    def buscar_por_nome(cls, nome: str):
        for restaurante in cls.restaurantes:
            if restaurante.nome.lower() == nome.lower():
                return restaurante
        return None
