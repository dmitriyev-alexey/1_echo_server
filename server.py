import socket

sock = socket.socket()
print('Binding server...')
sock.bind(('', 9090))
print('Opening server for connections...')
sock.listen(0)
print('Server is ready to accept connections')
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	print('Waiting for data from clients...')
	data = conn.recv(1024)
	if not data:
		print('Closing connection...')
		break
	msg += data.decode()
	print('Echoing data...')
	conn.send(data)

print('msg: ')
print(msg)
print('Closing server...')
conn.close()
