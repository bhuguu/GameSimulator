class InformationSet:
    def __init__(self, info_set_table, node):
        self.node_list = [node]
        self.choice_count = 0
        self.player = node.player
        self.info_set_table = info_set_table
        self.index = self.info_set_table.register_new_info_set(self)

    def get_node_list(self):
        return self.node_list

    def get_player(self):
        return self.player

    def get_index(self):
        return self.index

    def get_choice_count(self):
        return self.choice_count

    def count(self):
        flag_node = self.node_list[0]
        self.choice_count = len(flag_node.get_next_nodes())

    def create_action_list(self):
        self.player.add_action_function(self)

    def merge(self, other):
        if not self.player == other.get_player():
            print("Cannot merge: different player")
        if not self.choice_count == other.get_choice_count():
            print("Cannot merge: different branches")
        self.node_list += other.get_node_list()
        for node in other.get_node_list():
            node.set_info_set(self)
        self.info_set_table.remove_info_set(other.get_index())

    def __hash__(self):
        return self.index + hash("InformationSet")

    def __eq__(self, other):
        return self.index + hash("InformationSet") == other.__hash__()
