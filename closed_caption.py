'''import speech_recognition as sr
import whisper

def transcribe_audio_live():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    model = whisper.load_model("small")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # Ajuste do ruído ambiente
        print("Iniciando transcrição...")

        while True:
            audio = recognizer.listen(source)
            try:
                result = model.transcribe(audio, language='Portuguese')
                print(result["text"])
            except sr.UnknownValueError:
                print("Não foi possível reconhecer o áudio.")
            except sr.RequestError as e:
                print(f"Erro durante a transcrição: {e}")

transcribe_audio_live()
'''
import sounddevice as sd
import whisper

def transcribe_audio_live():
    model = whisper.load_model("base")

    def audio_callback(indata, frames, time, status):
        if status:
            print("Erro no dispositivo de áudio:", status)
        text = model.transcribe(indata)
        print(text)

    stream = sd.InputStream(callback=audio_callback, channels=1)

    with stream:
        print("Iniciando transcrição...")
        sd.sleep(int(10 * 1000))  # Captura de áudio por 10 segundos

# Realiza a transcrição em tempo real
transcribe_audio_live()