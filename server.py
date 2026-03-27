import socket
import ssl
import threading
import subprocess

HOST = "0.0.0.0"
PORT = 5000

def handle_client(conn, addr):
    print("Client connected:", addr)

    while True:
        try:
            data = conn.recv(1024).decode()

            if not data:
                break

            if data.startswith("PING"):
                host = data.split()[1]
                result = subprocess.getoutput(f"ping {host}")

            elif data.startswith("PORTSCAN"):
                host = data.split()[1]
                result = ""

                for port in range(20,200):                                  #for port in range(20,1025): this usually takes time because its scanning 1000 ports 
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.settimeout(0.5)

                    if s.connect_ex((host,port)) == 0:
                        result += f"Port {port} open\n"

                    s.close()

                if result == "":
                    result = "No open ports found"

            else:
                result = "Invalid command"

            conn.send(result.encode())

        except:
            break

    conn.close()
    print("Client disconnected")


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem",keyfile="key.pem")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)

secure_server = context.wrap_socket(server,server_side=True)

print("Secure Network Diagnostic Server Running...")

while True:
    conn,addr = secure_server.accept()
    thread = threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()