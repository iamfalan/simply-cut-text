from pythainlp import word_tokenize
from PIL import Image, ImageDraw, ImageFont
import sys

if len(sys.argv) < 6 or \
   sys.argv[1] is None or \
   sys.argv[2] is None or \
   sys.argv[3] is None or \
   sys.argv[4] is None or \
   sys.argv[5] is None:
    print("Usage: python cuttext.py [script_file] [desired_width] [font file name] [font size] [output file]")
    exit(-1)

scriptfile = sys.argv[1]
widthStr = sys.argv[2]
font_name = sys.argv[3]
font_size_str = sys.argv[4]
outfile = sys.argv[5]

width = int(widthStr)
font_size = int(font_size_str)
image = Image.new("RGB", (width+100, 80))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_name, font_size)

with open(outfile, 'a') as out:
    with open(scriptfile) as f:
        for line in f:
            words = word_tokenize(line, engine="newmm")
            test_text = ""
            for word in words:
                if word!=" ":
                    bbox = draw.textbbox((0, 20), test_text+word, font=font)
                    if bbox[2] > width:
                        out.write(test_text.rstrip()+"\n")
                        test_text=""
                test_text+=word
            out.write("\n")