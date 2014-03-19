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
  alleleIds, allelePatterns = GetSequences(patternFile, "fasta", os.getcwd() + "/Library/", False, "Allele Patterns")

  # Step 2: Load sample sequences and identify duplicates
  sampleIds, sampleSequences =  GetSequences(sampleFile, "fasta", os.getcwd() + "/Samples/", True, "Sample Sequences")

  # Step 3: Identify what pattern the sample sequence belongs
  numSamples = len(sampleIds)
  numPatterns = len(allelePatterns)

  # Loop through all samples and determine it's allele pattern combination
  for num in range(0, numSamples):
    if GlobalVars.DEBUG:
      print sampleIds[num]
    patternMatch = DeterminePattern(sampleSequences[num], allelePatterns, numPatterns)

    if GlobalVars.DEBUG:
      if patternMatch == None:
        print "No Match\n"
      else:
        print "Matched!\n"


if __name__ == '__main__':
  main(sys.argv[1:])
