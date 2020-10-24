import re

DIRECTORY_TO_CONVERT = '../functions.inc'
# case: line format -> eg. case 'something':
FUNCTION_AREA = "^(\s+?)?function(\s+?)"
# export case attribute -> eg. [case 'smth': => stmh]
EXPORT_FILE_NAME  = "((\s+?)?function(\s+?)|\((.*?)\)(\s+?)?\{(\s+?)(.*?))"

file = open(DIRECTORY_TO_CONVERT)

isFirstFunction = True
isCopyingContent = False
fileContent = ''

def writeIntoFile(fname, contents):
  newFile = open(fname + '.inc', "w+")
  newFile.write('<?php\n')
  newFile.write(contents)
  newFile.close()
  print(fname)

for line in file.readlines():
  isFunctionMatch = re.search(FUNCTION_AREA, line)


  if (isFunctionMatch != None):

    if (isFirstFunction == False):
      writeIntoFile(fileName, fileContent)
    else:
      isFirstFunction = False

    fileContent = line
    fileName = re.sub(EXPORT_FILE_NAME, "", line)
    print(fileName)

    isCopyingContent = True
    continue

  if (isCopyingContent == True ):
    fileContent += line
    