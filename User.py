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

    #reads the user file into the user object. If the file is not found
    #this function prompts the user to see if they would like to add
    #them selves as a user.
    def readUserFile(self):       
        if(os.path.isfile(self.path)):
            #read through the xml tree and pull out relevent information
            tree = ET.parse(self.path)
            root = tree.getroot()
            calorie_counts = root.find('calorie_counts')
            days = calorie_counts.findall(str('day'))
            cals = days[len(days)-1].find('todays_calories').text
            self.todays_calories = int(cals) 
            self.weight = int(root.find('weight').text)
        else:
            is_new_user = input("We dont have your name on file. Would you like to add it? (Y/N): ").lower()
            if(is_new_user == 'y'):
                self.createUserFile()
            else:
                print(50 * "-")
                self.name = input("Please enter your name: ").lower()
                self.path = os.path.join(getcwd(),('user_files/' + self.name + '.xml'))
                self.readUserFile()
                        
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
        self.updateWeight()
        tree = ET.parse(self.path)
        root = tree.getroot()
        calorie_counts = root.find('calorie_counts')        
        days = calorie_counts.findall(str('day'))
        current_calories = 0
        if(days[len(days)-1].find('date').text != str(date.today())):
            calorie_counts = root.find('calorie_counts')
            day = ET.SubElement(calorie_counts,'day')
            todays_date = ET.SubElement(day,'date')
            todays_date.text = str(date.today())
            todays_calories = ET.SubElement(day,'todays_calories')
            todays_calories.text = str(self.todays_calories)
        else:          
            current_calories = days[len(days)-1].find('todays_calories')
            current_calories.text = str(self.todays_calories)
        new_tree = ElementTree(root)
        new_tree.write(self.path)
           
    def updateWeight(self):
        if (self.todays_calories < 2000):
           self.weight = self.weight - (self.todays_calories * .002)
        else:
           self.weight = self.weight + (self.todays_calories * .002)

        tree = ET.parse(self.path)
        root = tree.getroot()
        current_weight = root.find('weight')
        current_weight = self.weight
        new_tree = ElementTree(root)
        new_tree.write(self.path)
        
