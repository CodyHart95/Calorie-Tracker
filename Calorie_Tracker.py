
class Calorie_Tracker(object):
    def __init__(self):
        self.getCommand()
        
    #provides an interface so that users may enter commands
    def getCommand(self):
        while True:
            print(50 * "-")
            command = input("\nPlease enter a command: ".lower())
            print()
        
if __name__ == "__main__":
    Calorie_Tracker()
