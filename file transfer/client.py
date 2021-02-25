import socket
server = socket.socket()
input_name = input("Enter the host/ip name =>")
if input_name == "mohsen" :
    host = "192.168.1.36"
else :
    host = input_name
port = 8080
server.connect((host,port))
print("You connected to the server sucssefully")
username = input("Enter your username => ")
username = username.encode()
server.send(username)
###########################
file_name = input("enter you file name =>")
file = open(file_name , "wb")
file_data = server.recv(999999999)
file.write(file_data)
file.close()
print("file as recived succesfully")
