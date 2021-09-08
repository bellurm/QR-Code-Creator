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