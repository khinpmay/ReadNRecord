# ==========================================
# Title: Read and record from microcontroller
# Author: P.M.Khin
# Date: 01/04/2020
# ==========================================

import os, sys, glob
import serial
import numpy as np

class Board:
	def __init__(self):	

		# change file name here
		self.file= open("insert_file_name","a+")
		self.controller = serial.Serial()
		# change port address here
		self.controller.port = "COM21"
		# change baudrate here
		self.controller.baudrate = 115200
		self.controller.timeout = 1
		self.controller.open()
		time.sleep(1) 

	def update(self):
		string = self.controller.readline()
		string = string.decode("utf-8")
		new_string = string.split(" ")
		new_strings = new_string[0:len(new_string)-1]
		lengthL = len(new_strings) 
		self.decodedbytes = np.zeros(lengthL)
		for index in range(len(new_strings)):
			toconvert = new_strings[index]
			self.decodedbytes[index] = float(toconvert) 
			self.file.write(str(self.decodedbytes[index]) + ',')
		self.file.write('\n')

	def closeFile(self):
		self.file.close()

