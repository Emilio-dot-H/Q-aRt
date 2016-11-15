# Data Structuring Module
# Author: Elton Kjeld Schiott
# This class handles interleaving of data codewords and error correction
# codewords.
## @mainpage Mainpage
#
##
# @file Structure.py
# @title Structure
# @date 4/11/2016
# @brief This class handles interleaving of data codewords and error correction
# codewords. 
# @details This class interleaves the generated data codewords and error correction
# codewords by QR code standards before the data is placed in the matrix.\n
# State variables: none\n
# @code
#   finalData = Structure.getFinalData(30, 'M', dataCodewords, errorCodewords)
# @endcode

# @uses Constant.py
import Constant

## @brief Method to structure final data.
#  @date 4/11/2016
#  @details Method accepts four parameters. 
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param dataCodewords Accepts an array containing arrays of data codewords
#  representing blocks.
#  @param errorCodewords Accepts an array containing error correction codewords.
#  @return Final binary string representing the data.
def getFinalData(version, ecl, dataCodewords, errorCodewords):
    pass

## @brief Method to interleave data codewords.
#  @date 4/11/2016
#  @details Method accepts three parameters. 
#  @param version Integer between 1 and 40 that specifies the size of the QR code.
#  @param ecl Accepts one of four values: 'L', 'M', 'Q', 'H' that specify the
#  level of error correction to be encoded.
#  @param dataCodewords Accepts an array containing arrays of data codewords
#  representing blocks.
#  @return Returns an array containing the interleaved data codewords.
def interleaveData(version, ecl, dataCodewords):
    pass

## @brief Method to interleave error codewords.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param errorCodewords Accepts an array containing error correction codewords.
#  @return Returns an array containing the interleaved data codewords.
def interleaveError(errorCodewords):
    pass
