import socket
target = "192.168.100.212"

print("starting port scan on",target)
for port in range(1,1025):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"port {port}is open")
        s.close()
        print("scan complete")


#this is a port scanner witten in python to scan ports 1-1024 to identify open ports
#i used it to practice python socket programming,how ports and sockets work and learn python socket programming



