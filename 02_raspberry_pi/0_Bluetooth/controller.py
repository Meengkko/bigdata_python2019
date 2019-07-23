from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
#client_socket.connect(("20:15:01:30:59:85", 1))
client_socket.connect(("00:18:E5:04:15:57", 1))
while True:
    msg = raw_input("Send : ")
    if msg[0] == 'q':
        break
    print( msg )
    client_socket.send(msg)

print("Finished")
client_socket.close()
