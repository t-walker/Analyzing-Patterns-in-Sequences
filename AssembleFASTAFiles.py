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


def WriteToFile(sampFileName, pattern, matches, sampIds, sampSeqs, output_path):
  outputPath = output_path + '/Match/'
  MakeDir(outputPath)

  fname = pattern.replace("/", "_")
  fname = fname.replace(",", "-")
  fname = fname.replace("(", "")
  fname = fname.replace(")", "")
  fname = fname.replace("gap", "g")

  try:
      patternFpDups = open(outputPath + '/' + fname + '_dp.fasta', 'w')
  except:
      pass

  try:
      patternFpNoDups = open(outputPath + '/' + fname + '_ndp.fasta', 'w')
  except:
      pass 

  count = 0
  for match in matches:
    sampIdx = match[1]
    patternFpNoDups.write('>%s\n' %(sampIds[sampIdx]))
    seq = '%s' %('\n'.join(SplitSequenceByLen(sampSeqs[sampIdx])) + '\n')
    patternFpNoDups.write(seq)

    ids = sampIds[sampIdx].split(',')

    for id in ids:
      patternFpDups.write('>%s\n' %(id))
      patternFpDups.write(seq)
      count += 1

  patternFpDups.close()
  patternFpNoDups.close()

#end WriteToFile()


def WriteToFileNoMatches(sampFileName, pattern, matches, sampIds, sampSeqs, output_path):
  outputPath = output_path + '/No_Match/'
  MakeDir(outputPath)

  fname = pattern.replace("/", "_")
  fname = fname.replace(",", "-")
  fname = fname.replace("(", "")
  fname = fname.replace(")", "")
  fname = fname.replace(" ", "_")
  fname = fname.replace("gap", "g")

  print "OUTPUT PATH\n", outputPath, "\nOUTPUT_PATH", output_path
  try:
      patternFpDups = open(outputPath + '/' + fname + '_dp.fasta', 'w')
  except:
      patternFpDups = open(outputPath + '/' + 'extraneous_patterns', 'a')
      patternFpDups.write("Pattern:\n")
      patternFpDups.write(fname)
      patternFpDups.write("------------------------------------------------------------------")
      

  try:
      patternFpNoDups = open(outputPath + '/' + fname + '_ndp.fasta', 'w')
  except:
      patternFpNoDups = open(outputPath + '/' + 'extraneous_patterns', 'a')
      patternFpNoDups.write("Pattern:\n")
      patternFpNoDups.write(fname)
      patternFpDups.write("------------------------------------------------------------------")

  count = 0
  for match in matches:
    sampIdx = match[1]
    patternFpNoDups.write('>%s\n' %(sampIds[sampIdx]))
    seq = '%s' %('\n'.join(SplitSequenceByLen(sampSeqs[sampIdx])) + '\n')
    patternFpNoDups.write(seq)

    ids = sampIds[sampIdx].split(',')

    for id in ids:
      patternFpDups.write('>%s\n' %(id))
      patternFpDups.write(seq)
      count += 1

  patternFpDups.close()
  patternFpNoDups.close()

#end WriteToFileNoMatches()


def WriteToFileStopCodons(sampFileName, matches, output_path):
  outputPath = output_path + '/No_Match'
  MakeDir(outputPath)

  matchesFp = open(outputPath + '/with_stop_codons.fasta', 'w')

  for match in matches:
    matchesFp.write('>%s\n' %(match[0]))
    matchesFp.write('%s' %('\n'.join(SplitSequenceByLen(match[1])) + '\n'))

  matchesFp.close()

#end WriteToFileNoMatches()
