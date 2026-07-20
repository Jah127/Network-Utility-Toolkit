#Contains the functionality for the Ping Host Tool.
import socket
import time

#Prompting for hostname or IP
def ping_host():
    host = input("Enter an IP address or hostname: ")
#Printing resolved IP & prompting for desired port #
    while True:
        try:
        #IP Resolution
            resolved_ip = socket.gethostbyname(host)
            print(f"\nResolved IP address: {resolved_ip}\n")
        #Port Number
            port = input(f"Enter port # to reach {host} through (hit 'Enter' to default to port 443): ")
            port = 443 if port == '' else int(port)
        #Shows user its processing
            print("==================================================")
            print(f"\nAttempting TCP connection to port {port}...\n")

        #Time calculations
            start_time = time.perf_counter()
            connection = socket.create_connection((resolved_ip, port), timeout=5)
            connection.close()
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000

        #Status Operations
            status = "Reachable" if elapsed_time > 0 else "Unreachable"

        #Output

            print("Host Reachability Report")

            print("=========================")

            print(f"Resolved IP address: {resolved_ip}\n")
            
            print(f"Status: {status}\n")
            
            print(f"Connection Time: {elapsed_time:.2f}ms.\n")

            print(f"Port Number: {port}\n")
            
            print("==================================================")
            break
#Crash prevention
        except ValueError:
            print("\nPlease enter a valid port #.\n")
        except socket.gaierror:
            print("\nPlease enter a valid host name or IP address.\n")
        except socket.timeout:
            print("\nConnection timed out, please try again.\n")
        except ConnectionRefusedError:
            print("\nPlease try againg by entering a valid port #.\n")
        