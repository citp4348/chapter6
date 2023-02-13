import socket
import ssl

server_key = 'server.key'
client_cert = 'client.crt'
server_cert = 'server.crt'
port = 8080

hostname = '127.0.0.1'
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_cert)
context.verify_mode = ssl.CERT_REQUIRED
context.options |= ssl.OP_SINGLE_ECDH_USE
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(('',port))
	sock.listen(1)
	with context.wrap_socket(sock,server_side=True) as ssock:
		conn,addr = ssock.accept()
		print(addr)
		message = conn.recv(1024).decode()
		capitalizedMessage = message.upper()
		conn.send(capitalizedMessage.encode())












