from network import LoRa
import socket

#Initiate LoRa Connection
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0

while True:
    print ('--------')
    if i==0:
        s.send('temperature_value')     #Request for Data at an interval
        print('Request Sent:temperature_value')
        data = s.recv(256)    # Receive Data from nearby LoRA Device
        print(data)


    time.sleep(2)
