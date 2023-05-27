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
class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []
    def getData(self):
        return self._data

table = DataTable("TableTeste")
print(table.getData())
