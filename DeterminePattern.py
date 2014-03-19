#!/usr/bin/python -tt
'''
Create on January 5, 2014

@author: Gabriel de la Cruz

TODO: When printing match sample/pattern, should show the SNPs from pattern

'''

import GlobalVars
from DataLibs import *

def DeterminePattern(sample, allelePatterns, numPatterns):
  '''
  @desc: Determine the pattern of the sample
  @return:
  '''
  if GlobalVars.DEBUG:
    print "S:%s" %(sample)

  sampleLength = len(sample)

  # Determine if sample sequence is exactly equal to any of the patterns
  patternIndex = SampleIsAPattern(sample, allelePatterns)
  if 0 <= patternIndex:
    sampleMatch = Sample(0, len(sample) - 1)
    patternMatch = Pattern(patternIndex, 0, sampleLength)
    return [(sampleMatch, patternMatch)]

  F_max_size = 0
  E_max_size = 0
  F_max_sampleMatch = None
  F_max_patternMatch = None
  E_max_sampleMatch = None
  E_max_patternMatch = None
  # Loop through the allele patterns and identify the sample's pattern
  for num in range(0, numPatterns):
    # Identify pattern of the front part of the sample
    F_sampleMatch, F_patternMatch = FrontSimilarity(sample, allelePatterns[num], num)
    # Identify pattern of the end part of the sample
    E_sampleMatch, E_patternMatch = EndSimilarity(sample, allelePatterns[num], num)

    if F_patternMatch != None and E_patternMatch != None:
      # Front and end match with the same pattern
      if F_patternMatch.size + E_patternMatch.size > sampleLength:
        if GlobalVars.DEBUG:
          snippetString = ListToString(F_sampleMatch.snippets, ",", True)
          print "F:%s PAT(%i)" %(allelePatterns[num][F_patternMatch.startIndex:F_patternMatch.endIndex], num+1),
          if snippetString != "":
            print "SNP(%s)" %(snippetString)
          else:
            print
          snippetString = ListToString(E_sampleMatch.snippets, ",", True)
          print "E:%s PAT(%i)" %(" " * (E_patternMatch.startIndex) + allelePatterns[num][E_patternMatch.startIndex:E_patternMatch.endIndex], num+1),
          if snippetString != "":
            print "SNP(%s)" %(snippetString)
          else:
            print
        return [(F_sampleMatch, F_patternMatch), (E_sampleMatch, E_patternMatch)]

    # (Front) F_patternMatch found
    if F_patternMatch != None:
      if F_patternMatch.size > F_max_size:
        F_max_size = F_patternMatch.size
        F_max_patternMatch = F_patternMatch
        F_max_sampleMatch = F_sampleMatch

    # (End) E_patternMatch found
    if E_patternMatch != None:
      if E_patternMatch.size > E_max_size:
        E_max_size = E_patternMatch.size
        E_max_patternMatch = E_patternMatch
        E_max_sampleMatch = E_sampleMatch


  # Match but from different patterns
  if F_max_patternMatch != None and E_max_patternMatch != None:

    # Front and end match from different patterns
    if F_max_patternMatch.size + E_max_patternMatch.size > sampleLength:
      if GlobalVars.DEBUG:
        snippetString = ListToString(F_max_sampleMatch.snippets, ",", True)
        print "F:%s PAT(%i)" %(allelePatterns[F_max_patternMatch.number][F_max_patternMatch.startIndex:F_max_patternMatch.endIndex], F_max_patternMatch.number+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print
        snippetString = ListToString(E_max_sampleMatch.snippets, ",", True)
        print "E:%s PAT(%i)" %(" " * (E_max_sampleMatch.startIndex) + allelePatterns[E_max_patternMatch.number][E_max_patternMatch.startIndex:E_max_patternMatch.endIndex], E_max_patternMatch.number+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print
      return [(F_max_sampleMatch, F_max_patternMatch), (E_max_sampleMatch, E_max_patternMatch)]

    # Need to find match in the middle part
    M_max_sampleMatch = Sample(F_max_sampleMatch.endIndex-1, E_max_sampleMatch.startIndex+1)
    M_max_patternMatch = Pattern(-1, 0)
    for num in range(0, numPatterns):
      patternMatches, snippets = MidSimilarity(sample, F_max_sampleMatch.endIndex-1, E_max_sampleMatch.startIndex+1, allelePatterns[num], num)

      if patternMatches != None:
        for index in range(0, len(patternMatches)):
          if M_max_sampleMatch.size == patternMatches[index].size:
            pattern = allelePatterns[num]
            startIndex = patternMatches[index].startIndex
            endIndex = patternMatches[index].endIndex

            M_max_patternMatch = patternMatches[index]
            M_max_sampleMatch.snippets = snippets[index]
            
            if GlobalVars.DEBUG:
              snippetString = ListToString(F_max_sampleMatch.snippets, ",", True)
              print "F:%s PAT(%i)" %(allelePatterns[F_max_patternMatch.number][F_max_patternMatch.startIndex:F_max_patternMatch.endIndex], F_max_patternMatch.number+1),
              if snippetString != "":
                print "SNP(%s)" %(snippetString)
              else:
                print
              snippetString = ListToString(M_max_sampleMatch.snippets, ",", True)
              print "M:%s PAT(%i)" %(" " * (M_max_sampleMatch.startIndex) + allelePatterns[M_max_patternMatch.number][M_max_patternMatch.startIndex:M_max_patternMatch.endIndex], M_max_patternMatch.number+1),
              if snippetString != "":
                print "SNP(%s)" %(snippetString)
              else:
                print
              snippetString = ListToString(E_max_sampleMatch.snippets, ",", True)
              print "E:%s PAT(%i)" %(" " * (E_max_sampleMatch.startIndex) + allelePatterns[E_max_patternMatch.number][E_max_patternMatch.startIndex:E_max_patternMatch.endIndex], E_max_patternMatch.number+1),
              if snippetString != "":
                print "SNP(%s)" %(snippetString)
              else:
                print
                
            return [(F_max_sampleMatch, F_max_patternMatch), (M_max_sampleMatch, M_max_patternMatch), (E_max_sampleMatch, E_max_patternMatch)]
              
          
  # No match
  return None

#end DeterminePattern()


def MidSimilarity(sample, sampleStartIndex, sampleEndIndex, pattern, patternNum):
  '''
  @desc:
  @return:
  '''
  sampleMidString = sample[sampleStartIndex:sampleEndIndex]
  sampleMidStringLen = len(sampleMidString)

  patternMatches = []
  snippets = []

  for i in range(3, len(pattern) - 3 - sampleMidStringLen + 1):
    patternTemp = pattern[i:i+sampleMidStringLen]

    patternMatch = None
    snippet = []
    startIndex = -1
    endIndex = -1

    countSimilarity = 0
    snippetCount = 0
    #tempString = ""
    addOne = False

    for index in range(0, sampleMidStringLen):
      if sampleMidString[index] == patternTemp[index]:
        if startIndex == -1:
          startIndex = index + i
        countSimilarity += 1
        #tempString += sampleMidString[index]
        if len(snippet) == 1:
          addOne = True
        if (index + 1) == sampleMidStringLen:
          if addOne:
            countSimilarity += 1
          if countSimilarity >= 4:
            endIndex = index + i + 1
            patternMatch = Pattern(patternNum, startIndex, endIndex)
            patternMatches.append(patternMatch)
            snippets.append(snippet)
            if GlobalVars.DEBUG:
              if 0 < len(snippet):
                snippetString = ListToString(snippet, ",", True)
                print "%s PAT(%i) SNP(%s)" %(pattern[patternMatch.startIndex:patternMatch.endIndex], patternNum+1, snippetString)
              else:
                print "%s PAT(%i)" %(pattern[patternMatch.startIndex:patternMatch.endIndex], patternNum+1)
##              #print tempString
      else:
        if startIndex != -1:
          #snippetCount += 1
          if len(snippet) == 0:
            snippet.append(sampleStartIndex + index)
            #tempString += '*'
          else:
            if addOne:
              countSimilarity += 1
              addOne = False
            if countSimilarity >= 4:
              if (index + i) == snippet[-1]:
                endIndex = index + i - 2
                #tempString = tempString[0:-2]
                snippet = []
              else:
                endIndex = index + i
              patternMatch = Pattern(patternNum, startIndex, endIndex)
              patternMatches.append(patternMatch)
              snippets.append(snippet)
              if GlobalVars.DEBUG:
                if 0 < len(snippet):
                  snippetString = ListToString(snippet, ",", True)
                  print "%s PAT(%i) SNP(%s)" %(pattern[patternMatch.startIndex:patternMatch.endIndex], patternNum+1, snippetString)
                else:
                  print "%s PAT(%i)" %(pattern[patternMatch.startIndex:patternMatch.endIndex], patternNum+1)
##                #print tempString
            snippetCount = 0
            #tempString = ""
            countSimilarity = 0
            patternMatch = Pattern(patternNum)
            snippet = []
            startIndex = -1
            endIndex = -1
            
  if len(patternMatches) == 0:
    return None, None
  else:
    return patternMatches, snippets
#end MidSimilarity()


def SampleIsAPattern(sample, allelePatterns):
  '''
  @desc: Finds the index of the sample in the list if exist, and
         throws an error if sample cannot be found in the list
  @return: the index if sample found, otherwise returns -1
  '''
  while True:
    try:
      index = allelePatterns.index(sample)
      if GlobalVars.DEBUG:
        print "P:%s PAT(%i)" %(sample, index+1)
      return index
    except ValueError:
      return -1

#end SampleIsAPattern()


def FrontSimilarity(sample, pattern, patternNum):
  '''
  @desc: Determine the pattern of the front portion of the sample
  @return:
  '''
  sampleLen = len(sample)
  patternLen = len(pattern)

  #noMismatch = True
  noMismatch = [True, True]
  prevMatch = False

  startIndex = -1
  endIndex = -1
  snippet = []

  patternMatch = None
  sampleMatch = None

  # loop matching pattern to sample starting at the start index
  for sampleIndex in range(0, sampleLen):
    if sample[sampleIndex] == pattern[sampleIndex]:
      if 0 == sampleIndex:
        # identify starting index of match pattern
        startIndex = 0
      endIndex = sampleIndex
      prevMatch = True
    # this elif allows to have one snippet in the pattern
    #elif True == noMismatch:
    elif True == prevMatch and len(noMismatch):
      noMismatch.pop()
      #endIndex = sampleIndex - 1
      endIndex = sampleIndex # CHANGE HERE
      snippet.append(sampleIndex)
      #noMismatch = False
      prevMatch = False
    else:
      # identify ending index of match pattern
      if True == prevMatch:
        #endIndex = sampleIndex - 1
        endIndex = sampleIndex # CHANGE HERE
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
      break

  # Disregard if number of similarities is < miminum length
  if (endIndex - startIndex) + 1 < GlobalVars.MIN_LEN:
    return sampleMatch, patternMatch
  else:
    # both sample and pattern indices are the same
    sampleMatch = Sample(startIndex, endIndex)
    patternMatch = Pattern(patternNum, startIndex, endIndex)
    sampleMatch.snippets = snippet

  if GlobalVars.DEBUG:
    if 0 < len(snippet):
      snippetString = ListToString(snippet, ",", True)
      print "F:%s PAT(%i) SNP(%s)" %(pattern[startIndex:endIndex], patternNum+1, snippetString)
    else:
      print "F:%s PAT(%i)" %(pattern[startIndex:endIndex], patternNum+1)

  return sampleMatch, patternMatch

#end FrontSimilarity()


def EndSimilarity(sample, pattern, patternNum):
  '''
  @desc: Determine the pattern of the end portion of the sample
  @return:
  '''
  sampleLen = len(sample)
  patternLen = len(pattern)

  #noMismatch = True
  noMismatch = [True, True]
  prevMatch = False

  startIndexP = -1
  endIndexP = -1
  startIndexS = -1
  endIndexS = -1
  snippet = []

  patternMatch = None
  sampleMatch = None

  # loop matching pattern to sample starting at the end index
  for sampleIndex in range(0, sampleLen):
    idx = (sampleIndex + 1) * -1
    if sample[idx] == pattern[idx]:
      if -1 == idx:
        # identify ending index of match pattern
        #endIndexP = endIndexS = patternLen - 1
        endIndexP = endIndexS = patternLen # CHANGE HERE

      prevMatch = True
    # this elif allows to have one snippet in the pattern
    #elif True == noMismatch:
    elif True == prevMatch and len(noMismatch):
      noMismatch.pop()
      startIndexP = (patternLen + idx) + 1
      startIndexS = (sampleLen + idx) + 1
      snippet.append(startIndexS - 1)
      #noMismatch = False
      prevMatch = False
    else:
      # idenfity starting index of match pattern
      if True == prevMatch:
        startIndexP = (patternLen + 1) + idx
        startIndexS = (sampleLen + 1) + idx
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
      break

  # Disregard if number of similarities is < miminum length
  if (endIndexP - startIndexP) + 1  < GlobalVars.MIN_LEN:
    return sampleMatch, patternMatch
  else:
    sampleMatch = Sample((startIndexS), endIndexS)
    patternMatch = Pattern(patternNum, startIndexP, endIndexP)
    sampleMatch.snippets = snippet

  if GlobalVars.DEBUG:
    # Compute for aligning string of the pattern
    temp = " " * startIndexS

    if 0 < len(snippet):
      snippetString = ListToString(snippet, ",", True)
      print "E:%s PAT(%i) SNP(%s)" %(temp+pattern[startIndexP:endIndexP], patternNum+1, snippetString)
    else:
      print "E:%s PAT(%i)" %(temp+pattern[startIndexP:endIndexP], patternNum+1)

  return sampleMatch, patternMatch

#end EndSimilarity()

