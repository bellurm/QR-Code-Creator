import qrcode, webbrowser, sys

sys.stdout.write("Press q and Enter for quit.\n")
choice = ["y", "n", "q"]
while True:
	try:
		qr_addr = input("Address: ")
		my_qr = qrcode.make(qr_addr)

		if(qr_addr == choice[-1]):
			sys.exit()

		qr_save = input("Choose a name: ")
		my_qr.save(qr_save)

		my_qr.show()

		#For Linux users
		if sys.platform.startswith('linux'):
			choose = input("Do you want to check your address of QR code? (y / n) > ")
			if(choose == choice[0]):
				webbrowser.open(qr_addr)
				sys.exit()
			elif(choose == choice[1]):
				sys.exit()
			else:
				print("Error: Invalid input.\n")
		#For Linux users

	except SyntaxError:
		sys.stderr.write("Error: If you are a Linux user, you should use the python3.\n")
		sys.stderr.flush()
		sys.exit()
	except KeyboardInterrupt:
		sys.exit()
"""
##### OLD CODE - SEP 8 2021 ####
import qrcode
import webbrowser

print("Press q and Enter for quit.\n")
choice = ["y", "n"]
while True:
	try:
		qr_addr = input("Address:")
		my_qr = qrcode.make(qr_addr)

		if(qr_addr == "q"):
			break

		qr_save = input("Choose a name:")
		my_qr.save(qr_save)

		my_qr.show()

		#For Kali Linux users
		while True:
			choose = input("Do you want to check your address of QR code? (y / n) ")
			if(choose == choice[0]):
				webbrowser.open(qr_addr)
				break
			elif(choose == choice[1]):
				break
			else:
				print("Error: Invalid input.\n")
		#For Kali Linux users

	except SyntaxError:
		print("Error: If you are a Linux user, you should use the python3.\n")
		break
	except KeyboardInterrupt:
		break
"""
