class Room:
    
    def __init__(self, name, description, items=None, tems=None):
        
        self.name = name
        
        self.description = description
       
        self.items = items or [] or tems

    
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

class ScoreSystem:
    
    def __init__(self):
        
        self.score = 0

    def increase_score(self, points):
        
        self.score += points

    def decrease_score(self, points):
        
        self.score -= points

    def reset_score(self):
       
        self.score = 0

    def get_score(self):
       
        return self.score





class Game:
   
   
       
    
        
 

   
       
        

    
    def setup_game(self):

        score_system = ScoreSystem()

        # Initialize rooms
       
        room1 = Room("starting room", "its a starting room.", )
        
        room2 = Room("hallway", "a long dark hallway could contain monsters or bodies who knows .", [Item("british short pistol", "An old british pistol probably left from an expedition during the early 1900s.", 20)])
       
        room3 = Room("queens chamber ", "a very dark room seems pretty big you can notice movement in there .", [Item("ancient candle", "its an ancient candle .", 2)] , [Item("psychte", "its a psychte .", 25)], )
       
        room4 = Room("King tuts grave", "its king tuts grave but unlike his queen this guy is maybe dead but his riches aint .", [Item("Khanjar", "its a curved arab sword .", 25)] ,  [Item("Gold", "you fou  nd them riches .", 20)])
        
        room5 = Room("omars proof of work room","its a room to show omars proof of work. good job omar",[Item("Omars mental abiility ", " congratulations you can think like a 5 year old now hope you like it .", 1)])
       
        

        
        self.current_room = room1
        pistol=[[Item("british short pistol", "An old british pistol probably left from an expedition during the early 1900s.", 20)]]
        inventory=[]
        sharpweapons=[[Item("Khanjar", "its a curved arab sword .", 25)] , [Item("psychte", "its a psychte .", 25)]]

       
        
        print("\nwelcome to the pyramid of giza habibi  You are in the", self.current_room.name)
        print(self.current_room.description)
        print('there are no items in this room')
        print(score_system.get_score())

       

        #start game loop  
       
        while True:
            
            

            action = input ("Enter your action (type 'help' for options'): ") 
            
            if action == 'help' :
               
                print("thats OK , there are multiple commands 1. look 2. inventory 3. to go to any room type the room number ex:room3  4. take 5. interact 6. quit")
           
            elif action == 'look' :
                
                print( self.current_room.description)
           
            elif action == 'inventory' :
                
                print(inventory)
           
            elif action.startswith('room1'):
               
                self.current_room = room1

                print('\n you entered the ' , self.current_room.name)
           
            elif action.startswith('room2'):
               
                self.current_room = room2

                print('\n you entered the ' , self.current_room.name)
            
            elif action.startswith('room3'):
                
                self.current_room = room3

                print('\n you entered the ' , self.current_room.name)
            
            elif action.startswith('room4'):
               
                self.current_room = room4

                print('\n you entered the ' , self.current_room.name)

            elif action.startswith('room5'):
               
                self.current_room = room5

                print('\n you entered the ' , self.current_room.name)
           
           
            elif action.startswith('take'):
                 
                if self.current_room == room2 : 
                    
                    if 'pistol' not in inventory:

                        print('you found a british short pistol ')
               
                        inventory.append ('pistol')
                        
                        score_system.increase_score(20)
                    
                    elif 'pistol' in inventory:
                        
                        print('you already took the items here')

                elif self.current_room == room3 : 
                 
                    if 'candle' not in inventory:

                        print('you found a psychte and an ancient candle ')
               
                        inventory.append ('psychte')

                        inventory.append('candle')
                        
                        score_system.increase_score(27)

                        
                    
                    elif 'candle' in inventory:
                       
                        print('you already took the items here')

                elif self.current_room == room4 : 
                 
                    if 'khanjar' not in inventory:

                        print('you found a psychte and some golden artifacts')
               
                        inventory.append ('khanjar')

                        inventory.append('golden artifacts')
                        
                        score_system.increase_score(45)
                    
                    elif 'khanjar' in inventory:
                       
                        print('you already took the items here')
                
                elif self.current_room == room5 : 

                 print('you found omars mentall abillity to think yay your 5 now ')
               
                 inventory.append ('omars mental abillity')

                 score_system.increase_score(1)
               
                else:
                   
                    print('there are no items in this room')
           
            elif action.startswith('interact'):
             
                

                    
           
                if self.current_room == room2: 
             
                 if 'psychte' in inventory:
                 
                        print('you decide to call out who ever is here since you sensed movement and a mummy approaches you and attacks you  but you fight back with youyr weapons and slash it and it dies good job plus 5 points ')
                
                        score_system.increase_score(5)
                 
                 elif 'khanjar' in inventory:
                 
                        print('you decide to call out who ever is here since you sensed movement and a mummy approaches you and attacks you  but you fight back with youyr weapons and slash it and it dies good job plus 5 points ')
                
                        score_system.increase_score(5)


                 else:
                     print('you decide to call out who ever is here since you sensed movement and a mummy approaches you and attacks you minus 5 points')

                     score_system.decrease_score(5)

                     

            
                
                
                
                    
        
            
                if self.current_room == room3:
               
                 if 'pistol' in inventory:
                   
                    print('you decide to see what was moving in the queens chamber you try to find a light source but it doesnt workand then you hear her behind you its queen ice spice before you know she said you thought I was feeling you but you were quick to react and shot her guess you werent feeling her eithier +20 points')

                    score_system.increase_score(20)
                 
                 else:
                        print('you decide to see what was moving in the queens chamber you try to find a light source but it doesnt workand then you hear her behind you its queen ice spice before you know she said you thought i was feeling you and she kicks you out -10 points')

                        score_system.decrease_score(20)

                        print(score_system.get_score())

                        

                    
                
                if self.current_room == room1: 
                    
                    print('theres no npc here')

                if self.current_room == room4: 
                    
                    print('theres no npc here')

                if self.current_room == room5: 
                    
                    print('theres no npc here')
                
            elif action.startswith('room6'):
               
                con = input ("in your face you see a long hallway that seems to never end maybe it goes in circles who knows maybe it leads to an exit  do you enter  (answer should be yes or no)")
                
                if con.startswith('no'):
                   
                    
                    print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")

                    print(score_system.get_score())

                    exit()
                
                elif con.startswith('yes'):

                    y = input ( "you keep on going and going for god knows how long you lost track of time is it days months hours or minutes you dont know it seems like your going in cirlces do you contunie   (answer should be yes or no) ")        
                    
                    if y.startswith('no'):
                       
                        print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")
                   
                    elif y.startswith('yes'):
                        
                        z = input("in your never ending journey and seeming for going in circles for god knows how long you lost track of the concept of time you decide your are tired and decide wether or not you should rest do you keep going   (answer should be yes or no) ")
                        
                        if z.startswith('yes'):
                           
                            
                            
                            print('in the end you decide to keep going but you felt more and more tired by the second then out of nowhere you see a light shinning on you telling you come join me you were hallucinating  in the end you collapsed and died your body was never found to this day ')
                        
                            print(score_system.get_score())

                            exit()
                        
                        elif z.startswith('no'):
                           
                            x = input('you decide to find a place to rest and you keep going and you get very tired do you keep looking or just sit on the floor ')
                            
                            if x.startswith('keep looking'):
                               
                               
                                
                                print('well you keep going being the germaphobe you are now and disgusted on the flor ou keep going good job in the end you pass out and die how exciting')
                                
                                print(score_system.get_score())

                                exit()
                            
                            elif x.startswith('sit') :
                               
                                L = input('you decide to sit down at the wall  and rest for a bit but as you sit down and put your back on the wall you felt the  wall move a bit and then  feel the ground shake what do you do investiagte or keep resting  ')
                               
                                if L.startswith('keep resting'):
                                   
                                    T = input('you decide to keep resting and to contunie later but while resting you fall asleep and after god knows how long you get woken up out of your sleep by a very loud screech that filled the halls you jump up and you hear it  get closer and closer what do you do do you run or investigate the sound  ')
                                    
                                    if T.startswith('run'):
                                        
                                        P = input('you start running as fast as you can and the voice is still getting louder but after a few moments its starts fading away and you think its gone now so you stand for a bit and take your breath what do you do next contunie resting or keep exploring')
                                        
                                        if P.startswith('keep exploring'):
                                           
                                            print('you decide to keep going and the adrenaline wears and you collapse on the floor and never wake up boo hoo you died what did you expect when you overstress for a tired body')

                                            print(score_system.get_score())

                                            exit()
                                        
                                        elif P.startswith('continue resting'):
                                            
                                            print('you decide to sit down and keep ressting and then you see a light you can escape you finally can getout as you approach the light you have a warm feeling in your heart and you get happier and happier until it all turns to black  ')
                                            
                                            print(score_system.get_score())

                                            exit()
                                   
                                    elif T.startswith('investigate'):
                                        
                                        Q = input('you decide to get up and investigate and then you found a new room never seen before  you find the screching noise to be a strong flow of air  what do you do start diiging a hole out of where the air is coming out of or find a tool to help you with it ')
                                        
                                        if Q.startswith('keep diging'):
                                           
                                            print('you decide to start right away and keep digiing with your hand and the whole gets bigger and bigger and you see its night out how long has it been it doesnt matter for now freedomn is right here until you feel something weird and then a sharp stinging pain on your right hand and it hurt you take it out and see scorpions crawl out and next thing you know you fall on the ground and nothing else for it all turned to black')
                                      
                                            print(score_system.get_score())

                                            exit()
                                        
                                        elif Q.startswith('look for a tool'):
                                           
                                            U = input('you decide to look in the room for something to make a hole with and ge out you keep looking and looking but then you find two things an old bone that seems sturdy and very old worn out shovel which do you choose')
                                            
                                            if U.startswith('shovel'):

                                                print('you decide to take the shove and you start digging then after a few rounds the shovl snaps in half and venemous spiders start crawling out of it guess it is a bad day to have arachnaphobia ')
                                                
                                                print(score_system.get_score())

                                                exit()
                                            
                                            elif U.startswith('bone'):
                                               
                                                print('you pick up to bone and start smashing a hole where the air is and it gets bigger and bigger then you notice scorpions crawling out they dont attack you tho then you hear the roof crack and next you know everything turns black your body was found a day later by locals due yo yhem noticing a huge hole in the sand near the pyramids your bdy was crushed in the procces though') 

                                elif L.startswith('investigate'):
                                    
                                    B = input('you decide to get up and ivestigate and you find a hidden room that you uncovered by accident you go in it and you see light yay your saved now do you dig a hole with your hands or look for a tool')

                                    if B.startswith('hands'):

                                        M = input(' you decide to go in as quikly as possible and dig a hole out of your hands and your and as the hole gets bigger and bigger you start crawling out and as you leave everything collapses on your foot what do you do try to cut it out or scream for help')

                                        if M.startswith('scream'):
                                            
                                            if 'pistol' in inventory:
                                                
                                                print('you try to scream for help your finally out now but then after a few minutes nothing happens so you stop until you notice movement you get excited but then its gets closer and closer and you see its a large snake but luckily you were quick enough to pull out your pistol and shoot it who knew you would have a use for that pistol you found  but shortly after you hear people screaming and running towards you yay your rescued you get found by the locals and they were able to get an exicvator to get you out next thing you know your all over the news man isnt egypt just great')
                                            
                                                print(score_system.get_score())
                                               
                                                exit()
                                            
                                            else :
                                                print('you try to scream for help your finally out now but then after a few minutes nothing happens so you stop until you notice movement you get excited but then its gets closer and closer and you see its a large snake what did you expect in a dessert') 
                                                
                                                print(score_system.get_score())
                                               
                                                exit()
                                        elif M.startswith('cut'):

                                            if 'khanjar' in inventory :

                                                print('you try to cut your leg off with the khanjar you found in the pyramid and you do succsefully you then run off into civlization where the people see you and approach you when they see what happend they rush to a hospital your saved yay too bad theres no insurance for you in egypt ')
                                                
                                                print(score_system.get_score())
                                               
                                                exit()
                                            if 'khanjar' not in inventory :
                                                print('you tried to cut your leg off but nothing really worked  so you just sit there hopelessly and think over your life and the actions you have done what a life you say as you die of a heat stroke buit finnaly at peace with yourself')

                                                print(score_system.get_score())
                                               
                                                exit()
                                        
                                        elif B.startswith('look'):
                                           
                                            qw = input('you decide to  look for a tool for god knows how long and then you find two things an axe and a mace which do you choose')
                                          
                                            if qw.startswith('axe'):
                                               
                                                print('you decide to take an axe and make a hole with it and you start choppingg out a rectangle big enough for you and it works you climb out  and start running to a town you see in the distance you make it there and the locals see you and welcome you thank god your saved ')

                                                print(score_system.get_score())

                                                exit()
                                           
                                            elif qw.startswith('mace') :
                                               
                                                print(' you decide to take the mace to blow a bigger hole through and as you try you realize how do I use a mace so you swing to try and figure it out but you miss the wall entirley and it spins back and hits your face good job I hope your are proud of yourself ')
                                            
                                        
            elif action.startswith('quit') :
             
             print("as time goes by and by and you cant find your exit  you decide to give up on life and wait until sarvation or the monsters get you in the end you died 2 years later your body is found heavily deformed but somehow your flesh didnt rot or decay. how??? that is a mystery for another day ")      

             print(score_system.get_score()) 

             exit()
            else:
                print('thats not a command habibi')

    
game = Game()
game.setup_game()







