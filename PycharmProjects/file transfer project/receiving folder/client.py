import socket

s = socket.socket()
host = input(str('Please enter the host address of sender: '))
port = 8080
s.connect((host, port))
print('connected...')

filename = input(str('enter a filename for the incoming file: '))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)

file.close()
print('file received successfully')
