"""
Audio callback handlers for voice recognition.

This module contains the callback function that processes audio input
and triggers game launch when the configured phrase is detected.
"""

from json import loads
from subprocess import Popen

from sounddevice import CallbackStop

from config import rec, trigger_phase, steam_path, game_id, state


def callback(indata, frames, time, status):
    """
    Audio input callback function for processing voice recognition.

    This function is called continuously by the audio input stream.
    It processes audio chunks, performs speech recognition, and launches
    the game when the trigger phrase is detected.

    Args:
        indata: Input audio data as a numpy array
        frames: Number of frames in the input buffer
        time: Current time information (CFFI structure)
        status: Status flags indicating any errors or warnings

    Raises:
        CallbackStop: Raised when the trigger phrase is detected to stop
                     the audio stream gracefully.
    """
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
