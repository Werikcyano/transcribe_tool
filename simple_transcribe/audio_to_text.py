import whisper #https://github.com/openai/whisper
import glob
import os
from download_video_to_audio import downlaod_video_youtube, video_to_audio

from split_audio import segmentacao_audio

video = downlaod_video_youtube(link="https://youtu.be/TqI8y1OYGsY?si=vx0W6rD-O0pk1qSm",
caminho_audio="audio_iot.mp3")

caminho_final_audio = video_to_audio(video, caminho_audio="audio_iot.mp3")

results = []

folder_audios_splits = "audio_splits/"
audio_file = "audio_iot.mp3"
qtd_audios, folder_audios_splits = segmentacao_audio(audio_file, folder_audios_splits, 5)

diretorio_atual = os.getcwd()
print(diretorio_atual)
audios =  glob.glob(diretorio_atual+"/" + folder_audios_splits + "*.mp3")
model = whisper.load_model("small")
for audio in sorted(audios):
    print(audio)
    result = model.transcribe(audio, language='Portuguese')
    results.append(result["text"])
    print(result["text"])

# Salvar a transcrição em um arquivo .txt
with open('transcricao.txt', 'a') as f:
    f.write(result["text"] + '\n')