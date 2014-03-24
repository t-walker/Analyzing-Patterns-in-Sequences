#!/usr/bin/python -tt
'''
Create on March 3, 2014

@author: Gabriel de la Cruz

'''

import os


def SplitSequenceByLen (sequence, length=60):
  return [sequence[i:i+length] for i in range(0, len(sequence), length)]
#end SplitSequenceBylen()


def MakeDir(folderName):
  try:
    os.makedirs(folderName)

  except OSError:
    if not os.path.isdir(folderName):
      raise
#end MakeDir()


def WriteToFile(sampleFileName, pattern, matches, sampleIds, sampleSequences):
  cwd = os.getcwd()
  outputPath = cwd + '/Results/' + sampleFileName
  MakeDir(outputPath)

  patternFpDups = open(outputPath + '/P_' + pattern + '_duplicates.fasta', 'w')
  patternFpNoDups = open(outputPath + '/P_' + pattern + '_no_duplicates.fasta', 'w')

  perPatternFp = {}
  for i in range(0, len(pattern)):
    patternNum = int(pattern[i])
    perPatternFp[patternNum - 1] = open(outputPath + '/P_' + pattern + '_with_P_' + str(patternNum) + '_only.fasta', 'w')

  count = 0
  for match in matches:
    sampleIndex = match[0][0].number
    patternFpNoDups.write('>%s\n' %(sampleIds[sampleIndex]))
    sequence = '%s' %('\n'.join(SplitSequenceByLen(sampleSequences[sampleIndex])) + '\n')
    patternFpNoDups.write(sequence)

    ids = sampleIds[sampleIndex].split(',')

    for id in ids:
      patternFpDups.write('>%s\n' %(id))
      patternFpDups.write(sequence)
      count += 1
      for perPattern in match:
        perPatternFp[perPattern[1].number].write('>%s\n' %(id))
        sequence = '%s' %('\n'.join(SplitSequenceByLen(sampleSequences[sampleIndex][perPattern[0].startIndex:perPattern[0].endIndex])) + '\n')
        perPatternFp[perPattern[1].number].write(sequence)

  for key in perPatternFp.keys():
    perPatternFp[key].close()
  patternFpDups.close()
  patternFpNoDups.close()

#end WriteToFile()


def WriteToFileNoMatches(sampleFileName, noMatches, sampleIds, sampleSequences):
  cwd = os.getcwd()
  outputPath = cwd + '/Results/' + sampleFileName
  MakeDir(outputPath)

  noMatchesFp = open(outputPath + '/No_matches.fasta', 'w')

  for noMatch in noMatches:
    noMatchesFp.write('>%s\n' %(noMatch[0]))
    noMatchesFp.write('%s' %('\n'.join(SplitSequenceByLen(noMatch[1])) + '\n'))

  noMatchesFp.close()

#end WriteToFileNoMatches()
