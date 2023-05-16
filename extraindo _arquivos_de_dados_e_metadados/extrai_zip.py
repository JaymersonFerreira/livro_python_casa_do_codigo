#coding: utf-8

import os
import zipfile
import sys

def main(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivo extraído")
if __name__ == "__main__":
    main(sys.argv[1])

'''Inicialmente, vemos a declaração do endcoding- é uma voa prática sempre ter e, se você usa textp com acentos na sua documentação, é obrigatário definir quase sempre utf-8
Importamos apenpas módulos: sys, os, e zipfile. com o módulo sys, pegamos o argumentos da linha de comando - nesse caso, o caminho do arquivo baixado - e também podemos encerrar a execução do nosso programa com sys.exit(return_code). Usamos o código de retorno -1 porque o arquivo passado não existe. 
Para testar a existência do arquivo, usamos os.path.exists(path). Essa função retorna True caso o caminho passado exista, e False caso não.
Existindo, vamos usar módulo zipfile para criar um objeto da classe ZipFile que possui o método extractall. Este extrai todo o conteúdo do arquivo zip para o diretório de trabalho.
Com poucas linhas, e alguns conceitos e coonstrutos iniciais, criamos dois programas: um deles faz o download de um arquivo zip de um servidor HTTP e o outro extrai o conteúdo do arquivo para o diretório corrente, para que os próximos programas possam usá-lo.''' 
