import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522() 

try:
    print("Acosta la teva targeta d'identificacio...") 
    id, text = reader.read() #llegeix la tarja i retorna el UID
    print(f"UID: {id}") 
finally:
    GPIO.cleanup() #neteja la configuracio dels pins GPIO despres d'executar el codi
