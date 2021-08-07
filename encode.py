import os, subprocess
import sys, re
import string, subprocess
from PIL import Image
from io import BytesIO

current_dir = os.getcwd()


allFiles = []
error = False

for root, _, files in os.walk('.'):
    root = root.lstrip('.').strip(os.sep)

    for file in files:
        if not file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif'):
            continue

        file = os.path.join(root, file)
        allFiles.append(file)


if error:
    print('Errors detected, please resolve before continuing')
    sys.exit()


for file in allFiles: 
    print(file)
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    imgInputFile = BytesIO()
    picture.save(imgInputFile, 'png')
    imgInputFileSize = imgInputFile.tell()
    print("old: {}".format(imgInputFileSize))
    picture.save(file, optimize=True)
    newFileSize = os.path.getsize(filepath)
    print("new: {}".format(newFileSize))
    if imgInputFileSize < newFileSize: # for some reason new size is larger?
        picture.save(file)
        print("!!! compressed file of {} was larger".format(filepath))


