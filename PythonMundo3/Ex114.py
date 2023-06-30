from urllib import request, error
import socket

try:
    request.urlopen('https://www.youtube.com')
    print("Site disponível =D")
except (socket.gaierror, error.URLError):
    print("Site indisponível =(")
