import requests
import cv2
import numpy as np

url = 'http://192.168.1.2:8080/shot.jpg'

def main_menu():
	print(""" 
 _____       _             ______     _            _             
/  __ \     | |            |  _  \   | |          | |            
| /  \/ ___ | | ___  _ __  | | | |___| |_ ___  ___| |_ ___  _ __ 
| |    / _ \| |/ _ \| '__| | | | / _ \ __/ _ \/ __| __/ _ \| '__|
| \__/\ (_) | | (_) | |    | |/ /  __/ ||  __/ (__| || (_) | |   
 \____/\___/|_|\___/|_|    |___/ \___|\__\___|\___|\__\___/|_| """)
	print("===============================================================")
	print("|| Menu:                                                     ||")
	print("|| 1. Scan Warna Apel                                        ||")
	print("|| 2. Keluar                                                 ||")
	print("===============================================================")
	
	command = int(input("Masukkan nomor menu pilihan anda: "))

	if command == 1:
		detect_color()
		main_menu()
	else:
		print("Terima kasih telah menggunakan aplikasi ini.")

def detect_color():
	while True:
		#Mengambil gambar url dari scanning Android
		img_resp = requests.get(url)

		#Konversi gambar ke NumPy array
		img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
		
		#Konversi NumPy array ke imdecode untuk di proses
		img = cv2.imdecode(img_arr, -1)
		
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		#Setting mask
		lower_red = np.array([150,0,0])
		upper_red = np.array([180,255,255])

		mask = cv2.inRange(hsv, lower_red, upper_red)
		res = cv2.bitwise_and(img,img, mask = mask)

		#Menampilkan window
		cv2.namedWindow("Normal", cv2.WINDOW_NORMAL)
		cv2.namedWindow("Filter", cv2.WINDOW_NORMAL)
		cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

		cv2.imshow('Normal', img)
		cv2.imshow('Filter', res)

		#Keluar dari program
		if cv2.waitKey(1) == 27:
			break

main_menu()
