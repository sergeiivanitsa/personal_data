from pdf2image import convert_from_path

from pathlib import Path  
import shutil

def makejpg(id):
	path_fakeoutput = Path("outputs", "fakeoutputs", f"{id}.pdf")
	#path_fakeoutput=r'C:\Dev\personal_data\personal_data\outputs\fakeoutputs\2.pdf'

	images = convert_from_path(path_fakeoutput, 500, poppler_path=r'C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin')

	for i in range(len(images)):
		images[i].save(f'{id}' + '.jpg', 'JPEG')
		#images[i].save('2' + '.jpg', 'JPEG')
		shutil.move(f'{id}.jpg', Path("media", "images"))