# This file is made to create gallery files
import glob
import os
import sys


dir = "/home/ryott/Projects/gutter-shows-website/gallery"
f = open("pix.txt", "a")
extlist = [".jpg", ".JPG", ".jpeg", ".gif"]
pyx = [k for k in os.listdir(dir) if os.path.isfile(os.path.join(dir, k))]
for file in pyx:
    for ext in extlist:
        if file.endswith(ext):
            print(str(file))
            f.write(f'<img src="gallery/{file}" height="200px">\n')

f.close()