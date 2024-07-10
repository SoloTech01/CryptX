import cryptography
from cryptography.fernet import Fernet
import sys
import time
import os
import colorama
colorama.init()
gr = colorama.Fore.GREEN
gray = colorama.Fore.LIGHTBLACK_EX
re = colorama.Fore.RESET
y = colorama.Fore.YELLOW
b = colorama.Fore.BLUE
lb = colorama.Fore.LIGHTBLUE_EX
lr = colorama.Fore.LIGHTRED_EX
r = colorama.Fore.RED

def write_key():
	key = Fernet.generate_key()
	path = "/storage/emulated/0/"
	with open(os.path.join(path, "key.txt"), "wb") as key_file:
		key_file.write(key)
		
def load_key():
	return open("/storage/emulated/0/key.txt", "rb").read()
	
def enc_dec():
	os.system("clear")
	print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
	print("""
	[1] Encrypt Text
	[2] Decrypt Text
	[3] Back
	[4] Exit program
	""")
	
	opt = input("Choose a valid option: ".strip().lower())
	def encrypt_text():
		os.system("clear")
		print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
		write_key()
		key = load_key()
		f = Fernet(key)
		message = input("Enter message: ").encode()
		print(f"{gr}Encrypting........{re}")
		time.sleep(3)
		encrypted_msg = f.encrypt(message)
		print(f"\n[✓] ENCRYPTED TEXT: {encrypted_msg}")
		print(f"\n[✓] Key has been saved as key.txt in the following path: /storage/emulated/0/key.txt")
		response= input("\n<<<<<<<<<<<<<<<<<Do you want to continue (y/n):>>>>>>>>>>>>>>>>>")
		if response.lower().strip() == "y":
			program_intro()
		elif response.lower().strip() == "n":
			print("\n")
			print(r)
			print("TERMINATING......")
			print(RESET)
			time.sleep(3)
			sys.exit()
		else:
			print("\n")
			print(r)
			print("INVALID OPTION!")
			print(RESET)
			sys.exit()
	
	def decrypt_text():
		os.system("clear")
		print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
		try:
			msg = input("Enter encrypted message: ")
			key = input("\nEnter the key: ")
			print(f"{gr}Decrypting........{re}")
			time.sleep(3)
			f = Fernet(key)
			decrypted_msg = f.decrypt(msg)
			print(f"\n[✓] DECRYPTED TEXT: {decrypted_msg}")
		except cryptography.fernet.InvalidToken:
			print(f"{gr}\nDecrypting........{re}")
			time.sleep(3)
			print(f"{lr}\n[x] Invalid Token!!")
		except ValueError as e:
			print(f"{gr}\nDecrypting........{re}")
			time.sleep(3)
			print(f"{lr}\n[x] An error occurred! : {e}")
		response= input(f"{gr}\n<<<<<<<<<<<<<<<<<Do you want to continue (y/n):>>>>>>>>>>>>>>>>>")
		if response.lower().strip() == "y":
			program_intro()
		elif response.lower().strip() == "n":
			print("\n")
			print(r)
			print("TERMINATING......")
			print(RESET)
			time.sleep(3)
			sys.exit()
		else:
			print("\n")
			print(r)
			print("INVALID OPTION!")
			print(RESET)
			sys.exit()
	if opt == "1":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		encrypt_text()
	elif opt == "2":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		decrypt_text()
	elif opt == "3":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		program_intro()
	elif opt == "4":
		print(f"{lr}Exiting.....")
		time.sleep(2)
		sys.exit()
	else:
		sys.exit()

def encrypt():
	os.system("clear")
	print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
	write_key()
	key = load_key()
	f = Fernet(key)
	inp = input("Enter the name of the file you want to encrypt(make sure it is in the following directory: /storage/emulated/0/): ")
	path = f"/storage/emulated/0/{inp}"
	if os.path.exists(path):
		with open(f"/storage/emulated/0/{inp}", "rb") as file:
			file_data = file.read()
		
		print(f"{gr}Decrypting........{re}")
		time.sleep(3)
		encrypted_data = f.encrypt(file_data)
		with open(os.path.join("/storage/emulated/0/", "encrypted_file.txt"), "wb") as file:
			file.write(encrypted_data)
			print("\n[✓] File encrypted successfully!")
			print(f"\n[✓] Key has been saved as key.txt in the following path: /storage/emulated/0/key.txt")
	else:
		print(f"{lr}\n[x] File Not Found!")
		time.sleep(2)
	response= input(f"{gr}\n<<<<<<<<<<<<<<<<<Do you want to continue (y/n):>>>>>>>>>>>>>>>>>")
	if response.lower().strip() == "y":
			program_intro()
	elif response.lower().strip() == "n":
			print("\n")
			print(r)
			print("TERMINATING......")
			print(RESET)
			time.sleep(3)
			sys.exit()
	else:
			print("\n")
			print(r)
			print("INVALID OPTION!")
			print(RESET)
			sys.exit()
		
