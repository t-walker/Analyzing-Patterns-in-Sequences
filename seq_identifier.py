#!/usr/bin/python -tt
# python seq_identifier.py -p Allels_Trimv2.fa -s MS_1376Translations.fa -d
import os
import sys
import getopt


import GlobalVars

from GetSequences import GetSequences
from DeterminePattern import DeterminePattern
from AssembleFASTAFiles import WriteToFile, WriteToFileNoMatches
from xhtml2pdf import pisa


html="""
<head>
  <style type="text/css">
    .A {
      color: hotpink;
      font-family: monospace;
      font-size: 10px;
    }
    .B {
      color: olivedrab;
      font-family: monospace;
      font-size: 10px;
    }
    .C {
      color: orchid;
      font-family: monospace;
      font-size: 10px;
    }
    .D {
      color: mediumvioletred;
      font-family: monospace;
      font-size: 10px;
    }
    .E {
      color: lightseagreen;
      font-family: monospace;
      font-size: 10px;
    }
    .F {
      color: indigo;
      font-family: monospace;
      font-size: 10px;
    }
    .G {
      color: lightcoral;
      font-family: monospace;
      font-size: 10px;
    }
    .H {
      color: red;
      font-family: monospace;
      font-size: 10px;
    }
    .I {
      color: orangered;
      font-family: monospace;
      font-size: 10px;
    }
    .K {
      color: steelblue;
      font-family: monospace;
      font-size: 10px;
    }
    .L {
      color: red;
      font-family: monospace;
      font-size: 10px;
    }
    .M {
      color: green;
      font-family: monospace;
      font-size: 10px;
    }
    .N {
      color: blue;
      font-family: monospace;
      font-size: 10px;
    }
    .P {
      color: darkgoldenrod;
      font-family: monospace;
      font-size: 10px;
    }
    .Q {
      color: maroon;
      font-family: monospace;
      font-size: 10px;
    }
    .R {
      color: midnightblue;
      font-family: monospace;
      font-size: 10px;
    }
    .S {
      color: darkkhaki;
      font-family: monospace;
      font-size: 10px;
    }
    .T {
      color: olive;
      font-family: monospace;
      font-size: 10px;
    }
    .V {
      color: magenta;
      font-family: monospace;
      font-size: 10px;
    }
    .W {
      color: rosybrown;
      font-family: monospace;
      font-size: 10px;
    }
    .X {
      color: tomato;
      font-family: monospace;
      font-size: 10px;
    }
    .Y {
      color: gold;
      font-family: monospace;
      font-size: 10px;
    }
    .Z {
      color: royalblue;
      font-family: monospace;
      font-size: 10px;
    }
    .* {
      color: slategray;
      font-family: monospace;
      font-size: 10px;
    }
    .TEXT {
      color: black;
      font-family: monospace;
      font-size: 10px;
    }
    .SPACE {
      color: white;
      font-family: monospace;
      font-size: 10px;
    }
  </style>
<head>
"""


def usage():
  print 'seq_identifier.py -p <patternFile> -s <sampleFile>'

##################################################################
# NEEDS SOME CHANGING TO CONSIDER MISSING CHARACTER IN SAMPLE    #
##################################################################
def CombineSamePattern(match):
  totalPatterns = len(match)
  if totalPatterns == 1:
    return match
  else:
    startIndex = 0
    while True:
      if match[startIndex][1].num == match[startIndex+1][1].num:
        match[startIndex][1].endIndex = match[startIndex+1][1].endIndex
        match[startIndex][1].size = match[startIndex][1].endIndex - match[startIndex][1].startIndex
        match[startIndex][0].snippets += match[startIndex+1][0].snippets
        match[startIndex][0].endIndex = match[startIndex+1][0].endIndex
        match[startIndex][0].size = match[startIndex][0].endIndex - match[startIndex][0].startIndex
        del match[startIndex+1]
        totalPatterns -= 1
      else:
        startIndex += 1
      if (startIndex+1) == totalPatterns:
        break
  return match

