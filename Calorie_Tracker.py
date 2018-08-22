from User import User
#The purpose of this class is to create an interface for the user to
#interact with the program. In addition it allows for interaction with the User class.
class Calorie_Tracker(object):
    
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
            elif(command == "--help"):
                self.commandHelper()
            else:
                print("I dont recognize that command. Here is a list of my commands:\n")
                self.commandHelper()
    
    def addCalories(self,current_user):
        cals = input("Please enter the calories you have eaten since your last log in: ")
        current_user.updateCalories(int(cals))

    def commandHelper(self):
         print(50 * "-")
         print("--a: Opens a prompt to allow you to add calories to your total for today.\n"
               "--t: Shows your current calorie count for today.\n"
               "--w: Shows your current calculated weight based on your total calorie intake. This is only an estimation and may not reflect your actual weight\n"
               )
            
if __name__ == "__main__":
    
    user = input("Please enter your name: ").lower()
    Calorie_Tracker(user)
