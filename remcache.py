import re
import sys

inputfile = sys.argv[1]

regex = re.compile("^INSERT\s+INTO\s+\`cache")

input = open(inputfile, "r")
output = open("output.sql", "w")

for line in input.readlines():
  if regex.match(line) == None:
    output.write(line)
    
input.close()
output.close()
