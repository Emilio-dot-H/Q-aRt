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

## @brief Method to obtain error correction codewords.
#  @date 2/11/2016
#  @details Method accepts three parameters
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param data Accepts binary string to generate codewords for.
#  @return Returns a list of codewords to be used for error correction.
def getCodewords(version, ecl, data):
    pass

## @brief Method to divide the message polynomial by the generator polynomial
#  @date 2/11/2016
#  @details Method accepts two parameters.
#  @param MP Accepts an array of coefficients representing the message polynomial.
#  @param GP Accepts an array of coefficients representing the generator polynomial.
#  @return Returns the remainder of this iteration of division.
def divide(MP, GP):
    pass

## @brief Method to obtain the result of the exclusive or operation on the
#  generator and message polynomials.
#  @details Method accepts two parameters.
#  @param MP Accepts an array of coefficients representing the message polynomial.
#  @param GP Accepts an array of coefficients representing the generator polynomial.
#  @return Returns the result of the exclusive or operation as an array.
def XOR(GP, MP):
    pass
