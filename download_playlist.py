import os
import sys
from pytube import Playlist
from pytube import YouTube
from moviepy.editor import VideoFileClip

def baixar_playlist_mp3(playlist_url):
    try:
        # Criar um objeto Playlist
        playlist = Playlist(playlist_url)

        # Criar o diretório de saída se não existir
        output_path = 'downloads'
        os.makedirs(output_path, exist_ok=True)

        # Iterar sobre cada vídeo na playlist
        for video in playlist.videos:
            print(f"Baixando: {video.title}")

            # Baixar o vídeo usando pytube
            video_stream = video.streams.filter(only_audio=True).first()
            video_stream.download(output_path)

            # Obter o nome original do arquivo baixado
            original_filename = os.path.join(output_path, video_stream.default_filename)

            # Formatar o nome do arquivo MP3
            mp3_filename = os.path.join(output_path, f"{video.title}.mp3")

            # Renomear o arquivo para ter uma extensão .mp3
            os.rename(original_filename, mp3_filename)

        print("Download da playlist concluído!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Verificar se o URL da playlist foi fornecido como argumento de linha de comando
    if len(sys.argv) < 2:
        print("Por favor, forneça o URL da playlist do YouTube como argumento.")
    else:
        playlist_url = sys.argv[1]
        baixar_playlist_mp3(playlist_url)
