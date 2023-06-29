import whisper

model = whisper.load_model("small")

audio = whisper.load_audio("audio_teste.m4a")
audio_iter = iter(audio)


#for i in range(10):

# load audio and pad/trim it to fit 30 seconds
#audio = whisper.load_audio("audio_teste.m4a")
audio = whisper.pad_or_trim(next(audio_iter))

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)