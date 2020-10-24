# read file
# loop into the first 'switch()' only
  # exclude internal switch-cases
    # copy only data as text
  # search for 'case :'
    # take parameter string of case -> this is fileName
    # copy data as text
    # when find the next 'case :'
      # create a seperate file name with the fileName of previous 'case:'
      # write tag <?php in the first line
      # paste data
      # close file
    # if find 'default :'
      # do the same process of write the last case file
      # exit loop
# ______________________ --------------------- ______________________ #

import re

DIRECTORY_TO_CONVERT = '../actions.inc'
# switch() format -> eg. switch (something)
SWITCH_AREA = "switch(\s+)?\(.*\)"
# case: line format -> eg. case 'something':
CASE_AREA = "case\s('|\").*('|\").*(:(\s+)?$)"
# default: format
DEFAULT_AREA = "default(\s+)?:(\s+)?"
# export case attribute -> eg. [case 'smth': => stmh] 
EXPORT_FILE_NAME  = "((\s+?)([a-zA-Z]+)(\s+?)('|\"))|(('|\")(\s+)?:(\s+)?)"

file = open(DIRECTORY_TO_CONVERT)

isSearchingForCase = False
switchCaseLoopIndex = 0
isCaseFound = False
isCopyingContent = False
fileContent = ''

def writeIntoFile(fname, contents):
  newFile = open(fname + '.inc', "w+")
  newFile.write('<?php\n')
  newFile.write(contents)
  newFile.close()
  print(fname)

for line in file.readlines():
  isSwitchMatch = re.search(SWITCH_AREA, line)

  ### match the line you want to loop into => only for the first switch-case
  if (isSwitchMatch != None):
    switchCaseLoopIndex += 1
    isSearchingForCase = True

  ###----- search for case: -----###
  if (isSearchingForCase == True):
    isLineMatchCase = re.search(CASE_AREA, line)
    isDefaultMatch = re.search(DEFAULT_AREA, line)

    if (switchCaseLoopIndex > 1):
      # if you meet internal switch cases copy only lines
      if (isCaseFound == True):
        fileContent += line
      # exit from internal switch-case
      if (isDefaultMatch != None):
        # print('Found internal Default: ' + str(switchCaseLoopIndex))
        switchCaseLoopIndex -= 1
    
    else:
      if (isDefaultMatch != None):
        # program finisihed - last default case
        writeIntoFile(fileName, fileContent)
        print('Found final default')
        break

      # line match the loop you want to copy lines into
      if (isLineMatchCase != None):
        # write file except first case
        if (isCaseFound == True):
          # if fileContent is null - go next case
          if (fileContent != ''):
            writeIntoFile(fileName, fileContent)
            fileContent = ''
        else:
          isCaseFound = True
    
        fileName = re.sub(EXPORT_FILE_NAME, "", line)
      
      elif (isCaseFound == True):
        fileContent += line
        