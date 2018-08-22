import os.path
from os import getcwd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
from datetime import date
class User(object):
    name = ''
    todays_calories = 0
    weight = 0
    def __init__(self,user):
        self.name = user
        self.readUserFile()
        
    #def setTodaysCalories:
    #def getTodaysCalories:
    #def setWeight:
        
    #def getWeight:
    def readUserFile(self):
        path = os.path.join(getcwd(),('user_files/' + self.name + '.xml'))
        if(os.path.isfile(path)):
            tree = ET.parse(path)
            root = tree.getroot()
            calorie_counts = root.find('calorie_counts')
            self.setTodaysCalories(calorie_counts.find(date.today()))
            self.setWeight(root.find(weight).text)
        else:
            self.createUserFile()
                        
    def createUserFile(self):
        current_weight = input("Please enter your current weight in pounds as an integer. ")
        root = ET.Element('root')
        tree = ElementTree(root)
        user_name = ET.SubElement(root,'name')
        user_name.text = self.name
        user_weight = ET.SubElement(root,'wieght')
        user_weight.text = current_weight
        calorie_counts = ET.SubElement(root,'calorie_counts')
        tree.write(os.path.join(getcwd(),('user_files/' + self.name + '.xml')))
