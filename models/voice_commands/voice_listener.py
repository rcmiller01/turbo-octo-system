import subprocess

class VoiceListener:
    def __init__(self, model_path='models/voice_commands/whisper.tflite'):
        self.model_path = model_path
        # In practice, load model or setup Vosk/Whisper API call here

    def transcribe_audio(self, audio_file_path: str):
        # Stub: simulate offline STT result for a given audio clip
        return "start workout"  # Replace with real STT inference logic
