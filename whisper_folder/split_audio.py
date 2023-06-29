import whisper
from pydub import AudioSegment
import numpy as np
import os


def segmentacao_audio(audio_file=str, output_folder=str, duracao_segmento_min=int):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    elif len(os.listdir(output_folder))>0:
        print("Já existem audios nesta pasta!")
        return 0, output_folder
    
    audio = AudioSegment.from_mp3(audio_file)
    duration_per_segment = 60000*duracao_segmento_min  # convertendo para milisegundos
    segments = [audio[i:i+duration_per_segment] for i in range(0, len(audio), duration_per_segment)]

    for i, segment in enumerate(segments):
        segment.export(output_folder + f"segmento_{i}.mp3", format="mp3")

    print("Segmentação concluída.")
    return len(segment), output_folder


