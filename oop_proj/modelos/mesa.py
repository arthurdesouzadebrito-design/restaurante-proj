class Mesa:
    """Representa uma mesa do restaurante."""

    def __init__(self, numero: int, capacidade: int):
        self._numero = numero
        self._capacidade = capacidade
        self._ocupada = False
        self._cliente_atual = None

    @property
    def numero(self):
        return self._numero

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def ocupada(self):
        return self._ocupada

    def ocupar(self, cliente: str):
        if self._ocupada:
            print(f"Mesa {self._numero} já está ocupada por {self._cliente_atual}.")
            return
        self._ocupada = True
        self._cliente_atual = cliente
        print(f"Mesa {self._numero} ocupada por {cliente}.")

    def liberar(self):
        if not self._ocupada:
            print(f"Mesa {self._numero} já está livre.")
            return
        print(f"Mesa {self._numero} liberada (estava com {self._cliente_atual}).")
        self._ocupada = False
        self._cliente_atual = None

    def exibir(self):
        status = f"Ocupada por {self._cliente_atual}" if self._ocupada else "Livre"
        print(f"Mesa {self._numero} | Capacidade: {self._capacidade} pessoas | Status: {status}")
