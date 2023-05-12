class Room:
    def __init__(self, name, description, items=None, character=None, ):
        self.name = name
        self.description = description
        self.items = items or []

    def __str__(self):
        return self.name


class Item:
    def __init__(self, name, description, point_value):
        self.name = name
        self.description = description
        self.point_value = point_value

    def __str__(self):
        return self.name


class Character:
    def __init__(self, name, description, point_value):
        self.name = name
        self.description = description
        self.point_value = point_value

    def __str__(self):
        return self.name







class Game:
    def __init__(self):
        self.score = 0
        self.current_room = None

    def start(self):
        print("welcome to the pyramid of giza habibi ")
        self.setup_game()

    def setup_game(self):
        # Initialize rooms
        room1 = Room("starting room", "its a starting room.", )
        room2 = Room("hallway", "a long dark hallway could contain monsters or bodies who knows .", [Item("british short pistol", "An old british pistol probably left from an expedition during the early 1900s.", 20)])
        room3 = Room("queens chamber ", "a very dark room seems pretty big you can notice movement in there .", [Item("ancient candle", "its an ancient candle .", 2)]  [Item("psychte", "its a psychte .", 25)], [Character("queen ice spice", "you thought she was feeling you????.", -20)])
        room4 = Room("King tuts grave", "its king tuts grave but unlike his queen this guy is maybe dead but his riches aint .", [Item("Khanjar", "its a curved arab sword .", 25)] ,  [Item("Gold", "you find them riches .", 20)])
        room2.items.append(Character("a mummy", "he came back from the dead to just kill you.", -5))
        room3.items.append(Character("queen ice spice", "you thought she was feeling you????.", -20))

        
        self.current_room = room1
        inventory=[]
        x = 1

        #start game loop  
        while x == 1:
            print("\nYou are in the", self.current_room.name)
            print(self.current_room.description)
            print(self.current_room.items)
            print(self.score)
            action = input ("Enter your action (type 'help' for options'): ") 
            if action == 'help' :
                print("ThaTS OK , there are multiple commands 1. look 2. inventory 3. go 4. take 5. interact 6. quit")
            elif action == 'look' :
                print( self.current_room.description)
            elif action == 'inventory' :
                print(inventory)
            elif action.startswith('room1'):
                self.current_room = room1
            elif action.startswith('room2'):
                self.current_room = room2
            elif action.startswith('room3'):
                self.current_room = room3
            elif action.startswith('room4'):
                self.current_room = room4
            elif action.startswith('take'):
                inventory.append (self.current_room.items)
            elif action.startswith('interact'):
                print(self.current_room.character)
            elif action == 'quit' :
             print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")      
            else:
                print("you broke it habibi thats not good")




Game()