
class Calorie_Tracker(object):
    user = ''
    def __init__(self, user):
        self.getCommand(user)
        
    #provides an interface so that users may enter commands
    def getCommand(self, user):
        while True:
            print(50 * "-")
            command = input("\nPlease enter a command: ").lower()
            print()
            if(command == "--a"):
                self.addCalories()
            elif(command == "--t"):
                self.displayTodaysCalories()
            elif(command == "--w"):
                self.displayUsersCurrentWeight(user)
            elif(command == "--help"):
                self.commandHelper()
            else:
                print("I dont recognize that command. Here is a list of my commands:\n")
                self.commandHelper()
    def addCalories(self):
        print("cal")
    def displayTodaysCalories(self):
        print("today")
    def getUserInformation(self, user_name):
        p = 0

    def displayUsersCurrentWeight(self, user_name):
        print("weight")
    def updateUserInformation(self, user_name):
        p = 0
    def commandHelper(self):
         print(50 * "-")
         print("--a: Opens a prompt to allow you to add calories to your total for today.\n"
               "--t: Shows your current calorie count for today.\n"
               "--w: Shows your current calculated weight based on your total calorie intake.\n"
               )
            
if __name__ == "__main__":
    Calorie_Tracker("Cody")
