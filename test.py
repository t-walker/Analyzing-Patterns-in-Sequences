string = "NAIESATGTTSGDELSKKVCGKGTTSGNQCGVNATSGSTNNGKLSTVFNTDGAEAISSMDTTASGTSNTISLQG"

length = len(string)
min_len = 4
counter = 0
print "String Length: ", length
while min_len <= length:
  for i in range(0, length):
    temp = string[i:(i+min_len)]
    if len(temp) == min_len:
      counter += 1
      print "%i: " %(counter), temp
      
  min_len += 1
  
print counter
