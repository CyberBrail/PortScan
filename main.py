import socket

def scan_ports(start_port, end_port):
    host = socket.gethostbyname(socket.gethostname())
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        
        sock.close()

# Scanning ports from 1 to 1000
scan_ports(1, 1000)
