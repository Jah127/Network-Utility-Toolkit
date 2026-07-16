#Contains the functionality for the Ping Host Tool.
import socket
import time

#Prompting for hostname or IP
def ping_host():
    host = input("Enter an IP address or hostname: ")
#Printing resolved IP & prompting for desired port #
    try:
        resolved_ip = socket.gethostbyname(host)
        print(f"\nResolved IP address: {resolved_ip}\n")
        
        port = int(input(f"Enter port to reach {host} through: "))

        #Time calculations
        start_time = time.perf_counter()
        connection = socket.create_connection((resolved_ip, port), timeout=5)
        connection.close()
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000

#Crash prevention
    except ValueError:
        print("\nPlease enter a valid port #.\n")
    except socket.gaierror:
        print("\nPlease enter a valid host name or IP address.\n")
    except socket.timeout:
        print("\nConnection timed out, please try again.\n")
    except ConnectionRefusedError:
        print("\nPlease enter a valid port #.\n")
    
    print("Status: Reachable")

    print(f"Your TTR is {elapsed_time:.2f}ms.\n")
