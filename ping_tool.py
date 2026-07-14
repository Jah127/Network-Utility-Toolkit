#Contains the functionality for the Ping Host Tool.
import subprocess

def ping_host():
    address = input("Enter an IP address or hostname: ")
    print()
    print(f"Pinging {address}...")

    command = ['ping', '-c', '1', address]
    subprocess.run(command)

    #print(subprocess)
#ping_host()