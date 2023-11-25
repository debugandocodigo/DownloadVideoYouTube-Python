import os
from pytube import YouTube

def baixar_video(url, caminho_destino='videos'):
    # Criar um objeto YouTube
    yt = YouTube(url)

    # Obter a melhor stream disponível (resolução mais alta)
    video_stream = yt.streams.get_highest_resolution()

    # Criar o diretório de destino se não existir
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    # Baixar o vídeo
    print(f'Baixando {yt.title}...')
    video_stream.download(caminho_destino)
    print('Download concluído!')


# Exemplo de uso
url_do_video = 'https://www.youtube.com/watch?v=stmNWeq8hc8'
baixar_video(url_do_video)
