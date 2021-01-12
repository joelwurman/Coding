# run this program first
import socket

s = socket.socket()  # initialise the socket
host = socket.gethostname()  # host addres which client will connect to
port = 8080
s.bind((host, port))
s.listen(1)  # number of incoming connections
print(host)
print('waiting for incoming connections . . . ')
conn, addr = s.accept()
print(addr, ' has connected to the server')

filename = input(str('please enter the name of the file: '))
file = open(filename, 'rb')
file_data = file.read(1024)

conn.send(file_data)
print('Data has been transmitted successfully')
