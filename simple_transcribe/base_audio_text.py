import whisper #https://github.com/openai/whisper

model = whisper.load_model("base")
result = model.transcribe("audio_iot.mp3")
print(result["text"])

with open('transcricao_iot.txt', 'a') as f:
    f.write(result["text"] + '\n')