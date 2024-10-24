from src.modulo1 import entrada_de_datos
from src.modulo2 import depresion
from src.modulo3 import salida_de_resultados

costo_i, valor_f, vida_n = entrada_de_datos()
resultados = depresion (costo_i, valor_f, vida_n)
salida_de_resultados (resultados)