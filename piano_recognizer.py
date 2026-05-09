import os
import serial
import time
from abracadabra import recognise

try:
    arduino = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=1)
    time.sleep(2)
except:
    print("serial port not found, your problem")
    arduino = None

print("listening to your beautiful piano")

while True:
    
    result = recognise.listen_to_song()

    if result:
        _, song_name, confidence = result
        print(f"Detected: {song_name} (Confidence: {confidence})")
        
        
        if "Via Nazario Sauro" in song_name and confidence > 50:
            print("unlocked, have fun eating an orange")
            if arduino:
                arduino.write('21ss4WSOSOskc2Spp+s#'.encode())
            
            
            time.sleep(10) 
    else:
        print("not the song, keep playing...")
    
    time.sleep(0.5)