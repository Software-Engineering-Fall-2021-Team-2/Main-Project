from socket import *
import random

serverPort = 7501
serverName = 'localhost'


def UDPconnect(redID, greenID):
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # WHAT: Why is this random?
    if random.randint(1, 2) == 1:
        message = str(random.choice(redID))
    else:
        message = str(random.choice(greenID))

    # Encodes message into bytes and sends to server
    messageBytes = message.encode('utf-8')
    clientSocket.sendto(messageBytes, (serverName, serverPort))

    # Receives from server
    # WHAT: is serverAddress needed?
    newMessage, serverAddress = clientSocket.recvfrom(2048)

    # Decodes message
    currentMessage = newMessage.decode('utf-8')

    # Closes the socket
    clientSocket.close()

    return currentMessage
