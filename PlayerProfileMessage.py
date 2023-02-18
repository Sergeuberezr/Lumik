from Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.ID = ID

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.ID)

        self.writeVint(0) # Brawlers Boolean

        self.writeVint(len(self.player.brawlers_trophies))
        for x in self.player.brawlers_trophies:
            self.writeDataReference(16, int(x))
            self.writeVint(0)
            self.writeVint(self.player.brawlers_trophies[f"{int(x)}"]) # Brawlers Trophies
            self.writeVint(self.player.brawlers_trophies_rank[f"{int(x)}"]) # Brawlers Trophies For Rank
            self.writeVint(9) # Powel LVL

        self.writeVint(4) # Count
        
        self.writeVint(3) # 3vs3
        self.writeVint(self.player.threexthree) # Count
        
        self.writeVint(3) # Trophies
        self.writeVint(self.player.trophies) # Count
        
        self.writeVint(4) # High Trophies
        self.writeVint(self.player.score) # Count
        
        self.writeVint(5)
        self.writeVint(len([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 34, 35, 36, 37, 38])) #Brawlers list

        # sub_64DF74
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000 + self.player.thumbnail)
        self.writeVint(43000000 + self.player.nameColor)
        self.writeVint(43000000 + self.player.nameColor)

        self.writeBoolean(False)
        self.writeVint(0)


