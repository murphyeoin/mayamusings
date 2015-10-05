import zmq
import threading
import time

port = "5556"


def server():
    context = zmq.Context().instance()
    socket = context.socket(zmq.PUB)
    socket.bind("inproc://testoid")
    
    while True:
        socket.send("blah")
        time.sleep(5)

t = threading.Thread(target=server, name='server')
t.start()