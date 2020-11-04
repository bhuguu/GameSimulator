from .Player import Player


class PlayerList:
    def __init__(self):
        self.player_list = []
        self.name_table = {}
        self.player_count = 0

    def register_new_player(self, num):
        for i in range(num):
            self.player_list.append(Player(self.player_count))
            self.player_count += 1

    def set_players_name(self, index, string):
        self.player_list[index].set_name(string)
        self.name_table[string] = index

    def get_player_by_index(self, index):
        return self.player_list[index]

    def get_player_by_name(self, string):
        return self.player_list[self.name_table[string]]
