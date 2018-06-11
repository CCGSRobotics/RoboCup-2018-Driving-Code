print("connect setup")
import socket

HOST, PORT = "192.168.100.1", 9999 #"169.254.44.240", 9999 #
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("trying to establish a connection")
try:
    sock.connect((HOST, PORT))
    print("connect ready")
except:
    print("CONNECTION FAILED.")
    print("have you run the code on the raspberry pi?")
    print("P.S. dont break the pi please")
    #raise RuntimeEror

print(sock)
