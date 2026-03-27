import socket
import ssl

HOST = "127.0.0.1"
PORT = 5000

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
secure_sock = context.wrap_socket(sock,server_hostname=HOST)

secure_sock.connect((HOST,PORT))

print("Connected to Secure Diagnostic Server")

while True:

    print("\n1. Ping Host")
    print("2. Port Scan")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        host = input("Enter host: ")
        cmd = f"PING {host}"

    elif choice == "2":
        host = input("Enter host: ")
        cmd = f"PORTSCAN {host}"

    elif choice == "3":
        break

    else:
        print("Invalid choice")
        continue

    secure_sock.send(cmd.encode())

    result = secure_sock.recv(8192).decode()

    print("\nResult:\n")
    print(result)

secure_sock.close()