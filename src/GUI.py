#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from Input import run
import os

class Application(Frame):
	""" A Gui App """
	def __init__(self, master):
	    Frame.__init__(self, master)
	    self.grid()
	    self.configure(background = '#8a8ac0')
	    self.create_widgets()

	def create_widgets(self):
	    self.photo = PhotoImage(file = "Icons/logo.png")
	    self.logo = Label(self, image = self.photo)
	    self.logo.pack()
	    self.instruction = Label(self, text = "Enter URL/Message", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.words = Entry(self, width = 30)
	    self.words.pack()

	    self.instruction = Label(self, text = "Enter Version (1-41)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.version = Entry(self, width = 30)
	    self.version.pack()

	    self.instruction = Label(self, text = "Enter Level (L, M, Q, H)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.level = Entry(self, width = 30)
	    self.level.pack()

	    self.instruction = Label(self, text = "Enter Media (png, jpg or gif)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.picture = Entry(self, width = 30)
	    self.picture.pack()

	    self.colVar = BooleanVar()
	    self.colorized = Checkbutton(self,text = "Select For Color", variable = self.colVar, bg = '#8a8ac0')
	    self.colorized.pack()

	    self.instruction = Label(self, text = "Enter Contrast (Default: 1.0)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.contrast = Entry(self, width = 30)
	    self.contrast.pack()

	    self.instruction = Label(self, text = "Enter Brightness (Default: 1.0)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.brightness = Entry(self, width = 30)
	    self.brightness.pack()

	    self.instruction = Label(self, text = "Enter New Name (.png or .gif)", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.name = Entry(self, width = 30)
	    self.name.pack()

	    self.instruction = Label(self, text = "Enter File Location", bg = '#8a8ac0')
	    self.instruction.pack()
	    self.directory = Entry(self, width = 30)
	    self.directory.pack()
	
	
	#Create first button
	    self.button1 = Button(self, text = "Generate", width =10, command = self.reveal, bg = '#383a39', fg = '#8a8ac0')
	    self.button1.pack()

	def reveal(self):
		if self.version.get() == '':    #DEFAULT for blank VERSION input
			versionInt = 1
		else:
			versionInt = int(self.version.get())

		if self.level.get() == '':      #DEFAULT for blank LEVEL input
			levelStr = 'L'
		else:
			levelStr = self.level.get()

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
			ver, ecl, qr_name = run(
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
def gui_main():
	root = Tk()
	root.title("Q-aRt Encoder")
	root.geometry("325x475")
	root.configure(background = '#8a8ac0')
	root.wm_iconbitmap('Icons/icon.ico')
	app = Application(root)
	root.mainloop()
