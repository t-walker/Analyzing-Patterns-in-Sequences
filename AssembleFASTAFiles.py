#!/usr/bin/python -tt
'''
Create on March 3, 2014

@author: Gabriel de la Cruz

'''

import os


def SplitSequenceByLen (seq, length=60):
  return [seq[i:i+length] for i in range(0, len(seq), length)]
#end SplitSequenceBylen()


def MakeDir(folderName):
  try:
    os.makedirs(folderName)

  except OSError:
    if not os.path.isdir(folderName):
      raise
#end MakeDir()


def WriteToFile(sampFileName, pattern, matches, sampIds, sampSeqs):
  cwd = os.getcwd()
  outputPath = cwd + '/Results/' + sampFileName
  MakeDir(outputPath)

  patternFpDups   = open(outputPath + '/P_' + pattern + '_duplicates.fasta', 'w')
  patternFpNoDups = open(outputPath + '/P_' + pattern + '_no_duplicates.fasta', 'w')

  perPatternFp = {}
  for i in range(0, len(pattern)):
    patternNum = int(pattern[i])
    perPatternFp[patternNum - 1] = open(outputPath + '/P_' + pattern + '_with_P_' + str(patternNum) + '_only.fasta', 'w')

  count = 0
  for match in matches:
    sampIdx = match[0][0].num
    patternFpNoDups.write('>%s\n' %(sampIds[sampIdx]))
    seq = '%s' %('\n'.join(SplitSequenceByLen(sampSeqs[sampIdx])) + '\n')
    patternFpNoDups.write(seq)

    ids = sampIds[sampIdx].split(',')

    for id in ids:
      patternFpDups.write('>%s\n' %(id))
      patternFpDups.write(seq)
      count += 1
      for perPattern in match:
        perPatternFp[perPattern[1].num].write('>%s\n' %(id))
        sequence = '%s' %('\n'.join(SplitSequenceByLen(sampSeqs[sampIdx][perPattern[0].startIndex:perPattern[0].endIndex])) + '\n')
        perPatternFp[perPattern[1].num].write(sequence)

  for key in perPatternFp.keys():
    perPatternFp[key].close()
  patternFpDups.close()
  patternFpNoDups.close()

#end WriteToFile()


def WriteToFileNoMatches(sampFileName, noMatches, sampIds, sampSeqs):
  cwd = os.getcwd()
  outputPath = cwd + '/Results/' + sampFileName
  MakeDir(outputPath)

  noMatchesFp = open(outputPath + '/No_matches.fasta', 'w')

  for noMatch in noMatches:
    noMatchesFp.write('>%s\n' %(noMatch[0]))
    noMatchesFp.write('%s' %('\n'.join(SplitSequenceByLen(noMatch[1])) + '\n'))

  noMatchesFp.close()

#end WriteToFileNoMatches()


def WriteToFileStopCodons(sampFileName, matches):
  cwd = os.getcwd()
  outputPath = cwd + '/Results/' + sampFileName
  MakeDir(outputPath)

  matchesFp = open(outputPath + '/With_stop_codons.fasta', 'w')

  for match in matches:
    matchesFp.write('>%s\n' %(match[0]))
    matchesFp.write('%s' %('\n'.join(SplitSequenceByLen(match[1])) + '\n'))

  matchesFp.close()

#end WriteToFileNoMatches()
