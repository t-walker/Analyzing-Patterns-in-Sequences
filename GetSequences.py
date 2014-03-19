#!/usr/bin/python -tt
'''
Create on January 2, 2014

@author: Gabriel de la Cruz
'''

# [BioPython] third party modules use to manipulate sequence files
from Bio import SeqIO

import GlobalVars


def GetSequences(fileName="", fileType="fasta", path="", noDuplicates=False, name=""):

  ctr = 0          # counter
  seqIds = []      # allele pattern's id names
  sequences = []   # allele pattern's amino acid sequences


  if GlobalVars.DEBUG:
    print "[%s]" %(name)

  # Parse through the file, normally a fasta file
  # and retrive all sequences
  for seq_record in SeqIO.parse(path + fileName, fileType):

    if GlobalVars.DEBUG:
      print "Seq %i:" %(ctr + 1), seq_record.id, str(seq_record.seq)

    # Duplicates accepted
    if not noDuplicates:
      seqIds.insert(ctr, seq_record.id)
      sequences.insert(ctr, str(seq_record.seq))

    # No Duplicates  
    else:
      isAdded = False  # flag variable to check whether sequence has been added

      # loop through the parsed sequences to check if current sequence exist
      for i in range(0, len(seqIds)):
        if str(seq_record.seq) == sequences[i]:
          seqIds[i] = seqIds[i] + ',' + seq_record.id
          isAdded = True
          break

      if not isAdded:
        seqIds.insert(ctr, seq_record.id)
        sequences.insert(ctr, str(seq_record.seq))

    ctr += 1

  if GlobalVars.DEBUG:
    print

  if noDuplicates and GlobalVars.DEBUG:
    print "[%s - No Duplicates]" %(name)

    for i in range(0, len(seqIds)):
      print "Seq %i:" %(i + 1), seqIds[i], sequences[i]
    print

  return seqIds, sequences
# end GetSequences()
