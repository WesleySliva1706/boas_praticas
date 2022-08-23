import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def inserir_cliente(self) -> None:
        self.fila.append(self.senha_atual)
