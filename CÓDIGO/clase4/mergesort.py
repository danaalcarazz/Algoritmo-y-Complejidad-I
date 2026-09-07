def merge_sort(arr):
    #si el arreglo tiene 0 o 1 elemento ya se encuentra ordenado
    if len(arr) <= 1:
        return arr

    #se obtiene la posición del medio y se divide el arreglo en dos mitades
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]

    #se ordena recursivamente las mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    #se combinan las dos mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    #se comparan los elementos de ambas mitades
    while i < len(izquierda) and j < len(derecha):

        #si el elemento de la izquierda es menor o igual se agrega al resultado
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1

        #sino, se agrega el elemento de la derecha
        else:
            resultado.append(derecha[j])
            j += 1

    #se agregan los elementos q quedan de la izquierda
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    #y de la derecha
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    #se devuelve el arreglo combinado y ordenado
    return resultado


#arreglo de ejemplo
numeros = [8, 3, 5, 4, 7, 6, 1, 2]

#se aplica el algoritmo mergesort
resultado = merge_sort(numeros)

print("arreglo original:", numeros)
print("arreglo ordenado:", resultado)