from .InformationSet import InformationSet


class Node:
    def __init__(self, info_set_table, player):
        self.next_nodes = []
        self.player = player
        self.info_set = InformationSet(info_set_table, self)

    def get_info_set(self):
        return self.info_set

    def set_info_set(self, info_set):
        self.info_set = info_set

    def get_next_nodes(self):
        return self.next_nodes

    def connect(self, other):
        self.next_nodes.append(other)

    def move(self):
        return self.next_nodes[self.player.choose_action(self.info_set)]

    def merge(self, other):
        self.info_set.merge(other.get_info_set())

    def set_as_terminal(self, payoff, result_table):
        result_table.register_info_set_as_terminal(self.info_set, payoff)
