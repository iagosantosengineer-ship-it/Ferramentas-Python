import socket

def get_ip_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = "N/A"

    return {
        "ip": ip,
        "hostname": hostname
    }