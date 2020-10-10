from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    # Fill in end
    #mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)

# Port number may change according to the mail server
    clientSocket.connect((mailserver, 587))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO \r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    mailfrom = 'MAIL FROM: <drishtimalik1995@gmail.com>\r\n'
    clientSocket.send(mailfrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server.')


    # Send RCPT TO command and print server response. 
    rcptto = 'RCPT TO: <bob@yahoo.com>\r\n'
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
        #print('250 reply not received from server.')

    # Send DATA command and print server response. 
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
        #print('354 reply not received from server.')

    # Send message data.
    msg = "\r\n My message"
    clientSocket.send(msg.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send QUIT command and get server response.
    quitcommand = 'QUIT\r\n'
    clientSocket.send(quitcommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != '221':
        #print('221 reply not received from server.')




if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