def decrypt():
	os.system("clear")
	print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
	inp = input("Enter the name of the file you want to decrypt(make sure it is in the following directory: /storage/emulated/0/): ")
	path = f"/storage/emulated/0/{inp}"
	key = input("\nEnter the key: ")
	if os.path.exists(path):
		try:
			f = Fernet(key)
		except ValueError as e:
			print(f"{lr}\n[x] An error occurred! : {e}")
			program_intro()
		with open(f"/storage/emulated/0/{inp}", "rb") as file:
			encrypted_data = file.read()
		try:
			decrypted_data = f.decrypt(encrypted_data)
		except ValueError as e:
			print(f"{lr}\n[x] An error occurred! : {e}")
			program_intro()
	
		with open(os.path.join("/storage/emulated/0/", "decrypted_file.txt"), "wb") as file:
			print(f"{gr} Decrypting......")
			time.sleep(3)
			file.write(decrypted_data)
			print(f"{gr}\n[✓] File decrypted successfully!")
			print("\n[✓] PATH: /storage/emulated/0/decrypted_file")
	else:
		print(f"{lr}\n[x] File Not Found!")
		time.sleep(2)
	response= input(f"{gr}\n<<<<<<<<<<<<<<<<<Do you want to continue (y/n):>>>>>>>>>>>>>>>>>")
	if response.lower().strip() == "y":
			program_intro()
	elif response.lower().strip() == "n":
			print("\n")
			print(r)
			print("TERMINATING......")
			print(RESET)
			time.sleep(3)
			sys.exit()
	else:
			print("\n")
			print(r)
			print("INVALID OPTION!")
			print(RESET)
			sys.exit()
		
def file_crypt():
	os.system("clear")
	print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
	print("""
	[1] Encrypt File
	[2] Decrypt File
	[3] Back
	[4] Exit program
	""")
	opt = input("Choose a valid option: ".strip().lower())
	if opt == "1":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		encrypt()
	elif opt == "2":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		decrypt()
	elif opt == "3":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		program_intro()
	elif opt == "4":
		print("Exiting.....")
		time.sleep(2)
		sys.exit()
	else:
		sys.exit()
		
def program_intro():
	os.system("clear")
	print(f"""{y}
	
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░░░░░░██╗░░██╗{lb}
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝░░░░░░╚██╗██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░╚███╔╝░{gr}
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░╚════╝░██╔██╗░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░░░░██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝
""")
	print("\n")
	print(re)
	print(f"{y}******" * 10)
	print(f"""
[+] Tool name: Crypt-X
[+] Author: Solomon Adenuga
[+] Version: 1.0
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
	print("******" * 10)
	print(re)
	print(f"""{gr}
[1] Encrypt/decrypt text
[2] Encrypt/decrypt File
[3] About and Usage
[4] Update the program
[5] Exit the program
""")
	option = input(f"{lb}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<CHOOSE A VALID OPTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{re} ".strip())
	if option == "1":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		enc_dec()
	elif option == "2":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		file_crypt()
	elif option == "3":
		print(f"{gr}Loading.....{re}")
		time.sleep(2)
		print(f"""{gr}
		Crypt-X is a cryptography tool for encrypting and decrypting texts and filles.After encrypting a text or file using Crypt-X,a special key will be generated and saved to your device,that key is needed in order in decrypt the text or file
		
		Created by: Solomon Adenuga
		
		Kindly follow me on Github for more tools: SoloTech01
		""")
	elif option == "4":
		print(f"{gr}Updating.....{re}")
		time.sleep(2)
		os.system("""
		cd -
		rm -rf CryptX
		git clone https://github.com/SoloTech01/CryptX
		cd CryptX
		python3 cryptx.py
			""")
	elif option == "5":
		print(f"{lr}Exiting.....{re}")
		time.sleep(2)
		sys.exit()
		
program_intro()