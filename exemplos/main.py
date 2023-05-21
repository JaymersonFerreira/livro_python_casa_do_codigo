'''O que temos afora é um script que faz o download de um arquivo ZIP. De acordo com a resposta do servidor, ele opta por uma determinada estatégia para download do arquivo'''


import io
import sys
import urllib.request as request


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('Content_Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    
    response.close()
    out_file.close()
    print('Finished')
if __name__ == "__main__":
    main()