def call_main(donor_file, input_path, sample_file, min_len, min_gap, max_gap, output):
  # CONFIGURATION VARIABLES
  noMatch = []
  totalNoMatches = 0
  results = {}
  results_ = {}
  minLen = min_len        # minimum length of pattern match
  minGap = min_gap        # minimum gap 1 means don't search for pattern with gap length of 1
  maxGap = max_gap        # anything over maxGap is considered a no match
  htmlToPdf = True  # set to True if you want pdf output file

  # Step 1: Retrieve allele patterns
  donor_path, donorFile = os.path.split(donor_file)

  alleleIds, allelePatterns, numPatterns, _ = GetSequences(donorFile, "fasta", donor_path + "/", True, "Allele Patterns")

  sampleFile = sample_file
  sample_path = input_path
  print "Sample File: " + str(sampleFile)
  print

  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  print "Pattern Sequences:"

  if htmlToPdf:
    pdfFile   = open(output + "/" + sampleFile.split('.')[0] + ".pdf", "w+b")
    bodyHTML  = "<span class=\"TEXT\">"
    bodyHTML += "Sample File: <strong>" + str(sampleFile) + "</strong><br /><br />"
    bodyHTML += "Pattern Sequences:<br />"
    bodyHTML += "</span>"

  for num in range(0, numPatterns):
    print "%s:\t%s" %(alleleIds[num], allelePatterns[num])

    if htmlToPdf:
      patHTML = "<span class=\"TEXT\">" + str(alleleIds[num]) + ": </span>"
      for letter in allelePatterns[num]:
        patHTML += "<span class=\"" + letter + "\">" + letter + "</span>"
      patHTML += "<br />"
      bodyHTML += patHTML

  if htmlToPdf:
    bodyHTML += "<br />"
  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

  # Step 2: Load sample sequences and identify duplicates
  sampleIds, sampleSequences, totalSeqs, totalSeqsStCodons =  GetSequences(sampleFile, "fasta", sample_path + "/", False, "Sample Sequences")

  # Step 3: Identify what pattern the sample sequence belongs
  numSamps = len(sampleIds)
  patLen = [len(allelePatterns[i]) for i in range(len(allelePatterns))]

  print "Total number of sequences (with duplicates)    : %d" %(totalSeqs)
  print "Total number of sequences (with no duplicates) : %d" %(numSamps)
  print "Total number of sequences (with stop codons)   : %d" %(totalSeqsStCodons)
  print

  if htmlToPdf:
    bodyHTML += "<span class=\"TEXT\">"
    bodyHTML += "Total number of sequences (with duplicates): " + str(totalSeqs) + "<br />"
    bodyHTML += "Total number of sequences (with no duplicates): " + str(numSamps) + "<br />"
    bodyHTML += "Total number of sequences (with stop codons): " + str(totalSeqsStCodons)
    bodyHTML += "</span><hr /><br />"

  # Loop through all samples and determine it's allele pattern combination
  for num in range(0, numSamps):
    numberOfSequences = len(sampleIds[num].split(","))
    print sampleIds[num]

    patternMatch, patKey, patHTML = DeterminePattern(sampleSequences[num],
                                                     alleleIds,
                                                     allelePatterns,
                                                     numPatterns,
                                                     patLen,
                                                     minLen,
                                                     minGap,
                                                     htmlToPdf)

    if patKey not in results:
      results[patKey] = numberOfSequences
      results_[patKey] = [(numberOfSequences,num)]
    else:
      results[patKey] += numberOfSequences
      results_[patKey].append((numberOfSequences,num))


    if htmlToPdf:
      sampIDHTML = "<span class=\"TEXT\">"
      groupBy = 115
      totalLen = len(sampleIds[num])
      start = 0
      end = groupBy
      while True:
        sampIDHTML += sampleIds[num][start:end]
        if end >= totalLen:
          break
        sampIDHTML += "<br />"
        start = end
        end = end + groupBy
      sampIDHTML += "</span><br />"
      bodyHTML += sampIDHTML + patHTML + "<br /><br />"


  sortedKeys = sorted(results, key=results.get, reverse=True)
  print "%s\t%s" %("# SEQ", "PATTERN")

  # Printing GOOD MATCH table
  if htmlToPdf:
    resultTable  = "<div><pdf:nextpage /></div>"
    resultTable += "<span class=\"TEXT\"><center>SEQUENCES CONSIDERED A <strong>MATCH</strong></center></span>"
    resultTable += "<table width=\"720px\" border=\"1px\" cellpadding=\"2px\" class=\"TEXT\">"
    resultTable += "<tr><td width=\"80px\" valign=\"bottom\" height=\"15px\"><strong># OF SEQ</strong></td><td valign=\"bottom\"><strong>PATTERN</strong></td></tr>"

  totalSeq = 0
  noMatchKeys = []
  totalNoMatch = 0
  print "SEQUENCES CONSIDERED A MATCH"
  for key in sortedKeys:

    # Checks that gap lengths are <= maxGap
    tempList = key.split("/")
    noMatch = False
    for t in tempList:
      if ("gap" in t) and (int(t[:-3]) > maxGap):
        totalNoMatch += results[key]
        noMatchKeys.append(key)
        noMatch = True
        break
    if noMatch:
      continue

    # Print out data for result table for GOOD MATCH
    totalSeq += results[key]
    print "%4d\t%s" %(results[key], key)



    if htmlToPdf:
      sResultTab = "<table cellpadding=\"0px\" width=\"640px\">"
    subResults = sorted(results_[key], reverse=True)
    for sResult in subResults:
      print "\t%4d\t%s" %(sResult[0], sampleSequences[sResult[1]])

      if htmlToPdf:
        sampHTML = ""
        for letter in sampleSequences[sResult[1]]:
          sampHTML += "<span class=\"" + letter + "\">" + letter + "</span>"

        sResultTab += "<tr><td class=\"TEXT\" width=\"50px\">" + str(sResult[0]) + \
                      "</td><td>" + sampHTML + "</td></tr>"

    if htmlToPdf:
      sResultTab  += "</table>"
      resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\">" + str(results[key]) + \
                     "</td><td style=\"vertical-align:middle\">" + str(key) + " " + sResultTab + "</td></tr>"

  if htmlToPdf:
    compute = totalSeqs - totalSeqsStCodons - totalNoMatch
    resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\"><em>" + str(totalSeq) + \
                   "</em></td><td style=\"vertical-align:middle\"><em>Seq w/ duplicates - Seq w/ stop codons - Seq (no match) = " + str(totalSeqs) + " - " + str(totalSeqsStCodons) + " - " + str(totalNoMatch) + " = " + str(compute) + "</em></td></tr>"
    resultTable += "</table>"


  # Printing NO MATCH table
  if htmlToPdf:
    resultTable += "<div><pdf:nextpage /></div>"
    resultTable += "<span class=\"TEXT\"><center>SEQUENCES CONSIDERED A <strong>NO MATCH</strong></center></span>"
    resultTable += "<table width=\"720px\" border=\"1px\" cellpadding=\"2px\" class=\"TEXT\">"
    resultTable += "<tr><td width=\"80px\" valign=\"bottom\" height=\"15px\"><strong># OF SEQ</strong></td><td valign=\"bottom\"><strong>PATTERN</strong></td></tr>"

  print "SEQUENCES CONSIDERED A NO MATCH"
  for key in noMatchKeys:

    # Print out data for result table for NO MATCH
    print "%4d\t%s" %(results[key], key)

    if htmlToPdf:
      sResultTab = "<table cellpadding=\"0px\" width=\"640px\">"
    subResults = sorted(results_[key], reverse=True)
    for sResult in subResults:
      print "\t%4d\t%s" %(sResult[0], sampleSequences[sResult[1]])

      if htmlToPdf:
        sampHTML = ""
        for letter in sampleSequences[sResult[1]]:
          sampHTML += "<span class=\"" + letter + "\">" + letter + "</span>"

        sResultTab += "<tr><td class=\"TEXT\" width=\"50px\">" + str(sResult[0]) + \
                      "</td><td>" + sampHTML + "</td></tr>"

    if htmlToPdf:
      sResultTab  += "</table>"
      resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\">" + str(results[key]) + \
                     "</td><td style=\"vertical-align:middle\">" + str(key) + " " + sResultTab + "</td></tr>"

  if htmlToPdf:
    resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\"><em>" + str(totalNoMatch) + \
                   "</em></td><td style=\"vertical-align:middle\"><em>Seq w/ gap length > " + str(maxGap) + "</em></td></tr>"
    resultTable += "</table>"


  # Write PDF File
  if htmlToPdf:
    global html
    html += bodyHTML + resultTable
    pisa.CreatePDF(html, dest=pdfFile)
    pdfFile.close()

