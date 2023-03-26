class RPGInfo():

    author = "Anonymous"

    def __init__(self, gametitle):
        self.title = gametitle

    def welcome(self):
        print("Welcome to " + self.title)

    def makealistofpartyweapons(self):
        listofweapons = []
        for character in party:
            listofweapons.append(character.holding)
        return listofweapons

    def checkiftwolistsshareanitem(self, list1, list2):
        for item in list1:
            if item in list2:
                return True
            else:
                return False
        
    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)

    

#currentroom.removecharacter(inhabitant)
