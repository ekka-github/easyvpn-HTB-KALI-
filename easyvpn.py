from time import sleep
import subprocess
print'''

  ______             __      _______  _   _ 
 |  ____|            \ \    / /  __ \| \ | |
 | |__   __ _ ___ _   \ \  / /| |__) |  \| |
 |  __| / _` / __| | | \ \/ / |  ___/| . ` |
 | |___| (_| \__ \ |_| |\  /  | |    | |\  |
 |______\__,_|___/\__, | \/   |_|    |_| \_|
                   __/ |                    
                  |___/                     


'''
print('By DeadlyPoizon')
print('1. Connect to HackTheBox OpenVPN')
print('2. Disconnect to HackTheBox OpenVPN')
print('3. Close EasyVPN')
option = int(input("Choose an option: "))

def EasyVPN():

	if option == 1:
		done = False
		connecting = True
		while done == False:
			while connecting == True:
				print('By DeadlyPoizon - Quick and easy')
				subprocess.Popen(['openvpn', 'Downloads/DeadlyPoizon.ovpn'])
				sleep(5)
				connecting = False
				break

			if connecting == False:
				print('Connected to HTB OpenVPN')
				done = True
				break

	elif option == 2:
		print('Disconnecting...')
		disconnecting = True

		while disconnecting == True:
			subprocess.Popen(['killall', 'openvpn'])
			sleep(3)
			break


	elif option == 3:
		exit()
EasyVPN()
