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
            tree = ET.parse(self.path)
            root = tree.getroot()
            calorie_counts = root.find('calorie_counts')
            days = calorie_counts.findall(str('day'))
            print(len(days))
            cals = days[len(days)-1].find('todays_calories').text
            self.todays_calories = int(cals) 
            self.weight = int(root.find('weight').text)
        else:
            self.createUserFile()
                        
    def createUserFile(self):
        current_weight = input("Please enter your current weight in pounds as an integer. ")
        self.weight = current_weight
        root = ET.Element('root')
        tree = ElementTree(root)
        user_name = ET.SubElement(root,'name')
        user_name.text = self.name
        user_weight = ET.SubElement(root,'weight')
        user_weight.text = current_weight
        calorie_counts = ET.SubElement(root,'calorie_counts')
        day = ET.SubElement(calorie_counts,'day')
        todays_date = ET.SubElement(day,'date')
        todays_date.text = str(date.today())
        todays_calories = ET.SubElement(day,'todays_calories')
        todays_calories.text = '0'
        tree.write(self.path)
        
    def updateCalories(self,new_calories):
        self.todays_calories = self.todays_calories + new_calories
        tree = ET.parse(self.path)
        root = tree.getroot()
        calorie_counts = root.find('calorie_counts')
        
        days = calorie_counts.findall(str('day'))
        print(len(days))
        current_calories = days[len(days)-1].find('todays_calories')
    
        current_calories.text = str(self.todays_calories)
        new_tree = ElementTree(root)
        new_tree.write(self.path)
        
