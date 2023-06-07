class Room:
    
    def __init__(self, name, description, items=None, tems=None):
        
        self.name = name
        
        self.description = description
       
        self.items = items or [] or tems

    
    def __str__(self):
      
        return self.name
