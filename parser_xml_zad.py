
import xml.dom.minidom as md
import xml.sax as sa
import json

def xml_func():
    plik_xml = md.parse('plik.xml')
    garage = plik_xml.documentElement
    cars = garage.getElementsByTagName('car')

    print("Wybrany model to:")
    print(cars[0].getElementsByTagName('model')[0].childNodes[0].data)

    tag = cars[0].getElementsByTagName('model')[0].childNodes[0].data

    print("Wpisz nowy model samochodu: ")
    new_tag = input()
    cars[0].getElementsByTagName('model')[0].childNodes[0].data = new_tag

    print(garage.toxml())
    plik_xml.writexml(open('plik_newtag', 'w'))
################################################################################ SAX
class SaxHandler(sa.ContentHandler):

    def startElement(self, name, attributes):
        self.name = name
        if self.name == "car":
            print("ID: {}".format(attributes['id']))

    def characters(self, cont):
        if self.name == "model":
            self.name = cont
            print("model: {}".format(self.name))
        elif self.name == "engine":
            self.age = cont
            print("engine: {}".format(self.age))

    def endElement(self, name):
        self.name = ""

def sax_func():
    xml_sax = sa.make_parser()

    handler = SaxHandler()
    xml_sax.setContentHandler(handler)
    xml_sax.parse('plik.xml')


############################################################################ JSON


file = open('baza_danych.json')
data_js = json.load(file)


def write_data(none=0):
    with open('baza_danych.json', 'w') as file:
        json.dump(data_js, file, indent=4)

def func_js():

    print("1.Display \n2.Add new data \n3.Delete data")
    tmp = int(input())

    if tmp == 1:
        for x in data_js['Garage']:
            print(x)  # Print all content
    elif tmp == 2:
        model = input("Model: ")
        engine = input("Engine: ")
        new_data={
            "Model": model,
            "Engine": engine,
        }
        temp = data_js['Garage']
        temp.append(new_data)
        write_data(data_js)
        print("New data: ", new_data)

    elif tmp == 3:
        delete_data = input("Which model do you want delete?")
        for i in data_js['Garage']:
            if i['Model'] == str(delete_data):
                del i['Model']
                del i['Engine']
                write_data(data_js)
##################################################################################3
if __name__ == "__main__":
    #xml_func()
    sax_func()
    #func_js()