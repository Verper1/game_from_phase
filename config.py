from os import path

from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv

from utils import require_env

load_dotenv()
model_path = require_env("model_path")  # Path to folder with model
steam_path = path.join(  # Path to folder with Steam
    require_env("steam_path"),
    "steam.exe"
)
if not path.exists(steam_path):
    raise RuntimeError(f"steam.exe not found at {steam_path}")
trigger_phase = require_env("trigger_phase")  # Phase which will trigger opening chosen game or some program in Steam
game_id = require_env("game_id")  # Game id in Steam for correct launching through Steam services

model = Model(model_path)
rec = KaldiRecognizer(model, 16000)
state = {"triggered": False}
