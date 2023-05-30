class Room:
    
    def __init__(self, name, description, items=None, Character=None, ):
        
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
        
        self.current_room=None

    def start(self):
        
        print("welcome to the pyramid of giza habibi ")
       
        

    
    def setup_game(self):
        
        # Initialize rooms
       
        room1 = Room("starting room", "its a starting room.", )
        
        room2 = Room("hallway", "a long dark hallway could contain monsters or bodies who knows .", [Item("british short pistol", "An old british pistol probably left from an expedition during the early 1900s.", 20)])
       
        room3 = Room("queens chamber ", "a very dark room seems pretty big you can notice movement in there .", [Item("ancient candle", "its an ancient candle .", 2)] , [Item("psychte", "its a psychte .", 25)], )
       
        room4 = Room("King tuts grave", "its king tuts grave but unlike his queen this guy is maybe dead but his riches aint .", [Item("Khanjar", "its a curved arab sword .", 25)] ,  [Item("Gold", "you fou  nd them riches .", 20)])
        
        room5 = Room("omars proof of work room","its a room to show omars proof of work. good job omar",[Item("Omars mental abiility ", " congratulations you can think like a 5 year old now hope you like it .", 1)])
       
        room2.items.append(Character("a mummy", "he came back from the dead to just kill you.", -5))
       
        room3.items.append(Character("queen ice spice", "you thought she was feeling you????.", -20))

        
        self.current_room = room1
        pistol=[[Item("british short pistol", "An old british pistol probably left from an expedition during the early 1900s.", 20)]]
        inventory=[]
        sharpweapons=[[Item("Khanjar", "its a curved arab sword .", 25)] , [Item("psychte", "its a psychte .", 25)]]
        
        print("\nYou are in the", self.current_room.name)
           
        print(self.current_room.description)
           
        print(self.current_room.items)
        
        print(self.score)

        #start game loop  
       
        while True:
            
            
            
            action = input ("Enter your action (type 'help' for options'): ") 
            
            if action == 'help' :
               
                print("thats OK , there are multiple commands 1. look 2. inventory 3. to go to any room type the room number  4. take 5. interact 6. quit")
           
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
                        
                            print(self.score)

                            quit
                        elif z.startswith('no'):
                           
                            x = input('you decide to find a place to rest and you keep going and you get very tired do you keep looking or just sit on the floor ')
                            
                            if x.startswith('keep looking'):
                               
                               
                                
                                print('well you keep going being the germaphobe you are now and disgusted on the flor ou keep going good job in the end you pass out and die how eciting')
                                
                                print(self.score)

                                quit
                            
                            elif x.startswith('sit') :
                               
                                L = input('you decide to sit down at the wall  an drest for a bit butt as sit down and put your back on the wall you felt the  wall move a bit and then you feel the ground shake what do you do investiagte or keep resting  ')
                               
                                if L.startswith('keep resting'):
                                   
                                    T = input('you decide to keep resting and to contunie later but while resting you fall asleep and after god knows how long you get woken up out of your sleep by a very loud screech that filled the halls you jump up and you hear it  get closer and closer what do you do do you run or investigate the sound  ')
                                    
                                    if T.startswith('run'):
                                        
                                        P = input('you start running as fast as you can and the voice is still getting louder but after a few moments its starts fading away and you think its gone now so you stand for a bit and take your breath what do you do next contunie resting or keep exploring')
                                        
                                        if P.startswith('Keep exploring'):
                                           
                                            print('you decide to keep going and the adrenaline wears and you collapse on the floor and never wake up boo hoo you died what did you expect when you overstress for a tired body')

                                            print(self.score)

                                            quit
                                        
                                        elif P.startswith('continue resting'):
                                            
                                            print('you decide to sit down and keep ressting and then you see a light you can escape you finally can getout as you approach the light you have a warm feeling in your heart and you get happier and happier until it all turns to black  ')
                                            
                                            print(self.score)

                                            quit
                                   
                                    elif T.startswith('investigate'):
                                        
                                        Q = input('you decide to get up and investigate and then you found a new room never seen before  you find the screching noise to be a strong flow of air  what do you do start diiging a hole out of where the air is coming out of or find a tool to help you with it ')
                                        
                                        if Q.startswith('keep diging'):
                                           
                                            print('you decide to start right away and keep digiing with your hand and the whole gets bigger and bigger and you see its night out how long has it been it doesnt matter for now freedomn is right here until you feel something weird and then a sharp stinging pain on your right hand and it hurt you take it out and see scorpions crawl out and next thing you know you fall on the ground and nothing else for it all turned to black')
                                      
                                            print(self.score)

                                            quit
                                        
                                        elif Q.startswith('look for a tool'):
                                           
                                            U = input('you decide to look in the room for something to make a hole with and ge out you keep looking and looking but then you find two things an old bone that seems sturdy and very old worn out shovel which do you choose')
                                            
                                            if U.startswith('shovel'):

                                                print('you decide to take the shove and you start digging then after a few rounds the shovl snaps in half and venemous spiders start crawling out of it guess it is a bad day to have arachnaphobia ')
                                                
                                                print(self.score)

                                                quit
                                            
                                            elif U.startswith('bone'):
                                               
                                                print('you pick up to bone and start smashing a hole where the air is and it gets bigger and bigger then you notice scorpions crawling out they dont attack you tho then you hear the roof crack and next you know everything turns black your body was found a day later by locals due yo yhem noticing a huge hole in the sand near the pyramids your bdy was crushed in the procces though') 

                                elif L.startswith('investigate'):
                                    
                                    B = input('you decide to get up and ivestigate and in it you find a hidden room that you uncovered by accident you go in it and you see light yay your saved now do you dig a hole with your hands or look for a tool')

                                    if B.startswith('hands'):

                                        M = input(' you decide to go in as quikly as possible and dig a hole out of your hands and your jand gets bigger and bigger you start crawling out and as you leave everything collapses on your foot what do you do try to cut it out or scream for help')

                                        if M.startswith('scream'):
                                            
                                            if pistol in inventory:
                                                
                                                print('you try to scream for help your finally out now but then after a few minutes nothing happens so you stop until you notice movement you get excited but then its gets closer and closer and you see its a large snake but luckily you were quick enough to pull out your pistol and shoot it who knew you would have a use for that pistol you found  but shortly after you hear people screaming and running towards you yay your rescued you get found by the locals and they were able to get an exicvator to get you out next thing you know your all over the news man isnt egypt just great')
                                            
                                                print(self.score)
                                               
                                                quit
                                            
                                            else :
                                                print(' you try to scream for help your finally out now but then after a few minutes nothing happens so you stop until you notice movement you get excited but then its gets closer and closer and you see its a large snake what did you expect in a dessert') 
                                                
                                                print(self.score)
                                               
                                                quit
                                        elif M.startswith('cut'):

                                            if sharpweapons in inventory :

                                                print('you try to cut your leg off with the sharpweaposn you found in the pyramid and you do succsefully you then run off into civlization where the people see you and approach you when they see what happend they rush to a hospital your saved yay too bad theres no insurance for you in egypt ')
                                                
                                                print(self.score)
                                               
                                                quit
                                            else :
                                                print('you tried to cut your leg off but nothing really worked  so you just sit there hopelessly and think over your life and the actions you have done what a life you say as you die of a heat stroke buit finnaly at peace with yourself')

                                                print(self.score)
                                               
                                                quit
                                        elif B.startswith('look'):
                                           
                                            qw = input('you decide to  look for a tool for god knows how long and then you find two things an axe and a mace which do you choose')
                                          
                                            if qw.startswith('axe'):
                                               
                                                print('you decide to take an axe and make a hole with it and you start choppingg out a rectangle big enough for you and it works you climb out  and start running to a town you see in the distance you make it there and the locals see you and welcome you thank god your saved ')

                                            elif    
                                            

            elif action.startswith('quit') :
             
             print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")      
            
            else:
               
                print("you broke it habibi thats not good")
    
game = Game()
game.setup_game()







