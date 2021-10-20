def meus_func(nome_depto, depto, func, funcXdepto):
    lista = []
    if nome_depto == 'Vendas':
        cont = 0
        for i in (funcXdepto):
            if i == 0:
                lista.append(func[cont])
            cont += 1
    if nome_depto == 'Compras':
        cont = 0
        for i in (funcXdepto):
            if i == 1:
                lista.append(func[cont])
            cont += 1
    if nome_depto == 'RH':
        cont = 0
        for i in (funcXdepto):
            if i == 2:
                lista.append(func[cont])
            cont += 1
    if nome_depto == 'TI':
        cont = 0
        for i in (funcXdepto):
            if i == 3:
                lista.append(func[cont])
            cont += 1
    if nome_depto == 'Marketing':
        cont = 0
        for i in (funcXdepto):
            if i == 4:
                lista.append(func[cont])
            cont += 1

    if nome_depto in depto:
        return lista
    else:
        return (["Departamento inexistente"])


def meu_depto(nome_func, depto, func, funcXdepto):
    if nome_func in func:
        cont = 0
        for i in func:
            if i == nome_func:
                x = (funcXdepto[cont])
                return(depto[x])
            cont += 1
    else:
        return ("Funcionario inexistente")


#Programa principal
depto = ['Vendas', 'Compras', 'RH', 'TI', 'Marketing']
func = ['Joao', 'Paulo', 'Clara', 'Eduardo', 'Ana', 'Jorge', 'Augusto', 'Pedro', 'Roberto', 'Manoel',
'Luis', 'Inacio', 'Dino', 'Flavio', 'Ciro', 'Fernando', 'Leonel']
funcXdepto = [1, 1, 4, 3, 0, 0, 1, 1, 1, 2, 0, 3, 4, 3, 2, 3, 2]

nome_depto = input() # Le o nome do departamento a pesquisar os funcionarios
nome_func = input() # Le o nome do funcionario a pesquisar o departamento
lista = meus_func(nome_depto, depto, func, funcXdepto)

for i in range(len(lista)):
    print(lista[i])

print(meu_depto(nome_func, depto, func, funcXdepto))
