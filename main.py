from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

# teste_fabrica = FabricaFila.pega_fila('normal')
# teste_fabrica.atualiza_fila()
# teste_fabrica.atualiza_fila()
# teste_fabrica.atualiza_fila()
# print(teste_fabrica.chama_cliente(10))

fila = FabricaFila.pega_fila('prioritaria')
fila = FabricaFila.pega_fila('prioritaria')
fila = FabricaFila.pega_fila('prioritaria')
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()

print(fila.chama_cliente(5))
print(fila.chama_cliente(8))
print(fila.chama_cliente(10))

print(fila.estatistica(EstatisticaResumida(1245, '20/03/2025')))
print(fila.estatistica(EstatisticaDetalhada(5468, '21/06/2080')))
