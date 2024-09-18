# References
# https://www.samlogic.net/articles/smtp-commands-reference.htm
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/

from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print("recv1: " + recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    #print("mail from command")
    clientSocket.send(("MAIL FROM: <test@nyu.edu>\r\n").encode())
    mailFrom = clientSocket.recv(1024).decode()
    #print("mailFrom code: " + mailFrom) #returns 250 OK
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    #print("rcpt to command")
    clientSocket.send(("RCPT TO: <test@gmail.com>\r\n").encode())
    rcpt = clientSocket.recv(1024).decode()
    #print("rcpt code: " + rcpt) #returns 250 OK
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    #print("data command")
    clientSocket.send(("DATA\r\n").encode())
    data = clientSocket.recv(1024).decode()
    #print("data code: " + data) #returns 354 - begin sending data
    # Fill in end

    # Send message data.
    # Fill in start
    #print("sending msg")
    clientSocket.send(("SUBJECT: CSGY-6843 Python Assignment 3 \r\n").encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    #print("sending endmsg")
    clientSocket.send(endmsg.encode())
    sentEND = clientSocket.recv(1024).decode()
    #print("sentEND code: " + sentEND)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    #print("quitting")
    clientSocket.send(("QUIT\r\n").encode())
    sentQUIT = clientSocket.recv(1024).decode()
    #print("sentQUIT code: " + sentQUIT) #should return 221
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')