import serial
import time
from abracadabra import recognise

try:
    arduino = serial.Serial('/dev/cu.usbmodem1201', 9600, timeout=1)
    time.sleep(2)
except:
    arduino = None

while True:
    print("ok suona il tuo piano grazie")
    result = recognise.listen_to_song()

    if result:
        result_str = str(result)
        
        if "song" in result_str:
            print("yippe adesso puoi mangiare la tua arancia")
            
            if arduino:
                arduino.write('21ss4WSOSOskc2Spp+s#\n'.encode())
                arduino.flush()
            break
            
            time.sleep(10) 
    
    time.sleep(0.5)
