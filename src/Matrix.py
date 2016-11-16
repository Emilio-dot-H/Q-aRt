# QR Matrix Module
# Author: Elton Kjeld Schiott
# This class places the data in a matrix.
## @mainpage Mainpage
#
##
# @file Matrix.py
# @title Matrix
# @date 4/11/2016
# @brief This class places the data in a matrix.
# @details This class creates a matrix, places structures required according to
# QR code standards, evaluates the best mask pattern and applies it to the data.\n
# State variables:\n
# int array qrmatrix - 2D array representing the QR code matrix.\n
# @code
#   QRMatrix = Matrix.getMatrix(2, 'L', finalData)
# @endcode

# @uses Constant.py
from Constant import alig_location, format_info_str, version_info_str, lindex

## @brief Method to get the matrix representing the final QR code.
#  @date 4/11/2016
#  @details Method accepts three parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param data Accepts the string containing the final binary data to be placed in the matrix.
#  @return Returns a 2D array representing the final QR code. 
def getMatrix(version, ecl, data):
	size = (version - 1) * 4 + 21
	qrmatrix = [[None] * size for i in range(size)]

    # Add the Finder Patterns & Add the Separators
	addFinders(qrmatrix)
    
    # Add the Alignment Patterns
	addAlignment(version, qrmatrix)
    
    # Add the Timing Patterns
	addTiming(qrmatrix)
    
    # Add the Dark Module and Reserved Areas
	addReserved(version, qrmatrix)
    
	maskMatrix = [i[:] for i in qrmatrix]
    
    # Place the Data Bits
	addDataBits(qrmatrix, data)
    
    # Data Masking
	maskNum, qrmatrix = mask(qrmatrix, maskMatrix)
    
    # Format Information
	addFormatVersion(version, ecl, maskNum, qrmatrix)

	return qrmatrix

## @brief Method to add finder and separator patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addFinders(qrmatrix):
	for i in range(8):
		for j in range(8):
			if i in (0, 6):
				qrmatrix[i][j] = qrmatrix[-i-1][j] = qrmatrix[i][-j-1] = 0 if j == 7 else 1
			elif i in (1, 5):
				qrmatrix[i][j] = qrmatrix[-i-1][j] = qrmatrix[i][-j-1] = 1 if j in (0, 6) else 0  
			elif i == 7:
				qrmatrix[i][j] = qrmatrix[-i-1][j] = qrmatrix[i][-j-1] = 0
			else:
				qrmatrix[i][j] = qrmatrix[-i-1][j] = qrmatrix[i][-j-1] = 0 if j in (1, 5, 7) else 1

## @brief Method to add alignment patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addAlignment(version, qrmatrix):
	if version > 1:
		coordinates = alig_location[version-2]
		for i in coordinates:
			for j in coordinates:
				if qrmatrix[i][j] is None:
					placeAlignmentPattern(qrmatrix, i, j)

## @brief Method to place an alignment pattern in the matrix.
#  @date 4/11/2016
#  @details Method accepts three parameters
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param row Accepts an integer specifying the row where the pattern will be placed.
#  @param column Accepts an integer specifying the column where the pattern will be placed.
#  @return Modifies the matrix, does not return a value.
def placeAlignmentPattern(qrmatrix, row, column):
	for i in range(row-2, row+3):
		for j in range(column-2, column+3):
			qrmatrix[i][j] = 1 if i in (row-2, row+2) or j in (column-2, column+2) else 0
	qrmatrix[row][column] = 1

## @brief Method to add timing patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addTiming(qrmatrix):
	for i in range(8, len(qrmatrix)-8):
		qrmatrix[i][6] = qrmatrix[6][i] = 1 if i % 2 ==0 else 0

## @brief Method to add the dark bit and reserved bits to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addReserved(version, qrmatrix):
	for j in range(8):
		qrmatrix[8][j] = qrmatrix[8][-j-1] = qrmatrix[j][8] = qrmatrix[-j-1][8] = 0
	qrmatrix[8][8] = 0
	qrmatrix[8][6] = qrmatrix[6][8] = qrmatrix[-8][8] = 1
    
	if version > 6:
		for i in range(6):
			for j in (-9, -10, -11):
				qrmatrix[i][j] = qrmatrix[j][i] = 0

## @brief Method to add data bits to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param data Accepts the string containing the final binary data to be placed in the matrix.
#  @return Modifies the matrix, does not return a value.
def addDataBits(qrmatrix, data):
	bit = (int(i) for i in data)

	up = True
	for a in range(len(qrmatrix)-1, 0, -2):
		a = a-1 if a <= 6 else a
		irange = range(len(qrmatrix)-1, -1, -1) if up else range(len(qrmatrix))
		for i in irange:
			for j in (a, a-1):
				if qrmatrix[i][j] is None:
					qrmatrix[i][j] = next(bit)
		up = not up

