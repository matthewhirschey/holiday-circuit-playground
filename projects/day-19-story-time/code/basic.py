# Basic audio story player for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

# Main loop
while True:
    if cp.button_a:
        # Play first part of story
        with open('story1.wav', 'rb') as wavfile:
            wav = audioio.WaveFile(wavfile)
            audio.play(wav)
            while audio.playing:
                # Use switch for volume control
                if cp.switch:
                    audio.volume = 0.3
                else:
                    audio.volume = 1.0
    
    elif cp.button_b:
        # Play second part of story
        with open('story2.wav', 'rb') as wavfile:
            wav = audioio.WaveFile(wavfile)
            audio.play(wav)
            while audio.playing:
                # Use switch for volume control
                if cp.switch:
                    audio.volume = 0.3
                else:
                    audio.volume = 1.0
    
    elif cp.button_a and cp.button_b:
        # Play special sound effect
        with open('effect.wav', 'rb') as wavfile:
            wav = audioio.WaveFile(wavfile)
            audio.play(wav)
            while audio.playing:
                pass
    
    time.sleep(0.1)