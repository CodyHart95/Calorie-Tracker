import os.path
from os import getcwd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

#The purpose of this class is to provide a structure through which we can controll
#the saving and retrival of foods that users have input into the system.
class Saved_Foods():

    #path to the foods file that we save all of our foods to
    path = os.path.join(getcwd(),('Saved Foods/Foods.xml'))
    foods = []
    def __init__(self):
        self.foods = self.getAllFoods()

    #saves a food to the food file and adds it to the foods array.
    def saveNewFood(self,food_name, calories):
        tree = ET.parse(self.path)
        root = tree.getroot()
        Foods = root.find('Foods')
        item = ET.SubElement(Foods,'item')

        item_name = ET.SubElement(item,'item_name')
        item_name.text = food_name

        item_calories = ET.SubElement(item,'calories')
        item_calories.text = calories

        new_tree = ElementTree(root)
        new_tree.write(self.path)

        self.foods.append([food_name, calories])

    #returns all foods and their calories currently saved to the food file.
    def getAllFoods(self):
        tree = ET.parse(self.path)
        root = tree.getroot()

        food_dir = root.find('Foods')

        items = food_dir.findall('item')

        names_and_cals = []
        for item in items:
            item_name = item.find('item_name')
            item_cals = item.find('calories')

            names_and_cals.append([item_name.text,item_cals.text])

        return names_and_cals

    #returns the index of the input food
    def indexOf(self,foods,food_name):
        for i in range(len(foods)):
            if foods[i][0] == food_name:
                return i
        return -1

    #returns the calories of input food
    def getFoodCalories(self,food_name):
        food_index = self.indexOf(self.foods,food_name)

        if food_index != -1:
            return self.foods[food_index][1]
        else:
            return ""

    #returns true if the food exists in the current system
    def foodExists(self, food_name):
        food_index = self.indexOf(self.foods,food_name)
        return food_index != -1

    #replaces the input foods calories
    def updateFoodCalories(self, food_name, new_cals):
        tree = ET.parse(self.path)
        root = tree.getroot()
        Foods = root.find('Foods')
        items = Foods.findall('item')

        for item in items:
            if item.find('item_name').text == food_name:
                item.find('calories').text = new_cals

        food_index = self.indexOf(self.foods,food_name)
        self.foods[food_index][1] = new_cals