import os
from abracadabra import recognise

# 1. Path to your songs folder
SONGS_DIR = 'songs'

# 2. Look for both mp3 and m4a just to be safe
valid_extensions = ('.mp3', '.m4a', '.wav', '.MP3')
files = [f for f in os.listdir(SONGS_DIR) if f.endswith(valid_extensions)]

if not files:
    print(f"Error: No music files found in '{SONGS_DIR}'.")
    print(f"Folder contains: {os.listdir(SONGS_DIR)}")
else:
    print(f"Found {len(files)} piano files. Starting registration...")

    for filename in files:
        file_path = os.path.join(SONGS_DIR, filename)
        print(f"Fingerprinting: {filename}...")
        
        try:
            # The corrected function name
            recognise.register_song(file_path)
        except Exception as e:
            print(f"Failed to register {filename}: {e}")

    print("\nSuccess! Your piano vault is indexed.")
    print("Check your folder for 'abracadabra.db'.")