from PyPDF2 import PdfWriter, PdfReader
import os
from os import listdir
from os.path import isfile, join

mypath = "materials"
onlyfiles = os.listdir(mypath)
onlyfiles.sort()

filist = input().split(";")
print(filist)
#crop 2 segments each pdf page
#  x1,y1        x3,y1
#    ________     ________
#   |________|   |________|
#   |________|   |________|
#   |________|   |________|
#   |________|   |________|
#          x2,y2        x4,y2

filelist = ["1","2-3","4-5","5-6","6-7","7-8","74"]
#set croping areas
x1 = 114
y1 = 815 - 755
x2 = 630
y2 = 822
x3 = 815 - 0
x4 = x3 + x2 - x1

writer = PdfWriter()
for name in filist:
    reader = PdfReader(name)
    reader2 = PdfReader(name)
    # add page from reader, but crop it to proper size:
    page1 = reader.pages[0]
    page2 = reader2.pages[0]
    page1.mediabox.upperLeft = (x1,y1)
    page1.mediabox.upperRight = (x2, y1)
    page1.mediabox.lowerLeft = (x1, y2)
    page1.mediabox.lowerRight = (x2, y2)
    writer.add_page(page1)
    page2.mediabox.upper_left = (x3,y1)
    page2.mediabox.upper_right = (x4, y1)
    page2.mediabox.lower_left = (x3, y2)
    page2.mediabox.lower_right = (x4, y2)
    writer.add_page(page2)

with open("Output.pdf", "wb") as fp:
    writer.write(fp)