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
def getDataBits(version, ecl, mode, inputString):
    pass

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
    pass

## @brief Method to encode the Input String as byte code
#  @details The URL or input string entered is assumed to be of 'byte' mode. Each
#  char in the input string is encoded into a byte code.
#  @param inputString Accepts an input string to be encoded into data bits for a
#  QR code.
#  @return byte code string representing input string/url
def byteEncoding(inputString):
    pass
