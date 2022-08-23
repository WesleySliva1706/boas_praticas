from fila_base import FilaBase


class FilaNormal(FilaBase):
    codigo: int = 0
    fila: list = []
    clintes_atendidos: list = []
    senha_atual: str = ''

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def chama_cliente(self, caixa) -> str:
        cliente_atual = self.fila.pop(0)
        self.clintes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'
