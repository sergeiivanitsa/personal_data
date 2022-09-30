from pdf2image import convert_from_path

import pathlib
from pathlib import Path  
import shutil

dir_path = pathlib.Path.cwd()

path_fakeoutput = Path("..\outputs", "fakeoutputs", "33.pdf")

# Store Pdf with convert_from_path function
images = convert_from_path(path_fakeoutput, 500, poppler_path=r'C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin')

#images.save(path_imagepath, 'page' + '.jpg', 'JPEG')

for i in range(len(images)):
#	Save pages as images in the pdf
	#path_imagepath = Path("..\outputs", "imgoutputs", str(images[i].save('page'+ str(i) +'.jpg', 'JPEG')))
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
	source = 'page0.jpg'
	destination = Path("..\outputs", "imgoutputs")
	path = shutil.move(source, destination)
	#with open(images[i], 'w') as f:
	#	f.write('test')

#with open(images, 'w') as f:
#    f.write('test')
