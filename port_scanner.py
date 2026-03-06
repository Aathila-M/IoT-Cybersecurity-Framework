import socket

services = {
21:"FTP",
22:"SSH",
23:"TELNET",
25:"SMTP",
53:"DNS",
80:"HTTP",
110:"POP3",
139:"NETBIOS",
143:"IMAP",
443:"HTTPS",
445:"SMB",
3389:"RDP"
}

def scan_ports(target):

    results = []

    for port in range(1,1025):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)

        result = s.connect_ex((target,port))

        if result == 0:

            service = services.get(port,"Unknown")

            results.append((port,service))

        s.close()

    return results