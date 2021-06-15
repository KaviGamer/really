import time;
import os;
import shutil;
path = input("Enter the name of the directory to be sorted > ")
source = input("Enter the source folder name > ")
destination = input("Enter the destination folder name > ")
source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(path)

for file in list_of_files:
    for file in list_of_files:
        shutil.copy((source+file), destination)


    name,ext = os.path.splitext(file)
    ext = ext[1:]

    if ext=='':
        continue

    if os.path.exists(path+'/'+file,path+'/'+ext+'/'+file):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.mkdirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)