import zmq
import threading
import maya.utils

def doSphere(radius):
    maya.cmds.sphere( radius=radius )


def createSphere(sphereName):
    from maya import cmds
    names = cmds.polySphere(r=10)
    cmds.rename(names[0],sphereName)



def client():
    # Socket to talk to server
    context = zmq.Context.instance() #we have to reuse the same context when using inproc..
    socket = context.socket(zmq.SUB)
    socket.connect ("inproc://testoid")
    socket.setsockopt(zmq.SUBSCRIBE, b'')
    
    print "Client connected..."
    
    """thread worker function"""
    for update_nbr in range (5):
        string = socket.recv()
        print "received", string
        #@note This is not going to work in batch mode
        maya.utils.executeInMainThreadWithResult( createSphere, string )
    print "my work here is done"
    return


t = threading.Thread(target=client)
t.start()



