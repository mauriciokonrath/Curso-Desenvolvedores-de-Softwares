def imposto_renda(nro_horas, valor_h, nro_filhos):
    valor = nro_horas * valor_h
    salario = (valor - (nro_filhos * 189.59))
    if salario <= 1903.98 :
        return 0.00
    elif 1903.99 < salario <= 2826.65:
        txx = ((salario * 7.5) / 100)
        total = (txx - 142.80)
        return total
    elif 2826.66 <= salario <= 3751.05:
        txx = ((salario * 15) / 100)
        total = (txx - 354.80)
        return total
    elif 3751.06 <= salario <= 4664.68:
        txx = ((salario * 22.5) / 100)
        total = (txx - 636.13)
        return total
    else:
        txx = ((salario * 27.5) / 100)
        total = (txx - 869.36)
        return total


# Programa Principal
nro_horas = int(input())
valor_h = float(input())
nro_filhos = int(input())
ir = imposto_renda(nro_horas, valor_h, nro_filhos)

ir_formatado = "{:.2f}".format(ir)
print(ir_formatado)
