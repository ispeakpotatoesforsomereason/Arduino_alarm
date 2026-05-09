# Piano Vault
## Description
This is python code that uses Abracadabra to recognize a spectrogram of your music and saves it in a .db file, then piano_recognizer.py uses the settings.py to recognize the piano with the help of the database, then sending a serial signal to whatever you want.

## Installation
On macOS and Windows (⚠️WARNING! This script has not been tested on Windows. You may need to modify the code yourself to make it work) run:
```bash
pip install click==8.3.3 future==1.0.0 iso8601==2.1.0 numpy==2.4.4 PyAudio==0.2.14 pydub==0.25.1 pyserial==3.5 PyYAML==6.0.3 scipy==1.17.1 simple-settings==1.2.0 tinytag==2.2.1 git+https://github.com/notexactlyawe/abracadabra
```

## How to use
To first make the model, make a songs folder with your music, then run:
```bash
song_recognizer initialise
python register.py
```

Then to start recognizing piano playing in real-time:
```bash
python piano_recognizer.py
```

Connect your Arduino to the serial port specified in piano_recognizer.py. When the script recognizes a song, it will send a serial command to trigger whatever you have connected (servo, LED, buzzer, etc).

## Technologies used
- **Abracadabra** - Audio fingerprinting library for song recognition
- **PyAudio** - Real-time audio capture from microphone
- **PySerial** - Serial communication with Arduino
- **NumPy/SciPy** - Audio signal processing
- **SQLite** - Database for storing audio fingerprints


## License
MIT License - do whatever you want with it
