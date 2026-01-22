"""
Configuration module for voice-activated game launcher.

This module loads environment variables, initializes the Vosk speech recognition
model, and sets up configuration for Steam game launching.

Environment Variables:
    model_path: Path to the folder containing the Vosk speech recognition model
    steam_path: Path to the Steam installation directory
    trigger_phase: The phrase that will trigger launching the game
    game_id: The Steam App ID of the game to launch

Raises:
    RuntimeError: If required environment variables are missing or if steam.exe
                 is not found at the specified path.
"""

from os import path

from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv

from utils import require_env

load_dotenv()

# Path to folder containing the Vosk speech recognition model
model_path = require_env("model_path")

# Path to Steam executable
steam_path = path.join(
    require_env("steam_path"),
    "steam.exe"
)
if not path.exists(steam_path):
    raise RuntimeError(f"steam.exe not found at {steam_path}")

# Phrase which will trigger opening the chosen game or program in Steam
trigger_phase = require_env("trigger_phase")

# Game ID in Steam for correct launching through Steam services
game_id = require_env("game_id")

# Initialize Vosk speech recognition model
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

# Global state to track if trigger phrase has been detected
state = {"triggered": False}
