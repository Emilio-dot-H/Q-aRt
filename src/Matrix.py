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
import Constant

## @brief Method to get the matrix representing the final QR code.
#  @date 4/11/2016
#  @details Method accepts three parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param data Accepts the string containing the final binary data to be placed in the matrix.
#  @return Returns a 2D array representing the final QR code. 
def getMatrix(version, ecl, data):
    pass

## @brief Method to add finder and separator patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addFinders(qrmatrix):
    pass

## @brief Method to add alignment patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addAlignment(version, qrmatrix):
    pass

## @brief Method to place an alignment pattern in the matrix.
#  @date 4/11/2016
#  @details Method accepts three parameters
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param row Accepts an integer specifying the row where the pattern will be placed.
#  @param column Accepts an integer specifying the column where the pattern will be placed.
#  @return Modifies the matrix, does not return a value.
def placeAlignmentPattern(qrmatrix, row, column):
    pass

## @brief Method to add timing patterns to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addTiming(qrmatrix):
    pass

## @brief Method to add the dark bit and reserved bits to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Modifies the matrix, does not return a value.
def addReserved(version, qrmatrix):
    pass

## @brief Method to add data bits to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param data Accepts the string containing the final binary data to be placed in the matrix.
#  @return Modifies the matrix, does not return a value.
def addDataBits(qrmatrix, data):
    pass

## @brief Method to mask the QR code data.
#  @date 4/11/2016
#  @details Method accepts two parameters.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param maskMatrix Accepts a 2D array representing the mask pattern matrix
#  @return Returns the masked matrix with the best score and the id of what mask pattern was used.
def mask(qrmatrix, maskMatrix):
    pass

## @brief Method to generate mask pattern matrices.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param maskMatrix Accepts a 2D array representing the mask pattern matrix
#  @return Returns an array containing all mask pattern matrices.
def getMaskPatterns(maskMatrix):
    pass

## @brief Method to evaluate the quality of a mask on the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @return Returns an integer indicating the score achieved by the mask pattern on the matrix.
def evaluateMask(qrmatrix):
    pass

## @brief Method to add format and version strings to the QR code matrix.
#  @date 4/11/2016
#  @details Method accepts four parameters.
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param qrmatrix Accepts a 2D array representing the QR code matrix.
#  @param maskNum Accepts an integer between 0 and 7 indicating the id of the mask pattern used.
#  @return Modifies the matrix, does not return a value.
def addFormatVersion():
    pass



