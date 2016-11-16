# Error Correction Codeword Module
# Author: Elton Kjeld Schiott
# This class generates error correction codewords for a given version, error correction
# level and data string.
## @mainpage Mainpage
#
##
# @file ECC.py
# @title ECC
# @date 2/11/2016
# @brief This class generates error correction codewords. 
# @details This class generates error correction codewords for a given version, error correction
# level and data string.\n
# State variables:\n
# int list MP - coefficients representing the message polynomial at each iteration.\n
# int list GP - coefficients representing the generator polynomial at each iteration.\n
# @code
#   codewords = ECC.getCodewords(1, 'Q', data)
# @endcode

# @uses Constant.py
from Constant import GP_list, ecc_num_per_block, lindex, po2, log

## @brief Method to obtain error correction codewords.
#  @date 2/11/2016
#  @details Method accepts three parameters
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param data Accepts binary string to generate codewords for.
#  @return Returns a list of codewords to be used for error correction.
def getCodewords(version, ecl, data):
	wordsPerBlock = ecc_num_per_block[version-1][lindex[ecl]]
	errorCorrectionCodewords = []
	for dataCodeword in data:
		errorCorrectionCodewords.append(codeword(dataCodeword, wordsPerBlock))
	return errorCorrectionCodewords

def codeword(dataCodeword, wordsPerBlock):
	generatorPolynomial = GP_list[wordsPerBlock]
	remainder = dataCodeword
	for i in range(len(dataCodeword)):
		remainder = divide(remainder, *generatorPolynomial)
	return remainder

## @brief Method to divide the message polynomial by the generator polynomial
#  @date 2/11/2016
#  @details Method accepts two parameters.
#  @param MP Accepts an array of coefficients representing the message polynomial.
#  @param GP Accepts an array of coefficients representing the generator polynomial.
#  @return Returns the remainder of this iteration of division.
def divide(MP, *GP):
	if MP[0]:
		GP = list(GP)
		for i in range(len(GP)):
			GP[i] += log[MP[0]]
			if GP[i] > 255:
				GP[i] %= 255
			GP[i] = po2[GP[i]]
		return XOR(GP, *MP)
	else:
		return XOR([0]*len(GP), *MP)

## @brief Method to obtain the result of the exclusive or operation on the
#  generator and message polynomials.
#  @details Method accepts two parameters.
#  @param MP Accepts an array of coefficients representing the message polynomial.
#  @param GP Accepts an array of coefficients representing the generator polynomial.
#  @return Returns the result of the exclusive or operation as an array.
def XOR(GP, *MP):
	MP = list(MP)
	a = len(MP) - len(GP)
	if a < 0:
		MP += [0] * (-a)
	elif a > 0:
		GP += [0] * a
    
	remainder = []
	for i in range(1, len(MP)):
		remainder.append(MP[i]^GP[i])
	return remainder
