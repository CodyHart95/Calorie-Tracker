import os.path
from os import getcwd
import xml.etree.ElementTree as ET
import xml.etree
from xml.etree.ElementTree import ElementTree
from datetime import date

class User(object):
    name = ''
    todays_calories = 0
    weight = 0
    path = ''
    def __init__(self,user):
        self.name = user
        self.path = os.path.join(getcwd(),('user_files/' + self.name + '.xml'))
        self.readUserFile()
        
    def readUserFile(self):       
        if(os.path.isfile(self.path)):
            tree = ET.parse(self.path, etree.XMLParser(encoding='utf-8'))
            root = tree.getroot()
            calorie_counts = root.find('calorie_counts')
            self.todays_calories = int(calorie_counts.find(str(date.today())).text)
            self.weight = int(root.find(weight).text)
        else:
            self.createUserFile()
                        
    def createUserFile(self):
        current_weight = input("Please enter your current weight in pounds as an integer. ")
        root = ET.Element('root')
        tree = ElementTree(root)
        user_name = ET.SubElement(root,'name')
        user_name.text = self.name
        user_weight = ET.SubElement(root,'weight')
        user_weight.text = current_weight
        calorie_counts = ET.SubElement(root,'calorie_counts')
        todays_calories = ET.SubElement(calorie_counts,str(date.today()))
        todays_calories.text = '0'
        tree.write(self.path)
        
    def updateCalories(self,new_calories):
        self.todays_calories = self.todays_calories + new_calories
        tree = ET.parse(self.path)
        root = tree.getroot()
        calorie_counts = root.find('calorie_counts')
        current_calories = calorie_counts.find(str(date.today()))
        current_calories.text = self.todays_calories
        new_tree = ElementTree(root)
        new_tree.write(self.path)
        
