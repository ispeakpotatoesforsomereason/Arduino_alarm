import serial
import time
import threading
from abracadabra import recognise

try:
    arduino = serial.Serial('/dev/cu.usbmodem1201', 9600, timeout=1)
    time.sleep(2)
except:
    print("Errore: Arduino non connesso.")
    arduino = None

def monitor_seriale():
    while True:
        if arduino and arduino.in_waiting > 0:
            try:
                line = arduino.readline().decode('utf-8').rstrip()
                if line:
                    print(f"arduino dice che: {line}")
            except:
                pass
        time.sleep(0.1)

if arduino:
    thread_arduino = threading.Thread(target=monitor_seriale, daemon=True)
    thread_arduino.start()

while True:
    result = recognise.listen_to_song()

    if result:
        artist, album, title = result
        print(f"Riconoscimento: artist={artist}, album={album}, title={title}")
        
        if "Via Nazario Sauro" in title:
            print("yippe adesso puoi mangiare la tua arancia")
            
            if arduino:
                arduino.write('21ss4WSOSOskc2Spp+s#\n'.encode())
                arduino.flush()
            
            time.sleep(10) 
        else:
            print("non è la canzone giusta, riprova")
    else:
        print("sei sicuro che hai fatto tutti i commandi per avviare il database?")

    time.sleep(0.5)
