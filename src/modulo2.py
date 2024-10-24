def depresion(costo_i, valor_f, vida_n):
    resultados = []
    calculo = (costo_i - valor_f) / vida_n
    acumulada = 0
    
    for valor_a in range(1, vida_n + 1):
        acumulada += calculo
        valor_actual = costo_i - acumulada
        resultados.append((valor_a, 2005 + valor_a, calculo, acumulada, valor_actual))
    
    return resultados