import csv
import sys

exf = open("ProductDetails.csv")
exr = csv.reader(exf)

# date = raw_input("Enter date: ")
date = sys.argv[1]
topNum = int(sys.argv[2])
total_items = dict()

for data in exr:
  if date in data:
    if data[1] in total_items.keys():
      total_items[data[1]] += int(data[2])
    else:
      total_items[data[1]] = int(data[2])
top = 0
for key, value in sorted(total_items.iteritems(), key=lambda (k,v): (v,k), reverse=True):
  print "%s: %s" % (key, value)
  top += 1;
  if top == topNum:
    break;
