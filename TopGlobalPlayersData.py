from Utils.Writer import Writer
from Database.Tables.Player import DataBase
import json

class TopGlobalPlayersData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        db = DataBase()
        players = db.getPlayerAccount()
        if len(players) >= 200:
            count = 200
        else:
            count = len(players)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeVint(count)
        
        for i in players:
         	   self.writeVint(0)
         	   self.writeVint(i[3]['ID'])

         	   self.writeVint(1)       
         	   self.writeVint(i[2])

         	   self.writeVint(1)

         	   self.writeString()#Club Name
         	   self.writeString(i[3]['Name'])#Player Name

         	   self.writeVint(1)
         	   self.writeVint(28000000 + i[3]['Thumbnail'])#Player icon
         	   self.writeVint(43000000 + i[3]['NameColor'])#Name Color
         	   self.writeVint(43000000 + i[3]['NameColor'])

        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeString(" Modern Brawl")
        print("[INFO] Message TopGlobalPlayersData has been sent.")