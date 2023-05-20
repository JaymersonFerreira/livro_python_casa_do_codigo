# import os 
# for meta_file in os.listdir('dados/data/meta-data'):
#     print(meta_file)

#extrair a extensao .txt
# def estract_entidy_name(filename):
#     return filename.split('.')[0]

# print(estract_entidy_name('Licitacao.txt'))

# '''Nesse código, obtemos o nome da entidade por meio do nome do arquivo texto associado. Por exemplo, Licitacao.txt transformada em Licitacao. Os nome serçao os chaves do dicionario e os valores serão um lista de tuplas que descrevem os compos da entidade'''

# #Adicionando e removendo elementos em uma lista
# def read_meta_data(path):
#     data =open(path, "rt")
#     meta_data = []
#     for line in data:
#         line_data = line.split('\t')
#         meta_data.append((line_data[0],
#                           line_data[1],
#                           line_data[2]))
#     data.close()
#     return meta_data
# read_meta_data('data/meta-data/Instituicao.txt')


#Outros operações de listas são:
# reverse() - incerter a ordem dos elementos
# sort() - ordenar por valor
# extend(lista) - concatenar com outra lista
# index(elemento) - descobrir a posição de um elemento
# clear() - apaga todos os elementos da lista.

lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)
'''[1, 2, 3, 4, 5, 6]'''
lista.insert(0, -1)
print(lista)
'''[-1, 1, 2, 3, 4, 5, 6]'''
lista.remove(6)
print(lista)
'''[-1, 1, 2, 3, 4, 5]'''
lista.pop(0)
print(lista)
'''[1, 2, 3, 4, 5]'''
lista.reverse()
print(lista)
'''[5, 4, 3, 2, 1]'''
lista.sort()
print(lista)
'''[1, 2, 3, 4, 5]'''
print(lista.index(5))
'''4'''
lista_b = [6, 7, 8]
lista.extend(lista_b)
print(lista)
'''[1, 2, 3, 4, 5, 6, 7, 8]'''
lista.clear()
print(lista)
'''[]'''



