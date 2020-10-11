import shutil
import os

source = '/Users/Zeroh/Desktop/Python/filetransfer1/'

destination = '/Users/Zeroh/Desktop/Python/filetransfer2'
files = os.listdir(source)
files.sort()

for f in files:
    print(f)
    src = source+f
    dst = destination+f
    shutil.copy(src,dst)
    if os.stat(src).st_mtime < os.stat(dst).st_mtime:
        continue
