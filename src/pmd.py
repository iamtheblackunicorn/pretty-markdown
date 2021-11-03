# PRETTY MARKDOWN by Alexander Abraham a.k.a. "The Black Unicorn"
# Licensed under the MIT license.

import sys
import colorama
import markdown
from sys import argv
from markdown import markdown
from colorama import init

"""Colorama needs to be initialized."""
init()

def getFC(fileName):
    """Here we try and get the file """
    """contents as a string."""
    try:
        return open(fileName).read()
    except Exception as error:
        print(colorama.Fore.RED + str(error) + colorama.Back.RESET)

def insertStyles(htmlCode, stylesheet, name):
    """We break up the HTML code into a list"""
    """and insert the styles."""
    htmlList = htmlCode.split('\n')
    preamble = [
     '<!DOCTYPE html>',
     '<html>',
     '<head>',
     '<link rel="stylesheet" href="' + stylesheet + '"/>',
     '<title>' + name + '</title>',
     '</head>',
     '<body>'
    ]
    fin = [
      '</body>',
      '</html>'
    ]
    htmlList = preamble + htmlList
    htmlList = htmlList + fin
    code = '\n'.join(htmlList)
    return code

def generateHTML(fileName, styles):
    """We generate the HTML"""
    """and write the string into a file."""
    code = markdown(getFC(fileName))
    htmlName = fileName.split('.')[0] + '.html'
    htmlFile = open(htmlName, 'w')
    compCode = insertStyles(code, styles, fileName.split('.')[0])
    htmlFile.write(compCode)
    htmlFile.close()

def main():
    """We attempt to convert it to HTML."""
    """If we fail, an error is displayed."""
    try:
        generateHTML(argv[1], argv[2])
        print(colorama.Fore.GREEN + 'Success!' + colorama.Back.RESET)
    except Exception as error:
        print(colorama.Fore.RED + str(error) + colorama.Back.RESET)
if __name__ == '__main__':
    main()
