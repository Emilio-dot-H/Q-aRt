# Data Encoding Module
# Author: Elton Kjeld Schiott
# This class encodes the data bits for a QR code given an input string, 
# version, and error correction level.
## @mainpage Mainpage
#
##
# @file Data.py
# @title Data
# @date 2/11/2016
# @brief This class encodes data bits for a QR code. 
# @details This class encodes the data bits for a QR code given an input
# string, version, error correction level, and mode.\n
# State variables:\n
# String data - contains the binary string that reprsents the encoded
# input string.
# @code
#   data = Data.getDataBits(5,'H',BYTE, inputString)
# @endcode		

# @uses Constant.py
from Constant import char_cap, required_bytes, mindex, lindex, num_list, alphanum_list, grouping_list, mode_indicator

## @brief Method to obtain data bits for a QR code.
#  @date 2/11/2016
#  @details Method accepts four parameters. 
#  @param version Integer between 1 and 40 that specifies the size of
#  the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that 
#  specify the level of error correction to be encoded.
#  @param mode Accepts one of four values: NUMERIC, ALPHANUMERIC, BYTE, 
#  KANJI that specify the acceptable characters and encoding mode for
#  the QR code.
#  @param inputString Accepts an input string to be encoded into data
#  bits for a QR code.
#  @return Encoded data bits.
#  Method accepts four parameters
#  version: QR code version
#  ecl: QR code error correction level
#  mode: QR code encoding mode
#  inputString: String to be encoded.
def getDataBits(version, ecl, inputString):
	
	modeEncoding = {
			'numeric': numericEncoding,
			'alphanumeric': alphanumericEncoding,
			'byte': byteEncoding,
			}
	
	version, mode = analyse(version, ecl, inputString)
    
	data = mode_indicator[mode]+getCharacterCount(version, mode, inputString)+modeEncoding[mode](inputString)
    
	# Add a Terminator
	requiredBits = 8 * required_bytes[version-1][lindex[ecl]]
	bits = requiredBits - len(data)
	data += '0000' if bits >= 4 else '0' * bits
    
    # Make the Length a Multiple of 8
	data += (8-(len(data)%8))*'0'
    
    # Add Pad Bytes if the String is Still too Short
	while len(data) < requiredBits:    
		data += '1110110000010001' if requiredBits - len(data) >= 16 else '11101100'
        
	dataCode = [data[i:i+8] for i in range(len(data)) if i%8 == 0]
	dataCode = [int(i,2) for i in dataCode]

	groups = grouping_list[version-1][lindex[ecl]]
	dataCodewords = []
	index = 0
	for n in range(groups[0]):
		dataCodewords.append(dataCode[index:index+groups[1]])
		index += groups[1]
	for n in range(groups[2]):
		dataCodewords.append(dataCode[index:index+groups[3]])
		index += groups[3]
    
	return version, dataCodewords

## @brief Method to create a suitable binary string for given data.
#  @details Method accepts two parameters.
#  @param data Accepts an integer or string to be converted.
#  @param length Accepts an integer that specifies the length of string
#  to be generated.
#  @return a converted binary string of appropriate length.
def binString(data, length):
    pass

## @brief Method to determine the appropriate mode and version for a QR code.
#  @details Method accepts three parameters, and determines the appropriate version
#  given a desired version and error correction level. If the given
#  version is too small to hold the data, an appropriate one is selected.
#  @param version Integer between 1 and 40 that specifies the desired size of the QR code. 
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param inputString Accepts an input string to be encoded into data bits for a
#  QR code.
#  @return Appropriate version
def analyse(version, ecl, inputString):
	if all(i in num_list for i in inputString):
		mode = 'numeric'
	elif all(i in alphanum_list for i in inputString):
		mode = 'alphanumeric'
	else:
		mode = 'byte'
    
	modeIndex = mindex[mode]
	length = len(inputString)
	for i in range(40):
		if char_cap[ecl][i][modeIndex] > length:
			version = i + 1 if i+1 > version else version
			break
 
	return version, mode

## @brief Method to encode the Input String in numeric mode
#  @details The input string entered is assumed to be of 'numeric' mode. Each
#  char in the input string is encoded.
#  @param inputString Accepts an input string to be encoded into data bits for a
#  QR code.
#  @return string representing encoded input string
def numericEncoding(inputString):   
	strList = [inputString[i:i+3] for i in range(0,len(inputString),3)]
	data = ''
	for i in strList:
		requiredLength = 10
		if len(i) == 1: 
			requiredLength = 4
		elif len(i) == 2:
			requiredLength = 7
		temp = bin(int(i))[2:]
		data += ('0'*(requiredLength - len(temp)) + temp)
	return data

def alphanumericEncoding(inputString):
	strList = [alphanum_list.index(i) for i in str]
	data = ''
	for i in range(1, len(strList), 2):
		temp = bin(strList[i-1] * 45 + strList[i])[2:]
		temp = '0'*(11-len(temp)) + temp
		data += temp
	if i != len(strList) - 1:
		temp = bin(strList[-1])[2:]
		temp = '0'*(6-len(temp)) + temp
		data += temp
    
	return data

## @brief Method to encode the Input String as byte code
#  @details The URL or input string entered is assumed to be of 'byte' mode. Each
#  char in the input string is encoded into a byte code.
#  @param inputString Accepts an input string to be encoded into data bits for a
#  QR code.
#  @return byte code string representing input string/url
def byteEncoding(inputString):
	data = ''
	for i in inputString:
		temp = bin(ord(i.encode('iso-8859-1')))[2:]
		temp = '0'*(8-len(temp)) + temp
		data += temp
	return data

def getCharacterCount(version, mode, inputString):
	if 1 <= version <= 9:
		charCount = (10, 9, 8, 8)[mindex[mode]]
	elif 10 <= version <= 26:
		charCount = (12, 11, 16, 10)[mindex[mode]]
	else:
		charCount = (14, 13, 16, 12)[mindex[mode]]
        
	cci = bin(len(inputString))[2:]
	cci = '0' * (charCount - len(cci)) + cci
	return cci
