from PIL import Image
import argparse

#doc input as args
parser = argparse.ArgumentParser()

parser.add_argument('file')  #input file
parser.add_argument('-o' , '--output') #output file
parser.add_argument('--width', type = int ,default = 80) #output_string width
parser.add_argument('--height' , type = int , default = 80) #output_string height

#get args
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("~!@#$%^&**()-=[];'\,./_+{}|qwertyuiopasdfghjklzxcvbnmQAZWSXEDCRFVYHIKJMPLH;'./,")

def get_char(r , g , b , alpha=256):
	#RGB值轉換爲字符值
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int (0.2126 *r + 0.7152* g + 0.0722 * b)   #灰度值計算公式
	unit = (256.0 + 1) /length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT) , Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
