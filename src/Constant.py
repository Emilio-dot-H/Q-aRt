# Constants for QR Generation
# Author: Elton Kjeld Schiott
# This class contains useful constants for qr processing.
## @mainpage Mainpage
#
##
# @file Constant.py
# @title Constant
# @date 13/11/2016
# @brief This class contains useful constants for qr processing.
# @details State variables:\n
# characterCapacity - list of character capacities for each version and error correction level\n
# requriedBytes - list of required bytes for each version\n
# numList - list of valid characters for numeric mode\n
# alphanumList - list of valid characters for alphanumeric mode\n
# groupingList - list of codeword grouping into blocks for each version\n
# modeIndicator - list of encoding mode strings\n
# GPList - lsit of generator polynomials\n
# codewordsPerBlock - list of error correction codewords per block for each version and error correction level\n
# powersOf2 - list of powers of two in Galois Field\n
# log - list of logarithms in Galois Field\n
# remainderBits - list of required remainder bits for each version for interleaving\n
# alignmentLocations - list of alignment pattern locations for each version\n
# formatString - list of format strings for each mask pattern\n
# versionString - list of version strings for each version\n


# import

#legal alphanumeric characters
legal_alphnum = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

#legal numerical characters
num_list = '0123456789'

#format information bits
format_info_str = [
    ['111011111000100', '111001011110011', '111110110101010', '111100010011101', '110011000101111', '110001100011000', '110110001000001', '110100101110110'], ['101010000010010', '101000100100101', '101111001111100', '101101101001011', '100010111111001', '100000011001110', '100111110010111', '100101010100000'], ['011010101011111', '011000001101000', '011111100110001', '011101000000110', '010010010110100', '010000110000011', '010111011011010', '010101111101101'], ['001011010001001', '001001110111110', '001110011100111', '001100111010000', '000011101100010', '000001001010101', '000110100001100', '000100000111011']
    ]

