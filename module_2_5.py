def get_matrix(n, m, value): #Объявление функции get_matrix и запись в ней параметров n, m и value.
    matrix = []              #пустой список matrix внутри функции get_matrix.
    for i in range(n):       #первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([])    #добавление пустого списка в список matrix.
        for j in range(m):   #второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value) #добавленние ранее добавленного пустого списка значениями value.
    return matrix            #возврат значения переменной matrix.
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

