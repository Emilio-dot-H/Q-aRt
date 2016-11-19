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
	    self.configure(background = 'DeepSkyBlue2')
	    self.create_widgets()

	def create_widgets(self):
	    self.photo = PhotoImage(file = "Icons/logo.png")
	    self.logo = Label(self, image = self.photo)
	    self.logo.grid(row=1, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.instruction = Label(self, text = "Enter URL/Message", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=3, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.words = Entry(self, width = 30)
	    self.words.grid(row =4, column=1, sticky=W)

	    self.instruction = Label(self, text = "Enter Version (1-41)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=5, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.version = Entry(self, width = 30)
	    self.version.grid(row =6, column =1, sticky=W)

	    self.instruction = Label(self, text = "Enter Level (L, M, Q, H)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=7, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.level = Entry(self, width = 30)
	    self.level.grid(row =8, column =1, sticky=W)

	    self.instruction = Label(self, text = "Enter Media (png, jpg or gif)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=9, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.picture = Entry(self, width = 30)
	    self.picture.grid(row =10, column =1, sticky=W)

##	    self.instruction = Label(self, text = "Select For Color")
##	    self.instruction.grid(row=9, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.colVar = BooleanVar()
	    self.colorized = Checkbutton(self,text = "Select For Color", variable = self.colVar, bg = 'DeepSkyBlue2')
	    self.colorized.grid(row =11, column = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Contrast (Default: 1.0)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=12, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.contrast = Entry(self, width = 30)
	    self.contrast.grid(row =13, column = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Brightness (Default: 1.0)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=14, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.brightness = Entry(self, width = 30)
	    self.brightness.grid(row =15, column =1, sticky=W)

	    self.instruction = Label(self, text = "Enter New Name (.png or .gif)", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=16, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.name = Entry(self, width = 30)
	    self.name.grid(row =17, column =1, sticky=W)

	    self.instruction = Label(self, text = "Enter File Location", bg = 'DeepSkyBlue2')
	    self.instruction.grid(row=18, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.directory = Entry(self, width = 30)
	    self.directory.grid(row =19, column =1, sticky=W)
	
	
	#Create first button
	    self.button1 = Button(self, text = "Generate", width =10, command = self.reveal)
	    self.button1.grid(row=20, column=1, sticky = W)

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
	root.geometry("305x435")
	root.configure(background = 'DeepSkyBlue2')
	root.wm_iconbitmap('Icons/paint.ico')
	app = Application(root)
	root.mainloop()
