import socket

BYTES_TO_READ=4096

def get(host, port):
    request = b"GET / HTTP/1.1\r\nHost: " + host.encode('utf-8') + b"\n\n"
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    response = s.recv(BYTES_TO_READ)
    while response:
        print(response)
        response = s.recv(BYTES_TO_READ)

    s.close()

# get("www.google.com", 80)
get("127.0.0.1", 8081)