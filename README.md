# Secure Client-Server Communication System

This project is a Computer Networks mini project that demonstrates secure communication between a client and a server using Python. It implements a secure network diagnostic tool where clients can perform ping operations and port scanning on remote hosts through a server, all secured with SSL/TLS encryption.

## Features

- **Secure Communication**: Uses SSL/TLS encryption for all client-server interactions
- **Network Diagnostics**: Supports ping and port scanning operations
- **Multi-threaded Server**: Handles multiple client connections concurrently
- **Error Handling**: Robust error handling for connection and command issues
- **Modular Design**: Clean separation between client and server components

## Technologies Used

- **Python**: Core programming language
- **Socket Programming**: For network communication
- **SSL/TLS**: For secure data transmission
- **Threading**: For concurrent client handling
- **Subprocess**: For executing system commands (ping, port scanning)

## Requirements

- Python 3.6 or higher
- OpenSSL (for SSL certificate generation)

## Installation & Setup

1. **Clone or download the project**:
   ```bash
   git clone <repository-url>
   cd "CN - Mini Project"
   ```

2. **Generate SSL certificates** (if not present):
   ```bash
   # Generate private key
   openssl genrsa -out key.pem 2048

   # Generate certificate
   openssl req -new -x509 -key key.pem -out cert.pem -days 365
   ```

## Project Structure

```
CN - Mini Project/
│
├── client.py          # Client application for sending diagnostic commands
├── server.py          # Server application for processing commands
├── cert.pem           # SSL certificate file
├── key.pem            # SSL private key file
└── README.md          # Project documentation
```

## Usage

### Starting the Server

Run the server first:

```bash
python server.py
```

The server will start listening on `0.0.0.0:5000` with SSL/TLS encryption enabled.

### Running the Client

In a separate terminal, run the client:

```bash
python client.py
```

The client will connect to the server and present a menu with the following options:

1. **Ping Host**: Enter a hostname or IP address to ping
2. **Port Scan**: Enter a hostname or IP address to scan ports (20-199)
3. **Exit**: Close the connection and exit

### Example Interaction

```
Connected to Secure Diagnostic Server

1. Ping Host
2. Port Scan
3. Exit

Select option: 1
Enter host: google.com

Result:
Pinging google.com [142.250.190.78] with 32 bytes of data:
Reply from 142.250.190.78: bytes=32 time=14ms TTL=117
...
```

## Security Notes

- The client uses `ssl.CERT_NONE` for simplicity (accepts any certificate)
- In production, proper certificate validation should be implemented
- The server requires valid SSL certificates (`cert.pem` and `key.pem`)

## Limitations

- Port scanning is limited to ports 20-199 for performance
- Ping functionality depends on system ping command availability
- No authentication mechanism implemented

## How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ishiii16/CN-Mini-Project.git
   cd CN-Mini-Project
   ```

2. **Run the Server**

   ```bash
   python server.py
   ```

3. **Run the Client** (in a separate terminal)

   ```bash
   python client.py
   ```

## Working

The server starts and listens on a specified port.
The client connects to the server.
A secure SSL/TLS connection is established.
The client sends messages and the server responds securely.

## Learning Outcomes

Understanding of socket programming
Implementation of secure communication using SSL/TLS
Knowledge of client-server architecture
Experience in handling network-related errors

## Notes

Ensure both client and server use the same port number.
SSL certificates must be properly configured.
Avoid using restricted ports unless necessary.

