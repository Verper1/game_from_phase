# Rock 'n' Stone activator - Voice-Activated Game Launcher

A voice-activated game launcher that uses speech recognition to launch Steam games. Simply say the configured trigger phrase, and the application will automatically launch your game via Steam.

## Features

- 🎤 Real-time voice recognition using Vosk speech recognition engine
- 🎮 Automatic Steam game launching via command line
- ⚙️ Configurable trigger phrase
- 🔧 Environment-based configuration

## Requirements

- Python >= 3.13
- Steam installed on your system
- Vosk speech recognition model (included: `vosk-model-small-en-us-0.15`)
- Microphone access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rock_n_stone
```

2. Install dependencies using `uv` (recommended) or `pip`:
```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory with the following variables:

```env
# Path to the folder containing the Vosk speech recognition model
model_path=./vosk-model-small-en-us-0.15

# Path to the Steam installation directory (without steam.exe)
steam_path=C:/Program Files (x86)/Steam

# The phrase that will trigger launching the game (case-insensitive)
trigger_phase=rock and stone

# Steam App ID of the game to launch
# You can find App IDs on https://steamdb.info/
game_id=548430
```

### Finding Steam App ID

To find the App ID of a game:
1. Visit [SteamDB](https://steamdb.info/)
2. Search for your game
3. The App ID is displayed on the game's page

### Finding Steam Installation Path

The default Steam installation paths are:
- **Windows**: `C:/Program Files (x86)/Steam` or `C:/Program Files/Steam`
- **Linux**: `~/.steam/steam` or `/usr/bin`
- **macOS**: `~/Library/Application Support/Steam/Steam.app/Contents/MacOS`

## Usage

1. Make sure your microphone is connected and working
2. Ensure Steam is installed and the path is correct in `.env`
3. Run the application:
```bash
python main.py
```

4. The application will start listening for your trigger phrase
5. Say the configured trigger phrase (e.g., "rock and stone")
6. The game will automatically launch via Steam

The application will exit after successfully detecting the trigger phrase and launching the game.

## Project Structure

```
rock_n_stone/
├── main.py              # Main entry point - initializes audio stream
├── handlers.py          # Audio callback handlers for voice recognition
├── config.py            # Configuration and environment variable loading
├── utils.py             # Utility functions for environment variables
├── config.py            # Configuration module
├── .env                 # Environment variables (create this file)
├── pyproject.toml       # Project dependencies and metadata
└── vosk-model-small-en-us-0.15/  # Vosk speech recognition model
```

## How It Works

1. **Audio Input**: The application uses `sounddevice` to capture audio from your microphone at 16kHz sample rate
2. **Speech Recognition**: Audio chunks are processed by the Vosk speech recognition engine
3. **Phrase Detection**: The recognized text is checked for the configured trigger phrase (case-insensitive)
4. **Game Launch**: When the phrase is detected, Steam is launched with the `-applaunch` parameter and the game's App ID
5. **Exit**: The application stops listening and exits after successful launch

## Troubleshooting

### Steam.exe not found
- Verify that the `steam_path` in your `.env` file points to the correct Steam installation directory
- Make sure `steam.exe` exists in that directory

### Microphone not working
- Check your system's microphone permissions
- Verify that your microphone is set as the default input device
- Test your microphone with other applications

### Speech recognition not working
- Ensure the `model_path` points to a valid Vosk model directory
- Check that the model matches your language (current model: English US)
- Speak clearly and ensure there's minimal background noise

### Game not launching
- Verify the `game_id` is correct for your game
- Make sure Steam is running or can be launched
- Check that you have the game installed in your Steam library

## Dependencies

- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- [sounddevice](https://github.com/spatialaudio/python-sounddevice) - Audio input/output
- [vosk](https://github.com/alphacep/vosk-api) - Offline speech recognition

## License

This project uses the Vosk speech recognition model, which is subject to its own license terms.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

# Rock 'n' Stone активатор - Голосовой Запуск Игр

Голосовой лаунчер игр, использующий распознавание речи для запуска игр через Steam. Просто произнесите настроенную фразу-триггер, и приложение автоматически запустит вашу игру через Steam.

## Возможности

- 🎤 Распознавание речи в реальном времени с использованием движка Vosk
- 🎮 Автоматический запуск игр Steam через командную строку
- ⚙️ Настраиваемая фраза-триггер
- 🔧 Конфигурация через переменные окружения

## Требования

- Python >= 3.13
- Установленный Steam на вашей системе
- Модель распознавания речи Vosk (включена: `vosk-model-small-en-us-0.15`)
- Доступ к микрофону

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd rock_n_stone
```

2. Установите зависимости используя `uv` (рекомендуется) или `pip`:
```bash
# Используя uv
uv sync

# Или используя pip
pip install -r requirements.txt
```

## Конфигурация

Создайте файл `.env` в корневой директории проекта со следующими переменными:

```env
# Путь к папке с моделью распознавания речи Vosk
model_path=./vosk-model-small-en-us-0.15

# Путь к директории установки Steam (без steam.exe)
steam_path=C:/Program Files (x86)/Steam

# Фраза, которая будет запускать игру (без учета регистра)
trigger_phase=rock and stone

# Steam App ID игры для запуска
# Вы можете найти App ID на https://steamdb.info/
game_id=548430
```

### Как найти Steam App ID

Чтобы найти App ID игры:
1. Посетите [SteamDB](https://steamdb.info/)
2. Найдите вашу игру
3. App ID отображается на странице игры

### Как найти путь установки Steam

Пути установки Steam по умолчанию:
- **Windows**: `C:/Program Files (x86)/Steam` или `C:/Program Files/Steam`
- **Linux**: `~/.steam/steam` или `/usr/bin`
- **macOS**: `~/Library/Application Support/Steam/Steam.app/Contents/MacOS`

## Использование

1. Убедитесь, что микрофон подключен и работает
2. Проверьте, что Steam установлен и путь указан правильно в `.env`
3. Запустите приложение:
```bash
python main.py
```

4. Приложение начнет прослушивать вашу фразу-триггер
5. Произнесите настроенную фразу-триггер (например, "rock and stone")
6. Игра автоматически запустится через Steam

Приложение завершит работу после успешного обнаружения фразы-триггера и запуска игры.

## Структура проекта

```
rock_n_stone/
├── main.py              # Точка входа - инициализирует аудио поток
├── handlers.py          # Обработчики аудио для распознавания речи
├── config.py            # Конфигурация и загрузка переменных окружения
├── utils.py             # Утилиты для работы с переменными окружения
├── .env                 # Переменные окружения (создайте этот файл)
├── pyproject.toml       # Зависимости проекта и метаданные
└── vosk-model-small-en-us-0.15/  # Модель распознавания речи Vosk
```

## Как это работает

1. **Аудио вход**: Приложение использует `sounddevice` для захвата аудио с микрофона с частотой дискретизации 16 кГц
2. **Распознавание речи**: Аудио фрагменты обрабатываются движком распознавания речи Vosk
3. **Обнаружение фразы**: Распознанный текст проверяется на наличие настроенной фразы-триггера (без учета регистра)
4. **Запуск игры**: При обнаружении фразы Steam запускается с параметром `-applaunch` и App ID игры
5. **Выход**: Приложение прекращает прослушивание и завершает работу после успешного запуска

## Решение проблем

### Steam.exe не найден
- Проверьте, что `steam_path` в вашем файле `.env` указывает на правильную директорию установки Steam
- Убедитесь, что `steam.exe` существует в этой директории

### Микрофон не работает
- Проверьте разрешения микрофона в системе
- Убедитесь, что микрофон установлен как устройство ввода по умолчанию
- Протестируйте микрофон в других приложениях

### Распознавание речи не работает
- Убедитесь, что `model_path` указывает на валидную директорию модели Vosk
- Проверьте, что модель соответствует вашему языку (текущая модель: английский US)
- Говорите четко и убедитесь, что фоновый шум минимален

### Игра не запускается
- Проверьте, что `game_id` правильный для вашей игры
- Убедитесь, что Steam запущен или может быть запущен
- Проверьте, что игра установлена в вашей библиотеке Steam

## Зависимости

- [python-dotenv](https://github.com/theskumar/python-dotenv) - Управление переменными окружения
- [sounddevice](https://github.com/spatialaudio/python-sounddevice) - Аудио ввод/вывод
- [vosk](https://github.com/alphacep/vosk-api) - Офлайн распознавание речи

## Лицензия

Этот проект использует модель распознавания речи Vosk, которая подчиняется своим условиям лицензирования.

## Вклад в проект

Вклад приветствуется! Пожалуйста, не стесняйтесь отправлять Pull Request.

