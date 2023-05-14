'''O response representa uma resposta do servidor, sendo dela que leremos os bytes dos arquivo de download. Como sabemos o tamanho, conseguimos saber quantas operações de response.read() vamos ter que realizar para ler tudo.  Para cada leitura, realizamos um output.write() dos bytes lidos em um arquivo.'''


BUFF_SIZE = 1024
def download_lenght(response, output, lenght):
    times = lenght / BUFF_SIZE
    if lenght %  BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/ lenght)*100))



'''ás vezes o servidor não reponde o tamanho em bytes do arquivo que queremos. Nesses casos reazamos leitura até que alguma não retorne nenhum byte. Basicamente, Trocamos o loop com for com range() po um loop while, visto que não conseguimos saber de antemão quando terminar. Quando a leitura não retorna nada, o comando break interrope o while'''

def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
        output.write(data)
        print('Download {bytes}'.format(bytes=total_download))