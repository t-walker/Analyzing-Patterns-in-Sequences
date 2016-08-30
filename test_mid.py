from DataLibs import *
from DeterminePattern import SearchForSNPs
import GlobalVars

GlobalVars.DEBUG = True

def MidSimilarity(sample, sampleStartIndex, sampleEndIndex, pattern, patternNum):
  '''
  @desc:
  @return:
  '''
  sampleMidString = sample[sampleStartIndex:sampleEndIndex]
  sampleMidStringLen = len(sampleMidString)

  patternMatches = []
  sampleMatches = []
  print len(pattern) - 3 - sampleMidStringLen + 1
  #for i in range(3, len(pattern) - 3 - sampleMidStringLen + 1):
  for i in range(3, len(pattern) - sampleMidStringLen):
    patternTemp = pattern[i:i+sampleMidStringLen+1]
    print patternTemp
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
    if GlobalVars.DEBUG:
      snippet = sampleMatches[index].snippets
      if 0 < len(snippet):
        snippetString = ListToString(snippet, ",", True)
        print "M :%s PAT(%i) SNP(%s)" %(" " * sampleMatches[index].startIndex + pattern[patternMatches[index].startIndex:patternMatches[index].endIndex], patternNum+1, snippetString)
      else:
        print "M :%s PAT(%i)" %(" " * sampleMatches[index].startIndex + pattern[patternMatches[index].startIndex:patternMatches[index].endIndex], patternNum+1)
  return patternMatches, sampleMatches
#end MidSimilarity()




sample = "KWGNAVENATNGDKVSQNVCKGTTSGNQCGVNATSGSTNNGKLSTVFNTDGAEAISSMDTTASGTSNTISLQGMA"
print sample
sampleStartIndex = 0
sampleEndIndex = len(sample) - 1
patterns = [0] * 5
patterns[0] = "KMTKGEAKKWGNAVENATNGDKVSQNVCKGTGSTGSSGNKCGTTDSTATTKISAVFTEDAAAQLSTMDNTTINTTGMANNINSL"
patterns[1] = "KMTKSEAKKWGNAIESATGTTSGDELSKKVCGKGEGSNGTKKCGTTDSTATTKISEVFTEGTDTLLSVEGNKDTINLQGMANNINNL"
patterns[2] = "KMTKSEAKKWGNAIESATGTTNGEKVSQKVCGNGTGSSGTQCGKNSGDTNGSSTTQHKISAVFTDEATLLSAAGDTINTTGMAGNINSL"
patterns[3] = "KMTKGEAKKWGTTVEAATNGQTVSQKVCGNGTGSSGSNCGKNTTDSTNNNGKITQAFTADSDTTLLSAESSNISTSGMATNINGL"
patterns[4] = "KMTKSEAKKWGNAIESATGTTSGDELSKKVCGKGTTSGNQCGVNATSGSTNNGKLSTVFNTDGAEAISSMDTTASGTSNTISLQGMAGNINSL"

for patternNum in range(5):
  pattern = patterns[patternNum]
  MidSimilarity(sample, sampleStartIndex, sampleEndIndex, pattern, patternNum)

