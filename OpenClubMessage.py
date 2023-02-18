from random import choice
from string import ascii_uppercase
import json
from Protocol.Messages.Server.Aliance.ClubProfileMessage import ClubProfileMessage

from Utils.Reader import Reader


class OpenClubMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        ClubProfileMessage(self.client, self.player).send()