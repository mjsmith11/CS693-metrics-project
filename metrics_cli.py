import argparse
import sys
from app.src.metrics import *

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to input file")
parser.add_argument("-c","--comments", help="include comments in LOC", choices=['on','off'], default='off')
parser.add_argument("-e","--empty", help="include empty lines in LOC", choices=['on','off'], default='off')
parser.add_argument("-i","--imports", help="include import lines in LOC", choices=['on','off'], default='on')
parser.add_argument("-o","--object", help="include object class in DIT", choices=['on','off'], default='off')
parser.add_argument("-n","--init", help="include constructor in WMC", choices=['on','off'], default='off')
args = parser.parse_args()

try:
    f= open(args.file)
    f.close()
except IOError:
    print("ERROR - could not read file: "+args.file)
    sys.exit()

print(">>>> OUTPUT START")
print("")

## LOC -------------------------------------------
comments = True if args.comments=="on" else False
empty = True if args.empty=="on" else False
imports = True if args.imports=="on" else False

myLoc = loc.LinesOfCode(args.file)
myLoc.countLines()
result = myLoc.getCount(comments, empty, imports)

print("LOC (comments="+args.comments.upper()+",emptyLines="+args.empty.upper()+",imports="+args.imports.upper()+")")
print("---")
print(result)
print("")
print("")

## LCOM4 -----------------------------------------
myLcom4 = lcom4.LCOM4(args.file)
result = myLcom4.calculateModuleLCOM4()

print("LCOM4")
print("-----")
for key, value in result.items():
    print(key+" = "+str(value))
print("")
print("")

## CBO -------------------------------------------
myCbo = cbo.CBO(args.file)
result = myCbo.calculateAllCBO()

print("CBO")
print("---")
for key, value in result.items():
    print(key+" = "+str(value))
print("")
print("")

## DIT -------------------------------------------
obj = True if args.object=="on" else False
myDit = dit.DIT(args.file)
result = myDit.calculateAll(obj)

print("DIT (object="+args.object.upper()+")")
print("---")
for key, value in result.items():
    print(key+" = "+str(value))
print("")
print("")

## NOC -------------------------------------------
myNoc = noc.NOC(args.file)
result = myNoc.calculateAll()

print("NOC")
print("---")
for key, value in result.items():
    print(key+" = "+str(value))
print("")
print("")

## WMC -------------------------------------------
constructor = True if args.init=="on" else False
myWmc = wmc.WMC(args.file)
result = myWmc.calculateAll(constructor)

print("WMC (constructor="+args.init.upper()+")")
print("---")
for key, value in result.items():
    print(key+" = "+str(value))
print("")

print(">>>> OUTPUT END")