from pytube import YouTube
from moviepy.editor import AudioFileClip

def downlaod_video_youtube(link=str, caminho_audio=str):
    # URL do vídeo do YouTube
    url = link

    # Baixe o vídeo
    video = YouTube(url).streams.first().download()
    return video

def video_to_audio(video, caminho_audio=str):
    # Extraia o áudio do vídeo
    audio = AudioFileClip(video)
    audio.write_audiofile(caminho_audio)
    return caminho_audio