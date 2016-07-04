port = 7777
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)
print ("Listening on port: "+str(port))
while 1:
    conn, sock_addr = sock.accept()
    print "accepted connection from", sock_addr
    while 1:
        command = raw_input('shell> ')
            conn.send(command)
                data = conn.recv(8000)
                if not data: break
                print data,
    conn.close()