'''
    patternMatch = DeterminePattern(sampleSequences[num], num, allelePatterns, numPatterns)
    if patternMatch != None:
      patternMatch = CombineSamePattern(patternMatch)

    if patternMatch != None:
      pattern = ""
      for index in range(0, len(patternMatch)):
        pattern += str(patternMatch[index][1].num + 1)

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
'''




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

  # CONFIGURATION VARIABLES
  noMatch = []
  totalNoMatches = 0
  results = {}
  results_ = {}
  minLen = 4        # minimum length of pattern match
  minGap = 0        # minimum gap 1 means don't search for pattern with gap length of 1
  maxGap = 4        # anything over maxGap is considered a no match
  htmlToPdf = True  # set to True if you want pdf output file

  # Step 1: Retrieve allele patterns
  alleleIds, allelePatterns, numPatterns, _ = GetSequences(patternFile, "fasta", os.getcwd() + "/Library/", True, "Allele Patterns")

  print "Sample File: " + str(sampleFile)
  print

  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  print "Pattern Sequences:"

  if htmlToPdf:
    pdfFile   = open("Results/" + sampleFile.split('.')[0] + ".pdf", "w+b")
    bodyHTML  = "<span class=\"TEXT\">"
    bodyHTML += "Sample File: <strong>" + str(sampleFile) + "</strong><br /><br />"
    bodyHTML += "Pattern Sequences:<br />"
    bodyHTML += "</span>"

  for num in range(0, numPatterns):
    print "%s:\t%s" %(alleleIds[num], allelePatterns[num])

    if htmlToPdf:
      patHTML = "<span class=\"TEXT\">" + str(alleleIds[num]) + ": </span>"
      for letter in allelePatterns[num]:
        patHTML += "<span class=\"" + letter + "\">" + letter + "</span>"
      patHTML += "<br />"
      bodyHTML += patHTML

  if htmlToPdf:
    bodyHTML += "<br />"
  print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

  # Step 2: Load sample sequences and identify duplicates
  sampleIds, sampleSequences, totalSeqs, totalSeqsStCodons =  GetSequences(sampleFile, "fasta", os.getcwd() + "/Samples/", False, "Sample Sequences")

  # Step 3: Identify what pattern the sample sequence belongs
  numSamps = len(sampleIds)
  patLen = [len(allelePatterns[i]) for i in range(len(allelePatterns))]

  print "Total number of sequences (with duplicates)    : %d" %(totalSeqs)
  print "Total number of sequences (with no duplicates) : %d" %(numSamps)
  print "Total number of sequences (with stop codons)   : %d" %(totalSeqsStCodons)
  print

  if htmlToPdf:
    bodyHTML += "<span class=\"TEXT\">"
    bodyHTML += "Total number of sequences (with duplicates): " + str(totalSeqs) + "<br />"
    bodyHTML += "Total number of sequences (with no duplicates): " + str(numSamps) + "<br />"
    bodyHTML += "Total number of sequences (with stop codons): " + str(totalSeqsStCodons)
    bodyHTML += "</span><hr /><br />"

  # Loop through all samples and determine it's allele pattern combination
  for num in range(0, numSamps):
    numberOfSequences = len(sampleIds[num].split(","))
    print sampleIds[num]

    patternMatch, patKey, patHTML = DeterminePattern(sampleSequences[num],
                                                     alleleIds,
                                                     allelePatterns,
                                                     numPatterns,
                                                     patLen,
                                                     minLen,
                                                     minGap,
                                                     htmlToPdf)

    if patKey not in results:
      results[patKey] = numberOfSequences
      results_[patKey] = [(numberOfSequences,num)]
    else:
      results[patKey] += numberOfSequences
      results_[patKey].append((numberOfSequences,num))


    if htmlToPdf:
      sampIDHTML = "<span class=\"TEXT\">"
      groupBy = 115
      totalLen = len(sampleIds[num])
      start = 0
      end = groupBy
      while True:
        sampIDHTML += sampleIds[num][start:end]
        if end >= totalLen:
          break
        sampIDHTML += "<br />"
        start = end
        end = end + groupBy
      sampIDHTML += "</span><br />"
      bodyHTML += sampIDHTML + patHTML + "<br /><br />"


  sortedKeys = sorted(results, key=results.get, reverse=True)
  print "%s\t%s" %("# SEQ", "PATTERN")

  # Printing GOOD MATCH table
  if htmlToPdf:
    resultTable  = "<div><pdf:nextpage /></div>"
    resultTable += "<span class=\"TEXT\"><center>SEQUENCES CONSIDERED A <strong>MATCH</strong></center></span>"
    resultTable += "<table width=\"720px\" border=\"1px\" cellpadding=\"2px\" class=\"TEXT\">"
    resultTable += "<tr><td width=\"80px\" valign=\"bottom\" height=\"15px\"><strong># OF SEQ</strong></td><td valign=\"bottom\"><strong>PATTERN</strong></td></tr>"

  totalSeq = 0
  noMatchKeys = []
  totalNoMatch = 0
  print "SEQUENCES CONSIDERED A MATCH"
  for key in sortedKeys:

    # Checks that gap lengths are <= maxGap
    tempList = key.split("/")
    noMatch = False
    for t in tempList:
      if ("gap" in t) and (int(t[:-3]) > maxGap):
        totalNoMatch += results[key]
        noMatchKeys.append(key)
        noMatch = True
        break
    if noMatch:
      continue

    # Print out data for result table for GOOD MATCH
    totalSeq += results[key]
    print "%4d\t%s" %(results[key], key)



    if htmlToPdf:
      sResultTab = "<table cellpadding=\"0px\" width=\"640px\">"
    subResults = sorted(results_[key], reverse=True)
    for sResult in subResults:
      print "\t%4d\t%s" %(sResult[0], sampleSequences[sResult[1]])

      if htmlToPdf:
        sampHTML = ""
        for letter in sampleSequences[sResult[1]]:
          sampHTML += "<span class=\"" + letter + "\">" + letter + "</span>"

        sResultTab += "<tr><td class=\"TEXT\" width=\"50px\">" + str(sResult[0]) + \
                      "</td><td>" + sampHTML + "</td></tr>"

    if htmlToPdf:
      sResultTab  += "</table>"
      resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\">" + str(results[key]) + \
                     "</td><td style=\"vertical-align:middle\">" + str(key) + " " + sResultTab + "</td></tr>"

  if htmlToPdf:
    compute = totalSeqs - totalSeqsStCodons - totalNoMatch
    resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\"><em>" + str(totalSeq) + \
                   "</em></td><td style=\"vertical-align:middle\"><em>Seq w/ duplicates - Seq w/ stop codons - Seq (no match) = " + str(totalSeqs) + " - " + str(totalSeqsStCodons) + " - " + str(totalNoMatch) + " = " + str(compute) + "</em></td></tr>"
    resultTable += "</table>"


  # Printing NO MATCH table
  if htmlToPdf:
    resultTable += "<div><pdf:nextpage /></div>"
    resultTable += "<span class=\"TEXT\"><center>SEQUENCES CONSIDERED A <strong>NO MATCH</strong></center></span>"
    resultTable += "<table width=\"720px\" border=\"1px\" cellpadding=\"2px\" class=\"TEXT\">"
    resultTable += "<tr><td width=\"80px\" valign=\"bottom\" height=\"15px\"><strong># OF SEQ</strong></td><td valign=\"bottom\"><strong>PATTERN</strong></td></tr>"

  print "SEQUENCES CONSIDERED A NO MATCH"
  for key in noMatchKeys:

    # Print out data for result table for NO MATCH
    print "%4d\t%s" %(results[key], key)

    if htmlToPdf:
      sResultTab = "<table cellpadding=\"0px\" width=\"640px\">"
    subResults = sorted(results_[key], reverse=True)
    for sResult in subResults:
      print "\t%4d\t%s" %(sResult[0], sampleSequences[sResult[1]])

      if htmlToPdf:
        sampHTML = ""
        for letter in sampleSequences[sResult[1]]:
          sampHTML += "<span class=\"" + letter + "\">" + letter + "</span>"

        sResultTab += "<tr><td class=\"TEXT\" width=\"50px\">" + str(sResult[0]) + \
                      "</td><td>" + sampHTML + "</td></tr>"

    if htmlToPdf:
      sResultTab  += "</table>"
      resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\">" + str(results[key]) + \
                     "</td><td style=\"vertical-align:middle\">" + str(key) + " " + sResultTab + "</td></tr>"

  if htmlToPdf:
    resultTable += "<tr><td style=\"vertical-align:middle\" align=\"center\"><em>" + str(totalNoMatch) + \
                   "</em></td><td style=\"vertical-align:middle\"><em>Seq w/ gap length > " + str(maxGap) + "</em></td></tr>"
    resultTable += "</table>"


  # Write PDF File
  if htmlToPdf:
    global html
    html += bodyHTML + resultTable
    pisa.CreatePDF(html, dest=pdfFile)
    pdfFile.close()

'''
    patternMatch = DeterminePattern(sampleSequences[num], num, allelePatterns, numPatterns)
    if patternMatch != None:
      patternMatch = CombineSamePattern(patternMatch)

    if patternMatch != None:
      pattern = ""
      for index in range(0, len(patternMatch)):
        pattern += str(patternMatch[index][1].num + 1)

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
'''


if __name__ == '__main__':
  main(sys.argv[1:])
