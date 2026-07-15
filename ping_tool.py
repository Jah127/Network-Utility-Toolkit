#Contains the functionality for the Ping Host Tool.
import socket

def ping_host():
    host = input("Enter an IP address or hostname: ")
    print()
    socket.create_connection(host)

    try:
        resolved_ip = socket.gethostbyname(host)
        print(f"Resolved IP address: {resolved_ip}")
        print()
    except socket.gaierror:
        print("Please enter a valid host name or IP address.")
        print()
