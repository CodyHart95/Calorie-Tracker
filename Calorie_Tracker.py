
class Calorie_Tracker(object):
    def __init__(self):
        self.getCommand()
        
    #provides an interface so that users may enter commands
    def getCommand(self):
        while True:
            print(50 * "-")
            command = input("\nPlease enter a command: ".lower())
            print()
    def addCalories(self,new_calories):
        p = 0

    def displayTodaysCalories(self,date):
        p = 0

    def getUserInformation(self, user_name):
        p = 0

    def displayUsersCurrentWeight(self, user_name):
        p = 0

    def updateUserInformation(self, user_name):
        p = 0
        
if __name__ == "__main__":
    Calorie_Tracker()
