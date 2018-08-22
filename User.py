import os.path
from os import getcwd
import xml.etree.ElementTree as ET
from datetime import date
class User(object):
    name = ''
    todays_calories = 0
    weight = 0
    def __init__(self,user):
    def setUserName:
    def getUserName:
    def setTodaysCalories:
    def getTodaysCalories:
    def setWeight:
    def getWeight:
    def readUserFile(self):
        path = os.path.join(getcwd(),('user_files/' + self.user + '.xml'))
        if(os.path.isfile(path)):
            tree = ET.parse(path)
            root = tree.getroot()
            self.setUserName(root.find('name').text)
            calorie_counts = root.find('calorie_counts')
            self.setTodaysCalories(calorie_counts.find(date.today())
            self.setWeight(root.find(weight).text)
        else:
            self.createUserFile(self.name)
                        
    def createUserFile(self):
        current_weight = 0
        root = ET.Element('root')
        user_name = ET.SubElement('name')
        user_name.text = self.name
        user_weight = ET.SubElement('wieght')
        user_weight.text = str(current_weight)
        calorie_counts = ET.SubElement('calorie_counts')
