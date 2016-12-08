# -*- coding: utf-8 -*-
# Input Module
# Author: Elton Kjeld Schiott
# This class takes input to generate a QR code
## @mainpage Mainpage
#
##
# @file Input.py
# @title Input
# @date 2/11/2016
# @brief This class takes input to generate a QR code 
# @details
# State variables: none

# @uses Data.py
# @uses Draw.py
# @uses ECC.py
# @uses Matrix.py
# @uses Structure.py
import Data, Draw, ECC, Matrix, Structure #, GUI
import os
from PIL import Image
from tkinter import messagebox
## @brief Method to create QR code using command prompt
#  @date 4/11/2016
#  @details Method accepts nine parameters. 
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param picture Accepts the file location of an image to combine
#  @param colorized Accepts a boolean indicating whether or not the output will be in colour
#  @param contrast Accepts an integer indicating the cotrast level
#  @param brightness Accepts an integer indicating the brightness level
#  @param saveName Accepts a string containing the desired save name for the finished qr code
#  @param saveDirectory Accpets a string contating the desired save location for the finished qr code
#  @return Final binary string representing the data.

def run(inputString, version = 1, ecl = 'H', picture = None, colorized = False, contrast = 1.0, brightness = 1.0, saveName = None, saveDirectory = os.getcwd()):
	supported_chars = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz Â·Â·,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
     
    
	# check every parameter
	if not isinstance(inputString, str) or any(i not in supported_chars for i in inputString):
		raise ValueError('String characters unsupported!')
	if (not isinstance(version, int)) or (version not in range(1, 41)):
		raise ValueError('Invalid version! Enter an integer between 1 and 40.') and messagebox.showinfo(title="Greetings", message="Hello World!")
	if not isinstance(ecl, str) or len(ecl)>1 or ecl not in 'LMQH':
		raise ValueError("Invalid error corection level! Enter one of the following options: L, M, Q, H.")
	if picture:
		if not isinstance(picture, str) or not os.path.isfile(picture) or picture[-4:] not in ('.jpg','.png','.bmp','.gif'):
			raise ValueError("Invalid image! Make sure the image exists and that it has one of the folloeing formats: .jpg, .png, .bmp, .gif .")
		if picture[-4:] == '.gif' and saveName and saveName[-4:] != '.gif':
			raise ValueError('Invalid file type! If the input image is a .gif, the output image must be as well.')
		if not isinstance(colorized, bool):
			raise ValueError('Invalid colorized! Please enter a boolean value: True, False.')
		if not isinstance(contrast, float):
			raise ValueError('Invalid contrast! Please enter a float value.')
		if not isinstance(brightness, float):
			raise ValueError('Invalid brightness! Please enter a float value.')
	if saveName and (not isinstance(saveName, str) or saveName[-4:] not in ('.jpg','.png','.bmp','.gif')):
		raise ValueError("Invalid save name! Input a filename tailed with one of .jpg, .png, .bmp, .gif.")
	if not os.path.isdir(saveDirectory):
		raise ValueError('Invalid save directory! Please enter an existing directory!')
	
	# Get encoded data
	version, dataCodewords = Data.getDataBits(version, ecl, inputString)
	
	# Get error correction codewords
	errorCodewords = ECC.getCodewords(version, ecl, dataCodewords)
	
	# Structure final bits
	finalBits = Structure.getFinalData(version, ecl, dataCodewords, errorCodewords)
    
    # Create QR matrix
	qrmatrix = Matrix.getMatrix(version, ecl, finalBits)
    
    # Draw QR code
	qr_name = Draw.drawQRCode(saveDirectory, qrmatrix)
	
	#creates temporary directory for combine operation
	tempdir = os.path.join(os.path.expanduser('~'), '.myqr')
    
	try:
		if not os.path.exists(tempdir):
			os.makedirs(tempdir)

		# method for combining animated gif image
		if picture and picture[-4:]=='.gif':
			import imageio
             
			im = Image.open(picture)
			im.save(os.path.join(tempdir, '0.png'))
			while True:
				try:
					seq = im.tell()
					im.seek(seq + 1)
					im.save(os.path.join(tempdir, '%s.png' %(seq+1)))
				except EOFError:
					break
            
			imsname = []
			for s in range(seq+1):
				bg_name = os.path.join(tempdir, '%s.png' % s)
				imsname.append(Draw.combine(version, qr_name, bg_name, colorized, contrast, brightness, tempdir))
            
			ims = [imageio.imread(pic) for pic in imsname]
			qr_name = os.path.join(saveDirectory, os.path.splitext(os.path.basename(picture))[0] + '_qrcode.gif') if not saveName else os.path.join(saveDirectory, saveName)
			imageio.mimsave(qr_name, ims)
		# methods for regular image combining
		elif picture:
			qr_name = Draw.combine(version, qr_name, picture, colorized, contrast, brightness, saveDirectory, saveName)
		elif qr_name:
			qr = Image.open(qr_name)
			qr_name = os.path.join(saveDirectory, os.path.basename(qr_name)) if not saveName else os.path.join(saveDirectory, saveName)
			qr.resize((qr.size[0]*3, qr.size[1]*3)).save(qr_name)
          
		return version, ecl, qr_name
        
	except:
		raise
	finally:
		import shutil
		if os.path.exists(tempdir):
			shutil.rmtree(tempdir)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## @brief Method to create QR code using GUI
