# File: word_frequencies3.py
# Usage:  1) python word_frequencies2.py a filename  --- sort entries alphabetically
#         2) python word_frequencies2.py f filename  --- sort entries by frequency

import sys
import frequency_table as FT
import re

def get_data(filename):
  f = open(filename, "r")
  data = f.read()
  f.close()
  return data

def run(args):
    data = get_data(args[2]).lower()
    data = re.sub(r'[!?.:;,-]', '', data)

    lines = data.split("\n")
    string = " ".join(lines)
    words_ = string.split(" ")
    words = list(filter(lambda x: x != '', words_))

    frequencies = FT.frequency_table(words)
    frequency_items = frequencies.items()

    if sys.argv[1] == 'a':
      frequency_items.sort(key=(lambda x: x[0]))
    else:
      frequency_items.sort(key=(lambda x:   x[1]))


    for item in frequency_items:
      print item

    print "--------------"
    print 'lines:   ' + str(len(lines))
    print 'words:   ' + str(len(words))
    print 'chars:   ' + str(len(data))


def print_message():
    print "Usage: python word_freq a filename    # or"
    print "       python word_freq f filename    #"
    print ""
    print "  First alternative for alphabetically sorted table"
    print "  Second alternative for table sorted by frequency"


if len(sys.argv) == 3:
    run(sys.argv)
else:
    print_message()
