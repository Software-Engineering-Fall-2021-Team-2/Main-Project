from socket import *
import random

serverPort = 7501

#Create socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Command to reuse same socket over and over again
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#Start listening
serverSocket.bind(('', serverPort))
print('Server is ready to recieve')

#Continue listening forever
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)

    #Constantly read files due to changing teams from game to game
    IDs = []
    with open('redID.txt', 'r') as file:
        p = json.load(file)
        for i in p:
            IDs.append(i)
    with open('green.txt', 'r') as file:
        p = json.load(file)
        for i in p:
            IDs.append(i)

    playerID = random.choice(IDs)
    if int(message) != int(playerID):
        newMessage = str(message) + ':' + str(playerID)
    else:
        playerID = random.choice(IDs)
        newMessage = str(message) + ':' + str(playerID)

    newMessageBytes = newMessage.encode('utf-8')
    serverSocket.sendto(newMessageBytes, clientAddress)
