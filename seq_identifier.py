#!/usr/bin/python -tt
# python seq_identifier.py -p Allels_Trimv2.fa -s MS_1376Translations.fa -d
import os
import sys
import getopt


import GlobalVars

from DataLibs import *
from GetSequences import GetSequences
from DeterminePattern import DeterminePattern
from AssembleFASTAFiles import WriteToFile, WriteToFileNoMatches


def usage():
  print 'seq_identifier.py -p <patternFile> -s <sampleFile>'

##################################################################
# NEEDS SOME CHANGING TO CONSIDER MISSING CHARACTER IN SAMPLE    #
##################################################################
def CombineSimilarPattern(patternMatch):
  totalPatterns = len(patternMatch)
  if totalPatterns == 1:
    return patternMatch
  else:
    startIndex = 0
    while True:
      if patternMatch[startIndex][1].number == patternMatch[startIndex+1][1].number:
        patternMatch[startIndex][1].endIndex = patternMatch[startIndex+1][1].endIndex
        patternMatch[startIndex][1].size = patternMatch[startIndex][1].endIndex - patternMatch[startIndex][1].startIndex
        patternMatch[startIndex][0].snippets += patternMatch[startIndex+1][0].snippets
        patternMatch[startIndex][0].endIndex = patternMatch[startIndex+1][0].endIndex
        patternMatch[startIndex][0].size = patternMatch[startIndex][0].endIndex - patternMatch[startIndex][0].startIndex
        del patternMatch[startIndex+1]
        totalPatterns -= 1
      else:
        startIndex += 1
      if (startIndex+1) == totalPatterns:
        break
  return patternMatch


def main(argv):

  try:
    opts, args = getopt.getopt(argv, "hp:s:d", ["help", "pattern=", "samplefile="])

  except getopt.GetoptError:
    usage()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt == '-d':
      print "[DEBUG MODE]"
      GlobalVars.DEBUG = True
    elif opt in ("-p", "--pattern"):
      patternFile = arg
    elif opt in ("-s", "--samplefile"):
      sampleFile = arg


  # Step 1: Retrieve allele patterns
  alleleIds, allelePatterns, numPatterns = GetSequences(patternFile, "fasta", os.getcwd() + "/Library/", False, "Allele Patterns")

  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  print "Pattern Sequences:"
  for num in range(0, numPatterns):
    print "PAT(%d): %s | %s" %(num+1, alleleIds[num], allelePatterns[num])
  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

  # Step 2: Load sample sequences and identify duplicates
  sampleIds, sampleSequences, totalSequences =  GetSequences(sampleFile, "fasta", os.getcwd() + "/Samples/", True, "Sample Sequences")

  # Step 3: Identify what pattern the sample sequence belongs
  numSamples = len(sampleIds)

  print "Total number of sequences (with duplicates)    : %d" %(totalSequences)
  print "Total number of sequences (with no duplicates) : %d" %(numSamples)
  print

  # Loop through all samples and determine it's allele pattern combination
  # [total, pattern, []]
  results = {}
  noMatch = []
  totalNoMatches = 0
  for num in range(0, numSamples):
    numberOfSequences = len(sampleIds[num].split(","))
    if GlobalVars.DEBUG:
      print sampleIds[num]
      #print "Seq #%d with %d sequence(s):" %(num + 1, numberOfSequences)

    patternMatch = DeterminePattern(sampleSequences[num], num, allelePatterns, numPatterns)
    if patternMatch != None:
      patternMatch = CombineSimilarPattern(patternMatch)

    if patternMatch != None:
      pattern = ""
      for index in range(0, len(patternMatch)):
        pattern += str(patternMatch[index][1].number + 1)

      if pattern not in results:
        results[pattern] = [numberOfSequences, [patternMatch]]
      else:
        results[pattern][0] += numberOfSequences
        results[pattern][1] += [patternMatch]
    else:
      totalNoMatches += numberOfSequences
      noMatch += [(sampleIds[num], sampleSequences[num])]

    if GlobalVars.DEBUG:
      if patternMatch == None:
        print "No Match\n"
      else:
        print "Matched!\n"

  sortedKeys = sorted(results, key=results.get, reverse=True)
  print "PATTERN   # SEQUENCES"
  for key in sortedKeys:
    print "%-7s   %d" %(key, results[key][0])
    WriteToFile(sampleFile.split('.')[0], key, results[key][1], sampleIds, sampleSequences)
  print

  noMatchLen = len(noMatch)
  if noMatchLen > 0:
    print "Total number of sequences (with no match) : %d" %(totalNoMatches)
    print
    WriteToFileNoMatches(sampleFile.split('.')[0], noMatch, sampleIds, sampleSequences)
    for index in range(0, noMatchLen):
      print "Seq %d: %s" %(index+1, noMatch[index][0])
      print "%s\n" %(noMatch[index][1])

if __name__ == '__main__':
  main(sys.argv[1:])
