import whisper
import glob
from split_audio import segmentacao_audio

results = []

folder_audios_splits = "audio_splits/"
audio_file = "audio_teste.mp3"
qtd_audios, folder_audios_splits = segmentacao_audio(audio_file, folder_audios_splits, 5)


audios =  glob.glob(folder_audios_splits + "*.mp3")
model = whisper.load_model("small")
for audio in sorted(audios):
    print(audio)
    result = model.transcribe(audio, language='Portuguese')
    results.append(result["text"])
    print(result["text"])
#result = model.transcribe("audio_teste.mp3", language='Portuguese')
#print(results)

