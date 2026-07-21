#Contains the functionality for the Ping Host Tool.
import socket
import time
#Output
def ping_output(host, resolved_ip, port, status, elapsed_time):
    print("=========================")
    print("Host Reachability Report")
    print("=========================\n")

    print(f"Host: {host}\n")

    print(f"Resolved IP: {resolved_ip}\n")
            
    print(f"Port: {port}\n")    
            
    print(f"Status: {status}\n")
                
    print(f"Connection Time: {elapsed_time:.2f} ms")

    print("==================================================\n")

def ping_host():
    while True:
        try:
        #Prompting for desired host
            host = input("Enter an IP address or website: ")

        #IP Resolution
            resolved_ip = socket.gethostbyname(host)
            print(f"\nResolved IP address: {resolved_ip}\n")
        #Port Number
            port = input(f"Enter port # to reach {host} through (hit 'Enter' to default to port 443): ")
            port = 443 if port == '' else int(port)
            if not 1 <= port <= 65535:
                raise ValueError
        #Shows user its processing
            print(f"\nAttempting TCP connection to port {port}...\n")

        #Time calculations
            start_time = time.perf_counter()
            connection = socket.create_connection((resolved_ip, port), timeout=5)
            connection.close()
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000

        #Status Operations
            status = "Reachable"
            #Did have 'if-else' statement here, but realized if the program reached this
            #line status would still equal "Reachable" no matter what

            ping_output(host, resolved_ip, port, status, elapsed_time)
            break
#Crash Prevention
        except ValueError:
            print("\nPlease enter a valid port #.\n")
        except socket.gaierror:
            print("\nPlease enter a valid host name or IP address.\n")
        except socket.timeout:
            print("\nConnection timed out, please try again.\n")
        except ConnectionRefusedError:
            print("\nConnection request to server blocked.\n")
            break
        except OSError:
            print("\nUnable to establish a network connection.\n")
        except ConnectionResetError:
            print("\nUnexpected connection loss. Please try again.\n")

        