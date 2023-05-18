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
        room5 = Room("omars proof of work room","its a room to show omars proof of work. good job omar"[Item("Omars mental abiility ", " congratulations you can think like a 5 year old now hope you like it .", 1)])
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
                print("ThaTS OK , there are multiple commands 1. look 2. inventory 3. to go to any room type the room number  4. take 5. interact 6. quit")
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
            elif action.startswith('room6'):
                con = input ("in your face you see a long hallway that seems to never end maybe it goes in circles who knows ")
                if con.startswith('no'):
                    print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")

                elif con.startswith('yes'):
                    y = input ( "you keep on going and going for god knows how long you lost track of time is it days months hours or minutes you dont know it seems like your going in cirlces do you contunie ")        
                    if y.startswith('no'):
                        print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")
                    elif y.startswith('yes'):
                        z = input("in your never ending journey and seeming for going in circles for god knows how long you lost track of the concept of time you decide your are tired and decide wether or not you should rest do you keep going yes or no ")
                        if z.startswith('yes'):
                            print('in the end you decide to keep going but you felt more and more tired by the second then out of nowhere you see a light shinning on you telling you come join me you were hallucinating  in the end you collapsed and died your body was never found to this day ')
                        elif z.startswith('no'):
                            x = input('you decide to find a place to rest and you keep going and you get very tired do you keep looking or just sit on the floor ')
                            if x.startswith('keep looking'):
                                print('well you keep going being the germaphobe you are now and disgusted on the flor ou keep going good job in the end you pass out and die how eciting')
                            elif x.startswith('sit') :
                                L = input('you decide to sit down at the wall  an drest for a bit butt as sit down and put your back on the wall you felt the  wall move a bit and then you feel the ground shake what do you do investiagte or keep resting  ')
                                if L.startswith('keep resting'):
                                    T = input('you decide to keep resting and to contunie later but while resting you fall asleep and after god knows how long you get woken up out of your sleep by a very loud screech that filled the halls you jump up and you hear it  get closer and closer what do you do do you run or investigate the sound  ')
                                    if T.startswith('run'):


            elif action.startswith('quit') :
             print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")      
            else:
                print("you broke it habibi thats not good")




Game()