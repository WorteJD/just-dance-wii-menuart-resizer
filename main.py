from PIL import Image
import os
inputfiles=os.listdir("input")
for inputfile in inputfiles:
    asset=Image.open("input/" + inputfile)
    result=asset.resize((256,256))
    result.save("output/" + inputfile.split(".")[0] + ".png")