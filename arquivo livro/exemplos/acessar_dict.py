meu_dict = {'Empreendimento': [('IdEmpreendimento', 'bigint', '...')], 'licitacao': [('IdLicitacao', 'bigint', '...')]}

##chaves e valores
# for (name, attributes) in meu_dict.items():
    # print("nome {} com atributos(s)".format(name, len(attributes)))
'''nome Empreendimento com atributos(s)
nome licitacao com atributos(s)'''

##valores
# for attributes in meu_dict.values():
#     print(attributes)
'''[('IdEmpreendimento', 'bigint', '...')]
[('IdLicitacao', 'bigint', '...')]'''

for name in meu_dict.keys():
    print(name)
'''Empreendimento
licitacao'''
