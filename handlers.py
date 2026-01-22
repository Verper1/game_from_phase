from json import loads
from subprocess import Popen

from sounddevice import CallbackStop

from config import rec, trigger_phase, steam_path, game_id, state


def callback(indata, frames, time, status):
    if status:
        print(status)
    if rec.AcceptWaveform(bytes(indata)):
        result = loads(rec.Result())
        text = result.get("text", "")

        if trigger_phase.lower() in text:
            print(f"Phase detected: '{text}'. Lunching the game!")
            Popen([
                steam_path,
                "-applaunch",
                game_id
            ])

            state["triggered"] = True
            raise CallbackStop
