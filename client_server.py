import argparse
import socket
import json
from time import ctime

HOST = 'localhost'
PORT = 54321
ADDR = (HOST, PORT)

def run_as_server():
    print('Running as server')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(5)

    while(True):
        print(f'Server listening on @{ADDR[0]} on port {ADDR[1]}')
        client, addr = s.accept()

        data = client.recv(2048)
        client_data = data.decode()
        print('\n\n====================')
        print_data(json.loads(data))
    

def run_as_client():
    print("Running as client")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDR)
    d= create_data('CLIENT')
    s.send(d.encode())

def create_data(sender='server'):
    result = {}
    result['Sender'] = sender
    result['name'] = 'Narendra'
    result['desc'] = 'He is evil'
    result['course'] = 'Python'
    result['time'] = ctime()
    return json.dumps(result)

def print_data(data):
    print(f"Sender: {data['Sender']}")
    print(f"Name: {data['name']}")
    print(f"Desc: {data['desc']}")
    print(F"Course: {data['course']}")
    print(f"Time: {data['time']}")


if __name__ == "__main__":
    #print("Running as an application")
    parser = argparse.ArgumentParser()
    parser.add_argument('-role',
                        choices=['client', 'server'],
                        help='server or client',
                        default='server')
    
    args = parser.parse_args()
    #print(args)    
    if args.role == 'server':
        run_as_server()
        #d = create_data('CLIENT')
        #print_data(d)
    else:
        run_as_client()
else:
    print("Running as a library")