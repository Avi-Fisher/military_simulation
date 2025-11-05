
class Unit():

    def __init__(self,name,commander,soldier):

        self.name = name
        self.commander = commander
        self.soldier =soldier

    def briefing(self):
        print(f"Unit name: {self.name}")
        self.commander.report()














