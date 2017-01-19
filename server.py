from socket import *
import time
import StringIO
from PIL import Image
import base64
from getClass import *
from predMnist import *
from predCifar import *
#Sohaib Ahmad
#Hamza Masud
#NUST - SEECS - BSCS 3
while 1:
        try:
                host = "0.0.0.0"

                serverSocket=socket(AF_INET,SOCK_STREAM)

                serverSocket.bind((host,40009))
                totalLength=""
                serverSocket.listen(10000)

                print "Ready to serve"

                data = []
                message = ""
                
                connectionSocket,clientAddress=serverSocket.accept()
                print clientAddress[1]

                while 1:
                        try:
                                message =connectionSocket.recv(16384)
                                data.append(message)
                                if len(message) == 0:
                                        print "Ended transmission"
                                        break
                        except:
                                print "Breaks"
                                break

                print "Transmitted"
                connectionSocket.send("BLAH")
                print "1"

                connectionSocket.close()
                fh = open("image.jpg", "wb+")

                for x in range(len(data)):
                    fh.write(data[x])
                fh.close()
                print "2"

                serverSocket.close()
                s = socket(AF_INET,SOCK_STREAM)

                print "3"

                s.connect((clientAddress[0],50000))
                print "4"

                customString = customClassifier()
                print "5"

                try:
                        customString += "/" + predMnist()
                        customString += "/" + predCifar()
                except:
                        customString += "/Cuda Unavailable"
                        customString += "/Cuda Unavailable"
                print "6"

                        
                s.send(customString)
                print "7"

                s.close()
                print "Done"
        except Exception:
                print Exception




