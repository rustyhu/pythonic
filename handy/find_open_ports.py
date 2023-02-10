# If want to use this in Python2, add following:
# from contextlib import closing
import socket


def find_open_ports():
    for port in range(1, 8081):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            res = sock.connect_ex(("localhost", port))
            if res == 0:
                print(f"Opened: port [{port}]")
                # yield port


find_open_ports()
