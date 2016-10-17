import ECC

def getDataBits():
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
	numPadBytes = int((reqBits-len(data))/8)
	
	for i in range(0, numPadBytes):
		if (i%2 == 0):
			data += '11101100' #specific bytes designated as pad bytes
		else:
			data += '00010001'
	#raw data encoding complete
	
	#data codewords
	
	data_code = [data[i:i+8] for i in range(len(data)) if i%8 == 0]
	data_code = [int(i,2) for i in data_code]

	g = (1, 13)
	data_codewords, i = [], 0
	for n in range(g[0]):
		data_codewords.append(data_code[i:i+g[1]])
		i += g[1]
	#error correction
	
	ecc = ECC.encode(1, 'Q', data_codewords)
	
	for i in range(0, len(ecc[0])):
		ecc[0][i] = binString(ecc[0][i], 8)
		
	finalString = data+''.join(ecc[0])
	
	return finalString
	
	
def padBits(inString, num):
	
	while (len(inString)<num):
		inString = '0'+inString
	return inString

def binString(str1, num):
	str1 = str(bin(str1))
	str1 = str1[2:]
	str1 = padBits(str1, num)
	return str1

def getMatrix(dataBits):
	qrmatrix = [[None] * 21 for i in range(21)]
	addFinders(qrmatrix)
	addAlignment(qrmatrix)
	addTiming(qrmatrix)
	addReserved(qrmatrix)
	
	for i in range(0,len(qrmatrix[0])):
		for j in range(0,len(qrmatrix[0])):
			if(qrmatrix[i][j] is None):
				qrmatrix[i][j] = 0
	for i in range(0,len(qrmatrix[0])):
		print(qrmatrix[i])

def addFinders(m):
	for i in range(8):
		for j in range(8):
			if i in (0, 6):
				m[i][j] = m[-i-1][j] = m[i][-j-1] = 0 if j == 7 else 1
			elif i in (1, 5):
				m[i][j] = m[-i-1][j] = m[i][-j-1] = 1 if j in (0, 6) else 0  
			elif i == 7:
				m[i][j] = m[-i-1][j] = m[i][-j-1] = 0
			else:
				m[i][j] = m[-i-1][j] = m[i][-j-1] = 0 if j in (1, 5, 7) else 1	
def addAlignment(m):
	#no alignment pattern for version 1 qr code
	pass
def addTiming(m):
	for i in range(21):
		for j in range(21):
			if(i==6 and m[i][j] is None):
				if(j%2==0):
					m[i][j] = 1
				else:
					m[i][j] = 0
			elif(j==6 and m[i][j] is None):
				if(i%2==0):
					m[i][j] = 1
				else:
					m[i][j] = 0
def addReserved(m):
	m[13][8] = 1
	for i in range(21):
		for j in range(21):
			if(i==8 and j not in range(9, 14) and m[i][j] is None):
				m[i][j] = 2
			elif(j==8 and i not in range(9,14) and m[i][j] is None):
				m[i][j] = 2
def addDataBits(m):
	


dataBits = getDataBits()
getMatrix(dataBits)
