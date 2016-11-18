#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Input import run
from GUI import gui_main
import os

def main():
    import argparse

##    response = input("Would you like to display and interface? Yes(Y) or No(N): ")
##    str(reply) = response
##    if reply == 'Yes' | 'yes' | 'y' | 'Y' :
##        gui_main()

    argparser = argparse.ArgumentParser()
<<<<<<< HEAD
    
    argparser.add_argument('-gui', '--interface', action = 'store_true', help = 'Display the Graphical User Interface')
    argparser.add_argument('-w', '--Words', help = 'The words to produce you QR-code picture, like a URL or a sentence. Please read the README file for the supported characters.')
    argparser.add_argument('-v', '--version', type = int, choices = range(1,41), default = 1, help = 'The version means the length of a side of the QR-Code picture. From little size to large is 1 to 40.')
    argparser.add_argument('-l', '--level', choices = list('LMQH'), default = 'H', help = 'Use this argument to choose an Error-Correction-Level: L(Low), M(Medium) or Q(Quartile), H(High). Otherwise, just use the default one: H')
=======
    argparser.add_argument('Words', help = 'The words or phrase, string to produce you QR-code picture, could be a URL or a sentence. Please read the README file for the supported characters.')
    argparser.add_argument('-v', '--version', type = int, choices = range(1,41), default = 1, help = 'The version designates the size of the QR-Code picture. From small to large is 1 to 40.')
    argparser.add_argument('-l', '--level', choices = list('LMQH'), default = 'H', help = 'Use this argument to choose an Error-Correction-Level: L(Low), M(Medium) or Q(Quartile), H(High). Otherwise, just use the default level: H')
>>>>>>> 3b881fc44ee205ee00e1d67a65ece6e73590c7fd
    argparser.add_argument('-p', '--picture', help = 'the picture  e.g. example.jpg')
    argparser.add_argument('-c', '--colorized', action = 'store_true', help = "Produce a colorized QR-Code of your picture. There must be a correct '-p' or '--picture'.")
    argparser.add_argument('-con', '--contrast', type = float, default = 1.0, help = 'A floating point value controlling the enhancement of contrast. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-bri', '--brightness', type = float, default = 1.0, help = 'A floating point value controlling the enhancement of brightness. Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more. There are no restrictions on this value. Default: 1.0')
    argparser.add_argument('-n', '--name', help = "The filename of output tailed with one of {'.jpg', '.png', '.bmp', '.gif'}. eg. example.png")
    argparser.add_argument('-d', '--directory', default = os.getcwd(), help = 'The directory of output.')

    args = argparser.parse_args()
    
    if args.interface:
        gui_main()
    if args.picture and args.picture[-4:]=='.gif':
<<<<<<< HEAD
        print('It may take a while, please wait for minutes...')

=======
        print('This may take a while, please be patient...')
    
>>>>>>> 3b881fc44ee205ee00e1d67a65ece6e73590c7fd
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
