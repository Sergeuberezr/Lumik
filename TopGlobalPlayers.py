from random import choice
from string import ascii_uppercase
import json
from Protocol.Messages.Server.Leaderboard.TopGlobalPlayersData import TopGlobalPlayersData

from Utils.Reader import Reader


class TopGlobalPlayers(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.LeaderboardType     = self.readVint()
        self.player.LeaderboardInfo     = self.readVint()

    def process(self):
        TopGlobalPlayersData(self.client, self.player).send()