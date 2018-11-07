from User import User
from Saved_Foods import Saved_Foods
#The purpose of this class is to create an interface for the user to
#interact with the program. In addition it allows for interaction with the User class.
class Calorie_Tracker(object):
    Foods = Saved_Foods()
    def __init__(self, user):
        #create a new user object when ever a user attempts to log in.
        current_user = User(user)
        self.getCommand(current_user)
    
    
    
    #provides an interface so that users may enter commands
    def getCommand(self,current_user):
        while True:                
            print(50 * "-")
            command = input("\nPlease enter a command: ").lower()
            print()
            if(command == "--a"):
                self.addCalories(current_user)
            elif(command == "--t"):
                print("You have consumed " + str(current_user.todays_calories) + " calories today!")
            elif(command == "--w"):
                print("Based on your current calorie intake you should weigh " + str(current_user.weight)+ " lbs.")
            elif(command == "--r"):
                self.removeCalories(current_user)
            elif(command =="--f"):
                food = input ("Please enter the name of the food you wish to add to your calorie count: ").lower()
                self.addFood(current_user,food)
            elif(command == "--sf"):
                food = input("Please enter a name for the new food: ").lower()
                if(self.Foods.foodExists(food)):
                    print("That food is already in the system.")
                else:
                    cals = input("Please enter the calorie content of the food: ")
                    self.Foods.saveNewFood(food, cals)
            elif(command == "--ufc"):
                food = input("Please enter the food name: ").lower()
                if(self.Foods.foodExists(food)):
                    new_cals = input("Please enter the new calorie count for the food: ")
                    self.Foods.updateFoodCalories(food,new_cals)
                else:
                     print("That food does not exist in the system.")
            elif(command == "--lf"):
                self.listFoods()
            elif(command == "--fc"):
                food = input("Please enter the food name: ").lower()
                cals = self.Foods.getFoodCalories(food)

                if cals == '':
                    print("That food does not exist in the system.")
                else:
                    print(cals)
            elif(command == "--bf"):
                foods = input("Please enter the list of foods you would like to add separated by commas: ")
                split_foods = foods.split(",")
                self.batchAddFoods(current_user,split_foods)
            elif(command == "--help"):
                self.commandHelper()
            else:
                print("I dont recognize that command. Here is a list of my commands:\n")
                self.commandHelper()
    
    #adds calories to the users current total.
    def addCalories(self,current_user):
        cals = input("Please enter the calories you have eaten since your last log in: ")
        current_user.updateCalories(int(cals))
    #removes calories from the users current total
    def removeCalories(self,current_user):
        cals = int(input("Please enter the calories you would like to remove: "))
        current_user.updateCalories(cals - (cals*2))
    
    #prints out a list of commands and their descriptions
    def commandHelper(self):
         print(50 * "-")
         print("--a: Opens a prompt to allow you to add calories to your total for today.\n"
               "--t: Shows your current calorie count for today.\n"
               "--w: Shows your current calculated weight based on your total calorie intake. This is only an estimation and may not reflect your actual weight\n"
               "--r: Opens a prompt to allow you to remove calories from your total for today. \n"
               "--f: Allows the user to add calories to their count by entering a food name. Adding a multiplier of the form xN to the end of each food will add the food N many times. If the food is not in the system they will be prompted to add it.\n"
               "--sf: Allows the user to add a new food to the system.\n"
               "--ufc: Allows the user to update the calories of a food that is in the system.\n"
               "--lf: Lists the names of all foods currently in the system.\n"
               "--fc: Prints the calories for the entered food.\n"
               "--bf: Prompts the user to add a batch of foods seperated by commas. Adding a multiplier of the form xN to the end of each food will add the food N many times. If any of the foods are not in the system they will be prompted to add them.\n"
               )

    #adds a foods calories to the users current total. If the food doesn't exist in the system
    #then the user is prompted to add the food.
    def addFood(self,current_user,food_name):
        multiplier = self.getMultiplier(food_name)
        if multiplier > 0:
           food_name = self.stripMultiplier(food_name)
        if(self.Foods.foodExists(food_name)):
            calories = self.Foods.getFoodCalories(food_name)
            if multiplier > 0:
                    for i in range(multiplier):
                        current_user.updateCalories(int(calories))
            else:
                current_user.updateCalories(int(calories))
        else:
            add_food = input("That food does not exist in the system. Would you like to add it? (Y/N): ").lower()
            if add_food == 'y':
                food_cals = input("Please enter the calories for this food: ").lower()
                self.Foods.saveNewFood(food_name,food_cals)
                if multiplier > 0:
                    for i in range(multiplier):
                        current_user.updateCalories(int(food_cals))
                else:
                    current_user.updateCalories(int(food_cals))
    
    #prints out a list of foods currently in the system.
    def listFoods(self):
        current_foods = self.Foods.getAllFoods()
        if len(current_foods) > 4:
            for i in range(0,len(current_foods),5):
                if len(current_foods) - i > 5:
                    print(current_foods[i][0],"|",current_foods[i+1][0],"|",current_foods[i+2][0],"|",current_foods[i+3][0],"|",current_foods[i+4][0],"|")
                else:
                    print_string = ""
                    for j in range(i,len(current_foods)):
                        print_string += current_foods[j][0] + " | "
                    print(print_string)
        else:
            food_string = ''
            for food in current_foods:
                food_string += food[0] + "|"
            print(food_string)
    
    #returns the multiplier attached to the input food string. If there is no multiplier returns 0.
    #if the user happens to enter a multiplier of 0 we switch this to a 1 since they did infact enter 1 food.
    def getMultiplier(self, food):
        multiplier = 0
        if food[len(food)-2].lower() == 'x' and food[len(food)-1].isdigit():
            if food[len(food)-1] == 0:
                multiplier = 1
            else:
                multiplier = int(food[len(food)-1])
        return multiplier

    #returns the food string stripped of its multiplier value and any left over trailing spaces.
    def stripMultiplier(self, food):
        food = food[:-2].strip()
        return food

    #adds all of the foods in the food_list to the users total. If any of those foods dont exist in the system we prompt the user to add them.
    def batchAddFoods(self, current_user, food_list):
        nonexistant_foods = []
        for i in range(len(food_list)):
            multiplier = self.getMultiplier(food_list[i])
            if multiplier > 0:
                for i in range(multiplier - 1):
                    food_list.append(self.stripMultiplier(food_list[i]))
                food_list[i] = self.stripMultiplier(food_list[i])

            if not self.Foods.foodExists(food_list[i]):
                nonexistant_foods.append(food_list[i])

        if len(nonexistant_foods) > 0:
            add_food = input("These foods dont exist in the system ",nonexistant_foods," would you like to add them? (Y/N): ").lower()
            if add_food == 'y':
                for food in nonexistant_foods:
                    cals = input("Please enter the calories for ",food,": ")
                    self.Foods.saveNewFood(food, cals)
                    #self.current_user.updateCalories)(int(cals))
                for food in food_list:
                    calories = self.Foods.getFoodCalories(food)
                    current_user.updateCalories(int(calories))
        else:
              for food in food_list:
                    calories = self.Foods.getFoodCalories(food)
                    current_user.updateCalories(int(calories))
      

if __name__ == "__main__":
    
    user = input("Please enter your name: ").lower()
    CT = Calorie_Tracker(user)
    print(CT.getMultiplier("Bla bla blax2"))
