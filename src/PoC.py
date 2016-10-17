

def run():
	MODE = '0010'
	LEGALCHARS = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
	
	print(MODE)
	
	version = 1
	level = 'Q'

	inputString = input('Enter string to be converted : ')
	
	if any(i not in LEGALCHARS for i in inputString):
		raise ValueError('Unsupported characters in input string')
		
	if (len(inputString)>16):
		raise ValueError('String must be less than 16 characters')
	
	charCount = binString(len(inputString), 9)	
	
	print(charCount)
	encInput = ''
	for i in range(0,len(inputString),2):
		try:
			temp = 45*LEGALCHARS.find(inputString[i])+LEGALCHARS.find(inputString[i+1])
			temp = binString(temp, 11)
		except IndexError:
			temp = LEGALCHARS.find(inputString[i])
			temp = binString(temp, 6)
		encInput += temp
	print(encInput)
	
	data = MODE+charCount+encInput
	
	print(data)
	
	reqBits = 13*8
	
	diff = reqBits-len(data)
	
	#Terminator bits
	if diff >= 4:
		data += '0000'
	elif diff < 4:
		data += diff*'0'
		
	#pad bits to make data string a mutiple of 8
	data += (8-(len(data)%8))*'0'
	
	#Still short, pad bytes
	numPadBytes = (reqBits-len(data))/8
	
	for i in range(0, numPadBytes):
		if (i%2 = 0):
			data += '11101100' #specific bytes designated as pad bytes
		else:
			data += '00010001'
	#raw data encoding complete
	
	#begin error correction encoding
	
def padBits(inString, num):
	
	while (len(inString)<num):
		inString = '0'+inString
	return inString

def binString(str1, num):
	str1 = str(bin(str1))
	str1 = str1[2:]
	str1 = padBits(str1, num)
	return str1

run()
