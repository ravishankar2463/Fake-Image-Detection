# from os import chdir
from PIL import Image,ImageChops,ImageEnhance
from PIL.ExifTags import TAGS
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
import eel
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import itertools
from PIL import Image
import os
from pylab import *
import re
# import re
# from pylab import *

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns


eel.init('web')


def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    
# @eel.expose
# def start_file():
	# globals()['root'] = Tk()
	

@eel.expose
def ELA():
	root = Tk()
	root.attributes("-topmost",True)
	root.withdraw()
	globals()['pic'] = askopenfilename(parent = root)
	

	orig = pic
	temp = './web/temp/temp.jpg'
	scale = 10

	globals()['original'] = Image.open(orig)
	

	original.save(temp,quality=90)
	temporary = Image.open(temp)

	diff = ImageChops.difference(original,temporary)
	d = diff.load()
	WIDTH,HEIGHT = diff.size

	for x in range(WIDTH):
		for y in range(HEIGHT):
			d[x,y] = tuple(k * scale for k in d[x,y])

	extrema = diff.getextrema()
	max_diff = max([ex[1] for ex in extrema])
	if max_diff == 0:
		max_diff = 1
	scale = 255.0 / max_diff

	diff = ImageEnhance.Brightness(diff).enhance(scale)
	diff.save("./web/temp/diff.jpg")
	root.destroy()

@eel.expose()
def generateResults():
	model = load_model("models/vacc8612-vlss3071-tacc9097-tlss2135.h5")
	Xnew = array(Image.open("./web/temp/diff.jpg").resize((150, 150))).flatten() / 255.0
	Xnew = Xnew.reshape(1,150, 150, 3)
	predclass = model.predict_classes(Xnew)[0]
	prob = model.predict_proba(Xnew)[0]
	tmppredclass= str(predclass[0])
	tmpprob= str(prob[0])
	file1 = open("./web/temp/res.json","w")
	str1 = "data = '["
	str2= '{{"class":"{}","prob":{}}}'.format(tmppredclass,tmpprob)
	str3 = "]';"
	str4 = str1+str2+str3
	print(str4)
	file1.write(str4)
	file1.close()
	return predclass,prob

@eel.expose
def meta_analysis():
	numn = random.randint(1000,9999)
	ww = open('exif'+str(numn)+'.txt','w')
	exif = {
		TAGS[k]:v
		for k,v in original._getexif().items()
		if k in TAGS
	}

	ww.write("tags"+";"+"values"+"\n")
	for k,v in exif.items():
		ww.write(str(k)+";"+str(v)+"\n")
	ww.close()


my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('index.html',size=(1300, 1000),position=(300, 50))