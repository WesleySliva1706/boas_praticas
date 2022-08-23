# Factory
""" Classe com metodo que recebe uma parametro, para retornar a classe que o
objeto que a chamamou necessita, atraves desse parametro. """

from typing import Union

from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo) -> Union[TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA]:
        if tipo == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo não cadastrado!!!')
