#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Error Correction Codeword Module
# Author: Emilio Hajj
# This class initializes the GUI
## @mainpage Mainpage
#
##
# @file GUI.py
# @title GUI
# @date 7/12/2016
# @brief This class initializes the GUI
# @details This class creates the graphical user interface for the program
# @code
#   codewords = ECC.getCodewords(1, 'Q', data)
# @endcode
from tkinter import *
from tkinter import messagebox
from Input import runGUI
import ctypes
import os

#Graphical User Interface Application
class Application(Frame):
	""" A Gui App """
	## @brief constructor for GUI
	def __init__(self, master):
	    Frame.__init__(self, master)
	    self.grid()
	    self.configure(background = '#8a8ac0')
	    self.create_widgets()
	## @brief Method to create all GUI widgets
	#  @details Creates the predefined widgets necessary for program operation.
	#  @return None
	def create_widgets(self):
	    self.photo = PhotoImage(file = "Icons/logo.png")
	    self.logo = Label(self, image = self.photo)
	    self.logo.pack()
	    self.instruction = Label(self, text = "Enter URL/Message", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.words = Entry(self, width = 40, bg = '#e1e281')
	    self.words.pack()

	    self.instruction = Label(self, text = "Enter Version (1-40)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.version = Entry(self, width = 40, bg = '#e1e281')
	    self.version.pack()

	    self.instruction = Label(self, text = "Enter Level (L, M, Q, H)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.level = Entry(self, width = 40, bg = '#e1e281')
	    self.level.pack()

	    self.instruction = Label(self, text = "Enter Media (png, jpg or gif)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.picture = Entry(self, width = 40, bg = '#e1e281')
	    self.picture.pack()

	    self.colVar = BooleanVar()
	    self.colorized = Checkbutton(self, activebackground= '#e1e281', bd=5, selectcolor= '#e1e281', text = "Select For Color", variable = self.colVar, bg = '#8a8ac0', font = ("arial", 11))
	    self.colorized.pack()

	    self.instruction = Label(self, text = "Enter Contrast (Default: 1.0)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.contrast = Entry(self, width = 40, bg = '#e1e281')
	    self.contrast.pack()

	    self.instruction = Label(self, text = "Enter Brightness (Default: 1.0)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.brightness = Entry(self, width = 40, bg = '#e1e281')
	    self.brightness.pack()

	    self.instruction = Label(self, text = "Enter New Name (.png or .gif)", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.name = Entry(self, width = 40, bg = '#e1e281')
	    self.name.pack()

	    self.instruction = Label(self, text = "Enter Save Location", bg = '#8a8ac0', font = ("arial", 11))
	    self.instruction.pack()
	    self.directory = Entry(self, width = 40, bg = '#e1e281')
	    self.directory.pack()
	    self.instruction = Label(self, text = "  ", bg = '#8a8ac0')
	    self.instruction.pack()
	    
	
	#Create generate button
	    self.button1 = Button(self, text = "Generate", width =20, command = self.reveal, bg = '#383a39', fg = '#e1e281', font = ("arial", 11))
	    self.button1.pack()
	def reveal(self):
		versionStr = self.version.get()
		if self.words.get() == '':
			messagebox.showerror(title='Error', message='Please enter a URL/Message')

		if self.version.get() == '':    #DEFAULT for blank VERSION input
			versionInt = 1
		elif versionStr.isalpha() == True:
			messagebox.showerror(title='Invalid Version!', message='Enter a version number from 1 to 40')
		elif int(self.version.get()) < 1 or int(self.version.get()) > 41:
			messagebox.showerror(title='Invalid Version!', message='Enter a version number from 1 to 40')

		else:
			versionInt = int(self.version.get())

		if self.level.get() == '':      #DEFAULT for blank LEVEL input
			levelStr = 'L'
		elif self.level.get() == 'L' or 'M' or 'Q' or 'H' or "l" or "m" or "q" or "h":
			levelStr = self.level.get()
		else:
			messagebox.showerror(title='Invalid Level!', message='Enter one of the following options: L, M, Q, H.')

		if self.directory.get() == '':  #DEFAULT for blank DIRECTORY input
			directoryStatus = os.getcwd()
		else:
			directoryStatus = self.directory.get()
		if self.contrast.get() == '':   #DEFAULT for blank Contrast input
			contrast = 1.0
		else:
			contrast = float(self.contrast.get())
		if self.brightness.get() == '': #DEFAULT for blank Brightness input
			brightness = 1.0
		else:
			brightness = float(self.brightness.get())
		try:
			ver, ecl, qr_name = runGUI(
				self.words.get(),
				versionInt,
				levelStr,
				self.picture.get(),
				self.colVar.get(),
				contrast,
				brightness,
				self.name.get(),
				directoryStatus
				)
			print('Succeed! \nCheck out your', str(ver) + '-' + str(ecl), 'QR-code:', qr_name)
		except:
			raise
			
##@brief Creates the GUI window
def gui_main():
	root = Tk()
	root.title("Q-aRt Encoder")
	root.geometry("325x550")
	root.configure(background = '#8a8ac0')
	root.wm_iconbitmap('Icons/icon.ico')
	app = Application(root)
	root.mainloop()
