import socket
import time

server = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 8080
server.bind((host, port))
print("the server is run succesfully")
print(f"the host name is {host}")
print(f"the ip address is : {ip}")
server.listen(1)
print("waiting for client")
connection , address = server.accept()
client_username = connection.recv(1024)
client_username = client_username.decode()
print(f"[{client_username}] has connected to the server.")
filename = input("what is your file name =>")
file = open(filename , "rb")
file_data = file.read(999999999)
connection.send(file_data)
print("the file sended sucessfully")
