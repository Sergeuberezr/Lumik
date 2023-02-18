from Utils.Writer import Writer
from random import randint as r

class Box(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(11) # Box ID
        
        self.writeVint(2)
        
        self.writeVint(1) # Value
        self.writeDataReference(16, r(1, 38))
        self.writeVint(1)
        self.writeVint(0) #29
        self.writeVint(0) #52
        self.writeVint(0) #23
        self.writeVint(0)
        
        self.writeVint(r(2, 35)) # Value
        self.writeDataReference(16, 0)
        self.writeVint(8)
        self.writeVint(0) #29
        self.writeVint(0) #52
        self.writeVint(0) #23
        self.writeVint(0)
        
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeLogicLong(68)
