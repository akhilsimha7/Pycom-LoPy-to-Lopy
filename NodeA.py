from network import LoRa
import socket
import time

#Initiate LoRa Connection
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)


while True:
    print ('--------')
    if s.recv(64) == b'temperature_value':
        s.send("23")
        print("Data Sent: 23")
    else:
        print ("No Request Received")
    time.sleep(2)
