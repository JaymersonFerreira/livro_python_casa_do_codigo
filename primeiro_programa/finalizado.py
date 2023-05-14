'''Utilizamos a função da biblioteca padrão urllib.request.urlopen, a classe io,FileIO para escrevemos o arquivo binário de saída, um comando if e alguma chamada de função. as funcões contêm um while, um for'''

#Programa que faz download dos arquivos de dados que usaremos daqui em diante

#coding: utf-8

import io
import sys 
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))


def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
        out_file.write(data)
        print('Download {bytes}'.format(bytes=total_download))


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('Content-Lengend')
    if content_lenght:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    response.close()
    out_file.close()
    print("Finished")


if __name__ == "__main__":
    main()