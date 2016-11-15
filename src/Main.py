# Input Module
# Author: Elton Kjeld Schiott
# This class takes input to generate a QR code
## @mainpage Mainpage
#
##
# @file Main.py
# @title Main
# @date 2/11/2016
# @brief This class takes input to generate a QR code 
# @details
# State variables: none

# @uses Data.py
# @uses Draw.py
# @uses ECC.py
# @uses Matrix.py
# @uses Structure.py
import Data
import Draw
import ECC
import Matrix
import Structure

## @brief Method to create QR code
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
def run(inputString, version, ecl, picture, colorized, contrast, brightness, saveName, saveDirectory):
	pass
