# import os 
# for meta_file in os.listdir('dados/data/meta-data'):
#     print(meta_file)

#extrair a extensao .txt
def estract_entidy_name(filename):
    return filename.split('.')[0]

print(estract_entidy_name('Licitacao.txt'))

'''Nesse código, obtemos o nome da entidade por meio do nome do arquivo texto associado. Por exemplo, Licitacao.txt transformada em Licitacao. Os nome serçao os chaves do dicionario e os valores serão um lista de tuplas que descrevem os compos da entidade'''

#Adicionando e removendo elemtentos em uma lista
def 