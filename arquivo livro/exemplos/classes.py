# class DataTable:
#     pass

# table = DataTable()
# print(type(table))
'''<class '__main__.DataTable'>'''

# table.name = 'Alerta'
# table.columns = ['IdProjeto', 'DescProjeto']
# table.data = []

## Definições de duas classes
# class DataTable:
#     def __init__(self,name):
#         self._name = name
#         self._columns = []
#         self._data = []

# class Column:
#     def __init__(self, name, kind, description):
#         self._name = name
#         self._kind = kind
#         self._description = description


##Encapsulamento sem private ou algo semelhante 
# class DataTable:
#     def __init__(self, name):
#         self._name = name
#         self._columns = []
#         self._data = []
#     def getData(self):
#         return self._data

# table = DataTable("TableTeste")
# print(table.getData())

##Decorator
#A vantagem de usar o decorator @property é que poderímaos acessar o atributo usuando epena  data  como se DataTable tivesse um atributo com esse nome
# class DataTable:
#     def __init__(self, name):
#         self._name = name
#         self._columns = []
#         self._data = []
#     @property
#     def data(self):
#         return self._data
    

# table = DataTable('TabelaTeste')
# print(table.data)


class DataTable:
    """
    Representa um Tabela de Dados.

    Essa classe representa uma tabela de dados do portal da trasparência.
    Deve ser capaz de validar linhas inseridas de acordo com as colunas que
    possui. As linhas inseridas ficam registradas dentro dela.

    Attributes:
        Name: Nome da tabela
        columns: [Lista de colunas]
        data: [Lista de dasdos]
    """

    def __init__(self,name):
        """Construtor
                Args:
                    name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self._data = []

class Column:
    """
    Representa uma coluna de um DataTabela

    Esssa Classe contèm as informações de um coluna e deve calidar um dado
    de acordo com o tipo de dado configurado do construtor

    Attributes:
        name: Nome da Coluna
        kung: Tipo do Dado (varchar, bigint, numeric)
        description: Descrição de coluna
    """

    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description

print(DataTable.__doc__)
print(Column.__doc__)