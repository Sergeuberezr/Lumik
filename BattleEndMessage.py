from Utils.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        if self.result == 1:
           #Replace Trophies
           self.player.brawlers_trophies[str(self.player.homeBrawler)] -= 6
           self.player.trophies -= 6
           self.player.updateAccount('brawlers_trophies', self.player.brawlers_trophies)
           self.player.updateAccount('trophies', self.player.trophies)
        else:
        	pass
        if self.result == 0:
           #Replace Trophies
           self.player.brawlers_trophies[str(self.player.homeBrawler)] += 8
           self.player.trophies += 8
           self.player.score += 8
           self.player.threexthree += 1
           self.player.updateAccount('brawlers_trophies', self.player.brawlers_trophies)
           self.player.updateAccount('Trophies', self.player.trophies)
           self.player.updateAccount('HighestTrophies', self.player.score)
           self.player.updateAccount('three&three', self.player.threexthree)
           #Replace Trophies for Rank
           self.player.brawlers_trophies_rank[str(self.player.homeBrawler)] += 8
           self.player.updateAccount('brawlers_trophies_rank', self.player.brawlers_trophies_rank)
        else:
        	pass
        self.writeVint(1) # Battle End Type 1 - 3vs3 2 - ShowDown
        self.writeVint(self.result)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(0)
        self.writeVint(32)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVint(player) if self.team == 0 else self.writeVint(2)
            else:
                self.writeVint(2 if self.team != 0 else 1) if self.type == 2 else self.writeVint(self.team if self.team != 1 else 2)

            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVint(0)
            self.writeDataReference(29, self.skin)   if self.skin != -1 else self.writeVint(0)

            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10)

            self.writeBool(False)

            # sub_64DF74
            self.writeString(self.username)
            self.writeVint(100)
            self.writeVint(28000000)
            self.writeVint(43000000)
            self.writeNullVint()


        self.writeBool(False)
        self.writeBool(False)
        self.writeBool(False)

        self.writeDataReference(28, 0)

        self.writeBool(False)
        
        self.player.animtrophy = 8

