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
	    self.create_widgets()

	def create_widgets(self):
	    self.instruction = Label(self, text = "Enter URL")
	    self.instruction.grid(row=1, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.words = Entry(self)
	    self.words.grid(row =2, column=1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Version")
	    self.instruction.grid(row=3, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.version = Entry(self)
	    self.version.grid(row =4, column =1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Level")
	    self.instruction.grid(row=5, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.level = Entry(self)
	    self.level.grid(row =6, column =1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Picture")
	    self.instruction.grid(row=7, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.picture = Entry(self)
	    self.picture.grid(row =8, column =1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Color")
	    self.instruction.grid(row=9, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.colVar = BooleanVar()
	    self.colorized = Checkbutton(self, variable = self.colVar)
	    self.colorized.grid(row =10, column = 1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Contrast")
	    self.instruction.grid(row=11, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.contrast = Entry(self)
	    self.contrast.grid(row =12, column = 1,rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter Brightness")
	    self.instruction.grid(row=13, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.brightness = Entry(self)
	    self.brightness.grid(row =14, column =1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter File Name")
	    self.instruction.grid(row=15, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.name = Entry(self)
	    self.name.grid(row =16, column =1, rowspan = 1, sticky=W)

	    self.instruction = Label(self, text = "Enter File Location")
	    self.instruction.grid(row=17, column=1, columnspan = 2, rowspan = 1, sticky = W)
	    self.directory = Entry(self)
	    self.directory.grid(row =18, column =1, rowspan = 1, sticky=W)
	
	
	#Create first button
	    self.button1 = Button(self, text = "GENERATE", width =10, command = self.reveal)
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

		if self.directory.get() == '':
			directoryStatus = os.getcwd()
		else:
			directoryStatus = self.directory.get()
		if self.contrast.get() == '':
			contrast = 1.0
		else:
			contrast = float(self.contrast.get())
		if self.brightness.get() == '':
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
	root.title("QR-Encoder")
	root.geometry("500x500")
	app = Application(root)
	root.mainloop()
