#!/usr/bin/python -tt
# python seq_identifier.py -p pseudogenes_aminoacidsHVR_5.fa -s MS_1376Translations.fa -d
import os
import sys
import getopt


import GlobalVars

from DataLibs import *
from GetSequences import GetSequences
from DeterminePattern import DeterminePattern


def usage():
  print 'seq_identifier.py -p <patternFile> -s <sampleFile>'

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
  for num in range(0, numSamples):
    if GlobalVars.DEBUG:
      print sampleIds[num]

    patternMatch = DeterminePattern(sampleSequences[num], allelePatterns, numPatterns)
    numberOfSequences = len(sampleIds[num].split(","))

    if patternMatch != None:
      pattern = ""
      for index in range(0, len(patternMatch)):
        pattern += str(patternMatch[index][1].number + 1)

      if pattern not in results:
        results[pattern] = [numberOfSequences, patternMatch]
      else:
        results[pattern][0] += numberOfSequences
        results[pattern][1] += patternMatch
    else:
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

  print

  noMatchLen = len(noMatch)
  if noMatchLen > 0:
    print "Total number of sequences (with no match) : %d" %(noMatchLen)
    print
    for index in range(0, noMatchLen):
      print "Seq %d: %s" %(index+1, noMatch[index][0])
      print "%s\n" %(noMatch[index][1])

if __name__ == '__main__':
  main(sys.argv[1:])
