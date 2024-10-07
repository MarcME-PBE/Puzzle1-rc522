import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:
    def __init__(self):
        # Configurar el lector RC522
        self.reader = SimpleMFRC522()

    def read_uid(self):
        try:
            # Llegir la targeta
            print("Aproximi la targeta al lector...")
            id, text = self.reader.read()
            
            # Convertir el UID a hexadecimal
            uid_hex = hex(id)[2:].upper()  # treure el '0x' i convertir a majuscules
            uid_hex = uid_hex.zfill(8)[:8] #omplir amb 0 si s'escau i truncar als 8 digits
            return uid_hex
        finally:
            GPIO.cleanup() #neteja la configuracio dels pins GPIO despres d'executar el codi

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    if uid:
        print(f"UID de la targeta: {uid}")
    else:
        print("No es pot llegir el UID.")
        
        
        
        
