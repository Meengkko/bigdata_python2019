from bluetooth import *
import RPi.GPIO as GPIO
import time

# Select GPIO mode
GPIO.setmode(GPIO.BCM)
buzzer = 18
GPIO.setup(buzzer, GPIO.OUT)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# import Adafruit_DHT
# Create the client socket
client_socket1=BluetoothSocket( RFCOMM )
client_socket2=BluetoothSocket( RFCOMM )
#client_socket.connect(("98:D3:71:FD:35:38", 1))
client_socket1.connect(("98:D3:71:FD:35:38", 1))
#client_socket2.connect(("20:15:12:15:40:68", 1))

menu = """  **select menu**
====================
1. Security mode
2. Temperature check
3. Morning call
====================
"""

while True:
    print(menu)
    msg = raw_input("Send : ")
    if msg[0] == 'q':
        break
    # print( msg )

    if msg == '1':
        try:
            while True:
                pulse_start = 0
                pulse_end = 0
                GPIO.output(TRIG, False)
                print("Waiting For Sensor To Settle")
                time.sleep(1)

                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO) == 0:
                    pulse_start = time.time()

                while GPIO.input(ECHO) == 1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                distance = pulse_duration * 17150

                distance = (170 - distance)*0.9
                print(distance)
                if distance < 30:
                    print("Warning!")
                    GPIO.output(buzzer, GPIO.HIGH)
                    time.sleep(0.5)  # Delay in seconds
                    GPIO.output(buzzer, GPIO.LOW)
        except KeyboardInterrupt:
            print("Cleaning up!")
            GPIO.cleanup()
    elif msg == '2':
        client_socket1.send(msg)
    # elif msg == '3':
    #     client_socket2.send(msg)

    else:
        print("Select right number!")

print("Finished")
client_socket.close()
