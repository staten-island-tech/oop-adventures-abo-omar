class Room:
    def __init__(self, name, description, items=None):
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
        room3 = Room("queens chamber ", "a very dark room seems pretty big you can notice movement in there .", [Item("ancient candle", "its an ancient candle .", 2)])
        room2.items.append(Character("a mummy", "he came back from the dead to just kill you.", -5))
        room3.items.append(Character("queen ice spice", "you thought she was feeling you????.", -20))

        # Set starting room
        self.current_room = room1

        #start game loop  
        while True:
            print("\nYou are in the", self.current_room.name)
            print(self.current_room.description)
            self.print_items_in_room()
            self.print_score()
          
            #player input
    action = input ("Enter your action (type 'help' for options'): ")

        # Parse Player Input
    if action == 'help' :
        self.print_help()
    elif action == 'look' :
        self.print_room_description()
    elif action == 'inventory' :
        self.print_inventory()
    elif action.startswith('go'):
        self.go_to_room(action)
    elif action.startswith('take'):
        self.take_item(action)
    elif action.startswith('interact'):
        self.interacr_with_character(action)
    elif action == 'quit' :
        print("Thank you for playing!") 
        break     
    else:
        print("you broke it habibi thats not good")


