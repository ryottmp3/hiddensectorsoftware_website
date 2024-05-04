# This file is made to create gallery files
# Copyright H. Ryott Glayzer 2024
# MIT License
import os
import random

cwd = os.getcwd()
dir = as.path.join(cwd, "gallery")
f = open(os.path.join(cwd, "pix.html"), "w")
pyx = [k for k in os.listdir(dir) if os.path.isfile(os.path.join(dir, k))]
newGallery = random.sample(pyx, 20)            
for file in newGallery:
    print(str(file))
    f.write(f'<img src="gallery/{file}" height="200px">\n')

f.close()