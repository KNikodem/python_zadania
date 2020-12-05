import os, os.path
from PIL import Image

def count():
    dirs = os.listdir('.')
    counter = 0;
    for i in range(len(dirs)):
        if os.path.isfile(dirs[i]):
            counter = counter + 1
    print(counter)

def files_print(loc):
    for element in os.listdir(loc):
        dire = os.path.join(loc, element);
        print(dire)
        if os.path.isdir(dire):
            files_print(dire)

def convert():
    counter = 0;
    for file in os.listdir('.'):
        if file.endswith(".jpg"):
            jpg = Image.open(file)
            png = jpg.save(file + '.png')


    #jpg1 = Image.open('5g.jpg')
    #png1 = jpg1.save('5g.png')


if __name__ == '__main__':
    #count()
    files_print('.')# NIE DZIALA
    #convert()