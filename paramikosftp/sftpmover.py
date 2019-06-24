#!/usr/bin/python3

import paramiko
import os

#where connect to

t=paramiko.Transport("10.10.2.3", 22) #IP

#how to connect

t.connect(username="bender", password="alta3")


        #make an sftp connection object

sftp = paramiko.SFTPClient.from_transport(t)

#iterate across the files within directory

for x in os.listdir("/home/student/filestocopy/"): #iterate on a directory
    if not os.path.isdir("/home/student/filestocopy/"+x): #filter everything NOT a dir
       sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) #moe files to a location

sftp.close() #close connection