#  @date 7/12/2016
#  @details Method accepts nine parameters. 
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param picture Accepts the file location of an image to combine
#  @param colorized Accepts a boolean indicating whether or not the output will be in colour
#  @param contrast Accepts an integer indicating the cotrast level
#  @param brightness Accepts an integer indicating the brightness level
#  @param saveName Accepts a string containing the desired save name for the finished qr code
#  @param saveDirectory Accpets a string contating the desired save location for the finished qr code
#  @return Final binary string representing the data.
def runGUI(inputString, version = 1, ecl = 'H', picture = None, colorized = False, contrast = 1.0, brightness = 1.0, saveName = None, saveDirectory = os.getcwd()):
	supported_chars = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz Â·Â·,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
     
    
	# check every parameter
	if not isinstance(inputString, str) or any(i not in supported_chars for i in inputString):
		raise ValueError(messagebox.showerror(title='Error Alert!', message='Unsupported character(s)'))
	if (not isinstance(version, int)) or (version not in range(1, 41)):
		raise ValueError(messagebox.showerror(title='Invalid version!', message='Invalid version! Enter a number between 1 and 40.'))
	if not isinstance(ecl, str) or len(ecl)>1 or ecl not in 'LMQH':
		raise ValueError(messagebox.showerror(title='Invalid error corection level!', message='Enter one of the following options: L, M, Q, H.'))
	if picture:
		if not isinstance(picture, str) or not os.path.isfile(picture) or picture[-4:] not in ('.jpg','.png','.bmp','.gif'):
			raise ValueError(messagebox.showerror(title='Invalid image!', message='Make sure the image exists and that it has one of the following formats: .jpg, .png, .bmp, .gif .'))
		if picture[-4:] == '.gif' and saveName and saveName[-4:] != '.gif':
			raise ValueError(messagebox.showerror(title='Invalid file type!', message='If the input image is a .gif, the output image must be as well.'))
	##	if not isinstance(colorized, bool):
	##		raise ValueError(messagebox.showerror(title='Invalid colorized!', message='Please enter a boolean value: True, False.'))
		if not isinstance(contrast, float):
			raise ValueError(messagebox.showerror(title='Invalid contrast!', message='Please enter a decimal value (1.0 to 5.9)'))
		if not isinstance(brightness, float):
			raise ValueError(messagebox.showerror(title='Invalid brightness!', message='Please enter a float value.'))
	if saveName and (not isinstance(saveName, str) or saveName[-4:] not in ('.jpg','.png','.bmp','.gif')):
		raise ValueError(messagebox.showerror(title='Invalid save name!', message='Input a filename tailed with one of .jpg, .png, .bmp, .gif.'))
	if not os.path.isdir(saveDirectory):
		raise ValueError(messagebox.showerror(title='Invalid save directory!', message='Please enter an existing directory (i.e. Desktop'))
	
	# Get encoded data
	version, dataCodewords = Data.getDataBits(version, ecl, inputString)
	
	# Get error correction codewords
	errorCodewords = ECC.getCodewords(version, ecl, dataCodewords)
	
	# Structure final bits
	finalBits = Structure.getFinalData(version, ecl, dataCodewords, errorCodewords)
    
    # Create QR matrix
	qrmatrix = Matrix.getMatrix(version, ecl, finalBits)
    
    # Draw QR code
	qr_name = Draw.drawQRCode(saveDirectory, qrmatrix)
	
	#creates temporary directory for combine operation
	tempdir = os.path.join(os.path.expanduser('~'), '.myqr')
    
	try:
		if not os.path.exists(tempdir):
			os.makedirs(tempdir)

		# method for combining animated gif image
		if picture and picture[-4:]=='.gif':
			import imageio
             
			im = Image.open(picture)
			im.save(os.path.join(tempdir, '0.png'))
			while True:
				try:
					seq = im.tell()
					im.seek(seq + 1)
					im.save(os.path.join(tempdir, '%s.png' %(seq+1)))
				except EOFError:
					break
            
			imsname = []
			for s in range(seq+1):
				bg_name = os.path.join(tempdir, '%s.png' % s)
				imsname.append(Draw.combine(version, qr_name, bg_name, colorized, contrast, brightness, tempdir))
            
			ims = [imageio.imread(pic) for pic in imsname]
			qr_name = os.path.join(saveDirectory, os.path.splitext(os.path.basename(picture))[0] + '_qrcode.gif') if not saveName else os.path.join(saveDirectory, saveName)
			imageio.mimsave(qr_name, ims)
		# methods for regular image combining
		elif picture:
			qr_name = Draw.combine(version, qr_name, picture, colorized, contrast, brightness, saveDirectory, saveName)
		elif qr_name:
			qr = Image.open(qr_name)
			qr_name = os.path.join(saveDirectory, os.path.basename(qr_name)) if not saveName else os.path.join(saveDirectory, saveName)
			qr.resize((qr.size[0]*3, qr.size[1]*3)).save(qr_name)
          
		return version, ecl, qr_name
        
	except:
		raise
	finally:
		import shutil
		if os.path.exists(tempdir):
			shutil.rmtree(tempdir) 
