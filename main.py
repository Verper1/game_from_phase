from time import sleep
from sounddevice import RawInputStream
from config import trigger_phase, state
from handlers import callback
from sys import exit

if __name__ == "__main__":
    print(f"I\'m listening for phase: '{trigger_phase}'")

    # Запуск потока прослушивания
    with RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while not state["triggered"]:
            sleep(0.1)

    exit(0)
