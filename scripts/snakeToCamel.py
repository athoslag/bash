import argparse
import os

## This script parses words in snake_case to camelCase.
## Example:
## "string_key" = "String Key" -> "stringKey" = "String Key"

def snakeToCamel(line):
    newLine = line
    for option in range(len(snakeAlphabet)):
        if snakeAlphabet[option] in newLine:
            newLine = (newLine.replace(snakeAlphabet[option], camelCaseAlphabet[option]))
    return newLine

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)

args = parser.parse_args()
snakeAlphabet = [
    "_a", "_b", "_c", "_d", "_e", "_f", "_g", "_h", "_i", "_j",
    "_k", "_l", "_m", "_n", "_o", "_p", "_q", "_r", "_s", "_t",
    "_u", "_v", "_w", "_x", "_y", "_z"
]

camelCaseAlphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

newFile = []

with open(args.file, 'r') as file:
    for line in file:
        newFile.append(snakeToCamel(line))

newFileName = os.path.basename(file.name)
with open(newFileName, 'w') as file:
    for line in newFile:
        file.write(line)
    
print("Done parsing file %s".replace("%s", newFileName))
