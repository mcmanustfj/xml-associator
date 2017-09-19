import xml.dom.minidom
import subprocess
import sys
from os import path

programs = {None : "C:\\Program Files (x86)\\Notepad++\\Notepad++.exe", "score-partwise" : "C:\\Program Files (x86)\\MuseScore 2\\bin\\MuseScore.exe"}

def parseFile(filename):

    #check filenames (poorly)
    if not(type(filename) is str):
        print("Error:",filename, "is not a string.",file=sys.stderr)
        return
    if not (".xml" in filename):
        print("Warning:", filename, "is not a .xml file.")

    #get path
    filename = path.abspath(filename)
    try:
        dom1 = xml.dom.minidom.parse(filename)
    except FileNotFoundError:
        print("Error:  File", filename, "not found.", file=sys.stderr)
        return


    if dom1.doctype == None:
        doctype = None
    else:
        doctype = dom1.doctype.name
    if not doctype in programs.keys():
        doctype = None
    subprocess.call([programs[doctype], filename])

def main():
    if len(sys.argv) == 1:
        print("No input file", file=sys.stderr)
    else:
        for i in range(1, len(sys.argv)):
            parseFile(sys.argv[i])

if __name__ == "__main__":
    main()