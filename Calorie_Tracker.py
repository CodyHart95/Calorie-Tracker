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
                self.selectFood(current_user,food)
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
            elif(command == "--help"):
                self.commandHelper()
            else:
                print("I dont recognize that command. Here is a list of my commands:\n")
                self.commandHelper()
    
    def addCalories(self,current_user):
        cals = input("Please enter the calories you have eaten since your last log in: ")
        current_user.updateCalories(int(cals))
    def removeCalories(self,current_user):
        cals = int(input("Please enter the calories you would like to remove: "))
        current_user.updateCalories(cals - (cals*2))
    def commandHelper(self):
         print(50 * "-")
         print("--a: Opens a prompt to allow you to add calories to your total for today.\n"
               "--t: Shows your current calorie count for today.\n"
               "--w: Shows your current calculated weight based on your total calorie intake. This is only an estimation and may not reflect your actual weight\n"
               "--r: Opens a prompt to allow you to remove calories from your total for today. \n"
               "--f: Allows the user to add calories to their count by entering a food name. If the food is not in the system they will be prompted to add it\n"
               "--sf: Allows the user to add a new food to the system.\n"
               "--ufc: Allows the user to update the calories of a food that is in the system.\n"
               "--lf: Lists the names of all foods currently in the system.\n"
               "--fc: Prints the calories for the entered food.\n"
               )

    def selectFood(self,current_user,food_name):
        if(self.Foods.foodExists(food_name)):
            calories = self.Foods.getFoodCalories(food_name)
            current_user.updateCalories(int(calories))
        else:
            add_food = input("That food does not exist in the system. Would you like to add it? (Y/N): ").lower()
            if add_food == 'y':
                food_cals = input("Please enter the calories for this food: ").lower()
                self.Foods.saveNewFood(food_name,food_cals)
                current_user.updateCalories(int(food_cals))

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
            
if __name__ == "__main__":
    
    user = input("Please enter your name: ").lower()
    Calorie_Tracker(user)
