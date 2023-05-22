#descobri que entidade compõe essa base de dados

# import os

# def main():
#     meta = {}
#     for meta_data_file in os.listdir("data/meta-data"):
#         table_name = meta_data_file.split('.')[0]
#         print(table_name)

# if __name__ == "__main__":
#     main()

#com ele, podemos verificar se o seu nome esta no dicionario, a cda atributo para um entidade, Se estiver, segnifica que ess a entidade, cujos atributos de identificador é o valor do dicionario de identificador ara o nome da entidade. 
import os

def estract_name(name):
    return name.split(".")[0]

def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read.split("\n")
    _file.close
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
    return metadata

def main():
    #dicionário nome entidade -> atributos
    meta = {}

    # dicionário identificador -> nome entidade
    keys = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attribuites[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print("Entiade' {} -> {}".format(key, col[0]))
if __name__ == "__main__":
    main()

