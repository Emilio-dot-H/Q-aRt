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
from Constant import required_remainder_bits, lindex, grouping_list

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
def getFinalData(version, ecl, dataCodewords, errorCorrectionCodewords):
    reorderedData = interleaveData(version, ecl, dataCodewords) + interleaveError(errorCorrectionCodewords)
    
    # convert to binary & Add Remainder Bits if Necessary
    finalData = ''.join(['0'*(8-len(i))+i for i in [bin(i)[2:] for i in reorderedData]]) + '0' * required_remainder_bits[version-1]
    
    return finalData

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
    data = []
    for t in zip(*dataCodewords):
        data += list(t)
    groups = grouping_list[version-1][lindex[ecl]]
    if groups[3]:
        for i in range(groups[2]):
            data.append(dataCodewords[i-groups[2]][-1])
    return data

## @brief Method to interleave error codewords.
#  @date 4/11/2016
#  @details Method accepts one parameter.
#  @param errorCodewords Accepts an array containing error correction codewords.
#  @return Returns an array containing the interleaved data codewords.
def interleaveError(errorCodewords):
    error = []
    for t in zip(*errorCodewords):
        error += list(t)
    return error
