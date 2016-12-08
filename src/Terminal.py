#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Command Line Argument Handling Module
# Author: Elton Kjeld Schiott, sylnsfar
# This class handles command line arguments to run the program.
## @mainpage Mainpage
#
##
# @file Terminal.py
# @title Terminal
# @date 4/11/2016
# @brief This class handles command line arguments to run the program.
# @details This class makes it possible to run the program through command line.\n
# State variables: none\n
from Input import run
from GUI import gui_main
import os

## @brief Method to obtain arguments via command line
#  @date 7/12/2016
#  @details Allows a user to interface with the program through command line.
def main():
    import argparse

    argparser = argparse.ArgumentParser()
    # adds possible arguments
    argparser.add_argument('-gui', '--interface', action = 'store_true', help = 'Display the Graphical User Interface')
    argparser.add_argument('-w', '--Words', help = 'The words to produce you QR-code picture, like a URL or a sentence. Please read the README file for the supported characters.')
    argparser.add_argument('-v', '--version', type = int, choices = range(1,41), default = 1, help = 'The version means the length of a side of the QR-Code picture. From little size to large is 1 to 40.')
    argparser.add_argument('-l', '--level', choices = list('LMQH'), default = 'H', help = 'Use this argument to choose an Error-Correction-Level: L(Low), M(Medium) or Q(Quartile), H(High). Otherwise, just use the default one: H')
    argparser.add_argument('-p', '--picture', help = 'the picture  e.g. example.jpg')
    argparser.add_argument('-c', '--colorized', action = 'store_true', help = "Produce a colorized QR-Code of your picture. There must be a correct '-p' or '--picture'.")
    argparser.add_argument('-con', '--contrast', type = float, default = 1.0, help = 'A floating point value controlling the enhancement of contrast. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-bri', '--brightness', type = float, default = 1.0, help = 'A floating point value controlling the enhancement of brightness. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-n', '--name', help = "The filename of output tailed with one of {'.jpg', '.png', '.bmp', '.gif'}. eg. example.png")
    argparser.add_argument('-d', '--directory', default = os.getcwd(), help = 'The directory of output.')

    args = argparser.parse_args()
    # run GUI
    if args.interface:
        gui_main()
	# gifs may take some time to process
    if args.picture and args.picture[-4:]=='.gif':

        print('It may take a while, please wait for minutes...')

        print('This may take a while, please be patient...')
	# run QR code encoder and combiner
    try:
        ver, ecl, qr_name = run(
            args.Words,
            args.version,
            args.level,
            args.picture,
            args.colorized,
            args.contrast,
            args.brightness,
            args.name,
            args.directory
            )   
        print('Success! \nCheck out your', str(ver) + '-' + str(ecl), 'QR-code under the name: ', qr_name)
    except:
        raise
