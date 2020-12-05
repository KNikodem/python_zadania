##! /usr/bin/env python         shebang
#print ("Hello World!")




def hello():
    print("Hello")

def input_data():
    imie,nazwisko,data = input("Wpisz imie nazwisko i date urodzenia").split()
    print(data)

def lock():
    print("Ustaw hasło: ")
    passwd = int(input())
    print("Wpisz hasło: ")
    temp = int(input())
    if (temp == passwd):
        print("Hasło poprawane")
    else:
        print("Hasło niepoprawne")


if __name__ == "__main__":
    #hello()
    #input_data()
    lock()