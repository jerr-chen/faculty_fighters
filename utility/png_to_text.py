from PIL import Image
from collections import Counter
from scipy.spatial import KDTree
from sys import argv
import numpy as np
def hex_to_rgb(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
def rgb_to_hex(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)

def main():
	if(len(argv) < 2):
		print "Usage: [script.py] [filename-to-convert]"
		return

	filename = argv[1]

	im = Image.open(filename + ".png") #Can be many different formats.
	im = im.convert("RGBA")

	outImg = Image.new('RGB', im.size, color='white')
	outFile = open(filename + '.txt', 'w')
	for y in range(im.size[1]):
	    for x in range(im.size[0]):
	        pixel = im.getpixel((x,y))
	        print(pixel)
	        outImg.putpixel((x,y), pixel)
	        r, g, b, a = im.getpixel((x,y))
	        outFile.write("%x%x%x\n" %(r,g,b))
	outFile.close()
	outImg.save(filename+ ".png")

if __name__ == '__main__':
	main()