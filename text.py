import os

def delate():
    f = open('Paweł Piskorski.txt', "r").read()
    file = f.split(' ')
    print(file)
    words = ["Podkarpackie", "się", "i", "oraz", "nigdy", "dlaczego"]
    for word in range (len(file),0,-1):
        if file[word-1] in words:
            file.remove(file[word-1])
    print(file)

def replacment():
    f = open('Paweł Piskorski.txt', "r").read()
    file = f.split(' ')
    print(file)
    words_dictonary = {'Podkarpackie': 'Malopolskie', 'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy',
                       'dlaczego': 'czemu', 'vut': 'prut'}
    for word in range(len(file)):
        if file[word - 1] in words_dictonary.keys():
            file[word - 1] = words_dictonary.get(file[word - 1], word)
    print(file)
if __name__ == '__main__':
    #delate()
    replacment()