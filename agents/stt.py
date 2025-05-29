import numpy as np
import sounddevice as sd
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="en", task="transcribe")

def record_audio(duration=10, sample_rate=16000):
    print("Recording audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    audio_array = np.squeeze(audio)
    input_features = processor(audio_array, sampling_rate=16000, return_tensors="pt").input_features 

    # generate token ids
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription

if __name__ == "__main__":
    result = record_audio()
    print("Transcribed:", result)