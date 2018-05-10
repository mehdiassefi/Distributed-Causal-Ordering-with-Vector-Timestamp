#!/usr/bin/env python
import sys
#import pygame
import socket
import time
import pickle
import os
import datetime
from threading import Thread
IP = '127.0.0.1'
global  flag0
global  flag1 
global  flag2 
global  flag3
global participants
global cmd
PORT0 = 36825
PORT1 = 36826
PORT2 = 36827
PORT3 = 36828
#matrix = [[[0 for x in range(48)] for x in range(7)] for x in range(4)]
message_list = []
buff = []
#matrix = [[0 for x in range(48)] for x in range(7)]

###print matrix
TCP_IP_SEND = '127.0.0.1'
TCP_PORT_SEND = 36825

TCP_IP_RCV = ''
TCP_PORT_RCV = 36828
BUFFER_SIZE = 1024
ignored = 0
seq = 0
MyId = 3
vect = [0, 0, 0, 0]
MSG_TYPE = 0
participants = 0
cmd = 0
#-------------------------------------------------------
#                       Message Packet
#-------------------------------------------------------
class msg:
      def __init__(self):
            self.type = 0
            self.id = 0
            self.cmd = 0
            self.seq = 0
            self.vect = [0, 0, 0, 0]
            self.participants = 0
     
msg0 = msg()
msg1 = msg()
msg2 = msg()
msg3 = msg()
msg4 = msg()
msg5 = msg()
msg6 = msg()


#-------------------------------------------------------
#                       Send Msg
#-------------------------------------------------------
def send(TCP_IP_SEND, TCP_PORT_SEND):
    global flag0
    global flag1
    global flag2
    global flag3
    global cmd
    global participants
    
    time.sleep(3)
    while True:
        #cmd = 4
        print("0: Command 0\n")
        print("1: Command 1\n")
        print("2: Command 2\n")
        print("3: Command 3\n")
        print("4: Command 4\n")
        cmd = input("Select your choice: ")
        participants = input("Enter the participans code : ")
        vect[MyId] = vect[MyId]+1
        msg0.vect = vect
        msg0.type = 0
        msg0.id = MyId
        msg0.cmd = cmd
        msg0.participants = participants
        pack = pickle.dumps(msg0)
        nn = participants
        nd = nn%2
        flag0 = nd 
        if (nd == 1 and MyId !=0):                         
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT0))
            s.send(pack)
            s.close()
        nn = nn/2
        nd = nn%2
        flag1 = nd
        if (nd == 1 and MyId !=1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT1))
            s.send(pack)
            s.close()
        nn = nn/2
        nd = nn%2
        flag2 = nd 
        if (nd == 1 and MyId !=2):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT2))
            s.send(pack)
            s.close()
        nn = nn/2
        nd = nn%2
        flag3 = nd 
        if (nd == 1 and MyId !=3):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT3))
            s.send(pack)
            s.close()
        continue                
#-------------------------------------------------------
#            Get ready for the next schedule!
#-------------------------------------------------------   
#-------------------------------------------------------
#------------                          -----------------
#-------------------------------------------------------
#-------------------------------------------------------
#                     Receiver thread
#-------------------------------------------------------

def rcv(TCP_IP_RCV, TCP_PORT_RCV):
    global flag0 
    global flag1
    global flag2
    global flag3   
    global participants
    global cmd
    while True:
        if len(message_list)>0 :
            msg1 = message_list.pop(0)
            flagtest = 0
##            if ((vect[msg1.id] +1) != msg1.vect[msg1.id] ):
##                  flagtest = 1
##            else:
##                  for i in range(0,4):
##                        if(msg1.id!=i and vect[i]  != msg1.vect[i]):
##                           flagtest = 1
            if (flagtest == 0 ):
                           vect[msg1.id] = vect[msg1.id] + 1
                           print 'Sequence of nodes"'
                           print (vect)
                           print 'Command :'
                           print msg1.cmd

            else :
                  buff.append(msg4)

                  
        s = len(buff)
        for i in range(0, s):
              msg1=buff.pop(0)
              flagtest = 0
              if ((vect[msg1.id] +1) != msg1.vect[msg1.id] ):
                    flagtest = 1
              else:
                    for i in range(0,4):
                          if(msg1.id!=i and vect[i]  != msg1.vect[i]):
                             flagtest = 1
              if (flagtest == 0 ):
                                
                    print "Buff"
                    print (len(buff))










def message_buffer(message_list):
      ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      ss.bind((TCP_IP_RCV, TCP_PORT_RCV))
      ss.listen(1)
      while True:
            
            conn, addr = ss.accept()
            datas = conn.recv(BUFFER_SIZE)
            msg4 = pickle.loads(datas)
            message_list.append(msg4)







Ts = Thread(target = send, args=(TCP_IP_SEND, TCP_PORT_SEND,))
Tp = Thread(target = rcv, args=(TCP_IP_RCV, TCP_PORT_RCV,))
Tq = Thread(target = message_buffer, args=(message_list,))
Ts.setDaemon(True)
Tp.setDaemon(True)
Tq.setDaemon(True)
Ts.start()
Tp.start()
Tq.start()
Ts.join()
Tp.join()
Tq.join()

