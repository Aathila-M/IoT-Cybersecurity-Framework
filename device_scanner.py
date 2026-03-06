import socket

def discover_devices():

    devices = []

    base_ip = "192.168.1."

    for i in range(1,20):

        ip = base_ip + str(i)

        try:
            socket.gethostbyaddr(ip)
            devices.append(ip)
        except:
            pass

    return devices