#!/usr/bin/python -tt
'''
Create on January 5, 2014

@author: Gabriel de la Cruz

'''

import GlobalVars
from DataLibs import *

def DeterminePattern(sample, sampleNum, allelePatterns, numPatterns):
  '''
  @desc: Determine the pattern of the sample
  @return:
  '''
  if GlobalVars.DEBUG:
    print "S :%s" %(sample)

  sampleLength = len(sample)

  # Determine if sample sequence is exactly equal to any of the patterns
  patternIndex = SampleIsAPattern(sample, allelePatterns)
  if 0 <= patternIndex:
    sampleMatch = Sample(0, len(sample) - 1, sampleNum)
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
    if F_sampleMatch != None:
      F_sampleMatch.number = sampleNum

    # Front match with the pattern with SNP
    if F_patternMatch != None and F_patternMatch.size == sampleLength:
      if GlobalVars.DEBUG:
        snippetString = ListToString(F_sampleMatch.snippets, ",", True)
        print "P*:%s PAT(%i)" %(allelePatterns[num][F_patternMatch.startIndex:F_patternMatch.endIndex], num+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print
      return [(F_sampleMatch, F_patternMatch)]

    # Identify pattern of the end part of the sample
    E_sampleMatch, E_patternMatch = EndSimilarity(sample, allelePatterns[num], num)
    if E_sampleMatch != None:
      E_sampleMatch.number = sampleNum

    if F_patternMatch != None and E_patternMatch != None:
      # Front and end match with the same pattern
      if F_patternMatch.size + E_patternMatch.size > sampleLength:
        if GlobalVars.DEBUG:
          snippetString = ListToString(F_sampleMatch.snippets, ",", True)
          print "F*:%s PAT(%i)" %(allelePatterns[num][F_patternMatch.startIndex:F_patternMatch.endIndex], num+1),
          if snippetString != "":
            print "SNP(%s)" %(snippetString)
          else:
            print
          snippetString = ListToString(E_sampleMatch.snippets, ",", True)
          print "E*:%s PAT(%i)" %(" " * (E_sampleMatch.startIndex) + allelePatterns[num][E_patternMatch.startIndex:E_patternMatch.endIndex], num+1),
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
        print "F*:%s PAT(%i)" %(allelePatterns[F_max_patternMatch.number][F_max_patternMatch.startIndex:F_max_patternMatch.endIndex], F_max_patternMatch.number+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print
        snippetString = ListToString(E_max_sampleMatch.snippets, ",", True)
        print "E*:%s PAT(%i)" %(" " * (E_max_sampleMatch.startIndex) + allelePatterns[E_max_patternMatch.number][E_max_patternMatch.startIndex:E_max_patternMatch.endIndex], E_max_patternMatch.number+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print
      return [(F_max_sampleMatch, F_max_patternMatch), (E_max_sampleMatch, E_max_patternMatch)]


  # Need to find match in the middle part
  if F_max_patternMatch == None or E_max_patternMatch == None:

    all_patternMatches = []
    all_sampleMatches = []
    returnList = []
    if F_max_patternMatch != None:
      returnList = [(F_max_sampleMatch, F_max_patternMatch)]

    if GlobalVars.DEBUG and F_max_sampleMatch != None:
      snippetString = ListToString(F_max_sampleMatch.snippets, ",", True)
      print "F*:%s PAT(%i)" %(allelePatterns[F_max_patternMatch.number][F_max_patternMatch.startIndex:F_max_patternMatch.endIndex], F_max_patternMatch.number+1),
      if snippetString != "":
        print "SNP(%s)" %(snippetString)
      else:
        print

    for num in range(0, numPatterns):
      # fron has match and end has match:
      if F_max_patternMatch != None and E_max_patternMatch != None:
        patternMatches, sampleMatches = MidSimilarity(sample, F_max_sampleMatch.endIndex-1, E_max_sampleMatch.startIndex+1, allelePatterns[num], num)
      # front has match but no match on end
      if F_max_patternMatch != None and E_max_patternMatch == None:
        # NEW CHANGES
        patternMatches, sampleMatches = MidSimilarity(sample, F_max_sampleMatch.endIndex-1, sampleLength-1, allelePatterns[num], num)
        #return None # TEMPORARY
      # front has no match but end has match
      elif F_max_patternMatch == None and E_max_patternMatch != None:
        # NEW CHANGES
        patternMatches, sampleMatches = MidSimilarity(sample, 0, E_max_sampleMatch.startIndex+1, allelePatterns[num], num)
        #return None # TEMPORARY
      else:
        patternMatches, sampleMatches = MidSimilarity(sample, 0, sampleLength-1, allelePatterns[num], num)
      #patternMatches, sampleMatches = MidSimilarity(sample, F_max_sampleMatch.endIndex-1, E_max_sampleMatch.startIndex+1, allelePatterns[num], num)
      for index in range (0, len(patternMatches)):
        if patternMatches[index] not in all_patternMatches:
          all_patternMatches.append(patternMatches[index])
          sampleMatches[index].number = sampleNum
          all_sampleMatches.append(sampleMatches[index])

    # remove patterns with the same length hitting on same part of the sample
    for outer_index in range(0, len(all_sampleMatches)):
      isDuplicate = False
      if all_sampleMatches[outer_index].startIndex == -1:
        continue
      for inner_index in range(0, len(all_sampleMatches)):
        if inner_index == outer_index:
          continue
        if all_sampleMatches[outer_index].startIndex == all_sampleMatches[inner_index].startIndex and \
           all_sampleMatches[outer_index].endIndex == all_sampleMatches[inner_index].endIndex:
          isDuplicate = True
          all_sampleMatches[inner_index].number = -1
        # this remove a pattern that is within another pattern that is bigger
        elif all_sampleMatches[outer_index].startIndex <= all_sampleMatches[inner_index].startIndex and \
             all_sampleMatches[outer_index].endIndex >= all_sampleMatches[inner_index].endIndex:
          all_sampleMatches[inner_index].number = -1
      if isDuplicate:
          all_sampleMatches[outer_index].number = -1

    index = len(all_sampleMatches) - 1
    while index >= 0:
      if all_sampleMatches[index].number == -1:
        del all_sampleMatches[index]
        del all_patternMatches[index]
      index = index - 1
      if index < 0:
        break

    hasNoMatch = False
    if len(all_patternMatches) > 0:
      if F_max_sampleMatch == None:
        startConvergeIndex = 0
      else:
        startConvergeIndex = F_max_sampleMatch.endIndex - 1
      if E_max_sampleMatch == None:
        endConvergeIndex = sampleLength - 1
      else:
        endConvergeIndex = E_max_sampleMatch.startIndex

      while startConvergeIndex < endConvergeIndex:
        M_max_sampleMatch = Sample(-1, -1, sampleNum)
        M_max_patternMatch = Pattern(-1, -1)

        for index in range(0, len(all_sampleMatches)):
          if (startConvergeIndex >= all_sampleMatches[index].startIndex) and (startConvergeIndex < all_sampleMatches[index].endIndex):
            if M_max_patternMatch.size < all_patternMatches[index].size:
              M_max_patternMatch = all_patternMatches[index]
              M_max_sampleMatch = all_sampleMatches[index]

        if M_max_patternMatch.size != 0:
          del_index = all_patternMatches.index(M_max_patternMatch)
          del all_patternMatches[del_index]
          del all_sampleMatches[del_index]

          returnList += [(M_max_sampleMatch, M_max_patternMatch)]
          startConvergeIndex = M_max_sampleMatch.endIndex - 1

          if GlobalVars.DEBUG:
            snippetString = ListToString(M_max_sampleMatch.snippets, ",", True)
            print "M*:%s PAT(%i)" %(" " * (M_max_sampleMatch.startIndex) + allelePatterns[M_max_patternMatch.number][M_max_patternMatch.startIndex:M_max_patternMatch.endIndex], M_max_patternMatch.number+1),
            if snippetString != "":
              print "SNP(%s)" %(snippetString)
            else:
              print
        else:
          hasNoMatch = True
          break

      if GlobalVars.DEBUG and E_max_sampleMatch != None:
        snippetString = ListToString(E_max_sampleMatch.snippets, ",", True)
        print "E*:%s PAT(%i)" %(" " * (E_max_sampleMatch.startIndex) + allelePatterns[E_max_patternMatch.number][E_max_patternMatch.startIndex:E_max_patternMatch.endIndex], E_max_patternMatch.number+1),
        if snippetString != "":
          print "SNP(%s)" %(snippetString)
        else:
          print

      if not hasNoMatch:
        if E_max_patternMatch != None:
          returnList += [(E_max_sampleMatch, E_max_patternMatch)]
        return returnList

##    if GlobalVars.DEBUG:
##      snippetString = ListToString(E_max_sampleMatch.snippets, ",", True)
##      print "E*:%s PAT(%i)" %(" " * (E_max_sampleMatch.startIndex) + allelePatterns[E_max_patternMatch.number][E_max_patternMatch.startIndex:E_max_patternMatch.endIndex], E_max_patternMatch.number+1),
##      if snippetString != "":
##        print "SNP(%s)" %(snippetString)
##      else:
##        print

  # No match
  return None

#end DeterminePattern()


def SearchForSNPs(sample, sampleClass, pattern, patternClass):
  '''
  @desc:
  @return:
  '''

  S_startIndex = sampleClass.startIndex - 1
  P_startIndex = patternClass.startIndex - 1
  S_endIndex = sampleClass.endIndex
  P_endIndex = patternClass.endIndex

  # Search towards FRONT
  snippet = []
  count = len(sampleClass.snippets)
  prevMatch = True

  while True:
    if sample[S_startIndex] == pattern[P_startIndex]:
      P_startIndex -= 1
      S_startIndex -= 1
      prevMatch = True
    # this elif allows to have snippet in the pattern
    elif True == prevMatch:
      snippet.append(S_startIndex)
      S_startIndex -= 1
      P_startIndex -= 1
      prevMatch = False
    else:
      # idenfity starting index of match pattern
      if True == prevMatch:
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
          S_startIndex += 2
          P_startIndex += 2

      break

  sampleClass.snippets += snippet

  # Search towards END
  snippet = []
  count = len(sampleClass.snippets)
  prevMatch = True

  while True:

    if sample[S_endIndex] == pattern[P_endIndex]:
      P_endIndex += 1
      S_endIndex += 1
      prevMatch = True
    # this elif allows to have snippet in the pattern
    elif True == prevMatch:
      snippet.append(S_endIndex)
      P_endIndex += 1
      S_endIndex += 1
      prevMatch = False
    else:
      # idenfity starting index of match pattern
      if True == prevMatch:
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
          P_endIndex -= 1
          S_endIndex -= 1
      break

    if S_endIndex == len(sample):
      if False == prevMatch:
        if len(snippet):
          snippet.pop()
          P_endIndex -= 1
          S_endIndex -= 1
      break

  sampleClass.startIndex = S_startIndex
  sampleClass.endIndex = S_endIndex
  sampleClass.size = S_endIndex - S_startIndex
  sampleClass.snippets += snippet

  patternClass.startIndex = P_startIndex
  patternClass.endIndex = P_endIndex
  patternClass.size = P_endIndex - P_startIndex

  return patternClass, sampleClass

#end SearchForSNPs()


def MidSimilarity(sample, sampleStartIndex, sampleEndIndex, pattern, patternNum):
  '''
  @desc:
  @return:
  '''
  sampleMidString = sample[sampleStartIndex:sampleEndIndex]
  sampleMidStringLen = len(sampleMidString)

  patternMatches = []
  sampleMatches = []

  for i in range(3, len(pattern) - 3 - sampleMidStringLen + 1):
    patternTemp = pattern[i:i+sampleMidStringLen]

    patternMatch = None
    sampleMatch = None
    snippet = []
    P_startIndex = -1
    P_endIndex = -1
    S_startIndex = -1
    S_endIndex = -1

    countSimilarity = 0
    snippetCount = 0
    addOne = False
    prevMatch = False

    for index in range(0, sampleMidStringLen):
      if sampleMidString[index] == patternTemp[index]:
        prevMatch = True
        if P_startIndex == -1:
          P_startIndex = index + i
          S_startIndex = sampleStartIndex + index
        countSimilarity += 1
        if len(snippet) == 1 and prevMatch == False:
          addOne = True
        if (index + 1) == sampleMidStringLen:
          if addOne:
            countSimilarity += 1
          if countSimilarity >= 2:
            P_endIndex = index + i + 1
            patternMatch = Pattern(patternNum, P_startIndex, P_endIndex)
            sampleMatch = Sample(S_startIndex, S_startIndex + patternMatch.size)
            sampleMatch.snippets = snippet
            patternMatches.append(patternMatch)
            sampleMatches.append(sampleMatch)
          snippetCount = 0
          countSimilarity = 0
          patternMatch = Pattern(patternNum)
          snippet = []
          P_startIndex = -1
          P_endIndex = -1
          prevMatch = False
      else:
        if P_startIndex != -1:
          if prevMatch == True and len(snippet) == 0:
            snippet.append(sampleStartIndex + index)
            prevMatch = False
          else:
            if addOne:
              countSimilarity += 1
              addOne = False
            if countSimilarity >= 2:
              if (sampleStartIndex + index - 1) == snippet[-1]:
                P_endIndex = index + i - 1
                snippet = []
              else:
                P_endIndex = index + i
              patternMatch = Pattern(patternNum, P_startIndex, P_endIndex)
              sampleMatch = Sample(S_startIndex, S_startIndex + patternMatch.size)
              sampleMatch.snippets = snippet
              patternMatches.append(patternMatch)
              sampleMatches.append(sampleMatch)
            snippetCount = 0
            countSimilarity = 0
            patternMatch = Pattern(patternNum)
            snippet = []
            P_startIndex = -1
            P_endIndex = -1
            prevMatch = False

  for index in range(0, len(patternMatches)):
    patternMatches[index], sampleMatches[index] = SearchForSNPs(sample, sampleMatches[index], pattern, patternMatches[index])
    #if GlobalVars.DEBUG:
      #snippet = sampleMatches[index].snippets
      #if 0 < len(snippet):
        #snippetString = ListToString(snippet, ",", True)
        #print "M :%s PAT(%i) SNP(%s)" %(" " * sampleMatches[index].startIndex + pattern[patternMatches[index].startIndex:patternMatches[index].endIndex], patternNum+1, snippetString)
      #else:
        #print "M :%s PAT(%i)" %(" " * sampleMatches[index].startIndex + pattern[patternMatches[index].startIndex:patternMatches[index].endIndex], patternNum+1)

  return patternMatches, sampleMatches
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
        print "P*:%s PAT(%i)" %(sample, index+1)
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

  noMismatch = [True] * patternLen # CAN BE REMOVED
  prevMatch = True

  startIndex = 0
  endIndex = 0
  snippet = []

  patternMatch = None
  sampleMatch = None
  #isAddOne = False

  # loop matching pattern to sample starting at the start index
  while endIndex < sampleLen and endIndex < patternLen:
    if sample[endIndex] == pattern[endIndex]:
      endIndex += 1
      prevMatch = True
      #isAddOne = True
    # this elif allows to have snippet in the pattern
    elif True == prevMatch and len(noMismatch):
      noMismatch.pop()
      snippet.append(endIndex)
      endIndex += 1
      prevMatch = False
    else:
      # identify ending index of match pattern
      if True == prevMatch:
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
          endIndex -= 1
      #isAddOne = False
      break
  # Disregard if number of similarities is < miminum length
  if (endIndex - startIndex) < GlobalVars.MIN_LEN:
    return sampleMatch, patternMatch
  else:
    sampleMatch = Sample(startIndex, endIndex)
    patternMatch = Pattern(patternNum, startIndex, endIndex)
    sampleMatch.snippets = snippet

##  if GlobalVars.DEBUG:
##    if 0 < len(snippet):
##      snippetString = ListToString(snippet, ",", True)
##      print "F :%s PAT(%i) SNP(%s)" %(pattern[startIndex:endIndex], patternNum+1, snippetString)
##    else:
##      print "F :%s PAT(%i)" %(pattern[startIndex:endIndex], patternNum+1)

  return sampleMatch, patternMatch

#end FrontSimilarity()


def EndSimilarity(sample, pattern, patternNum):
  '''
  @desc: Determine the pattern of the end portion of the sample
  @return:
  '''
  sampleLen = len(sample)
  patternLen = len(pattern)

  noMismatch = [True] * patternLen # CAN BE REMOVED
  prevMatch = True

  startIndexP = patternLen - 1
  endIndexP = patternLen
  startIndexS = sampleLen - 1
  endIndexS = sampleLen
  snippet = []

  patternMatch = None
  sampleMatch = None

  # loop matching pattern to sample starting at the end index
  for sampleIndex in range(0, sampleLen):
    if sample[startIndexS] == pattern[startIndexP]:
      startIndexS -= 1
      startIndexP -= 1
      prevMatch = True
    # this elif allows to have snippet in the pattern
    elif True == prevMatch and len(noMismatch):
      noMismatch.pop()
      snippet.append(startIndexS)
      startIndexS -= 1
      startIndexP -= 1
      prevMatch = False
    else:
      # idenfity starting index of match pattern
      if True == prevMatch:
        prevMatch = False
      else:
        if len(snippet):
          snippet.pop()
          startIndexP += 2
          startIndexS += 2
      break

  # Disregard if number of similarities is < miminum length
  if (endIndexP - startIndexP) < GlobalVars.MIN_LEN:
    return sampleMatch, patternMatch
  else:
    sampleMatch = Sample((startIndexS), endIndexS)
    patternMatch = Pattern(patternNum, startIndexP, endIndexP)
    sampleMatch.snippets = snippet

##  if GlobalVars.DEBUG:
##    # Compute for aligning string of the pattern
##    temp = " " * startIndexS
##
##    if 0 < len(snippet):
##      snippetString = ListToString(snippet, ",", True)
##      print "E :%s PAT(%i) SNP(%s)" %(temp+pattern[startIndexP:endIndexP], patternNum+1, snippetString)
##    else:
##      print "E :%s PAT(%i)" %(temp+pattern[startIndexP:endIndexP], patternNum+1)

  return sampleMatch, patternMatch

#end EndSimilarity()
