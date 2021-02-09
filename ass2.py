import socket
import sys
import os
from  threading import Thread
from _thread import start_new_thread
from collections import OrderedDict
import numpy as np
###################################GLOBAL  VARS#################################

serverport=9000

host='127.0.0.1'

alpha_dict=OrderedDict()

A=np.array([[-3,-3,-4],[0,1,1],[4,3,4]])

inv_A=np.array([[1,0,1],[4,4,3],[-4,-3,-3]])



#################################################################################


class MySocket:      # for createing socket objects with client and server functionalities 

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def clientConnect(self, host, port):
        self.sock.connect((host, port))

    def bindServer(self,host,port):

        self.sock.bind((host,port))

    def serverListen(self,no):
        self.sock.listen(no)

    def serverAccept(self):
        return self.sock.accept()

    def closeConnection(self):
        self.sock.close()

    def setSocket(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def sendmsg(self,msg):
        self.sock.send(msg)

    def receive(self,num):
        return self.sock.recv(num)



def crc(msg,div,code='000'):
    msg=msg+code
    msg=list(msg)
    div=list(div)
    for i in range(len(msg)-len(code)):
        if msg[i]=='1':
            for j in range(len(div)):
                msg[i+j]


def padding(sentence):
    chars_to_be_padded=3-(len(sentence)%3)
    
    return sentence+" "*chars_to_be_padded
    

def initialiseDict():
    for i in range(0,255):
        alpha_dict[chr(i)]=i
    alpha_dict[" "]=27


def clientfunc(clientPort,clientSoc):
    '''
    try:
        clientSoc.clientConnect(host, serverport)

        print("CONNECTED TO SERVER")
    except socket.error as e:
    
        print(str(e))
        exit()
    '''
    
    while True:
        inp = input()
        inp="PENGUINS ARE ONE TO ONE"   # sample input 
        inp=inp.strip()
        if not(len(inp)%3==0):
            #print("Entering here r\n")
            inp=padding(inp) 
        inp=[char for char in inp]
        P=[]
        count=0
        while count<len(inp):
            temp=[]
            for j in range(3):
                character=inp[count]

                if str(character).isupper():
                    temp.append(ord(character)-65+1)
                if str(character).islower():
                    temp.append(ord(character)-97+1)
                if str(character)==" ":
                    temp.append(27)
                
                count+=1
            P.append(temp)
            T=np.dot(A,np.transpose(P))

        print(T)
        
        
        








  



def main():
     # each client inturnacts as server to sense messages 
    clientPort=""      # this port will be used for server listening 
    if len(sys.argv)>1:
        clientPort=int(sys.argv[1])
    else:
        print("you need to give port number as command line argument ")
        exit()

    clientSoc=MySocket()

    initialiseDict()

    th = Thread(target=clientfunc,args=(clientPort,clientSoc)).start()


if __name__=="__main__":
    main()