## @brief Method to mask the QR code data.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param maskMatrix Accepts a 2D array representing the mask pattern matrix
#  @return Returns the masked matrix with the best score and the id of what mask pattern was used.
def mask(qrmatrix, maskMatrix):
	maskPatterns = getMaskPatterns(maskMatrix)
	scores = []
	for maskPattern in maskPatterns:
		for i in range(len(maskPattern)):
			for j in range(len(maskPattern)):
				maskPattern[i][j] = maskPattern[i][j] ^ qrmatrix[i][j]
		scores.append(evaluateMask(maskPattern))
	best = scores.index(min(scores))
	return best, maskPatterns[best]

## @brief Method to generate mask pattern matrices.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param maskMatrix Accepts a 2D array representing the mask pattern matrix
#  @return Returns an array containing all mask pattern matrices.
def getMaskPatterns(maskMatrix):
	def formula(i, row, column):
		if i == 0:
			return (row + column) % 2 == 0
		elif i == 1:
			return row % 2 == 0
		elif i == 2:
			return column % 3 == 0
		elif i == 3:
			return (row + column) % 3 == 0
		elif i == 4:
			return (row // 2 + column // 3) % 2 == 0
		elif i == 5:
			return ((row * column) % 2) + ((row * column) % 3) == 0
		elif i == 6:
			return (((row * column) % 2) + ((row * column) % 3)) % 2 == 0
		elif i == 7:
			return 	(((row + column) % 2) + ((row * column) % 3)) % 2 == 0

	maskMatrix[-8][8] = None
	for i in range(len(maskMatrix)):
		for j in range(len(maskMatrix)):
			maskMatrix[i][j] = 0 if maskMatrix[i][j] is not None else maskMatrix[i][j]
	maskPatterns = []
	for i in range(8):
		maskPattern = [ii[:] for ii in maskMatrix]
		for row in range(len(maskPattern)):
			for column in range(len(maskPattern)):
				maskPattern[row][column] = 1 if maskPattern[row][column] is None and formula(i, row, column) else 0
		maskPatterns.append(maskPattern)
        
	return maskPatterns

## @brief Method to evaluate the quality of a mask on the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Returns an integer indicating the score achieved by the mask pattern on the matrix.
def evaluateMask(qrmatrix):
	def evaluation1(qrmatrix):
		def ev1(ma):
			sc = 0
			for mi in ma:
				j = 0
				while j < len(mi)-4:
					n = 4
					while mi[j:j+n+1] in [[1]*(n+1), [0]*(n+1)]:
						n += 1
					(sc, j) = (sc+n-2, j+n) if n > 4 else (sc, j+1)
			return sc
		return ev1(qrmatrix) + ev1(list(map(list, zip(*qrmatrix))))
        
	def evaluation2(qrmatrix):
		sc = 0
		for i in range(len(qrmatrix)-1):
			for j in range(len(qrmatrix)-1):
				sc += 3 if qrmatrix[i][j] == qrmatrix[i+1][j] == qrmatrix[i][j+1] == qrmatrix[i+1][j+1] else 0
		return sc
        
	def evaluation3(qrmatrix):
		def ev3(ma):
			sc = 0
			for mi in ma:
				j = 0
				while j < len(mi)-10:
					if mi[j:j+11] == [1,0,1,1,1,0,1,0,0,0,0]:
						sc += 40
						j += 7
					elif mi[j:j+11] == [0,0,0,0,1,0,1,1,1,0,1]:
						sc += 40
						j += 4
					else:
						j += 1
			return sc
		return ev3(qrmatrix) + ev3(list(map(list, zip(*qrmatrix))))
        
	def evaluation4(qrmatrix):
		darknum = 0
		for i in qrmatrix:
			darknum += sum(i)
		percent = darknum  / (len(qrmatrix)**2) * 100
		s = int((50 - percent) / 5) * 5
		return 2*s if s >=0 else -2*s

	score = evaluation1(qrmatrix) + evaluation2(qrmatrix)+ evaluation3(qrmatrix) + evaluation4(qrmatrix)
	return score

## @brief Method to add format and version strings to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts four parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param maskNum Accepts an integer between 0 and 7 indicating the id of the mask pattern used.
#  @return Modifies the matrix, does not return a value.
def addFormatVersion(version, ecl, maskNum, qrmatrix):
	formatString = [int(i) for i in format_info_str[lindex[ecl]][maskNum]]
	for j in range(6):
		qrmatrix[8][j] = qrmatrix[-j-1][8] = formatString[j]
		qrmatrix[8][-j-1] = qrmatrix[j][8] = formatString[-j-1]
	qrmatrix[8][7] = qrmatrix[-7][8] = formatString[6]
	qrmatrix[8][8] = qrmatrix[8][-8] = formatString[7]
	qrmatrix[7][8] = qrmatrix[8][-7] = formatString[8]
    
	if version > 6:
		versionString = (int(i) for i in version_info_str[version-7])
		for j in range(5, -1, -1):
			for i in (-9, -10, -11):
				qrmatrix[i][j] = qrmatrix[j][i] = next(versionString)



